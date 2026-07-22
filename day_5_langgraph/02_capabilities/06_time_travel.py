from typing import TypedDict, Annotated
from operator import add
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.runnables import RunnableConfig

class S(TypedDict):
    steps: Annotated[list, add]

def a(state):
    return {"steps": ["a"]}

def b(state):
    return {"steps": ["b"]}

def c(state):
    return {"steps": ["c"]}

g = StateGraph(S)
g.add_node("a", a)
g.add_node("b", b)
g.add_node("c", c)
g.add_edge(START, "a")
g.add_edge("a", "b")
g.add_edge("b", "c")
g.add_edge("c", END)
graph = g.compile(checkpointer=InMemorySaver())

cfg: RunnableConfig = {"configurable": {"thread_id": "run-1"}}
graph.invoke({"steps": []}, cfg)

history = list(graph.get_state_history(cfg))
for snap in history:
    print("steps so far:", snap.values.get("steps"))
print("total checkpoints you could rewind to: ", len(history))