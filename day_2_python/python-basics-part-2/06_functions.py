# what is a function in Python?
# A function in Python is a block of reusable code that performs a specific task.
# Functions help to organize code, make it more readable, and allow for code reuse.
# They can take inputs (called parameters), perform operations, and return outputs (results).
# Functions are defined using the `def` keyword followed by the function name and parentheses,
# which may include parameters.

# part 1 - defining a function
def greet(name):  # defines a reusable function called greet that takes one input, name
    """This function takes a name as input and prints a greeting message."""
    return f"Hello, {name}!"  # hands back a greeting with the name filled in

message = greet("Alice")  # runs the function with "Alice" and stores what comes back
print(message)  # shows that greeting
print(greet("Mukesh"))  # runs the function with "Mukesh" and shows the result straight away

# part 2 - parameters: positional, keyword, default
def make_ticket(customer, product, priority="normal"):  # defines a function; priority defaults to "normal" if not given
    """This function creates a ticket for a customer with a specified product and priority."""
    return f"Ticket for {customer} regarding {product} with priority {priority}"  # builds and returns the ticket text

print(make_ticket("Diksha", "Home Loan"))  # runs it without a priority, so it uses "normal"
print(make_ticket("Muthu", "Car Loan", priority="high"))  # runs it with priority set to "high"
print(make_ticket(product="Personal Loan", customer="Deepak"))  # runs it naming the inputs, so order does not matter

# part 3 - return values
def add(a, b):  # defines a function that takes two numbers
    """This function takes two numbers and returns their sum."""
    return a + b  # hands back the two numbers added together

total = add(5, 7)  # runs add with 5 and 7 and stores the answer
print(f"The sum of 5 and 7 is: {total}")  # shows the answer

def shout(text):  # defines a function that takes some text
    """This function takes a string and returns it in uppercase."""
    print(text.upper())  # prints the text in capitals but does not return anything

result = shout("hello world")  # This will print "HELLO WORLD" but return None
print(f"The result of shout function is: {result}")  # This will print "The result of shout function is: None"

def classify(balance):  # defines a function that labels a balance
    if balance < 0:  # if the balance is below zero
        return "overdrawn" # returns here and stops executing the function
    if balance == 0:  # if the balance is exactly zero
        return "empty"  # hands back "empty" and stops
    return "positive"  # otherwise hands back "positive"
print("classify(-5):", classify(-5))  # shows the label for -5
print("classify(100):", classify(100))  # shows the label for 100

# function can return several values as a tuple
def stats(numbers):  # defines a function that takes a list of numbers
    return min(numbers), max(numbers), sum(numbers) / len(numbers)  # hands back the smallest, biggest and average together
low, high, average = stats([4, 8, 15, 16, 23, 42])  # runs it and unpacks the three answers into three names
print(f"low: {low}, high: {high}, average: {average}")  # shows all three values

# part 4 scope: local vs global
tax_rate = 0.18 # global module-level variable

def price_with_tax(amount):  # defines a function that adds tax to an amount
    fee = amount * tax_rate # can access global variable tax_rate
    note = "computed"  # a helper value that only exists inside this function
    return amount + fee  # hands back the amount plus the tax fee

print("\nprice_with_tax(100):", price_with_tax(100))  # shows the price of 100 with tax added

# part 5 - default arguments
def add_items(item, basket=None):  # defines a function; basket starts as None if not given
    if basket is None:  # if no basket was passed in
        basket = []  # makes a fresh empty basket
    basket.append(item)  # puts the item into the basket
    return basket  # hands the basket back

print("\nadd_items('apple'):", add_items("apple"))  # shows a basket holding just apple
print("add_items('banana'):", add_items("banana")) # basket is reset to a new list each time because of the default argument being None\

# part 6 - brief: *args / **kwargs
def log_all(*args, **kwargs):  # defines a function that accepts any number of inputs
    """This function logs all positional and keyword arguments."""
    print("Positional arguments:", args) # tuple of positional arguments
    print("Keyword arguments:", kwargs) # dictionary of keyword arguments
print()  # prints a blank line
log_all("a", "b", level="info", retries=3)  # runs it with two plain inputs and two named ones


# ==========================================================================
# 🏋️  PRACTICE ACTIVITIES  —  functions
# --------------------------------------------------------------------------
# Write your code below each task, then run:  python 06_functions.py
#
# 1. Write  area_of_rectangle(width, height)  that RETURNS width * height
#    (return it, don't just print it).
# 2. Write  greet(name, greeting="Hello")  with a default argument. Call it
#    once WITHOUT the greeting and once WITH  greeting="Hi".
# 3. Write  is_even(n)  that returns True or False.
# 4. Write  summary(numbers)  that returns (min, max, average) as a tuple,
#    then unpack the three values where you call it.
# 5. In a comment, explain WHY  add_items(item, basket=None)  uses None and
#    then creates the list inside, instead of  basket=[]  as the default.
# ==========================================================================