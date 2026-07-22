from dataclasses import dataclass  # borrows a shortcut for making simple containers that hold named values
from typing import TypedDict, NotRequired  # borrows tools for describing shapes and marking fields that may be empty
from langgraph.graph import StateGraph, START, END  # borrows the pieces we need to build and mark the start and finish of our flow
from langgraph.runtime import Runtime  # borrows a tool that gives steps access to extra settings passed in at run time

@dataclass  # marks the next class as a simple container of named values
class Ctx:  # a container that holds settings we pass in when running the flow
    fee_rate: float  # the fee percentage to charge, as a number with decimals

class S(TypedDict):  # describes what our shared box of info looks like and what it holds
    amount: float  # the money amount, as a number with decimals
    fee: NotRequired[float]  # the calculated fee, which may or may not be filled in yet

def charge(state, runtime: Runtime[Ctx]):  # a step that works out the fee using the amount and the passed-in fee rate
    return {"fee": state["amount"] * runtime.context.fee_rate}  # multiplies the amount by the fee rate and hands back the fee

b = StateGraph(S, context_schema=Ctx)  # starts a new flow and tells it what extra run-time settings to expect
b.add_node("charge", charge)  # adds the charge step to the flow and names it
b.add_edge(START, "charge")  # connects the very beginning to the charge step
b.add_edge("charge", END)  # connects the charge step to the finish
graph = b.compile()  # finalizes the flow so it is ready to be run

print(graph.invoke({"amount": 100000}, context=Ctx(fee_rate=0.005)))  # runs the flow with a 0.5% fee rate and shows the result
print(graph.invoke({"amount": 100000}, context=Ctx(fee_rate=0.010)))  # runs the flow with a 1% fee rate and shows the result
