# ==========================================================================
# DAY 2 · Python Basics · 04 — List / dict / set comprehensions
# --------------------------------------------------------------------------
# Learn: the short one-line way to build a new list, dict or set from an
# existing one — with an optional filter (if). Every example is shown as a
# normal loop first, then as a comprehension. Run: python 04_comprenhensions.py
# ==========================================================================

numbers = [1, 2, 3, 4, 5, 6]

# part 1 - the same transform, two ways
evens_loop = []
for number in numbers:
    if number % 2 == 0:
        evens_loop.append(number)
print(f"evens using loop: {evens_loop}")

evens_comp = [n for n in numbers if n % 2 == 0]
print(f"evens using comprehension: {evens_comp}")

# part 2 - transform no filter
doubled = [n * 2 for n in numbers]
print(f"doubled numbers: {doubled}")

squares = [n ** 2 for n in numbers]
print(f"squared numbers: {squares}")

upper = [word.upper() for word in ["hello", "world"]]
print(f"uppercased words: {upper}")

lengths = [len(word) for word in ["hello", "world"]]
print(f"lengths of words: {lengths}")

# part 3 - filter only
words = ["hello", "world", "python", "is", "awesome"]
long_words = [word for word in words if len(word) >= 5]
print(f"long words: {long_words}")

# part 4 - filter 'retrieved chunks' by score
chunks = [
    {"text": "Home loan interest start at 8.4%", "score": 0.91},
    {"text": "Branch opens at 9am", "score": 0.75},
    {"text": "Get your home loan today", "score": 0.85},
    {"text": "We are open on weekends", "score": 0.65},
]

# filter chunks with score >= 0.8
relevant_chunks = [c["text"] for c in chunks if c["score"] >= 0.8]
print(f"relevant chunks:")
for t in relevant_chunks:
    print(f"  {t}")


# part 5 - dictionary comprehensions
score_by_text = {c["text"]: c["score"] for c in chunks if c["score"] >= 0.8}
print(f"score by text: {score_by_text}")

products = ["home", "car", "personal"]
rates = [8.4, 9.2, 15.5]
rate_of = {p: r for p, r in zip(products, rates)}
print("rate of : ", rate_of)
print("rate of car: ", rate_of["car"])

# part 6 - set comprehensions
first_letters = {word[0] for word in ["hello", "world", "python", "is", "awesome"]}
print(f"first letters: {first_letters}")


# ==========================================================================
# 🏋️  PRACTICE ACTIVITIES  —  comprehensions
# --------------------------------------------------------------------------
# Write your code below each task, then run:  python 04_comprenhensions.py
# Tip: write it first as a normal for-loop, THEN shrink it to a comprehension.
#
# 1. From  nums = list(range(1, 11)), build a list of only the ODD numbers.
# 2. Build a list of the squares of 1..8  (i.e. [1, 4, 9, ...]).
# 3. From  ["hi", "hello", "hey", "howdy"], keep only words longer than 3
#    letters.
# 4. Build a dict  {word: length_of_word}  for a list of words using a dict
#    comprehension.
# 5. From the 'chunks' list above, keep the text of chunks with score < 0.8
#    (the LOW-relevance ones) — the opposite of the worked example.
# ==========================================================================
