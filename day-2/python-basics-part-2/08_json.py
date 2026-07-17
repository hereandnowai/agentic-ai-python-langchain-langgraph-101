import json

# part 1 - python dict --> json text
customer = {
    "name": "Alice",
    "account_type": "savings",
    "balance": 1000.50,
    "verified": True,
    "tags": ["priority", "kyc-complete"],
    "phone": None
}

json_text = json.dumps(customer)
print("compact JSON:")
print(json_text)

pretty = json.dumps(customer, indent=2)
print("pretty JSON:")
print(pretty)

# part 2 - json text --> python object
incoming = '{"intent": "loan_query", "product": "home_loa", "amount": 250000}'
parsed = json.loads(incoming)
print("\nparsed type: ", type(parsed))
print("intent : ", parsed["intent"])
print("amount : ", parsed["amount"])