# what is a function in Python?
# A function in Python is a block of reusable code that performs a specific task.
# Functions help to organize code, make it more readable, and allow for code reuse.
# They can take inputs (called parameters), perform operations, and return outputs (results).
# Functions are defined using the `def` keyword followed by the function name and parentheses,
# which may include parameters.

# part 1 - defining a function
def greet(name):
    """This function takes a name as input and prints a greeting message."""
    return f"Hello, {name}!"

message = greet("Alice")
print(message)
print(greet("Mukesh"))

# part 2 - parameters: positional, keyword, default
def make_ticket(customer, product, priority="normal"):
    """This function creates a ticket for a customer with a specified product and priority."""
    return f"Ticket for {customer} regarding {product} with priority {priority}"

print(make_ticket("Diksha", "Home Loan"))
print(make_ticket("Muthu", "Car Loan", priority="high"))
print(make_ticket(product="Personal Loan", customer="Deepak"))

# part 3 - return values
def add(a, b):
    """This function takes two numbers and returns their sum."""
    return a + b

total = add(5, 7)
print(f"The sum of 5 and 7 is: {total}")

def shout(text):
    """This function takes a string and returns it in uppercase."""
    print(text.upper())

result = shout("hello world")  # This will print "HELLO WORLD" but return None
print(f"The result of shout function is: {result}")  # This will print "The result of shout function is: None"

def classify(balance):
    if balance < 0:
        return "overdrawn" # returns here and stops executing the function
    if balance == 0:
        return "empty"
    return "positive"
print("classify(-5):", classify(-5))
print("classify100):", classify(100))

# function can return several values as a tuple
def stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)
low, high, average = stats([4, 8, 15, 16, 23, 42])
print(f"low: {low}, high: {high}, average: {average}")

# part 4 scope: local vs global
tax_rate = 0.18 # global module-level variable

def price_with_tax(amount):
    fee = amount * tax_rate # can access global variable tax_rate
    note = "computed"
    return amount + fee

print("\nprice_with_tax(100):", price_with_tax(100))

# part 5 - default arguments
def add_items(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket

print("\nadd_items('apple'):", add_items("apple"))
print("add_items('banana'):", add_items("banana")) # basket is reset to a new list each time because of the default argument being None\

# part 6 - brief: *args / **kwargs
def log_all(*args, **kwargs):
    """This function logs all positional and keyword arguments."""
    print("Positional arguments:", args) # tuple of positional arguments
    print("Keyword arguments:", kwargs) # dictionary of keyword arguments
print()
log_all("a", "b", level="info", retries=3)