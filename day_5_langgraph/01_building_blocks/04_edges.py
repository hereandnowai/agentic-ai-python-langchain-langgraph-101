# What is an edge in langgraph?
# An edge in langgraph is a connection between two nodes that defines the flow of data and
# the order of execution within a graph. It represents a directed relationship between
# the source node (the starting point) and the target node (the endpoint).

from typing import TypedDict, Annotated  # borrows tools for describing the shape of our shared box and adding special rules to it
from operator import add  # borrows the plus action so lists can be joined together
from langgraph.graph import StateGraph, START, END  # borrows the pieces we need to build and mark the start and finish of our flow

class S(TypedDict):  # describes what our shared box of info looks like and what it holds
    steps: Annotated[list, add] # 'add' is a reducer -> new items appended to the list

def intake(state):  # a step that records that the intake stage happened
    return {"steps": ["intake"]}  # adds the word "intake" to the running list of steps

def price(state):  # a step that records that the pricing stage happened
    return {"steps": ["price"]}  # adds the word "price" to the running list of steps

def notify(state):  # a step that records that the notify stage happened
    return {"steps": ["notify"]}  # adds the word "notify" to the running list of steps

b = StateGraph(S)  # starts a new empty flow that uses our shared box shape
b.add_node("intake", intake)  # adds the intake step to the flow and names it
b.add_node("price", price)  # adds the price step to the flow and names it
b.add_node("notify", notify)  # adds the notify step to the flow and names it
b.add_edge(START, "intake")  # connects the very beginning to the intake step
b.add_edge("intake", "price")  # connects the intake step to the price step
b.add_edge("price", "notify")  # connects the price step to the notify step
b.add_edge("notify", END)  # connects the notify step to the finish
graph = b.compile()  # finalizes the flow so it is ready to be run

print(graph.invoke({"steps": []})["steps"])  # runs the flow starting with an empty list and shows the list of steps taken
