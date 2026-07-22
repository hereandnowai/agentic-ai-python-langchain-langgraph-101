from typing import TypedDict, NotRequired  # tools to describe our data, with some optional parts
from langgraph.graph import StateGraph, START, END  # building blocks for a step-by-step flow

class S(TypedDict):  # describes what our shared data looks like
    applicant: str  # the name of the person applying
    kyc_ok: NotRequired[bool]  # whether the identity check passed, filled in later
    decision: NotRequired[str]  # the final approve-or-reject decision, filled in later

def check_id(state):  # a step that checks the applicant's identity
    return {"kyc_ok": True}  # marks the identity check as passed

# subgraph
sub = StateGraph(S)  # starts building a small inner flow for the identity check
sub.add_node("check_id", check_id)  # adds the identity-check step
sub.add_edge(START, "check_id")  # says the inner flow begins at the identity check
sub.add_edge("check_id", END)  # says the inner flow finishes after the identity check
kyc = sub.compile()  # finishes the inner flow so it can be reused as one block

def decide(state):  # a step that decides based on the identity check
    return {"decision": "approved" if state["kyc_ok"] else "rejected"}  # approves if the check passed, else rejects

# parent graph
parent = StateGraph(S)  # starts building the main flow using our data shape
parent.add_node("kyc", kyc)  # plugs the whole inner flow in as one step named "kyc"
parent.add_node("decide", decide)  # adds the decision step
parent.add_edge(START, "kyc")  # says the main flow begins with the identity check
parent.add_edge("kyc", "decide")  # says after the check we go to the decision
parent.add_edge("decide", END)  # says the main flow finishes after the decision
graph = parent.compile()  # finishes building the main flow so it is ready to run

print(graph.invoke({"applicant": "Alice"}))  # runs the whole flow for Alice and prints the result