import os
from typing import TypedDict, NotRequired
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.runnables import RunnableConfig
from langgraph.types import interrupt, Command

load_dotenv()
model = init_chat_model(
    os.environ.get("MODEL", "google/gemini-3.1-flash-lite"),
    model_provider="openrouter",
    temperature=0,
)

class S(TypedDict):
    request: str
    draft: NotRequired[str]
    sent: NotRequired[str]

def write_draft(state):
    reply = model.invoke("Write a polite one-line reply to this customer:\n" + state["request"])
    return {"draft": reply.content}

def approve(state):
    decision = interrupt({"draft": state["draft"]})
    decision = str(decision).strip()
    if decision.lower() in ("yes", "y"):
        return {"sent": state["draft"]}
    if decision.lower() in ("no", "n"):
        return {"sent": "Escalated to human support."}
    return {"sent": decision}

b = StateGraph(S)
b.add_node("write_draft", write_draft)
b.add_node("approve", approve)
b.add_edge(START, "write_draft")
b.add_edge("write_draft", "approve")
b.add_edge("approve", END)
graph = b.compile(checkpointer=InMemorySaver())

cfg: RunnableConfig = {"configurable": {"thread_id": "ticket-1"}}
REQUEST = "Please waive my late fee on my credit card this month"

# 1. Run the graph to write a draft reply
paused = graph.invoke({"request": REQUEST}, cfg)
draft = paused["__interrupt__"][0].value["draft"]

# 2. Ask the human to approve the draft
print("\n" + "=" * 40)
print("Agent Paused - it needs your approval to send the reply.")
print("=" * 40)
print("Customer asked: ", REQUEST)
print("AI Draft Reply: ", draft)
answer = input("Do you approve the draft? (yes /no / or type. your own reply): ")

# 3. Resume the agent with the human's decision
done = graph.invoke(Command(resume=answer), cfg)
print("\n>>> FINAL MESSAGE SENT TO CUSTOMER: ", done["sent"])
