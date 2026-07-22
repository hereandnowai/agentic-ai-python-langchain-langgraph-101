import os  # lets us read settings from the computer's environment
from typing import cast  # lets us tell Python to treat a value as a certain type
from dotenv import load_dotenv  # tool that loads secret settings from a file
from langchain.chat_models import init_chat_model  # helper to set up the AI chat model
from langchain_core.messages import HumanMessage, BaseMessage  # a person's message and the general message type
from langgraph.graph import StateGraph, START, END, MessagesState  # building blocks for a chat flow

load_dotenv()  # reads the secret settings file so we can use it
model = init_chat_model(  # sets up the AI model we will chat with
    os.environ.get("MODEL", "google/gemini-3.1-flash-lite"),
    model_provider="openrouter",
    temperature=0,
)

def chat(state):  # a step that sends the chat so far to the AI and gets a reply
    return {"messages": [model.invoke(state["messages"])]}  # asks the AI and hands back its answer

b = StateGraph(MessagesState)  # starts building a chat flow that keeps a list of messages
b.add_node("chat", chat)  # adds our chat step and names it "chat"
b.add_edge(START, "chat")  # says the flow begins at the chat step
b.add_edge("chat", END)  # says the flow finishes after the chat step
graph = b.compile()  # finishes building the flow so it is ready to run

question: MessagesState = {"messages": [HumanMessage("Write a funny story on home loan!")]}  # the question we ask the AI
print("AI (streaming): ", end="", flush=True)  # prints a label without moving to a new line yet
for token, meta in graph.stream(question, stream_mode="messages"):  # gets the AI's reply piece by piece as it arrives
    print(cast(BaseMessage, token).content, end="", flush=True)  # prints each piece right away so it appears live
