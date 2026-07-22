import os  # borrows tools for reading settings from the computer's environment
from typing import TypedDict, Annotated, Literal, cast  # borrows tools for describing shapes, adding rules, fixed choices, and type hints
from operator import add  # borrows the plus action so lists can be joined together
from pydantic import BaseModel  # borrows a tool for making tidy data containers with checks
from dotenv import load_dotenv  # borrows a tool that loads secret settings from a hidden file
from langchain.chat_models import init_chat_model  # borrows a tool that sets up a connection to an AI chat model
from langgraph.graph import StateGraph, START, END  # borrows the pieces we need to build and mark the start and finish of our flow
from langgraph.types import Send  # borrows a tool that fans out work to run the same step many times at once

load_dotenv()  # loads the secret settings so the program can use them
model = init_chat_model(  # sets up the AI chat model we will talk to, using the settings below
    os.environ.get("MODEL", "google/gemini-3.1-flash-lite"),
    model_provider="openrouter",
    temperature=0,
)

class S(TypedDict):  # describes what our shared box of info looks like and what it holds
    applicants: list  # the full list of people applying for a loan
    results: Annotated[list, add] # every worker adds its verdict here

class Verdict(BaseModel):  # a tidy container that holds one loan decision
    decision: Literal["approve", "review", "decline"]  # the decision must be one of these three exact choices

def dispatch(state):  # a step that hands each applicant off to its own scoring run
    return [Send("score_one", a) for a in state["applicants"]]  # makes one scoring job per applicant so they can all be judged separately

def score_one(state):  # a step that decides the loan verdict for a single applicant
    verdict = cast(Verdict, model.with_structured_output(Verdict).invoke(  # asks the AI for this person's verdict in a tidy form
        f"Loan verdict for {state['name']}: {state['profile']}"
    ))
    return {"results": [f"{state['name']}: {verdict.decision}"]}  # adds this person's name and decision to the shared results list

b = StateGraph(S)  # starts a new empty flow that uses our shared box shape
b.add_node("score_one", score_one)  # adds the single-applicant scoring step to the flow and names it
b.add_conditional_edges(START, dispatch, ["score_one"])  # from the start, uses dispatch to fan out one scoring run per applicant
b.add_edge("score_one", END)  # connects the scoring step to the finish
graph = b.compile()  # finalizes the flow so it is ready to be run

people = [  # a list of sample applicants, each with a name and profile
    {"name": "Sanju", "profile": "Income: 2 lakhs/month, CIBIL Score: 780"},
    {"name": "Shivam", "profile": "Income: 1 lakh/month, CIBIL Score: 650"},
    {"name": "Sachin", "profile": "Income: 3 lakhs/month, CIBIL Score: 720"},
]

print(graph.invoke({"applicants": people, "results": []})["results"])  # runs the flow over all applicants and shows the list of verdicts
