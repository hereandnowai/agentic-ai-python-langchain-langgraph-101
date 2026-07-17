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
