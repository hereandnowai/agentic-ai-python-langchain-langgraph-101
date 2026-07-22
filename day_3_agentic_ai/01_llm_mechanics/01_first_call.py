import os  # lets us read settings from the computer, like secret keys
from openai import OpenAI  # brings in the tool that talks to the AI service
from dotenv import load_dotenv  # brings in a helper that reads a hidden settings file

load_dotenv() # reads the .env file and loads the environment variables

client = OpenAI(  # sets up the connection to the AI service using the address and secret key below
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"]
)

# MODEL = "openai/gpt-4o-mini"  # The model to use for the API call
MODEL = "meta-llama/llama-3.1-8b-instruct"  # The model to use for the API call

response = client.chat.completions.create(  # sends our messages to the AI and waits for its reply
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a concise banking assistant built by Muthu Bank?"},
        {"role": "user", "content": "List ten benefits of a fixed deposit, briefly."}
    ]
)

print("Bot: ", response.choices[0].message.content)  # shows the AI's written answer on the screen

usage = response.usage  # grabs the info about how much work the AI did
if usage is not None:  # checks whether that usage info actually exists
    print("promt_tokens: ", usage.prompt_tokens)  # shows how many word-pieces our question used
    print("completion_tokens: ", usage.completion_tokens)  # shows how many word-pieces the answer used
    print("total_tokens: ", usage.total_tokens)  # shows the two counts added together
else:  # runs when there was no usage info
    print("Usage : Not available for this model.")  # tells us the counts were not provided

