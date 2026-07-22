# ==========================================================================
# DAY 1 · Python Basics · 02 — Core types, numbers & booleans
# --------------------------------------------------------------------------
# Learn: int / float / str / bool / None, converting between types (int(),
# float(), str()), arithmetic and comparison operators, logical and/or/not,
# and "truthiness". Run:  python 02_core_types.py
# ==========================================================================

count = 42              # integer
temperature = 0.7       # float
name = "Caramel"        # string
is_active = True        # boolean - True or False (note the capital T and F)
missing = None          # NoneType - represents the absence of a value

print(count)  # shows the number stored in count (42)
print(type(count))  # shows what kind of value count is (a whole number)

print(f"count: {count}, type: {type(count)}")  # shows the count value and its kind in one sentence
print(f"temperature: {temperature}, type: {type(temperature)}")  # shows the temperature value and its kind
print(f"name: {name}, type: {type(name)}")  # shows the name value and its kind
print(f"is_active: {is_active}, type: {type(is_active)}")  # shows the is_active value and its kind
print(f"missing: {missing}, type: {type(missing)}")  # shows the missing value and its kind

age_text = "42"  # string representation of an integer
age_number = int(age_text)  # turns the text "42" into the actual number 42

print(type(age_text))  # shows that age_text is text
print(type(age_number))  # shows that age_number is a whole number

price = float("19.99") # str -> float
print("float('19.99') ->", price)  # shows the label and the number 19.99

print(int('30') + 5)  # turns "30" into a number, adds 5, and shows 35

print("\n\nArithmetic operations:")  # prints a blank gap then the heading Arithmetic operations
print(" 7 + 3 =", 7 + 3)  # shows the sum of 7 and 3
print(" 7 - 3 =", 7 - 3)  # shows 7 take away 3
print(" 7 * 3 =", 7 * 3)  # shows 7 multiplied by 3
print(" 7 / 3 =", 7 / 3)   # always returns a float
print(" 7 // 3 =", 7 // 3) # floor division throws away the decimal part
print(" 7 % 3 =", 7 % 3)   # modulus operator returns the remainder of the division
print(" 7 ** 3 =", 7 ** 3)  # shows 7 to the power of 3 (7 times 7 times 7)

print(" is 10 even? ->", 10 % 2 == 0) # True if 10 is even, False otherwise
print(" is 11 even? ->", 11 % 2 == 0) # True if 11 is even, False otherwise

# comparison operators: <, <=, >, >=, ==, !=
print("\nComparison operations:")  # prints a blank line then the heading Comparison operations
print(" 5 > 3 -->", 5 > 3) # greater than
print(" 5 < 3 -->", 5 < 3) # less than
print(" 5 >= 3 -->", 5 >= 3) # greater than or equal to
print(" 5 <= 3 -->", 5 <= 3) # less than or equal to
print(" 5 == 3 -->", 5 == 3) # equal to ('==' asking if 5 is equal to 3)
print(" 5 != 3 -->", 5 != 3) # not equal to

# logical operators: and, or, not
has_account = True  # puts the True/False value True into a box named has_account
is_verified = False  # puts the value False into a box named is_verified
print("\nLogical operations:")  # prints a blank line then the heading Logical operations
print(has_account and is_verified)  # True only if BOTH are True, so here it is False
print(has_account or is_verified)  # True if EITHER one is True, so here it is True
print(not has_account)  # flips True to False
print(not is_verified)  # flips False to True

balance = 15000  # puts the number 15000 into a box named balance
eligible = balance > 10000 and has_account  # True only if balance is over 10000 AND they have an account
print(" eligible for a loan? ->", eligible)  # shows whether they qualify for the loan

# truthiness of values in Python
print("\nTruthiness of values:")  # prints a blank line then the heading Truthiness of values
print("\nbool('') ->", bool('')) # empty string is False
print("bool('Hello') ->", bool("Hello")) # non-empty string is True
print("bool(0) ->", bool(0)) # 0 is False
print("bool(None) ->", bool(None)) # None is False


# ==========================================================================
# 🏋️  PRACTICE ACTIVITIES  —  core types, numbers & booleans
# --------------------------------------------------------------------------
# Write your code below each task, then run:  python 02_core_types.py
#
# 1. Make an int and a float, add them together, and print the result AND
#    its type().  Which type "wins" when you mix them?
# 2. Is 2026 an even number? Print the result of  2026 % 2 == 0.
# 3. Convert the string "150" to an int and add 25 to it.
# 4. Predict the answer BEFORE running, then check each one:
#       bool("0")    bool(0)    bool(" ")    bool([])
#    (Surprise: the *string* "0" is True, but the *number* 0 is False!)
# 5. Two flags: has_ticket = True, is_member = False.  Print the result of
#    (has_ticket and is_member), (has_ticket or is_member), (not is_member).
# ==========================================================================