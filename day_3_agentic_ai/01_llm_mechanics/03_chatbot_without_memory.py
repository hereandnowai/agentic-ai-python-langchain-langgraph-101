import os  # lets us read settings from the computer, like secret keys
from openai import OpenAI  # brings in the tool that talks to the AI service
from dotenv import load_dotenv  # brings in a helper that reads a hidden settings file

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

MODEL = os.environ.get("MODEL", "openai/gpt-oss-120b") # The model to use for the API call

SYSTEM_PROMPT = "You are a friendly banking assistant. Answer in one or two short sentences."  # the instructions that tell the AI how to behave

print("=== Chatbot WOM ===")  # prints a title for the chatbot
print("Type 'exit' to quit the chatbot.\n")  # tells the user how to stop the chatbot

while True:  # keeps repeating the chat over and over until we tell it to stop
    user_input = input("You: ").strip()  # waits for the user to type something and cleans off extra spaces
    if not user_input:  # checks whether the user typed nothing
        print("Please enter a message.")  # asks the user to type something
        continue  # goes back to the top to ask again
    if user_input.lower() in {"quit", "exit"}:  # checks if the user typed quit or exit
        print("Exiting chatbot. Goodbye!")  # says goodbye
        break  # leaves the repeating chat loop

    messages = [  # builds the fresh list of messages to send this turn (no past memory kept)
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_input}
    ]

    response = client.chat.completions.create(  # sends the messages to the AI and waits for its reply
        model=MODEL,
        messages=messages, # type: ignore
        temperature=0.0,
      )
    reply = response.choices[0].message.content or ""  # takes the AI's answer text, or an empty string if none
    print(f"Caramel AI: {reply}\n")  # shows the AI's answer on the screen