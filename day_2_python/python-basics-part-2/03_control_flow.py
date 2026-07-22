# ==========================================================================
# DAY 2 · Python Basics · 03 — Control flow (decisions & loops)
# --------------------------------------------------------------------------
# Learn: if / elif / else, for loops with range(), looping over data with
# enumerate(), continue & break, and while loops.
# Run:  python 03_control_flow.py
# ==========================================================================

# part 1 if / elif / else (make a decision)
balance = 150000.0  # stores the account balance we will make decisions about

if balance >= 100000.0:  # if the balance is 100,000 or more
    tier = "priority"  # label this customer as priority
elif balance >= 10000.0:  # otherwise, if the balance is 10,000 or more
    tier = "standard"  # label them as standard
else:  # otherwise (balance is below 10,000)
    tier = "basic"  # label them as basic
print(f"tier: {tier}")  # shows which tier was chosen


verified = True  # stores whether the customer is verified (yes/no)
if balance >= 10000.0 and verified:  # if the balance is high enough AND they are verified
    print("Eligible for an instant top-up loan")  # shows they qualify

if balance < 500 or not verified:  # if the balance is very low OR they are not verified
    print("Not eligible for an instant top-up loan")  # shows they do not qualify


name = "Muthu Kumar"  # stores a name to check
if name:  # a non-empty piece of text counts as "yes"
    print("has a name")  # shows the name is filled in
else:  # if the name were empty
    print("name is empty")  # shows the name is blank

# part 2 for loops with range()
print("\nrange(3):")  # prints a heading
for i in range(3):  # repeats three times, with i being 0, then 1, then 2
    print(" step: ", i)  # shows the current step number

# range(start, stop) and range(start, stop, step)
print("\nrange(2, 6):", list(range(2, 6)))  # shows the numbers 2, 3, 4, 5
print("range(0, 10, 2):", list(range(0, 10, 2)))  # shows every second number from 0 up to 10

# summing with a for loop
total = 0  # makes a running total that starts at zero
for n in range(1, 6):  # goes through the numbers 1, 2, 3, 4, 5
    total += n # total = total + n
print(f"sum of numbers from 1 to 5: {total}")  # shows the final total

# part 3 for loops over data (with enumerate)
messages = [  # a chat history: a list where each item is a little dictionary
    {"role": "system", "content": "You are a helpful banking assistant."},
    {"role": "user", "content": "I want to check my account balance."},
    {"role": "assistant", "content": "Your current account balance is $15,000."},
]

print("\nenumerate over messages (index + item):")  # prints a heading
for index, message in enumerate(messages):  # goes through the messages giving each one and its position number
    print(f" index: {index}, role: {message['role']}, content: {message['content']}")  # shows the position, sender and text


# part 4 branching inside a loop (continue = skip to the next iteration)
print("\nuser turns only")  # prints a heading
for msg in messages:  # goes through each message
    if msg["role"] != "user":  # if this message was not sent by the user
        continue # skip to the next iteration
    print(" -", msg["content"])  # shows the user's message text

# counting with a condition (very common):
user_count = 0  # makes a counter that starts at zero
for msg in messages:  # goes through each message
    if msg["role"] == "user":  # if this message was sent by the user
        user_count += 1  # add one to the counter
print(f"number of user turns: {user_count}")  # shows how many user messages there were

# part 5 - while loops (loop until a condition is false) + break (exit the loop)
print("\ncountdown:")  # prints a heading
n = 30  # the number we will count down from
while n > 0:  # keep going as long as n is still above zero
    print(" step: ", n)  # shows the current number
    n -= 1 # n = n - 1 decrement n by 1
print("blast off!")  # shows the countdown is finished

attempts = 0  # makes a counter for how many tries we have made
while True:  # loop forever (until we choose to break out)
    attempts += 1  # add one to the try counter
    print(f"attempt: {attempts}")  # shows which try this is
    if attempts >= 3:  # once we have made 3 tries
        print("max attempts reached, exiting loop")  # shows we are stopping
        break # exit the loop

# part 6 - quick word on nested logic
transactions = [120, -50, 3000, -1200, 75]  # a list of money amounts (plus = in, minus = out)
for amount in transactions:  # goes through each amount one by one
    if amount > 0:  # if the amount is positive (money coming in)
        kind = "credit"  # label it as a credit
    else:  # otherwise (money going out)
        kind = "debit"  # label it as a debit
    size = "large" if abs(amount) >= 1000 else "small"  # calls it large if 1000 or more, else small
    print(f"transaction: {amount}, kind: {kind}, size: {size}")  # shows the amount with its labels


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
