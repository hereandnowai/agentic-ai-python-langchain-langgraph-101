import os  # brings in tools to read settings from the computer, like secret keys
from langchain.chat_models import init_chat_model  # brings in a helper that sets up a chat AI model
from langchain.messages import SystemMessage, HumanMessage  # brings in two ways to write messages: one for rules, one for the person
from dotenv import load_dotenv  # brings in a helper that loads secret settings from a file

load_dotenv()  # reads the hidden .env file so secret keys become available
MODEL = os.environ.get("MODEL", "openai/gpt-4o-mini")  # picks which AI model to use, with a default if none is set

model = init_chat_model(MODEL, model_provider="openrouter", temperature=0)  # gets the chat AI ready, set to give steady, non-random answers

response = model.invoke([  # sends the messages below to the AI and waits for its reply
    SystemMessage("You are a concise banking assistant"),
    HumanMessage("Answer in one sentence, what is a floating interest rate?")
])

print("type :", type(response).__name__)  # shows what kind of thing the reply is
print("content :", response.content)  # shows the actual words the AI replied with
print("tokens :", response.usage_metadata)  # shows how many word-pieces the request and reply used

print("\nstreaming: ", end="", flush=True)  # prints a label and keeps the line open for live text
for chunk in model.stream([HumanMessage("List two types of bank account briefly.")]):  # asks the AI and receives the answer piece by piece as it comes
    print(chunk.content, end="", flush=True)  # prints each small piece right away on the same line
print()  # prints a blank line to finish neatly



# langgraph - multi-agent - blog writing and publishing agent
# agent 1 - manager (opus)
# agent 2 - research + plan (opus)
# agent 3 - writing (gpt)
# agent 4 - editing (sonnet / gpt)
# agent 5 - publishing (sonnet)
# agent 6 - gemini (react, angular, nextjs) - antigravity

# OpenAI
# system message
# user message
# assistant message

# in LangChain
# SystemMessage
# HumanMessage
# AIMessage
