import os  # brings in tools to read settings from the computer, like secret keys
from langchain_chroma import Chroma  # brings in a searchable storage box for text and its number-lists
from langchain_openai import OpenAIEmbeddings  # brings in a helper that turns text into lists of numbers
from langchain_core.documents import Document  # brings in a wrapper that holds a piece of text plus notes about it
from dotenv import load_dotenv  # brings in a helper that loads secret settings from a file
from pydantic import SecretStr  # brings in a safe wrapper for holding secret text like a key

load_dotenv()  # reads the hidden .env file so secret keys become available
EMBEDDING_MODEL = os.environ.get("EMBED_MODEL", "openai/text-embedding-3-small")  # picks which text-to-numbers model to use, with a default
embeddings = OpenAIEmbeddings(  # sets up the text-to-numbers helper with the settings below
    model=EMBEDDING_MODEL,
    base_url="https://openrouter.ai/api/v1",
    api_key=SecretStr(os.environ["OPENROUTER_API_KEY"]),
    check_embedding_ctx_length=False,
)

docs = [  # makes a list of text pieces, each with a label and category attached
    Document(page_content="Home loans require a minimum CIBIL score of 700.",
             metadata={"id": "hl-001", "category": "home_loan"}),
    Document(page_content="Home loan rates start at 8.4 percentage for scores of 750+",
             metadata={"id": "hl-002", "category": "home_loan"}),
    Document(page_content="Savings accounts earn 3% interest, per annum.",
            metadata={"id": "sa-001", "category": "savings_account"}),
    Document(page_content="Report a lost or stolen card immediately via the app.",
            metadata={"id": "cc-001", "category": "credit_card"}),
]

store = Chroma(  # opens a searchable storage box with the settings below
    collection_name="meridian_demo",
    embedding_function=embeddings,
    persist_directory="./chroma_db"
)
store.add_documents(docs)  # puts all the text pieces into the storage box

# --- Similarity search ---
print("\n--- plain search: 'Credit score to buy a house' ---")  # prints a heading for the first search
for d in store.similarity_search("credit score to buy a house", k=2):  # finds the two closest text pieces to the question
    print(f" [{d.metadata['category']}] {d.page_content}")  # prints each match's category and its text

# --- Metadata filter search ---
print("\n--- metadata filter search: (category = home loan) ---")  # prints a heading for the filtered search
hits = store.similarity_search("interest rate", k=2, filter={"category": "home_loan"})  # finds the two closest matches, but only among home-loan pieces
for d in hits:  # goes through each match found
    print(f" [{d.metadata['id']}] {d.page_content}")  # prints each match's label and its text

# With scores (lower distance = closer)
print("\n--- with scores ---")  # prints a heading for the scored search
for d, score in store.similarity_search_with_score("stolen card", k=1):  # finds the single best match and its closeness number
    print(f" score {score:.3f}: {d.page_content}")  # prints the closeness number and the matching text
