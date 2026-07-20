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

client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)

MODEL = os.environ.get("MODEL", "openai/gpt-oss-120b") # The model to use for the API call

messages: list[ChatCompletionMessageParam] = [ # list of messages to send to the model
    {"role": "system", "content": "You are a friendly banking assistant. Answer in one or two short sentences."}]

print("=== Chatbot With Memory ===")
print("Type 'history' to see the transcript of the conversation so far, or 'quit' to exit the chatbot.\n")
while True:
    user_input = input("You: ").strip()
    if not user_input:
        continue
    if user_input.lower() in {"quit", "exit"}:
        print("Exiting chatbot. Goodbye!")
        break
    if user_input.lower() == "history":
        print(f"\n--- what we send to the model every turn ---")
        for msg in messages:
            print(f" {msg['role']:>9}: {str(msg.get('content'))[:70]}")
        print(f"--- {len(messages)} messages in total ---\n")
        continue
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.0,
      )
    reply = response.choices[0].message.content or ""
    messages.append({"role": "assistant", "content": reply})
    print(f"Caramel AI: {reply}\n")






