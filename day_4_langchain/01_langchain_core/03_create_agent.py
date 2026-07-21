import os
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool
from dotenv import load_dotenv
from langchain.messages import AIMessage

load_dotenv()
MODEL = os.environ.get("MODEL", "openai/gpt-4o-mini")
model = init_chat_model(MODEL, model_provider="openrouter", temperature=0)

# tool creation - a function with @tool decorator
@tool
def calculate_emi(principal: float, annual_rate: float, years: int) -> dict:
    """Calculate the monthly EMI and total payable for a loan.
    
    Args:
        principal (float): The principal loan amount in rupees.
        annual_rate (float): The annual interest rate in percentage (e.g. 8.4%).
        years (int): The loan tenure in years.
    """
    r = annual_rate / 100 / 12  # monthly interest rate
    n = years * 12  # total number of monthly payments
    emi = principal / n if r == 0 else principal * r * (1 + r) ** n / ((1 + r) ** n - 1) # the standard EMI formula
    return {"emi": round(emi, 2), "total_payable": round(emi * n, 2)}

# building the agent with the model and tools
agent = create_agent(
    model=model,
    tools=[calculate_emi],
    system_prompt="You are Meridian Bank's assistant. Use tools for emi calculation."
)

#invoke with a message dict; the agetn decides to call the tool
result = agent.invoke({
    "messages": [
        {"role": "user",
         "content": "what's the EMI on a 50 lakh loan at 8.4 percentage over 25 years"}]
})

# The full step trace lives in the result["messages"]
print("=== Step Trace ===")
for m in result["messages"]:
    kind = m.type
    if isinstance(m, AIMessage) and m.tool_calls:
        print(f"{kind} (tool call): {m.tool_calls[0]['name']}({m.tool_calls[0]['args']})")
    elif m.content:
        print(f"[{kind}] {m.content}")

print("\nfinal answer: ", result["messages"][-1].content)    