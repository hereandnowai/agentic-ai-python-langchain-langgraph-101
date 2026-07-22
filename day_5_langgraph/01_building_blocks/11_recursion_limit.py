from typing import TypedDict  # borrows a tool for describing the shape of our shared box of info
from langgraph.graph import StateGraph, START, END  # borrows the pieces we need to build and mark the start and finish of our flow
from langgraph.errors import GraphRecursionError  # borrows the special warning raised when a flow loops too many times

class S(TypedDict):  # describes what our shared box of info looks like and what it holds
    count: int  # a whole number counter

def tick(state):  # a step that does nothing but exist so we can loop on it
    return  # hands back nothing

def loop_back(state):  # a decision step that always sends the flow back to tick
    return "tick"  # always points to the tick step, creating an endless loop

b = StateGraph(S)  # starts a new empty flow that uses our shared box shape
b.add_node("tick", tick)  # adds the tick step to the flow and names it
b.add_edge(START, "tick")  # connects the very beginning to the tick step
b.add_conditional_edges("tick", loop_back, ["tick"])  # after tick, uses loop_back to keep returning to tick over and over
graph = b.compile()  # finalizes the flow so it is ready to be run

try:  # tries the risky code below and watches for a problem
    graph.invoke({"count": 0}, {"recursion_limit": 5})  # runs the looping flow but caps it at 5 rounds to avoid running forever
except GraphRecursionError:  # catches the warning that fires when the 5-round cap is reached
    print("Stopped by recursion limit=5 - the seatbelt worked, no infinite loop!")  # shows a message confirming the safety cap stopped the endless loop
