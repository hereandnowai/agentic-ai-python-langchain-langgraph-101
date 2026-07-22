import os  # brings in tools to read settings from the computer, like secret keys
from importlib import import_module  # brings in a way to load another Python file by its name
from langchain.chat_models import init_chat_model  # brings in a helper that sets up a chat AI model
from langchain_core.prompts import ChatPromptTemplate  # brings in a way to build reusable message templates with blanks to fill
from dotenv import load_dotenv  # brings in a helper that loads secret settings from a file

load_dotenv()  # reads the hidden .env file so secret keys become available
MODEL = os.environ.get("MODEL", "gpt-4o-mini")  # picks which AI model to use, with a default if none is set
ingest = import_module("01_ingestion_chunking")  # loads the earlier file so we can reuse its recipes
store = ingest.build_strore()  # builds and fills the storage box using that file's recipe
model = init_chat_model(MODEL, model_provider="openrouter", temperature=0.0)  # gets the chat AI ready, set to give steady, non-random answers

GROUNDED_PROMPT = ChatPromptTemplate.from_messages([  # builds the instructions telling the AI to answer only from the given context
    ("system",
     "You are Meridian Bank's assistant. Answers questions USING ONLY the context below."
     "cite the source ID in square brackets after each fact, example: [hl-001]."
     "if the context does not contain the answer reply exactly:"
     "\"I don't have that in our policy I'll escalate to a human.\""
     "Do not use outside knowledge.\n\n"
     "CONTEXT:\n{context}\n\n"),
     ("user", "{question}")
    ]
)

def format_context(docs) -> str:  # a recipe that joins the found chunks into one labeled block of text
    return "n".join(f" [{d.metadata['id']}] {d.page_content}" for d in docs)  # sticks each chunk's label and text together into a single string

def answer(question: str) -> str:  # a recipe that finds relevant chunks and asks the AI for a grounded answer
    docs = store.similarity_search(question, k=3)  # finds the three closest chunks to the question
    chain = GROUNDED_PROMPT | model  # links the instructions and the AI into one pipeline
    return chain.invoke({"context": format_context(docs), "question": question}).text  # fills in the context and question, runs it, and returns the reply text

# In-policy quesiton -> cited answer
print("Q: what documents do I need for a home loan?")  # prints the first test question
print("A:", answer("what documents do I need for a home loan?"), "\n")  # prints the AI's answer to that question

# Out-of-policy question -> fallback answer
print("Q: what is the interest rate on a car loan?")  # prints the second test question
print("A:", answer("what is the interest rate on a car loan?"))  # prints the AI's answer to that question
