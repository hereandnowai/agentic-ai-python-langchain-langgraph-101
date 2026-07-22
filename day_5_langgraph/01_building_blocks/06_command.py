import os  # borrows tools for reading settings from the computer's environment
from typing import TypedDict, NotRequired, Literal, cast  # borrows tools for describing shapes, optional fields, fixed choices, and type hints
from pydantic import BaseModel  # borrows a tool for making tidy data containers with checks
from dotenv import load_dotenv  # borrows a tool that loads secret settings from a hidden file
from langchain.chat_models import init_chat_model  # borrows a tool that sets up a connection to an AI chat model
from langgraph.graph import StateGraph, START, END  # borrows the pieces we need to build and mark the start and finish of our flow
from langgraph.types import Command  # borrows a tool that lets a step both update info and choose where to go next

load_dotenv()  # loads the secret settings so the program can use them
model = init_chat_model(  # sets up the AI chat model we will talk to, using the settings below
    os.environ.get("MODEL", "google/gemini-3.1-flash-lite"),
    model_provider="openrouter",
    temperature=0,
)

class S(TypedDict):  # describes what our shared box of info looks like and what it holds
    request: str  # the loan request from the customer, written as text
    decision: NotRequired[str]  # the approve-or-reject outcome, which may or may not be filled in yet
    reason: NotRequired[str]  # the short reason for the decision, which may or may not be filled in yet

class Verdict(BaseModel):  # a tidy container that holds the decision and its reason
    decision: Literal["approve", "reject"]  # the decision must be either approve or reject
    reason: str  # a short explanation for the decision, written as text

def triage(state) -> Command[Literal["approve", "reject"]]:  # a step that judges the loan and then decides where to go next
    verdict = cast(Verdict, model.with_structured_output(Verdict).invoke(  # asks the AI to approve or reject with a reason in a tidy form
        "Approve or reject this loan, with a short reason:\n:" + state["request"]
    ))
    return Command(update=verdict.model_dump(), goto=verdict.decision)  # saves the AI's decision and reason, then jumps to the matching approve or reject step

def approve(state):  # the approve step that does nothing extra here
    return {}  # hands back nothing new to add

def reject(state):  # the reject step that does nothing extra here
    return {}  # hands back nothing new to add

b = StateGraph(S)  # starts a new empty flow that uses our shared box shape
b.add_node("triage", triage)  # adds the triage step to the flow and names it
b.add_node("approve", approve)  # adds the approve step to the flow and names it
b.add_node("reject", reject)  # adds the reject step to the flow and names it
b.add_edge(START, "triage")  # connects the very beginning to the triage step
b.add_edge("approve", END)  # connects the approve step to the finish
b.add_edge("reject", END)  # connects the reject step to the finish
graph = b.compile()  # finalizes the flow so it is ready to be run

print(graph.invoke({"request": "I want to apply for a home loan of 30 lakhs, My income is 2 lakhs/month, CIBIL Score is 780."}))  # runs the flow with a sample loan request and shows the result
