# ==========================================================================
# DAY 2 · Python Basics · 02 — Dictionaries (key → value data)
# --------------------------------------------------------------------------
# Learn: create/read/update/delete keys, safe lookup with .get(), looping
# with .items(), and nesting (lists of dicts) — the exact shape that LLM
# chat "messages" use. Run:  python 02_dicts.py
# ==========================================================================

# part 1 - creating a dictionary and accessing its values
customer = {
    "name": "Muthu Kumar",
    "account_type": "savings",
    "balance": 15000.0,
    "verified": True,
    }

print(f"customer dictionary: {customer}")
print(f"customer name: {customer['name']}")
print(f"customer account type: {customer['account_type']}")
print(f"customer balance: {customer['balance']}")

print("number of keys in customer dictionary:", len(customer))

# part 2 safe lookup using get method
print("\n.get('phone): ", customer.get("phone")) # returns None if key doesn't exist
print("phone of the customer: ", customer.get("phone", "not available")) # returns default value if key doesn't exist
print("customer name: ", customer.get("name", "not available")) # returns value if key exists

print("balance in customer?: ", "balance" in customer) # checking if a key exists in the dictionary
print("phone in customer?: ", "phone" in customer) # checking if a key exists in the dictionary

# part 3 - modifying a dictionary add / update key-value pairs / deleting key-value pairs
customer["phone"] = "123-456-7890" # adding a new key-value
customer["balance"] = 20000.0 # updating an existing key-value
del customer["verified"] # deleting a key-value pair
print(f"\nmodified customer dictionary: {customer}")

account = customer.pop("account_type") # removing a key-value pair and returning the value
print(f"removed account type: {account}")

# part 4 - iterating through a dictionary - looping over a dictionary's keys, values, and key-value pairs
print("\nkeys : ", list(customer.keys())) # getting all the keys in the dictionary
print("values : ", list(customer.values())) # getting all the values in the dictionary
print("items : ")
for key, value in customer.items(): # getting all the key-value pairs in the dictionary
    print(f" {key} = {value}")

# part 5 - nesting: the shape the whole GenAI  stack runs on!
messages = [
    {"role": "system", "content": "You are a helpful banking assistant."},
    {"role": "user", "content": "I want to check my account balance."},
    {"role": "assistant", "content": "Your current account balance is $15,000."},
]
print("\nmessages : (a list of dictionaries)")
for message in messages:
    print(f" {message['role']}: {message['content']} ")

first_user_message = messages[1]["content"] # accessing the content of the first user message
print(f"\nfirst user message: {first_user_message}")

role_of_last = messages[-1]["role"] # accessing the role of the last message
print(f"role of last message: {role_of_last}")

role_of_last = messages[-1].get("role", "not available") # accessing the role of the last message using get method
print(f"role of last message using get method: {role_of_last}")

by_role = {
    "user": ["what is my account balance?", "I want to transfer money."],
    "assistant": ["Your current account balance is $15,000.", "Please provide the recipient's account number."],
}
print("\nall user turns : ", by_role["user"])
print("first user turn : ", by_role["user"][0])

# part 6 - building a dictionary in a loop
sentence = "loan loan card loan card savings"
counts = {}
for word in sentence.split():
    counts[word] = counts.get(word, 0) + 1 # using get method to handle missing keys
print("\nword counts : ", counts)


# ==========================================================================
# 🏋️  PRACTICE ACTIVITIES  —  dictionaries
# --------------------------------------------------------------------------
# Write your code below each task, then run:  python 02_dicts.py
#
# 1. Build a dict for a book: title, author, year, in_stock (bool). Print
#    the title and the author.
# 2. Use .get() to safely read a "publisher" key that does NOT exist, with
#    a default value of "unknown".
# 3. Add a "price" key, update the "year", then delete the "in_stock" key.
# 4. Loop over the dict with .items() and print each pair as  key = value.
# 5. Count the words in  "red blue red green blue red"  into a dict using
#    the  counts.get(word, 0) + 1  trick shown above.
# ==========================================================================