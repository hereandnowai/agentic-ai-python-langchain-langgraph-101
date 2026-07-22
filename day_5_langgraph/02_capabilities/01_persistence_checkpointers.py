import os  # lets us read settings from the computer's environment
from dotenv import load_dotenv  # tool that loads secret settings from a file
from langchain.chat_models import init_chat_model  # helper to set up the AI chat model
from langchain_core.messages import HumanMessage  # a way to write a message as if from a person
from langgraph.graph import StateGraph, START, END, MessagesState  # building blocks for a chat flow
from langgraph.checkpoint.memory import InMemorySaver  # remembers past chats in the computer's memory
from langchain_core.runnables import RunnableConfig  # a settings bag we pass along with each run

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
graph = b.compile(checkpointer=InMemorySaver())  # finishes the flow and lets it remember past chats

alice: RunnableConfig = {"configurable": {"thread_id": "alice"}}  # a name tag for Alice's own chat thread
graph.invoke({"messages": [HumanMessage("Hi, my name is Alice.")]}, alice)  # Alice tells the AI her name
answer = graph.invoke({"messages": [HumanMessage("What is my name?")]}, alice)  # asks the AI to recall her name
print("same thread:", answer["messages"][-1].content)  # shows the AI's answer for Alice's thread

stranger: RunnableConfig = {"configurable": {"thread_id": "stranger"}}  # a name tag for a brand new chat thread
fresh = graph.invoke({"messages": [HumanMessage("What is my name?")]}, stranger)  # asks the same question on the new thread
print("new thread:", fresh["messages"][-1].content)  # shows the AI cannot recall a name it never heard