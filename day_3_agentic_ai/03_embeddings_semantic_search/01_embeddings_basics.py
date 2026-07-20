import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"]
)
EMBEB_MODEL = os.environ.get("EMBED_MODEL", "openai/text-embedding-3-small")  # The model to use for the API call

def embed(text: str) -> list[float]:
    """return the embedding vector for a piece of text"""
    resp = client.embeddings.create(model=EMBEB_MODEL, input=text)
    return resp.data[0].embedding

vec = embed("home loan eligibility")
print("text: 'home loan eligibility' => embedding vector length:")
print("vector dim: ", len(vec))
print("first 5 dims: ", [round(x, 4) for x in vec[:5]])

resp = client.embeddings.create(
    model=EMBEB_MODEL,
    input=["savings account interest", "how to block a stolen card"],
)
print("\nbatched embeddings: ", len(resp.data), "vectors, each dim", len(resp.data[0].embedding ))