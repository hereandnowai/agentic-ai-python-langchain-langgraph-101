import os  # lets us read settings from the computer, like secret keys
from openai import OpenAI  # brings in the tool that talks to the AI service
from dotenv import load_dotenv  # brings in a helper that reads a hidden settings file

# Load environment variables from .env file
load_dotenv()  # reads the hidden settings file so the secret key becomes available

client = OpenAI(  # sets up the connection to the AI service using the address and secret key below
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"]
)
MODEL = os.environ.get("MODEL", "openai/gpt-oss-120b") # The model to use for the API call

stream = client.chat.completions.create(  # asks the AI but requests the answer piece by piece as it is written
    model=MODEL,
    messages=[{"role": "user", "content": "List ten benefits of a fixed deposit, briefly."}],
    stream=True,  # Enable streaming
)

print("=== Streaming Chatbot ===", end="", flush=True)  # prints a heading and shows it right away
collected = []  # makes an empty list to hold the answer pieces as they arrive
for chunk in stream:  # goes through each small piece of the answer as it comes in
    delta = chunk.choices[0].delta.content  # takes the bit of new text from this piece
    if delta:  # checks that this piece actually has some text
        print(delta, end="", flush=True)  # prints the new bit right away without a line break
        collected.append(delta)  # saves the new bit into our list

full_text = "".join(collected)  # joins all the saved pieces into one complete answer
print("\n\nFull Response:", len(full_text), "characters")  # shows how many letters the whole answer had
 