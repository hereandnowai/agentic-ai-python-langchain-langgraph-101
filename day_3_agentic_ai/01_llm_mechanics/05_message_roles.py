import os
from openai import OpenAI
from dotenv import load_dotenv
from openai.types.chat import ChatCompletionMessageParam # label describing the role of the message

# Load environment variables from .env file
load_dotenv()

api_key = os.environ.get("OPENROUTER_API_KEY")
if not api_key:
    raise SystemExit(
        "OPENROUTER_API_KEY not found in environment variables.\n"
        "Copy .env.example to .env in the content root and add your key"
        )

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)
# MODEL = os.environ.get("MODEL", "openai/gpt-oss-120b") # The model to use for the API call
MODEL = "openai/gpt-4o-mini" # The model to use for the API call

def ask(messages: list[ChatCompletionMessageParam]) -> str:
    resp = client.chat.completions.create(model=MODEL, messages=messages, temperature=0.0)
    return resp.choices[0].message.content or ""

messages: list[ChatCompletionMessageParam] = [
    {"role": "system", "content": "you are Meridian banks assistant answer briefly"
                                  "if asked for legal or tax advice decline politely"},
    {"role": "user", "content": "what documents do I need for a home loan?"}
]
answer1 = ask(messages)
print("assistant: ", answer1)

messages.append({"role": "assistant", "content": answer1})
messages.append({"role": "user", "content": "and is the interest rate fixed or floating?"})
answer2 = ask(messages)
print("\nassistant: ", answer2)

messages.append({"role": "assistant", "content": answer2})
messages.append({"role": "user", "content": "Give me tax advice to reduce my liability"})
print("\nassistant: ", ask(messages))
