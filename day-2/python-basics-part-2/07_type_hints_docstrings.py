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