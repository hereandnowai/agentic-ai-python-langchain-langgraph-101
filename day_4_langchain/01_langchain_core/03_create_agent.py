import os  # brings in tools to read settings from the computer, like secret keys
from langchain.chat_models import init_chat_model  # brings in a helper that sets up a chat AI model
from langchain.agents import create_agent  # brings in a helper that builds an AI assistant that can use tools
from langchain.tools import tool  # brings in a tag that turns a normal function into a tool the AI can call
from dotenv import load_dotenv  # brings in a helper that loads secret settings from a file
from langchain.messages import AIMessage  # brings in the type used for messages that come from the AI

load_dotenv()  # reads the hidden .env file so secret keys become available
MODEL = os.environ.get("MODEL", "openai/gpt-4o-mini")  # picks which AI model to use, with a default if none is set
model = init_chat_model(MODEL, model_provider="openrouter", temperature=0)  # gets the chat AI ready, set to give steady, non-random answers

# tool creation - a function with @tool decorator
@tool  # marks the function below as a tool the AI is allowed to use
def calculate_emi(principal: float, annual_rate: float, years: int) -> dict:  # a recipe that works out the monthly loan payment
    """Calculate the monthly EMI and total payable for a loan.

    Args:
        principal (float): The principal loan amount in rupees.
        annual_rate (float): The annual interest rate in percentage (e.g. 8.4%).
        years (int): The loan tenure in years.
    """
    r = annual_rate / 100 / 12  # monthly interest rate
    n = years * 12  # total number of monthly payments
    emi = principal / n if r == 0 else principal * r * (1 + r) ** n / ((1 + r) ** n - 1) # the standard EMI formula
    return {"emi": round(emi, 2), "total_payable": round(emi * n, 2)}  # hands back the monthly payment and the total, rounded to two decimals

# building the agent with the model and tools
agent = create_agent(  # creates the AI assistant and tells it which model and tools to use
    model=model,
    tools=[calculate_emi],
    system_prompt="You are Meridian Bank's assistant. Use tools for emi calculation."
)

#invoke with a message dict; the agetn decides to call the tool
result = agent.invoke({  # sends the person's question to the assistant and waits for the full result
    "messages": [
        {"role": "user",
         "content": "what's the EMI on a 50 lakh loan at 8.4 percentage over 25 years"}]
})

# The full step trace lives in the result["messages"]
print("=== Step Trace ===")  # prints a header before listing the steps
for m in result["messages"]:  # goes through each message that happened during the conversation
    kind = m.type  # notes what kind of message this is (person, AI, or tool)
    if isinstance(m, AIMessage) and m.tool_calls:  # checks if this is the AI deciding to use a tool
        print(f"{kind} (tool call): {m.tool_calls[0]['name']}({m.tool_calls[0]['args']})")  # shows which tool was called and with what numbers
    elif m.content:  # otherwise, if the message has any words in it
        print(f"[{kind}] {m.content}")  # shows the kind of message and its words

print("\nfinal answer: ", result["messages"][-1].content)    # prints the very last message, which is the assistant's final reply
