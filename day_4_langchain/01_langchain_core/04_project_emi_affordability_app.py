import os  # brings in tools to read settings from the computer, like secret keys
from langchain.chat_models import init_chat_model  # brings in a helper that sets up a chat AI model
from langchain.agents import create_agent  # brings in a helper that builds an AI assistant that can use tools
from langchain.tools import tool  # brings in a tag that turns a normal function into a tool the AI can call
from dotenv import load_dotenv  # brings in a helper that loads secret settings from a file
import gradio as gr  # brings in a toolkit for making a simple web chat window

load_dotenv()  # reads the hidden .env file so secret keys become available
MODEL = os.environ.get("MODEL", "openai/gpt-4o-mini")  # picks which AI model to use, with a default if none is set
model = init_chat_model(MODEL, model_provider="openrouter", temperature=0)  # gets the chat AI ready, set to give steady, non-random answers

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
    return {"emi": round(emi, 2)}  # hands back the monthly payment, rounded to two decimals

@tool  # marks the function below as a tool the AI is allowed to use
def check_affordability(monthly_income: float, emi: float) -> dict:  # a recipe that checks if the payment fits the person's income
    """Check if the EMI is affordable based on the user's monthly income.

    Args:
        monthly_income (float): The user's monthly income in rupees.
        emi (float): The calculated EMI in rupees.
    """
    ratio = emi / monthly_income if monthly_income else 1.0  # works out what share of income the payment takes
    return {"emi_to_income": round(ratio, 2), "affordable": ratio <= 0.5}  # hands back that share and whether it is under half the income

agent = create_agent(  # creates the AI assistant and tells it which model and tools to use
    model,
    tools=[calculate_emi, check_affordability],
    system_prompt=("""You are Meridian Bank's assistant.
                    Use emi calculation tool for replayment maths
                    and affordability check tool to check if the emi is
                    affordable based on the user's monthly income.
                    Amount are in rupees (1 lakh = ₹100000.00).
                    Give factual guidance only - never regulatory or legal advice.""")
                    )

def respond(message, history):  # a recipe that answers one chat message using the past conversation
    messages = history + [{"role": "user", "content": message}]  # adds the new message onto the earlier chat history
    result = agent.invoke({"messages": messages})  # sends the whole conversation to the assistant and waits for the result
    return result["messages"][-1].content  # gives back just the assistant's latest reply

demo = gr.ChatInterface(  # builds the web chat window and connects it to the respond recipe
    respond,
    title="Meridian Bank EMI Affordability Assistant",
    description="Ask about EMI calculations and affordability checks for loans.",
    examples=[
        ["What's the EMI on a 50 lakh loan at 8.4% over 25 years?"],
        ["I earn 1.5 lakh per month - Can I afford a 30 lakh loan at 9% over 20 years?"],
])

if __name__ == "__main__":  # runs the part below only when this file is started directly
    demo.launch()  # opens the chat window in the browser
