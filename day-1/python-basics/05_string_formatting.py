# ==========================================================================
# DAY 1 · Python Basics · 05 — Formatting numbers & text for output
# --------------------------------------------------------------------------
# Learn: format specifiers inside f-strings — decimals (:.2f), percentages
# (:.1%), thousands separators (:,), alignment (<, >, ^) and zero-padding
# (:03d). Run:  python 05_string_formatting.py
# ==========================================================================

price = 1234.5
ratio = 0.8375
count = 42
name = "Priya"

print(f"raw price: {price}")
print(f"two decimal places: {price:.2f}")
print(f"0 decimal places: {price:.0f}")
print(f"pi to 4 places: {3.141592653589793:.4f}")

print(f"\nratio as percent: {ratio:.1%}")
print(f"ratio as percent: {ratio:.0%}")

big = 5000000
print(f"\nplain : {big}")
print(f"comma : {big:,}")
print(f"money style: {big:,.2f}")

print("\n Alignment: (each field is 10 wide, shown between ||)")
print(f"|{name:<10}| left aligned")
print(f"|{name:>10}| right aligned")
print(f"|{name:^10}| centered")

rows = [("Home Loan", 5000000, 0.084),
        ("Car Loan", 800000, 0.099),
        ("Personal", 150000, 0.155)]
print("\nProduct      Amount      Rate")
print("-" * 30)
for product, amount, rate in rows:
    print(f"{product:<12} {amount:>10,} {rate:>6.1%}")


print("\n\nZero padding:")
print(f"ticket #{7:03d}")
print(f"ticket #{42:03d}")
print(f"time {9:02d}:{5:02d}:{3:02d}")

print("\n\nSame sentences, three styles")
print(f"f-string: {name} has {count} points") # modern way
print("format(): {} has {} points".format(name, count)) # older way 
print("percent: %s has %d points" % (name, count)) # oldest way

print("\nLiteral braces:")
print(f"{{this is in curly braces}} and {name} is the client")


# ==========================================================================
# 🏋️  PRACTICE ACTIVITIES  —  formatting numbers & text
# --------------------------------------------------------------------------
# Write your code below each task, then run:  python 05_string_formatting.py
#
# 1. Store a price like 2599.5 and print it as money with a thousands
#    separator and 2 decimals:  2,599.50
# 2. Print the fraction 0.734 as a percentage with 1 decimal place (73.4%).
# 3. Print three names left-aligned in a column 12 characters wide, each
#    wrapped in | | so you can see the alignment.
# 4. Print a ticket number as  #007  using zero-padding (:03d).
# 5. Print the sentence "<name> scored <n>" THREE ways: with an f-string,
#    with .format(), and with % formatting.
# ==========================================================================