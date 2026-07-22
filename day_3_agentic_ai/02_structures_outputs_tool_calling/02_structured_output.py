import os  # lets us read settings from the computer, like secret keys
from openai import OpenAI  # brings in the tool that talks to the AI service
from pydantic import BaseModel, Field # tools for describing structured outputs
from dotenv import load_dotenv  # brings in a helper that reads a hidden settings file

load_dotenv() # reads the .env file and loads the environment variables

client = OpenAI(  # sets up the connection to the AI service using the address and secret key below
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"]
)
MODEL = os.environ.get("MODEL", "openai/gpt-oss-120b") # The model to use for the API call

# 1. Declare the exact shape you want back from the model using Pydantic models
class LoadEnquiry(BaseModel):  # describes the neat form we want the AI to fill in
    intent: str = Field(description="e.g. apply, enquire, complain")  # a text box for what the person wants to do
    product: str  # a text box for which product they mentioned
    amount: float | None = Field(default=None, description="loana amount if stated, else null")  # a number box for the money amount, or empty if not said
    tenure_years: int | None = None  # a number box for how many years, or empty if not said
    application_name: str | None = None  # a text box for the person's name, or empty if not said

message = ("Hi, I am Vaibhav Suryavanshi. I'd like to apply for a home loan of 50 lakhs for 20 years. ")  # the customer's message we want the AI to read

# 2. Ask for structured output from the model using the parse method, which will validate the output against the Pydantic model
completion = client.beta.chat.completions.parse(  # asks the AI and makes it fill in our neat form
    model=MODEL,
    messages=[{"role": "system", "content": "Extract the loan inquiry into the given schema. "
                                            "use now for anything not stated. Amount in rupees "
                                            "(e.g. 50 lakhs = 5000000). Return only the JSON object, no other text."},
              {"role": "user", "content": message}
               ],
    response_format=LoadEnquiry,
)

# 3. The output is now a Pydantic model instance, which you can access like a normal Python object
inquiry = completion.choices[0].message.parsed  # takes the filled-in form out of the AI's reply
if inquiry is None:  # checks whether the form failed to be filled in
    raise RuntimeError("Failed to parse the model output into the LoadEnquiry schema.")  # stops the program with an error message
print("parsed object: ", inquiry)  # shows the whole filled-in form
print("product      : ", inquiry.product)  # shows just the product from the form
print("amount       : ", inquiry.amount)  # shows just the money amount from the form
print("as JSON      : ", inquiry.model_dump_json(indent=2))  # shows the form written out as neat text