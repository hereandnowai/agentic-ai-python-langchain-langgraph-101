import os  # brings in tools to read settings from the computer, like secret keys
from dotenv import load_dotenv  # brings in a helper that loads secret settings from a file
from pydantic import SecretStr  # brings in a safe wrapper for holding secret text like a key

import json  # brings in a helper that reads and writes data in JSON format
from pathlib import Path  # brings in a tidy way to work with file and folder locations
from langchain_core.documents import Document  # brings in a wrapper that holds a piece of text plus notes about it
from langchain_text_splitters import RecursiveCharacterTextSplitter  # brings in a tool that cuts long text into smaller chunks
from langchain_openai import OpenAIEmbeddings  # brings in a helper that turns text into lists of numbers
from langchain_chroma import Chroma  # brings in a searchable storage box for text and its number-lists

load_dotenv()  # reads the hidden .env file so secret keys become available
EMBEDDING_MODEL = os.environ.get("EMBEB_MODEL", "openai/text-embedding-3-small")  # picks which text-to-numbers model to use, with a default
embeddings = OpenAIEmbeddings(  # sets up the text-to-numbers helper with the settings below
    model=EMBEDDING_MODEL,
    base_url="https://openrouter.ai/api/v1",
    api_key=SecretStr(os.environ["OPENROUTER_API_KEY"]),
    check_embedding_ctx_length=False,
)

KB = Path(__file__).resolve().parents[1] / "data" / "meridian_kb.json"  # builds the full path to the knowledge file
CHROMA_DIR = str(Path(__file__).with_name("rag_chroma_db"))  # builds the folder path where the storage box will live

def load_and_chunk() -> list[Document]:  # a recipe that reads the knowledge file and cuts it into small chunks
    entries = json.loads(KB.read_text())["documents"]  # reads the file and pulls out the list of documents
    base_docs = [  # wraps each entry as a Document with its text and labels
        Document(page_content=e["text"],
                 metadata={"id": e["id"], "category": e["category"], "title": e["title"]})
        for e in entries
    ]

    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)  # sets up the cutter to make chunks of about 300 letters that slightly overlap
    chunks = splitter.split_documents(base_docs)  # cuts all the documents into those smaller chunks
    return chunks  # gives back the list of chunks

def build_strore() -> Chroma:  # a recipe that fills the storage box with the chunks and returns it
    chunks = load_and_chunk()  # gets the chunks by running the recipe above
    print(f"{len(chunks)} chunks created from {KB}")  # prints how many chunks were made and from which file
    store = Chroma(  # opens a searchable storage box with the settings below
        collection_name="meridian_rag",
        embedding_function=embeddings,
        persist_directory=CHROMA_DIR)
    if not store.get()["ids"]:  # checks whether the storage box is still empty
        store.add_documents(chunks)  # puts the chunks into the storage box
        print("ingested chunks into Chroma store")  # says the chunks were added
    else:  # otherwise, if the box already had data
        print("Chroma store already has data, skipping ingestion")  # says it skipped adding again
    return store  # gives back the ready storage box

if __name__ == "__main__":  # runs the part below only when this file is started directly
    store = build_strore()  # builds and fills the storage box
    for d in store.similarity_search("home loan documents", k=2):  # finds the two closest chunks to the test question
        print(f" [{d.metadata['id']}] {d.page_content[:100]}...")  # prints each match's label and the first 100 letters of its text

