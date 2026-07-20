import os
from openai import OpenAI
from dotenv import load_dotenv

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

MODEL = os.environ.get("MODEL", "openai/gpt-oss-120b") # The model to use for the API call

SYSTEM_PROMPT = "You are a friendly banking assistant. Answer in one or two short sentences."

print("=== Chatbot WOM ===")
print("Type 'exit' to quit the chatbot.\n")

while True:
    user_input = input("You: ").strip()
    if not user_input:
        print("Please enter a message.")
        continue
    if user_input.lower() in {"quit", "exit"}:
        print("Exiting chatbot. Goodbye!")
        break

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_input}
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages, # type: ignore
        temperature=0.0,
      )
    reply = response.choices[0].message.content or ""
    print(f"Caramel AI: {reply}\n")