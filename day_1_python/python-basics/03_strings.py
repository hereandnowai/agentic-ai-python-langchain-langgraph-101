# ==========================================================================
# DAY 1 · Python Basics · 03 — Working with strings (text)
# --------------------------------------------------------------------------
# Learn: indexing & slicing text[start:end], common string methods
# (.strip / .upper / .lower / .title / .replace / .split / .join / .find),
# chaining methods, and multi-line f-strings. Run:  python 03_strings.py
# ==========================================================================

text = "Meridian Retail Bank"  # puts the words Meridian Retail Bank into a box named text

print("text:", text)  # shows the whole piece of text
print("type:", type(text))  # shows that this value is text
print("length:", len(text))  # shows how many characters are in the text
print("first character:", text[0])  # shows the very first letter (counting starts at 0)
print("second character:", text[1])  # shows the second letter
print("last character:", text[-1])  # shows the last letter (minus 1 counts from the end)
print("second last character:", text[-2])  # shows the second-to-last letter

# Slicing: grab a range of characters with [start:end] where start is inclusive and end is exclusive
print(text[0:8])  # shows letters 0 up to (but not including) 8, which spells Meridian
print(text[9:15])  # shows letters 9 up to 15, which spells Retail
print(text[9:])  # shows everything from letter 9 to the end
print(text[:8])  # shows everything from the start up to letter 8
print(text[-4:])  # shows the last four letters, which spell Bank

messy = "  Hello, world!   "  # puts some text with extra spaces into a box named messy
print("\nWhitespaces removed:", repr(messy.strip())) # removes leading and trailing whitespaces
print(messy.upper())  # shows the text with every letter made CAPITAL
print(messy.lower())  # shows the text with every letter made small
print(messy.title())  # shows the text with the first letter of each word capitalised
print("home loan".title())  # shows Home Loan with each word starting with a capital
print("Replace 'world' with 'Python':", messy.replace("world", "Python"))  # swaps the word world for Python in the text
print("Count: ", text.count("i"))  # counts how many times the letter i appears
print("Find: ", text.find("Retail"))  # shows the position where the word Retail begins
print("Does it start with 'Meridian'? ->", text.startswith("Meridian"))  # True if the text begins with Meridian
print("Does it end with 'Bank'? ->", text.endswith("Bank"))  # True if the text ends with Bank

print("Split: ", text.split()) # splits the string into a list of words
print("Slipt with comma: ", "a,b,c,d".split(",")) # splits the string into a list of words using comma as separator

words = ["compliant", "grounded", "auditable"]  # makes a list holding three words
print("Join: ", ", ".join(words))  # glues the list of words into one text, separated by commas

raw = " YES, Please "  # puts some messy text with extra spaces into a box named raw
cleaned = raw.strip().lower()  # removes the outer spaces and makes everything small letters
print("chained clean:", repr(cleaned))  # shows the tidied-up text with its quote marks

# more f-strings
customer = "Priya"  # puts the name Priya into a box named customer
product = "Home Loan"  # puts Home Loan into a box named product
tone = "formal"  # puts the word formal into a box named tone

prompt = f"Respond to {customer} about their {product} enquiry in a {tone} tone."  # builds a sentence with the boxes filled in
print(prompt)  # shows that built sentence

print(f"Product converted into uppercase: {product.upper()}")  # shows the product name in all capitals
print(f"Name Length: {len(customer)}")  # shows how many letters are in the customer name
print(f"Two products: {product} and a Car Loan")  # shows a sentence naming two products

print("\n")  # prints a blank line to add spacing
# multi-line strings
system_prompt = f""" You are a helpful banking assistant.
Customer name: {customer}
Product: {product}
Rules: answer only from approved policy; keep the tone {tone}.

"""
print(system_prompt)  # shows the whole multi-line message built above

print('She said, "Hello!"')  # shows text that contains double quotes inside single quotes
print("It's a beautiful day!")  # shows text with an apostrophe inside double quotes
print('It\'s a beautiful day!') # escaping single quote with backslash


# ==========================================================================
# 🏋️  PRACTICE ACTIVITIES  —  working with strings
# --------------------------------------------------------------------------
# Write your code below each task, then run:  python 03_strings.py
#
# 1. Store your full name in a variable. Print its length, its first
#    character, and its last character.
# 2. From "Meridian Retail Bank", use slicing to print JUST the word
#    "Retail".
# 3. Take "  Mix of UPPER and lower  " and print it stripped AND lowercased
#    (chain the two methods together).
# 4. Use .split() to break "one,two,three" into a list, then .join() it back
#    together with " - " between each word.
# 5. Build an f-string prompt: "Reply to <name> about <product> politely."
#    using your own name and product variables.
# ==========================================================================