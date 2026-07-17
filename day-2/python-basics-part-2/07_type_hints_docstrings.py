# ==========================================================================
# DAY 2 · Python Basics · 07 — Type hints & docstrings
# --------------------------------------------------------------------------
# Learn: telling readers (and tools) what types a function expects and
# returns  (name: str, quantity: int) -> float,  and documenting what it
# does with a docstring. Run:  python 07_type_hints_docstrings.py
# ==========================================================================

# part 1 - a fully hinted, fully documented function

def total_price(unit_price: float, quantity: int) -> float:
    """
    Calculate the total price of items based on unit price and quantity.

    Args:
        unit_price (float): The price of a single item.
        quantity (int): The number of items.

    Returns:
        float: The total price for the given quantity of items.
    """
    return unit_price * quantity

print("total_price(19.99, 3): ", total_price(19.99, 3))

# part 2 - the common hints you will use constantly
# str               a piece of text
# int               a whole number
# float             a decimal number
# bool              a True or False value
# list[str]         a list of strings
# list[int]         a list of integers
# dict              a dictionary (key-value pairs)
# dict[str, int]    a dictionary with string keys and integer values
# str | None        a string or None (optional string)

def tags_for(product: str) -> list[str]:
    """
    Generate a list of tags for a given product.
    Args: product (str): The name of the product.
    """
    return product.lower().split()

def build_customer(name: str, age: int, verified: bool = False) -> dict:
    """
    Build a customer dictionary with name, age, and verification status.

    Args:
        name (str): The name of the customer.
        age (int): The age of the customer.
        verified (bool, optional): Whether the customer is verified. Defaults to False.

    Returns:
        dict: A dictionary containing the customer's information.
    """
    return {"name": name, "age": age, "verified": verified}

print("tags_for('Home Loan') : ", tags_for("Home Loan"))
print("build_customer : ", build_customer("Alice", 30, verified=True))


# ==========================================================================
# 🏋️  PRACTICE ACTIVITIES  —  type hints & docstrings
# --------------------------------------------------------------------------
# Write your code below each task, then run:  python 07_type_hints_docstrings.py
# NOTE: type hints are NOTES for humans & tools — Python does not enforce
# them, but they make code far easier to read and catch mistakes early.
#
# 1. Add type hints to:   def repeat(text, times): return text * times
# 2. Write  discount(price: float, percent: float) -> float  with a full
#    docstring (Args + Returns).
# 3. Write  initials(full_name: str) -> str  that returns "P.R." for the
#    input "Priya Raman".
# 4. Write  safe_divide(a: float, b: float) -> float | None  that returns
#    None when b is 0 (the "| None" means it may also return None).
# 5. Add a proper docstring to build_customer() explaining each argument.
# ==========================================================================