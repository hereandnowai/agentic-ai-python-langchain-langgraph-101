# ==========================================================================
# DAY 1 · Python Basics · 05 — Formatting numbers & text for output
# --------------------------------------------------------------------------
# Learn: format specifiers inside f-strings — decimals (:.2f), percentages
# (:.1%), thousands separators (:,), alignment (<, >, ^) and zero-padding
# (:03d). Run:  python 05_string_formatting.py
# ==========================================================================

price = 1234.5  # puts the number 1234.5 into a box named price
ratio = 0.8375  # puts the number 0.8375 into a box named ratio
count = 42  # puts the number 42 into a box named count
name = "Priya"  # puts the name Priya into a box named name

print(f"raw price: {price}")  # shows the price exactly as it is stored
print(f"two decimal places: {price:.2f}")  # shows the price rounded to two numbers after the dot
print(f"0 decimal places: {price:.0f}")  # shows the price rounded to a whole number
print(f"pi to 4 places: {3.141592653589793:.4f}")  # shows pi cut to four numbers after the dot

print(f"\nratio as percent: {ratio:.1%}")  # shows the ratio as a percentage with one decimal
print(f"ratio as percent: {ratio:.0%}")  # shows the ratio as a whole-number percentage

big = 5000000  # puts the big number five million into a box named big
print(f"\nplain : {big}")  # shows the big number with no separators
print(f"comma : {big:,}")  # shows the big number with commas between the thousands
print(f"money style: {big:,.2f}")  # shows the big number with commas and two decimals, like money

print("\n Alignment: (each field is 10 wide, shown between ||)")  # prints the heading explaining the alignment demo
print(f"|{name:<10}| left aligned")  # shows the name pushed to the left in a 10-wide space
print(f"|{name:>10}| right aligned")  # shows the name pushed to the right in a 10-wide space
print(f"|{name:^10}| centered")  # shows the name centred in a 10-wide space

rows = [("Home Loan", 5000000, 0.084),  # makes a list of three loan records (name, amount, rate)
        ("Car Loan", 800000, 0.099),
        ("Personal", 150000, 0.155)]
print("\nProduct      Amount      Rate")  # prints the column headings for the table
print("-" * 30)  # prints a line of 30 dashes as a divider
for product, amount, rate in rows:  # goes through each loan record one at a time
    print(f"{product:<12} {amount:>10,} {rate:>6.1%}")  # prints one neatly lined-up row of the table


print("\n\nZero padding:")  # prints a blank gap then the heading Zero padding
print(f"ticket #{7:03d}")  # shows the number 7 padded with zeros to three digits (007)
print(f"ticket #{42:03d}")  # shows the number 42 padded with zeros to three digits (042)
print(f"time {9:02d}:{5:02d}:{3:02d}")  # shows a time with each part padded to two digits (09:05:03)

print("\n\nSame sentences, three styles")  # prints a blank gap then a heading
print(f"f-string: {name} has {count} points") # modern way
print("format(): {} has {} points".format(name, count)) # older way 
print("percent: %s has %d points" % (name, count)) # oldest way

print("\nLiteral braces:")  # prints a blank line then the heading Literal braces
print(f"{{this is in curly braces}} and {name} is the client")  # doubled braces show real curly brackets, and name gets filled in


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