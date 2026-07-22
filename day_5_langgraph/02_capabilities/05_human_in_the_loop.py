import os  # lets us read settings from the computer's environment
from typing import TypedDict, NotRequired  # tools to describe our data, with some optional parts
from dotenv import load_dotenv  # tool that loads secret settings from a file
from langchain.chat_models import init_chat_model  # helper to set up the AI chat model
from langgraph.graph import StateGraph, START, END  # building blocks for a step-by-step flow
from langgraph.checkpoint.memory import InMemorySaver  # remembers progress in the computer's memory
from langchain_core.runnables import RunnableConfig  # a settings bag we pass along with each run
from langgraph.types import interrupt, Command  # tools to pause the flow and later resume it

load_dotenv()  # reads the secret settings file so we can use it
model = init_chat_model(  # sets up the AI model we will chat with
    os.environ.get("MODEL", "google/gemini-3.1-flash-lite"),
    model_provider="openrouter",
    temperature=0,
)

class S(TypedDict):  # describes what our shared data looks like
    request: str  # the customer's original request
    draft: NotRequired[str]  # the AI's draft reply, filled in later
    sent: NotRequired[str]  # the final reply that gets sent, filled in later

def write_draft(state):  # the step that writes a draft reply
    reply = model.invoke("Write a polite one-line reply to this customer:\n" + state["request"])  # asks the AI to write a polite reply
    return {"draft": reply.content}  # saves the AI's draft text

def approve(state):  # the step that pauses to get a human's approval
    decision = interrupt({"draft": state["draft"]})  # pauses and shows the draft to a person, waiting for their answer
    decision = str(decision).strip()  # tidies up the person's answer as text
    if decision.lower() in ("yes", "y"):  # checks if the person said yes
        return {"sent": state["draft"]}  # sends the AI's draft as-is
    if decision.lower() in ("no", "n"):  # checks if the person said no
        return {"sent": "Escalated to human support."}  # hands the case to a human instead
    return {"sent": decision}  # otherwise sends whatever the person typed themselves

b = StateGraph(S)  # starts building the flow using our data shape
b.add_node("write_draft", write_draft)  # adds the write-draft step
b.add_node("approve", approve)  # adds the approval step
b.add_edge(START, "write_draft")  # says the flow begins by writing a draft
b.add_edge("write_draft", "approve")  # says after writing we go to approval
b.add_edge("approve", END)  # says the flow finishes after approval
graph = b.compile(checkpointer=InMemorySaver())  # finishes the flow and lets it remember progress

cfg: RunnableConfig = {"configurable": {"thread_id": "ticket-1"}}  # a name tag for this one support ticket
REQUEST = "Please waive my late fee on my credit card this month"  # the customer's request text

# 1. Run the graph to write a draft reply
paused = graph.invoke({"request": REQUEST}, cfg)  # runs the flow until it pauses for approval
draft = paused["__interrupt__"][0].value["draft"]  # pulls out the draft the flow paused on

# 2. Ask the human to approve the draft
print("\n" + "=" * 40)  # prints a line of equals signs as a divider
print("Agent Paused - it needs your approval to send the reply.")  # tells the user the agent is waiting
print("=" * 40)  # prints another divider line
print("Customer asked: ", REQUEST)  # shows what the customer asked
print("AI Draft Reply: ", draft)  # shows the draft the AI wrote
answer = input("Do you approve the draft? (yes /no / or type. your own reply): ")  # waits for the person to type a decision

# 3. Resume the agent with the human's decision
done = graph.invoke(Command(resume=answer), cfg)  # continues the flow using the person's decision
print("\n>>> FINAL MESSAGE SENT TO CUSTOMER: ", done["sent"])  # shows the final reply that was sent
