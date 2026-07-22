# what is a state?
# A state is a representation of the current condition or status of a system,
# object, or process at a specific point in time. It encompasses all relevant
# information that defines the system's behavior and characteristics, allowing
# for predictions and decisions based on that information. In programming and
# computer science, a state often refers to the values of variables, data structures,
# or objects that determine how a program operates at any given moment.

# state in langgraph!
# state is one shared box of information that all nodes can read from and write to.
# It is a shared memory space that allows nodes to communicate and share data with each other.
# The state can be used to store information about the current status of the system,
# such as the values of variables, the results of computations, or any other relevant data.
# By using a shared state, nodes can collaborate and coordinate their actions, enabling more
# complex and dynamic behaviors in the system.

from typing import TypedDict, NotRequired  # borrows tools for describing the shape of our shared box of info
from langgraph.graph import StateGraph, START, END  # borrows the pieces we need to build and mark the start and finish of our flow

class LoadState(TypedDict):  # describes what our shared box of info looks like and what it holds
    applicant: str  # the name of the person, written as text
    income: float  # how much money the person earns, as a number with decimals
    emi: float  # the monthly loan payment amount, as a number with decimals
    ratio: NotRequired[float]  # the payment-to-income ratio, which may or may not be filled in yet

def compute_ratio(state):  # a step that works out the payment-to-income ratio from the current info
    return {"ratio": round(state["emi"] / state["income"], 2)}  # divides payment by income, rounds to 2 decimals, and hands it back

b = StateGraph(LoadState)  # starts a new empty flow that uses our shared box shape
b.add_node("compute_ratio", compute_ratio)  # adds our ratio step to the flow and names it
b.add_edge(START, "compute_ratio")  # connects the very beginning to the ratio step
b.add_edge("compute_ratio", END)  # connects the ratio step to the finish
graph = b.compile()  # finalizes the flow so it is ready to be run

print(graph.invoke({"applicant": "John", "income": 50000, "emi": 1500}))  # runs the flow with John's details and shows the result on screen
