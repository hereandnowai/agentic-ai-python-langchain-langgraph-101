import os  # brings in tools to read settings from the computer, like secret keys
from langchain_qdrant import QdrantVectorStore  # brings in a connector to the Qdrant search database
from langchain_openai import OpenAIEmbeddings  # brings in a helper that turns text into lists of numbers
from langchain_core.documents import Document  # brings in a wrapper that holds a piece of text plus notes about it
from qdrant_client import QdrantClient  # brings in the tool that talks to the Qdrant database
from qdrant_client import models  # brings in ready-made building blocks for Qdrant, like filters
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
QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")  # picks the web address of the Qdrant database, with a default

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

try:  # tries the following steps, ready to catch any problem
    store = QdrantVectorStore.from_documents(  # loads all the text pieces into the Qdrant database
        docs,
        embedding=embeddings,
        url=QDRANT_URL,
        collection_name="meridian_demo",
    )
except Exception as error:  # runs this part only if something above went wrong
    print("could not reach a qdrant. Please run 'docker run -p 6333:6333 qdrant/qdrant'")  # tells the user how to start the database
    print("Details: ", error)  # prints what exactly went wrong
    raise SystemExit(1)  # stops the program because it cannot continue

# --- Plain search ---
print("\n--- plain search: 'Credit score to buy a house' ---")  # prints a heading for the first search
for d in store.similarity_search("credit score to buy a house", k=2):  # finds the two closest text pieces to the question
    print(f" [{d.metadata['category']}] {d.page_content}")  # prints each match's category and its text

# --- Metadata filter search ---
print("\n--- metadata filter search: (category = home loan) ---")  # prints a heading for the filtered search
qdrant_filter = models.Filter(  # builds a rule that keeps only home-loan pieces
    must=[models.FieldCondition(key="metadata.category",
                                match=models.MatchValue(value="home_loan"))])

# With scores (lower distance = closer)
print("\n--- filtered search (category = home loan) ---")  # prints a heading for the scored search
for d in store.similarity_search("interest rate", k=2):  # finds the two closest text pieces to the question
    print(f" [{d.metadata['id']}] {d.page_content}")  # prints each match's label and its text
