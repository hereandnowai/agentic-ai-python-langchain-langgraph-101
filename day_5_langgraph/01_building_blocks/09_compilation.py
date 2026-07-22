from typing import TypedDict  # borrows a tool for describing the shape of our shared box of info
from langgraph.graph import StateGraph, START, END  # borrows the pieces we need to build and mark the start and finish of our flow

class S(TypedDict):  # describes what our shared box of info looks like and what it holds
    n: int  # a single whole number

def double(state):  # a step that doubles the number
    return {"n": state["n"] * 2}  # multiplies the current number by two and hands it back

builder = StateGraph(S)  # starts a new empty flow that uses our shared box shape
builder.add_node("double", double)  # adds the double step to the flow and names it
builder.add_edge(START, "double")  # connects the very beginning to the double step
builder.add_edge("double", END)  # connects the double step to the finish

print("before compile:", type(builder).__name__)  # shows the kind of thing the flow is before it is finalized
graph = builder.compile()  # finalizes the flow so it is ready to be run
print("after compile:", type(graph).__name__)  # shows the kind of thing the flow becomes after it is finalized

print(graph.invoke({"n": 21}))  # runs the flow with the number 21 and shows the result
print(graph.invoke({"n": 42}))  # runs the flow with the number 42 and shows the result
