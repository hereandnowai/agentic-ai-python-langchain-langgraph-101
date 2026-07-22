import os  # brings in tools to read settings from the computer, like secret keys
import math  # brings in common math helpers like square root
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

def cosine_similarity(a: list[float], b: list[float]) -> float:  # a recipe that measures how alike two lists of numbers are
    """Compute the cosine similarity between two vectors."""
    dot = sum(x * y for x, y in zip(a, b))  # multiplies matching numbers and adds them all up
    norm_a = math.sqrt(sum(x * x for x in a))  # works out the overall length of the first list
    norm_b = math.sqrt(sum(y * y for y in b))  # works out the overall length of the second list
    return dot / (norm_a * norm_b) if norm_a and norm_b else 0.0  # gives back the closeness score, or zero if a list is empty

passages = [  # makes a list holding a few sentences to search through
    "Meridian home loans require a minimum credit score of 700",
    "savings accounts earn 3% interest, per annum"
    "Report a lost or stole stolen card immediately via the app"
]
query = "what credit score do I need to borrow a house?"  # the question we want to match against the sentences

passage_vecs = embeddings.embed_documents(passages)  # turns each sentence into its own list of numbers
query_vec = embeddings.embed_query(query)  # turns the question into a list of numbers

scored = [(cosine_similarity(query_vec, pv), p) for pv, p in zip(passage_vecs, passages)]  # gives each sentence a closeness score against the question
scored.sort(reverse=True)  # puts the best-matching sentences at the top

print(f"query: {query}\n")  # prints the question being asked
for score, passage in scored:  # goes through each scored sentence one by one
    print(f" {score:.4f} {passage}")  # prints the score and the sentence next to it

print(f"\nbest match: {scored[0][1]}")  # prints the sentence that matched the question best
