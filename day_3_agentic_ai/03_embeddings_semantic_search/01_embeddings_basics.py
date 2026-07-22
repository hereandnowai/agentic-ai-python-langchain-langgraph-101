import os  # lets us read settings from the computer, like secret keys
from openai import OpenAI  # brings in the tool that talks to the AI service
from dotenv import load_dotenv  # brings in a helper that reads a hidden settings file

load_dotenv()  # Load environment variables from .env file
client = OpenAI(  # sets up the connection to the AI service using the address and secret key below
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"]
)
EMBEB_MODEL = os.environ.get("EMBED_MODEL", "openai/text-embedding-3-small")  # The model to use for the API call

def embed(text: str) -> list[float]:  # makes a reusable recipe that turns text into a list of numbers
    """return the embedding vector for a piece of text"""
    resp = client.embeddings.create(model=EMBEB_MODEL, input=text)  # sends the text to the AI to get its number version
    return resp.data[0].embedding  # hands back the list of numbers that stands for the text

vec = embed("home loan eligibility")  # turns the phrase into its list of numbers
print("text: 'home loan eligibility' => embedding vector length:")  # prints a label describing what comes next
print("vector dim: ", len(vec))  # shows how many numbers are in the list
print("first 5 dims: ", [round(x, 4) for x in vec[:5]])  # shows the first five numbers rounded off

resp = client.embeddings.create(  # sends two phrases at once to get number versions of both
    model=EMBEB_MODEL,
    input=["savings account interest", "how to block a stolen card"],
)
print("\nbatched embeddings: ", len(resp.data), "vectors, each dim", len(resp.data[0].embedding ))  # shows how many lists came back and how long each one is