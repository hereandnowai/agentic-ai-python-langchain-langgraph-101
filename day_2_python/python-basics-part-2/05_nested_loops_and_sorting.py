# ==========================================================================
# DAY 2 · Python Basics · 05 — Nested loops & sorting with a key
# --------------------------------------------------------------------------
# Learn: loops inside loops (tables & grids) and sorting lists of dicts with
# sorted(data, key=lambda item: item["field"]).
# Run:  python 05_nested_loops_and_sorting.py
# ==========================================================================

# part 1 - nested loops
print("Times table: (2 and 3)")  # prints a heading
for a in [2, 3]:  # goes through the outer numbers 2 then 3
    for b in [1, 2, 3]:  # for each of those, goes through 1, 2, 3
        print(f" {a} x {b} = {a * b}")  # shows the two numbers multiplied together
    print(" ---")  # prints a divider line after each outer number

grid = [  # a table of rows, where each row is [name, product]
    ["Diksha", "Home Loan"],
    ["Muthu", "Car Loan"],
    ["Deepak", "Personal Loan"]
]
print("\nWalking through a grid:")  # prints a heading
for row in grid:  # goes through each row of the table
    name = row[0]  # takes the first item of the row as the name
    product = row[1]  # takes the second item of the row as the product
    print(f"  {name} has a {product}")  # shows who has which product

# part 2 - building a grid with nested loops
print("\nA 3x3 coordinate grid:")  # prints a heading
for r in range(3):  # goes through the rows 0, 1, 2
    line = ""  # starts an empty piece of text for this row
    for c in range(3):  # goes through the columns 0, 1, 2
        line += f"({r},{c}) "  # adds the row,column pair onto the line
    print(" " + line)  # shows the finished row

# part 3 - sorting with a key
customers = [  # a list of customers, each stored as a dictionary
    {"name": "Diksha", "product": "Home Loan", "score": 0.91},
    {"name": "Muthu", "product": "Car Loan", "score": 0.75},
    {"name": "Deepak", "product": "Personal Loan", "score": 0.85},
]

# sort by score
sorted_customers = sorted(customers, key=lambda c: c["score"], reverse=True)  # makes a new list ordered by score, highest first
print("\nCustomers sorted by score:")  # prints a heading
for c in sorted_customers:  # goes through the sorted customers
    print(f"  {c['name']} has a {c['product']} with score {c['score']}")  # shows each customer's details


# ==========================================================================
# 🏋️  PRACTICE ACTIVITIES  —  nested loops & sorting
# --------------------------------------------------------------------------
# Write your code below each task, then run: python 05_nested_loops_and_sorting.py
#
# 1. Print the full 1..5 times table for the numbers 2, 3, and 4 using
#    nested loops (a loop inside a loop).
# 2. Given a grid (list of [name, product] rows), print "<name> -> <product>"
#    for every row.
# 3. Sort the 'customers' list by NAME (A -> Z) instead of by score.
# 4. Sort the 'customers' by score ASCENDING (lowest first).
# 5. BONUS: find the single customer with the HIGHEST score using
#    max(customers, key=lambda c: c["score"]).
# ==========================================================================

