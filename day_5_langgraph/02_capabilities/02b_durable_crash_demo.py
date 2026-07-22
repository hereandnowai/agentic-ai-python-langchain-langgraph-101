from typing import TypedDict, Annotated  # tools to describe the shape of our data
from operator import add  # the plus action, used here to join lists together
from langgraph.graph import StateGraph, START, END  # building blocks for a step-by-step flow
from langgraph.checkpoint.memory import InMemorySaver  # remembers progress in the computer's memory
from langchain_core.runnables import RunnableConfig  # a settings bag we pass along with each run

DEBITS = {"count": 0}  # a counter that tracks how many times money was taken out
NETWORK = {"down": True}  # a pretend switch saying the bank network is broken at first

class Payment(TypedDict):  # describes what our payment data looks like
    log: Annotated[list, add]  # a growing list of notes about what happened
    status: str  # a word describing where the payment is right now

def debit_payer(state):  # the step that takes money from the sender
    DEBITS["count"] += 1  # add one to the count of times money was taken
    return {"log": ["debited 500 from Simran"], "status": "processing"}  # notes the money left and marks it in progress

def credit_payee(state):  # the step that gives money to the receiver
    if NETWORK["down"]:  # checks if the pretend network is broken
        NETWORK["down"] = False  # fixes the network so the next try works
        raise RuntimeError("Bank Network timed out")  # crashes on purpose to mimic a failure
    return {"log": ["credited 500 to Virat"], "status": "success"}  # notes the money arrived and marks it done

b = StateGraph(Payment)  # starts building the payment flow using our data shape
b.add_node("debit_payer", debit_payer)  # adds the take-money step
b.add_node("credit_payee", credit_payee)  # adds the give-money step
b.add_edge(START, "debit_payer")  # says the flow begins by taking money
b.add_edge("debit_payer", "credit_payee")  # says after taking money we give money
b.add_edge("credit_payee", END)  # says the flow finishes after giving money
graph = b.compile(checkpointer=InMemorySaver())  # finishes the flow and lets it remember progress

cfg: RunnableConfig = {"configurable": {"thread_id": "txn-9001"}}  # a name tag for this one payment

# 1. User taps pay button, transaction initiated
try:  # tries to run the payment, ready to catch a crash
    graph.invoke({"log": [], "status": "initiated"}, cfg, durability="sync")  # runs the payment flow from the start
except RuntimeError as e:  # if it crashed, catch the error here
    print("BACKEND CRASHED:", e)  # tells us the backend crashed and why

# 2. What the user sees after the crash (money gone, screen frozen)
snap = graph.get_state(cfg).values  # reads the saved state after the crash
print("saved log        : ", snap["log"])  # shows the notes recorded so far
print("user sees status : ", snap["status"], " <-- money gone, but shows PROCESSING")  # shows the stuck status the user sees
print("time debited     : ", DEBITS["count"], "time")  # shows how many times money was taken so far

# 3. The System Resumes (auto-retry) and completes the payment
graph.invoke(None, cfg)  # runs the flow again, picking up where it crashed
snap = graph.get_state(cfg).values  # reads the saved state after finishing
print("after resume log : ", snap["log"])  # shows the full notes now that it finished
print("user sees status : ", snap["status"], " <-- money credited, shows SUCCESS")  # shows the finished success status
print("times debited    : ", DEBITS["count"], "time <-- debited only once, no double charge")  # shows money was taken only once


