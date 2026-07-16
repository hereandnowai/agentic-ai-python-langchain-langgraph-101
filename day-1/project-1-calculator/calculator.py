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
    """Run one operation on two numbers and return the result"""
    ops = {"add": add, "subtract": subtract, "multiply": multiply, "divide": divide}
    func = ops.get(operation)
    if func is None:
        raise ValueError(f"Invalid operation: {operation}")
    return func(a, b)