import os  # lets us read settings from the computer's environment
from dotenv import load_dotenv  # tool that loads secret settings from a file
from langchain.chat_models import init_chat_model  # helper to set up the AI chat model
from langchain_core.messages import HumanMessage  # a way to write a message as if from a person
from langgraph.graph import StateGraph, START, END, MessagesState  # building blocks for a chat flow
from langgraph.checkpoint.memory import InMemorySaver  # remembers past chats in the computer's memory
from langgraph.store.memory import InMemoryStore  # a long-term notebook for facts about customers
from langchain_core.runnables import RunnableConfig  # a settings bag we pass along with each run

load_dotenv()  # reads the secret settings file so we can use it
model = init_chat_model(  # sets up the AI model we will chat with
    os.environ.get("MODEL", "google/gemini-3.1-flash-lite"),
    model_provider="openrouter",
    temperature=0,
)

STORE = InMemoryStore()  # creates the notebook to hold customer facts
STORE.put(("customer-1",), "profile", {"name": "Travis", "segment": "premium"})  # saves Travis's details in the notebook

def chat(state):  # a step that greets the customer using their saved details
    item = STORE.get(("customer-1",), "profile")  # looks up the customer's saved details
    profile = item.value if item else {"name": "there", "segment": "standard"}  # uses the details, or defaults if none found
    system = {  # builds a hidden instruction telling the AI how to greet
        "role": "system",
        "content": f"Help {profile['name']}, a {profile['segment']} customer, One short line."
    }
    return {"messages": [model.invoke([system] + state["messages"])]}  # asks the AI using the instruction plus the chat

b = StateGraph(MessagesState)  # starts building a chat flow that keeps a list of messages
b.add_node("chat", chat)  # adds our chat step and names it "chat"
b.add_edge(START, "chat")  # says the flow begins at the chat step
b.add_edge("chat", END)  # says the flow finishes after the chat step
graph = b.compile(checkpointer=InMemorySaver())  # finishes the flow and lets it remember past chats

today: RunnableConfig = {"configurable": {"thread_id": "chat-today"}}  # a name tag for today's chat thread
week: RunnableConfig = {"configurable": {"thread_id": "chat-next-week"}}  # a name tag for next week's chat thread
reply_today = graph.invoke({"messages": [HumanMessage("Hello")]}, today)  # says hello on today's thread
reply_week = graph.invoke({"messages": [HumanMessage("Hello")]}, week)  # says hello on next week's thread
print("today:", reply_today["messages"][-1].content)  # shows the AI's greeting from today's thread
print("next week:", reply_week["messages"][-1].content)  # shows the AI's greeting from next week's thread