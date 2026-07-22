# ==========================================================================
# DAY 2 · Python Basics · 08 — JSON: turning data into text and back
# --------------------------------------------------------------------------
# Learn: json.dumps (Python dict -> JSON text) and json.loads (JSON text ->
# Python dict). JSON is how AI APIs, web services and files exchange data.
# Run:  python 08_json.py
# ==========================================================================

import json  # brings in Python's built-in toolkit for working with JSON

# part 1 - python dict --> json text
customer = {  # makes a dictionary describing one customer
    "name": "Alice",
    "account_type": "savings",
    "balance": 1000.50,
    "verified": True,
    "tags": ["priority", "kyc-complete"],
    "phone": None
}

json_text = json.dumps(customer)  # turns the dictionary into one line of JSON text
print("compact JSON:")  # prints a heading
print(json_text)  # shows the JSON text

pretty = json.dumps(customer, indent=2)  # turns it into JSON text with tidy spacing and line breaks
print("pretty JSON:")  # prints a heading
print(pretty)  # shows the nicely spaced JSON

# part 2 - json text --> python object
incoming = '{"intent": "loan_query", "product": "home_loa", "amount": 250000}'  # a piece of JSON text that arrived as a string
parsed = json.loads(incoming)  # turns that JSON text back into a Python dictionary
print("\nparsed type: ", type(parsed))  # shows that it is now a dictionary
print("intent : ", parsed["intent"])  # looks up the value stored under "intent"
print("amount : ", parsed["amount"])  # looks up the value stored under "amount"


# ==========================================================================
# 🏋️  PRACTICE ACTIVITIES  —  JSON
# --------------------------------------------------------------------------
# Write your code below each task, then run:  python 08_json.py
# Remember: json.dumps = dict -> text (dump-STRING);
#           json.loads = text -> dict (load-STRING).
#
# 1. Build a dict for a product (name, price, in_stock) and convert it to a
#    PRETTY JSON string with  json.dumps(..., indent=2). Print it.
# 2. Parse this JSON text and print the "name":
#       '{"name": "Asha", "age": 30, "city": "Chennai"}'
# 3. After parsing task 2, safely read a MISSING key "email" using .get()
#    with a default.
# 4. Put two customer dicts in a list, convert the list to JSON, then parse
#    it back and print how many customers you got.
# 5. BONUS: write your dict to a real file with json.dump(), then read it
#    back with json.load(). (See day-2/contact_book/contacts.py for a real
#    working example of exactly this.)
# ==========================================================================