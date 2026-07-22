# ==========================================================================
# DAY 2 · Python Basics · 04 — List / dict / set comprehensions
# --------------------------------------------------------------------------
# Learn: the short one-line way to build a new list, dict or set from an
# existing one — with an optional filter (if). Every example is shown as a
# normal loop first, then as a comprehension. Run: python 04_comprenhensions.py
# ==========================================================================

numbers = [1, 2, 3, 4, 5, 6]  # a list of six numbers to work with

# part 1 - the same transform, two ways
evens_loop = []  # makes an empty list to collect the even numbers
for number in numbers:  # goes through each number one by one
    if number % 2 == 0:  # if the number divides evenly by 2 (no remainder)
        evens_loop.append(number)  # adds that even number to the list
print(f"evens using loop: {evens_loop}")  # shows the even numbers found the long way

evens_comp = [n for n in numbers if n % 2 == 0]  # the same thing in one short line
print(f"evens using comprehension: {evens_comp}")  # shows the even numbers found the short way

# part 2 - transform no filter
doubled = [n * 2 for n in numbers]  # makes a new list with every number doubled
print(f"doubled numbers: {doubled}")  # shows the doubled numbers

squares = [n ** 2 for n in numbers]  # makes a new list with every number multiplied by itself
print(f"squared numbers: {squares}")  # shows the squared numbers

upper = [word.upper() for word in ["hello", "world"]]  # makes a new list with each word in capitals
print(f"uppercased words: {upper}")  # shows the capitalised words

lengths = [len(word) for word in ["hello", "world"]]  # makes a new list of how long each word is
print(f"lengths of words: {lengths}")  # shows those lengths

# part 3 - filter only
words = ["hello", "world", "python", "is", "awesome"]  # a list of words
long_words = [word for word in words if len(word) >= 5]  # keeps only the words with 5 or more letters
print(f"long words: {long_words}")  # shows the long words

# part 4 - filter 'retrieved chunks' by score
chunks = [  # a list of pieces of text, each with a relevance score
    {"text": "Home loan interest start at 8.4%", "score": 0.91},
    {"text": "Branch opens at 9am", "score": 0.75},
    {"text": "Get your home loan today", "score": 0.85},
    {"text": "We are open on weekends", "score": 0.65},
]

# filter chunks with score >= 0.8
relevant_chunks = [c["text"] for c in chunks if c["score"] >= 0.8]  # keeps the text of chunks scoring 0.8 or higher
print(f"relevant chunks:")  # prints a heading
for t in relevant_chunks:  # goes through each kept piece of text
    print(f"  {t}")  # shows that piece of text


# part 5 - dictionary comprehensions
score_by_text = {c["text"]: c["score"] for c in chunks if c["score"] >= 0.8}  # builds a dict of text to score for the high scorers
print(f"score by text: {score_by_text}")  # shows that dictionary

products = ["home", "car", "personal"]  # a list of loan types
rates = [8.4, 9.2, 15.5]  # the matching interest rates
rate_of = {p: r for p, r in zip(products, rates)}  # pairs each product with its rate into a dictionary
print("rate of : ", rate_of)  # shows the product-to-rate dictionary
print("rate of car: ", rate_of["car"])  # looks up just the car rate

# part 6 - set comprehensions
first_letters = {word[0] for word in ["hello", "world", "python", "is", "awesome"]}  # collects the first letter of each word, no repeats
print(f"first letters: {first_letters}")  # shows the set of first letters


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
