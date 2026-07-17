# ==========================================================================
# DAY 2 · Python Basics · 03 — Control flow (decisions & loops)
# --------------------------------------------------------------------------
# Learn: if / elif / else, for loops with range(), looping over data with
# enumerate(), continue & break, and while loops.
# Run:  python 03_control_flow.py
# ==========================================================================

# part 1 if / elif / else (make a decision)
balance = 150000.0

if balance >= 100000.0:
    tier = "priority"
elif balance >= 10000.0:
    tier = "standard"
else:
    tier = "basic"
print(f"tier: {tier}")


verified = True
if balance >= 10000.0 and verified:
    print("Eligible for an instant top-up loan")

if balance < 500 or not verified:
    print("Not eligible for an instant top-up loan")


name = "Muthu Kumar"
if name:
    print("has a name")
else:
    print("name is empty")

# part 2 for loops with range()
print("\nrange(3):")
for i in range(3):
    print(" step: ", i)

# range(start, stop) and range(start, stop, step)
print("\nrange(2, 6):", list(range(2, 6)))
print("range(0, 10, 2):", list(range(0, 10, 2)))

# summing with a for loop
total = 0
for n in range(1, 6):
    total += n # total = total + n
print(f"sum of numbers from 1 to 5: {total}")

# part 3 for loops over data (with enumerate)
messages = [
    {"role": "system", "content": "You are a helpful banking assistant."},
    {"role": "user", "content": "I want to check my account balance."},
    {"role": "assistant", "content": "Your current account balance is $15,000."},
]

print("\nenumerate over messages (index + item):")
for index, message in enumerate(messages):
    print(f" index: {index}, role: {message['role']}, content: {message['content']}")


# part 4 branching inside a loop (continue = skip to the next iteration)
print("\nuser turns only")
for msg in messages:
    if msg["role"] != "user":
        continue # skip to the next iteration
    print(" -", msg["content"])

# counting with a condition (very common):
user_count = 0
for msg in messages:
    if msg["role"] == "user":
        user_count += 1
print(f"number of user turns: {user_count}")

# part 5 - while loops (loop until a condition is false) + break (exit the loop)
print("\ncountdown:")
n = 30
while n > 0:
    print(" step: ", n)
    n -= 1 # n = n - 1 decrement n by 1
print("blast off!")

attempts = 0
while True:
    attempts += 1
    print(f"attempt: {attempts}")
    if attempts >= 3:
        print("max attempts reached, exiting loop")
        break # exit the loop

# part 6 - quick word on nested logic
transactions = [120, -50, 3000, -1200, 75]
for amount in transactions:
    if amount > 0:
        kind = "credit"
    else:
        kind = "debit"
    size = "large" if abs(amount) >= 1000 else "small"
    print(f"transaction: {amount}, kind: {kind}, size: {size}")


# ==========================================================================
# 🏋️  PRACTICE ACTIVITIES  —  control flow (decisions & loops)
# --------------------------------------------------------------------------
# Write your code below each task, then run:  python 03_control_flow.py
#
# 1. Write an if/elif/else that prints a grade for a score:
#       >= 90 -> "A",  >= 75 -> "B",  >= 50 -> "C",  else -> "Fail".
# 2. Use a for loop with range() to print the 5-times table (5, 10, ... 50).
# 3. Add up ONLY the even numbers from 1 to 20 using a loop and the % operator.
# 4. Loop over the 'messages' list and print ONLY the assistant turns
#    (use 'continue' to skip the others).
# 5. Use a while loop to keep halving a number (start at 100), printing each
#    step, until it drops below 1.
# ==========================================================================
