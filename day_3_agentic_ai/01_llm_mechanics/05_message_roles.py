import os  # lets us read settings from the computer, like secret keys
from openai import OpenAI  # brings in the tool that talks to the AI service
from dotenv import load_dotenv  # brings in a helper that reads a hidden settings file
from openai.types.chat import ChatCompletionMessageParam # label describing the role of the message

# Load environment variables from .env file
load_dotenv()  # reads the hidden settings file so the secret key becomes available

api_key = os.environ.get("OPENROUTER_API_KEY")  # fetches the secret key and puts it in a box
if not api_key:  # checks whether the key was missing
    raise SystemExit(  # stops the program and shows the message below
        "OPENROUTER_API_KEY not found in environment variables.\n"
        "Copy .env.example to .env in the content root and add your key"
        )

client = OpenAI(  # sets up the connection to the AI service using the address and secret key below
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)
# MODEL = os.environ.get("MODEL", "openai/gpt-oss-120b") # The model to use for the API call
MODEL = "openai/gpt-4o-mini" # The model to use for the API call

def ask(messages: list[ChatCompletionMessageParam]) -> str:  # makes a reusable recipe that sends messages to the AI and returns its answer
    resp = client.chat.completions.create(model=MODEL, messages=messages, temperature=0.0)  # sends the messages to the AI and waits for its reply
    return resp.choices[0].message.content or ""  # hands back the AI's answer text, or an empty string if none

messages: list[ChatCompletionMessageParam] = [  # makes the starting list of messages for the conversation
    {"role": "system", "content": "you are Meridian banks assistant answer briefly"
                                  "if asked for legal or tax advice decline politely"},
    {"role": "user", "content": "what documents do I need for a home loan?"}
]
answer1 = ask(messages)  # asks the AI the first question and saves its answer
print("assistant: ", answer1)  # shows the AI's first answer on the screen

messages.append({"role": "assistant", "content": answer1})  # adds the AI's answer back into the conversation
messages.append({"role": "user", "content": "and is the interest rate fixed or floating?"})  # adds the user's follow-up question
answer2 = ask(messages)  # asks the AI again with the growing conversation and saves the answer
print("\nassistant: ", answer2)  # shows the AI's second answer on the screen

messages.append({"role": "assistant", "content": answer2})  # adds the second answer back into the conversation
messages.append({"role": "user", "content": "Give me tax advice to reduce my liability"})  # adds a question the AI should politely decline
print("\nassistant: ", ask(messages))  # asks the AI once more and shows its answer right away
