# ==========================================================================
# DAY 2 · Python Basics · 05 — Nested loops & sorting with a key
# --------------------------------------------------------------------------
# Learn: loops inside loops (tables & grids) and sorting lists of dicts with
# sorted(data, key=lambda item: item["field"]).
# Run:  python 05_nested_loops_and_sorting.py
# ==========================================================================

# part 1 - nested loops
print("Times table: (2 and 3)")
for a in [2, 3]:
    for b in [1, 2, 3]:
        print(f" {a} x {b} = {a * b}")
    print(" ---")

grid = [
    ["Diksha", "Home Loan"],
    ["Muthu", "Car Loan"],
    ["Deepak", "Personal Loan"]
]
print("\nWalking through a grid:")
for row in grid:
    name = row[0]
    product = row[1]
    print(f"  {name} has a {product}")

# part 2 - building a grid with nested loops
print("\nA 3x3 coordinate grid:")
for r in range(3):
    line = ""
    for c in range(3):
        line += f"({r},{c}) "
    print(" " + line)

# part 3 - sorting with a key
customers = [
    {"name": "Diksha", "product": "Home Loan", "score": 0.91},
    {"name": "Muthu", "product": "Car Loan", "score": 0.75},
    {"name": "Deepak", "product": "Personal Loan", "score": 0.85},
]

# sort by score
sorted_customers = sorted(customers, key=lambda c: c["score"], reverse=True)
print("\nCustomers sorted by score:")
for c in sorted_customers:
    print(f"  {c['name']} has a {c['product']} with score {c['score']}")


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

