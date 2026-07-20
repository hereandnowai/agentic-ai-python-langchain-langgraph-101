import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"]
)
MODEL = os.environ.get("MODEL", "openai/gpt-oss-120b") # The model to use for the API call

stream = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "List ten benefits of a fixed deposit, briefly."}],
    stream=True,  # Enable streaming
)

print("=== Streaming Chatbot ===", end="", flush=True)
collected = []
for chunk in stream:
    delta = chunk.choices[0].delta.content
    if delta:
        print(delta, end="", flush=True)
        collected.append(delta)

full_text = "".join(collected)
print("\n\nFull Response:", len(full_text), "characters")
 