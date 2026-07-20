import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() # reads the .env file and loads the environment variables

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"]
)

MODEL = "openai/gpt-4o-mini"  # The model to use for the API call

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a concise banking assistant."},
        {"role": "user", "content": "In one sentence, explain what a home loan EMI is."}
    ]
)

print("Caramel AI: ", response.choices[0].message.content)


