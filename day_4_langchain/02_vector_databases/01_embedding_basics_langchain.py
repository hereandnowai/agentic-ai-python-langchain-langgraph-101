import os  # brings in tools to read settings from the computer, like secret keys
from langchain_openai import OpenAIEmbeddings  # brings in a helper that turns text into lists of numbers
from dotenv import load_dotenv  # brings in a helper that loads secret settings from a file
from pydantic import SecretStr  # brings in a safe wrapper for holding secret text like a key

load_dotenv()  # reads the hidden .env file so secret keys become available
EMBED_MODEL = os.environ.get("EMBED_MODEL", "openai/text-embedding-3-small")  # picks which text-to-numbers model to use, with a default
embeddings = OpenAIEmbeddings(  # sets up the text-to-numbers helper with the settings below
    model=EMBED_MODEL,
    base_url="https://openrouter.ai/api/v1",
    api_key=SecretStr(os.environ["OPENROUTER_API_KEY"]),
    check_embedding_ctx_length=False,
)

vec = embeddings.embed_query("home loan eligibility")  # turns that phrase into a long list of numbers
print("text : 'home loan eligibility'")  # prints the original phrase for reference
print("vector dim : ", len(vec))  # prints how many numbers are in the list
print("first 5 dims:", [round(x, 4) for x in vec[:5]])  # prints the first five numbers, tidied to four decimals

docs = ["savings account interest", "how to block a stole card"]  # makes a list holding two short pieces of text
docs_vecs = embeddings.embed_documents(docs)  # turns both pieces of text into their own lists of numbers
print("\nbactched embeddings: ", len(docs_vecs), "vectors, each dim", len(docs_vecs[0]))  # prints how many lists were made and how long each one is
