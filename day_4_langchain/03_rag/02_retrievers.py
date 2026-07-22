from importlib import import_module  # brings in a way to load another Python file by its name

ingest = import_module("01_ingestion_chunking")  # loads the earlier file so we can reuse its recipes
store = ingest.build_strore()  # builds and fills the storage box using that file's recipe

query = "home loan interest and fees"  # the question we want to search for

print("=== Type 1. Similarity (k=3) ===")  # prints a heading for the plain closeness search
sim = store.as_retriever(search_type="similarity", search_kwargs={"k": 3})  # sets up a searcher that returns the three closest chunks
for d in sim.invoke(query):  # runs the search and goes through each result
    print(f" [{d.metadata['id']}] {d.page_content[:100]}...")  # prints each match's label and the first 100 letters of its text

print("\n=== Type 2. Maximal Marginal Relevance (MMR) (k=3, diverse) ===")  # prints a heading for the variety-focused search
mmr = store.as_retriever(search_type="mmr", search_kwargs={"k": 3, "fetch_k": 10})  # sets up a searcher that picks three results that are close but also different from each other
for d in mmr.invoke(query):  # runs the search and goes through each result
    print(f" [{d.metadata['id']}] {d.page_content[:100]}...")  # prints each match's label and the first 100 letters of its text

print("\n=== Type 3. Metadata-Filtered (category = credit card) ===")  # prints a heading for the filtered search
filtered = store.as_retriever(search_kwargs={"k": 2, "filter": {"category": "credit_card"}})  # sets up a searcher that only looks among credit-card chunks
for d in filtered.invoke("fee"):  # searches for the word fee and goes through each result
    print(f" [{d.metadata['id']}] {d.page_content[:100]}...")  # prints each match's label and the first 100 letters of its text
