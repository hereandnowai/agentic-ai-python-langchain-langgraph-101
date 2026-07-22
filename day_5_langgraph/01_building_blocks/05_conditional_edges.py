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

class S(TypedDict):  # describes what our shared box of info looks like and what it holds
    message: str  # the customer's message, written as text
    reply: NotRequired[str]  # the answer we will send back, which may or may not be filled in yet

class Desk(BaseModel):  # a tidy container that holds which desk should handle the message
    desk: Literal["loans", "cards", "fraud"]  # the desk must be one of these three exact choices

def route(state):  # a step that decides which desk should deal with the message
    choice = cast(Desk, model.with_structured_output(Desk).invoke(  # asks the AI to pick the right desk in a tidy form
        "Which desk should handle this message:\n" + state["message"]
    ))
    return choice.desk  # hands back the name of the chosen desk to decide where to go next

def loans(state):  # the loans desk step that writes a loan-related reply
    return {"reply": "[loan desk] happy to help you with your loan application."}  # sets the reply to a friendly loan message

def cards(state):  # the cards desk step that writes a card-related reply
    return {"reply": "[card desk] let's assist you with your card-related query."}  # sets the reply to a friendly card message

def fraud(state):  # the fraud desk step that writes a fraud-related reply
    return {"reply": "[fraud desk] we'll secure your account and investigate the issue."}  # sets the reply to a reassuring fraud message

b = StateGraph(S)  # starts a new empty flow that uses our shared box shape
b.add_node("loans", loans)  # adds the loans desk step to the flow and names it
b.add_node("cards", cards)  # adds the cards desk step to the flow and names it
b.add_node("fraud", fraud)  # adds the fraud desk step to the flow and names it
b.add_conditional_edges(START, route, ["loans", "cards", "fraud"])  # from the start, uses the route decision to send the flow to one of the three desks
b.add_edge("loans", END)  # connects the loans desk step to the finish
b.add_edge("cards", END)  # connects the cards desk step to the finish
b.add_edge("fraud", END)  # connects the fraud desk step to the finish
graph = b.compile()  # finalizes the flow so it is ready to be run

for msg in ["I want to apply for a home loan.", "I lost my credit card.", "I think my account has been compromised."]:  # goes through each sample message one at a time
    print(msg, "-> ", graph.invoke({"message": msg})["reply"])  # runs the flow for the message and shows the message alongside its reply
