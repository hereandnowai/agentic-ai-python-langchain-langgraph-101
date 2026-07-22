import os  # lets us read settings from the computer, like secret keys
from openai import OpenAI  # brings in the tool that talks to the AI service
from dotenv import load_dotenv  # brings in a helper that reads a hidden settings file

# Load environment variables from .env file
load_dotenv()  # reads the hidden settings file so the secret key becomes available

client = OpenAI(  # sets up the connection to the AI service using the address and secret key below
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"]
)

MODEL = "meta-llama/llama-3.1-8b-instruct"  # The model to use for the API call

PROMPT = "Give a name for a new savings account product. Replay with just the name, no other text."  # the question we will send to the AI

def generate(temperature: float, max_tokens: int = 20, stop=None):  # makes a reusable recipe that asks the AI and returns its answer
    resp = client.chat.completions.create(  # sends the request to the AI and waits for its reply
        model=MODEL,
        messages=[{"role": "user", "content": PROMPT}],
        temperature=temperature, # 0 = deterministic, 1 = more random / more varied answers
        top_p=1.0,               # nucleus sampling, 1.0 = no filtering
        max_tokens=max_tokens,   # hard cap on completion length, can be used to limit cost
        stop=stop
    )
    return (resp.choices[0].message.content or "").strip()  # hands back the AI's answer with extra spaces removed

print("=== temperature 0.0 (run 3x - expect near-identical) ===")  # prints a heading for the next test
for _ in range(3):  # repeats the next step three times
    print(" ", generate(0.0))  # asks the AI with no randomness and prints the answer

print("\n=== temperature 1.0 (run 3x - expect some variation) ===")  # prints a heading for the next test
for _ in range(3):  # repeats the next step three times
    print(" ", generate(1.0))  # asks the AI with high randomness and prints the answer

print("\n=== max_tokens=2 (truncates) ===")  # prints a heading for the next test
print(" ", generate(temperature=0.7, max_tokens=5))  # asks the AI but limits the answer to a few word-pieces