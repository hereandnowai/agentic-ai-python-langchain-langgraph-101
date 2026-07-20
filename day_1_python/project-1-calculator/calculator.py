# what are the functionalities of a calculator?
# A calculator typically has the following functionalities:
# Basic Arithmetic Operations: Addition, Subtraction, Multiplication, Division

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def calculate(a, operation, b):
    """Run one operation on two numbers and return the result.

    'ops' is a dictionary that maps an operation NAME (a string like "add")
    to the actual FUNCTION that does the work. In Python, functions are
    values, so we can store them in a dict and look one up by name — this
    is much cleaner than a long if/elif chain.
    """
    ops = {"add": add, "subtract": subtract, "multiply": multiply, "divide": divide}
    func = ops.get(operation)          # look up the function by its name
    if func is None:                   # the name was not in our dictionary
        raise ValueError(f"Invalid operation: {operation}")
    return func(a, b)                  # call the chosen function on the numbers


# ==========================================================================
# 🏋️  PRACTICE ACTIVITIES  —  the calculator "backend"
# --------------------------------------------------------------------------
# This file is the BACKEND (the logic). app.py is the FRONTEND (the screen).
# Do these here, then run:  python calculator.py   (add print()s to test).
#
# 1. Add a new operation  power(a, b)  that returns  a ** b, and register it
#    in the 'ops' dictionary so calculate(2, "power", 3) returns 8.
# 2. Add a  modulo(a, b)  operation that returns the remainder  a % b.
# 3. calculate() already raises ValueError for a bad operation name. Call it
#    with a wrong name inside a try/except and print a friendly message
#    instead of letting the program crash.
# 4. Add a function  percentage(part, whole)  that returns what percent
#    'part' is of 'whole'. Guard against  whole == 0  (like divide does).
# 5. Write 3 quick self-tests using assert, e.g.:
#       assert add(2, 3) == 5
#       assert divide(10, 2) == 5
#    An assert that is False will stop the program — a simple, free test!
# ==========================================================================