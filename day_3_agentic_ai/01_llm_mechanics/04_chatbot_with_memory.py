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

client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)  # sets up the connection to the AI service

MODEL = os.environ.get("MODEL", "openai/gpt-oss-120b") # The model to use for the API call

messages: list[ChatCompletionMessageParam] = [ # list of messages to send to the model
    {"role": "system", "content": "You are a friendly banking assistant. Answer in one or two short sentences."}]

print("=== Chatbot With Memory ===")  # prints a title for the chatbot
print("Type 'history' to see the transcript of the conversation so far, or 'quit' to exit the chatbot.\n")  # explains the commands the user can type
while True:  # keeps repeating the chat over and over until we tell it to stop
    user_input = input("You: ").strip()  # waits for the user to type something and cleans off extra spaces
    if not user_input:  # checks whether the user typed nothing
        continue  # goes back to the top to ask again
    if user_input.lower() in {"quit", "exit"}:  # checks if the user typed quit or exit
        print("Exiting chatbot. Goodbye!")  # says goodbye
        break  # leaves the repeating chat loop
    if user_input.lower() == "history":  # checks if the user asked to see the conversation so far
        print(f"\n--- what we send to the model every turn ---")  # prints a heading for the history
        for msg in messages:  # goes through each saved message one by one
            print(f" {msg['role']:>9}: {str(msg.get('content'))[:70]}")  # shows who said it and the first part of the text
        print(f"--- {len(messages)} messages in total ---\n")  # shows how many messages are saved
        continue  # goes back to the top without asking the AI
    messages.append({"role": "user", "content": user_input})  # saves the user's new message to the memory list
    response = client.chat.completions.create(  # sends the whole conversation to the AI and waits for its reply
        model=MODEL,
        messages=messages,
        temperature=0.0,
      )
    reply = response.choices[0].message.content or ""  # takes the AI's answer text, or an empty string if none
    messages.append({"role": "assistant", "content": reply})  # saves the AI's answer to the memory list too
    print(f"Caramel AI: {reply}\n")  # shows the AI's answer on the screen






