# What is node in langgraph?
# A node in langgraph is a fundamental building block that
# represents a specific operation or computation within a graph.
# It encapsulates a function or a set of instructions that can be
# executed to process data and produce an output. Nodes can be connected
# to form a directed graph, allowing for the flow of information and the
# execution of complex workflows.

import os  # borrows tools for reading settings from the computer's environment
from typing import TypedDict, NotRequired, Literal, cast  # borrows tools for describing shapes, optional fields, fixed choices, and type hints
from pydantic import BaseModel  # borrows a tool for making tidy data containers with checks
from dotenv import load_dotenv  # borrows a tool that loads secret settings from a hidden file
from langchain.chat_models import init_chat_model  # borrows a tool that sets up a connection to an AI chat model
from langgraph.graph import StateGraph, START, END  # borrows the pieces we need to build and mark the start and finish of our flow

load_dotenv()  # loads the secret settings so the program can use them
model = init_chat_model(  # sets up the AI chat model we will talk to, using the settings below
    os.environ.get("MODEL", "google/gemini-3.1-flash-lite"),
    model_provider="openrouter",
    temperature=0,
)

class App(TypedDict):  # describes what our shared box of info looks like and what it holds
    message: str  # the customer's message, written as text
    intent: NotRequired[str]  # what the customer wants, which may or may not be filled in yet
    reply: NotRequired[str]  # the answer we will send back, which may or may not be filled in yet

class Intent(BaseModel):  # a tidy container that holds just the customer's intent
    intent: Literal["apply", "complain", "enquire"]  # the intent must be one of these three exact choices

def classify(state):  # a step that figures out what the customer wants from their message
    result = cast(Intent, model.with_structured_output(Intent).invoke(  # asks the AI to read the message and return the intent in a tidy form
        "Classify the customer's intent: " + state["message"]
    ))
    return {"intent": result.intent}  # hands back the intent the AI decided on

def respond(state):  # a step that picks the right reply based on the customer's intent
    replies = {  # a lookup table matching each intent to a ready-made reply
        "apply": "Starting your application process.",
        "complain": "Logging your complaint. We will get back to you shortly.",
        "enquire": "Here is the information you requested.",
    }
    return {"reply": replies[state["intent"]]}  # hands back the reply that matches the customer's intent

b = StateGraph(App)  # starts a new empty flow that uses our shared box shape
b.add_node("classify", classify)  # adds the classify step to the flow and names it
b.add_node("respond", respond)  # adds the respond step to the flow and names it
b.add_edge(START, "classify")  # connects the very beginning to the classify step
b.add_edge("classify", "respond")  # connects the classify step to the respond step
b.add_edge("respond", END)  # connects the respond step to the finish
graph = b.compile()  # finalizes the flow so it is ready to be run

print(graph.invoke({'message': "I want to open a home loan account."}))  # runs the flow with a sample customer message and shows the result
