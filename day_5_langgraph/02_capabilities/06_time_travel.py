from typing import TypedDict, Annotated  # tools to describe the shape of our data
from operator import add  # the plus action, used here to join lists together
from langgraph.graph import StateGraph, START, END  # building blocks for a step-by-step flow
from langgraph.checkpoint.memory import InMemorySaver  # remembers progress in the computer's memory
from langchain_core.runnables import RunnableConfig  # a settings bag we pass along with each run

class S(TypedDict):  # describes what our shared data looks like
    steps: Annotated[list, add]  # a growing list of the steps that have run

def a(state):  # the first step
    return {"steps": ["a"]}  # records that step a ran

def b(state):  # the second step
    return {"steps": ["b"]}  # records that step b ran

def c(state):  # the third step
    return {"steps": ["c"]}  # records that step c ran

g = StateGraph(S)  # starts building the flow using our data shape
g.add_node("a", a)  # adds the first step, named "a"
g.add_node("b", b)  # adds the second step, named "b"
g.add_node("c", c)  # adds the third step, named "c"
g.add_edge(START, "a")  # says the flow begins at step a
g.add_edge("a", "b")  # says a goes to b next
g.add_edge("b", "c")  # says b goes to c next
g.add_edge("c", END)  # says the flow finishes after c
graph = g.compile(checkpointer=InMemorySaver())  # finishes the flow and lets it remember progress

cfg: RunnableConfig = {"configurable": {"thread_id": "run-1"}}  # a name tag for this one run
graph.invoke({"steps": []}, cfg)  # runs the whole flow starting with an empty steps-list

history = list(graph.get_state_history(cfg))  # collects every saved snapshot of the run
for snap in history:  # goes through each saved snapshot one by one
    print("steps so far:", snap.values.get("steps"))  # shows the steps recorded at that snapshot
print("total checkpoints you could rewind to: ", len(history))  # shows how many snapshots we could go back to