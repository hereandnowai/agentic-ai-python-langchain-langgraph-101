import os  # lets us read settings from the computer, like secret keys
import json  # brings in a tool for handling data written as text
from openai import OpenAI  # brings in the tool that talks to the AI service
from dotenv import load_dotenv  # brings in a helper that reads a hidden settings file
from typing import cast  # brings in a helper that tells the type checker to relax about a value's type
from openai.types.chat import ChatCompletionMessageParam, ChatCompletionToolParam  # brings in labels for messages and tools

load_dotenv()  # Load environment variables from .env file

client = OpenAI(  # sets up the connection to the AI service using the address and secret key below
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"]
)
# MODEL = os.environ.get("MODEL", "openai/gpt-oss-120b")  # The model to use for the API call
MODEL = "openai/gpt-4o-mini"  # The model to use for the API call

# 1. A real python function we want the model to call
def calculate_emi(principal: float, annual_rate: float, years: int) -> dict:  # makes a reusable recipe that works out a monthly loan payment
    """Calculate the Equated Monthly Installment (EMI) for a loan."""
    r = annual_rate / 100 / 12  # monthly interest rate
    n = years * 12  # total number of monthly payments
    if r == 0:  # checks for the special case where there is no interest
        emi = principal / n  # simply splits the loan evenly across all the months
    else:  # runs when there is some interest
        emi = principal * r * (1 + r) ** n / ((1 + r) ** n - 1) # usual EMI formula
    return {"emi": round(emi, 2), "total_payment": round(emi * n, 2)}  # hands back the monthly payment and the grand total

# 2. Describe the tool to the model
tools: list[ChatCompletionToolParam] = [{  # describes our recipe to the AI so it knows the tool exists and how to use it
    "type": "function",
    "function": {
        "name": "calculate_emi",
        "description": "Calculate the Equated Monthly Installment (EMI) for a loan",
        "parameters": {
            "type": "object",
            "properties": {
                "principal": {"type": "number", "description": "loan amount in rupees"},
                "annual_rate": {"type": "number", "description": "annual interest rate in percentage"},
                "years": {"type": "integer", "description": "loan tenure in years"},
            },
            "required": ["principal", "annual_rate", "years"],
        },
    },
}]

messages: list[ChatCompletionMessageParam] = [  # makes the starting list of messages for the conversation
    {"role": "system", "content": "What is the EMI on 50 lakh home loan at 8.4 percentage for 25 years"}]

# 3 First call: the model decides to call the tool
first = client.chat.completions.create(model=MODEL, messages=messages, tools=tools)  # sends the question and the tool list to the AI
msg = first.choices[0].message  # takes the AI's reply out of the response

messages.append(cast(ChatCompletionMessageParam, msg))  # adds the AI's reply into the conversation

if msg.tool_calls:  # checks whether the AI asked to use our tool
    for tc in msg.tool_calls:  # goes through each tool request one by one
        if tc.type != "function":  # checks whether this request is not for a function
            continue  # skips it and moves to the next one
        args = json.loads(tc.function.arguments)  # turns the AI's text arguments into real values
        print("model wanst to call: ", tc.function.name, "with args: ", args)  # shows which tool the AI wants and with what values
        result = calculate_emi(**args)  # actually runs our recipe with those values

        # 4. return the result to the model in a new message
        messages.append({  # adds the tool's answer back into the conversation
            "role": "tool",
            "tool_call_id": tc.id,
            "content": json.dumps(result)
        })

# 5. Second call: the model now has the tool's output and can respond to the user
final = client.chat.completions.create(model=MODEL, messages=messages, tools=tools)  # asks the AI again, now that it can see the tool's answer
print("=== Final Response ===")  # prints a heading for the final answer
print(final.choices[0].message.content)  # shows the AI's final answer on the screen