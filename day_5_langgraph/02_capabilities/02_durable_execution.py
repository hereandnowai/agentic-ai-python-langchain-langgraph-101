# what is durable execution?
# Durable execution in langgraph refers to the ability of a graph to maintain
# its state and progress even in the face of interruptions or failures. This means that if a graph execution is paused, stopped, or encounters an error, it can be resumed from the last known state without losing any data or progress. Durable execution is particularly useful in long-running processes, workflows, or tasks that require reliability and fault tolerance.

from typing import TypedDict, Annotated  # tools to describe the shape of our data
from operator import add  # the plus action, used here to join lists together
from langgraph.graph import StateGraph, START, END  # building blocks for a step-by-step flow
from langgraph.checkpoint.memory import InMemorySaver  # remembers progress in the computer's memory
from langchain_core.runnables import RunnableConfig  # a settings bag we pass along with each run

class S(TypedDict):  # describes what our shared data looks like
    done: Annotated[list, add] # 'add' is a reducer -> new items appended to the list

def step_a(state):  # the first step in the flow
    return {"done": ["A"]}  # records that step A finished

def step_b(state):  # the second step in the flow
    return {"done": ["B"]}  # records that step B finished

b = StateGraph(S)  # starts building the flow using our data shape
b.add_node("step_a", step_a)  # adds the first step and names it "step_a"
b.add_node("step_b", step_b)  # adds the second step and names it "step_b"
b.add_edge(START, "step_a")  # says the flow begins at step_a
b.add_edge("step_a", "step_b")  # says step_a goes to step_b next
b.add_edge("step_b", END)  # says the flow finishes after step_b
graph = b.compile(checkpointer=InMemorySaver())  # finishes the flow and lets it remember progress

cfg: RunnableConfig = {"configurable": {"thread_id": "loan-42"}}  # a name tag for this particular run
graph.invoke({"done": []}, cfg, durablility="sync")  # runs the flow starting with an empty done-list
print("state read back from the checkpoint:", graph.get_state(cfg).values["done"])  # reads back the saved progress and shows it