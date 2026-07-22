# what is a reducer in programming?
# A reducer is a function that takes an input (often an array or collection of data)
# and processes it to produce a single output value. It "reduces" the input data into
# a more concise form, often by applying a specific operation or transformation.
# Reducers are commonly used in functional programming and data processing tasks,
# such as aggregating values, filtering data, or transforming collections.

from typing import TypedDict, Annotated  # borrows tools for describing the shape of our shared box and adding special rules to it
from operator import add  # borrows the plus action so lists can be joined together
from langgraph.graph import StateGraph, START, END  # borrows the pieces we need to build and mark the start and finish of our flow

class S(TypedDict):  # describes what our shared box of info looks like and what it holds
    audit: Annotated[list, add] # 'add' is a reducer -> new items appended to the list
    status: str                 # no reducer -> new value overwrites the old value

def receive(state):  # a step that marks the item as received and under review
    return {"audit": ["received"], "status": "in_review"}  # adds "received" to the history list and sets the status to in review

def decide(state):  # a step that marks the item as approved
    return {"audit": ["approved"], "status": "approved"}  # adds "approved" to the history list and sets the status to approved

b = StateGraph(S)  # starts a new empty flow that uses our shared box shape
b.add_node("receive", receive)  # adds the receive step to the flow and names it
b.add_node("decide", decide)  # adds the decide step to the flow and names it
b.add_edge(START, "receive")  # connects the very beginning to the receive step
b.add_edge("receive", "decide")  # connects the receive step to the decide step
b.add_edge("decide", END)  # connects the decide step to the finish
graph = b.compile()  # finalizes the flow so it is ready to be run

print(graph.invoke({"audit": ["created"], "status": "new"}))  # runs the flow starting with a "created" history and "new" status, then shows the result
