import os  # brings in tools to read settings from the computer, like secret keys
from langchain.chat_models import init_chat_model  # brings in a helper that sets up a chat AI model
from langchain_core.prompts import ChatPromptTemplate  # brings in a way to build reusable message templates with blanks to fill
from langchain_core.output_parsers import StrOutputParser  # brings in a helper that turns the AI reply into plain text
from pydantic import BaseModel, Field  # brings in tools to describe the shape of data we want back
from typing import cast  # brings in a helper that tells the editor what type something is
from dotenv import load_dotenv  # brings in a helper that loads secret settings from a file

load_dotenv()  # reads the hidden .env file so secret keys become available
MODEL = os.environ.get("MODEL", "openai/gpt-4o-mini")  # picks which AI model to use, with a default if none is set
model = init_chat_model(MODEL, model_provider="openrouter", temperature=0)  # gets the chat AI ready, set to give steady, non-random answers

# 1. prompt template with {placeholder}
prompt = ChatPromptTemplate.from_messages([  # builds a reusable message template with blanks to fill in later
    ("system", "You are Meridian Bank's assistant. Answer in one sentence."),
    ("user", "Explain '{term}' to a {audience}")
])

# 2. compose a chain with the pipe operator
chain = prompt | model | StrOutputParser()  # links the template, the AI, and the text cleaner into one pipeline
print(chain.invoke({"term": "EMI", "audience": "first-time borrower"}))  # fills the blanks, runs the pipeline, and prints the plain-text answer

# 3. structured output parsing with Pydantic
class LoanEnquiry(BaseModel):  # describes the neat form we want the answer to fit into
    intent: str  # a text field for what the person wants to do
    product: str  # a text field for which banking product they mean
    amount: float | None = Field(default=None, description="rupees; null if unstated")  # a number field for the money amount, empty if not said

structured_model = model.with_structured_output(LoanEnquiry)  # makes a version of the AI that must answer in that neat form
result = cast(LoanEnquiry, structured_model.invoke(  # sends the sentence to the AI and gets back a filled-in form
    "I'd like to apply for a home loan of about 50 lakhs."))
print("\nstructure:", result)  # shows the whole filled-in form
print("product:", result.product, "| amount:", result.amount)  # shows just the product and the amount from the form

extracted_chain = ChatPromptTemplate.from_messages([  # builds another template and joins it to the form-filling AI
    ("system", "extract the inquiry amounts in rupees (1 lakh = ₹100000.00). Null if unstated."),
    ("user", "{message}"),
]) | structured_model
print("\nchained: ", extracted_chain.invoke({"message": "Enquiring about a 30 lakh home loan."}))  # runs that pipeline and prints the filled-in form
