import os
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from pydantic import SecretStr

load_dotenv()
EMBED_MODEL = os.environ.get("EMBED_MODEL", "openai/text-embedding-3-small")
embeddings = OpenAIEmbeddings(
    model=EMBED_MODEL,
    base_url="https://openrouter.ai/api/v1",
    api_key=SecretStr(os.environ["OPENROUTER_API_KEY"]),
    check_embedding_ctx_length=False,
)

vec = embeddings.embed_query("home loan eligibility")
print("text : 'home loan eligibility'")
print("vector dim : ", len(vec))
print("first 5 dims:", [round(x, 4) for x in vec[:5]])

docs = ["savings account interest", "how to block a stole card"]
docs_vecs = embeddings.embed_documents(docs)
print("\nbactched embeddings: ", len(docs_vecs), "vectors, each dim", len(docs_vecs[0]))