from typing import TypedDict  # borrows a tool for describing the shape of our shared box of info
from langgraph.graph import StateGraph, START, END  # borrows the pieces we need to build and mark the start and finish of our flow

class S(TypedDict):  # describes what our shared box of info looks like and what it holds
    msg: str  # a single message, written as text

def process(state):  # a step that marks the message as processed
    return {"msg": "processed"}  # sets the message to the word "processed"

b = StateGraph(S)  # starts a new empty flow that uses our shared box shape
b.add_node("process", process)  # adds the process step to the flow and names it
b.add_edge(START, "process")  # connects the very beginning to the process step
b.add_edge("process", END)  # connects the process step to the finish
graph = b.compile()  # finalizes the flow so it is ready to be run

print(graph.invoke({"msg": "initial message"}))  # runs the flow with a starting message and shows the result
print("START node:", repr(START), "| END node:", repr(END))  # shows what the special start and finish markers actually look like inside
