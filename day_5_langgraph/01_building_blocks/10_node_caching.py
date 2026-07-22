import time  # borrows tools for pausing and measuring time
from typing import TypedDict, NotRequired  # borrows tools for describing shapes and marking fields that may be empty
from langgraph.graph import StateGraph, START, END  # borrows the pieces we need to build and mark the start and finish of our flow
from langgraph.types import CachePolicy  # borrows a tool that sets rules for remembering a step's past results
from langgraph.cache.memory import InMemoryCache  # borrows a memory box that keeps remembered results while the program runs

EXECUTIONS = {"count": 0}  # a little counter box that tracks how many times the slow step really ran

class S(TypedDict):  # describes what our shared box of info looks like and what it holds
    x: int  # the input whole number
    y: NotRequired[int]  # the result number, which may or may not be filled in yet

def slow_credit_check(state):  # a deliberately slow step that pretends to do a credit check
    EXECUTIONS["count"] += 1  # adds one to the counter each time this step actually runs
    time.sleep(2)  # waits two seconds to imitate slow work
    return {"y": state["x"] * 2}  # doubles the input number and hands it back

b = StateGraph(S)  # starts a new empty flow that uses our shared box shape
b.add_node("slow_credit_check", slow_credit_check, cache_policy=CachePolicy(ttl=120))  # adds the slow step and tells it to remember its result for 120 seconds
b.add_edge(START, "slow_credit_check")  # connects the very beginning to the slow step
b.add_edge("slow_credit_check", END)  # connects the slow step to the finish
graph = b.compile(cache=InMemoryCache())  # finalizes the flow and gives it a memory box for remembered results

graph.invoke({"x": 5})  # runs the flow with 5, which actually does the slow work once
graph.invoke({"x": 6})  # runs the flow with 6, which reuses a remembered result instead of redoing the slow work
print("times the slow node actually ran:", EXECUTIONS["count"], "(cached, so 1 not 2)")  # shows how many times the slow step truly ran, proving the memory saved a run
