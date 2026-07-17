# ==========================================================================
# DAY 1 · Python Basics · 01 — Variables & f-strings
# --------------------------------------------------------------------------
# In this file you will learn:
#   • what a variable is, and the basic types str / int / bool
#   • how to build text with f-strings
#   • that a variable can be reassigned (changed)
#   • the PEP 8 style rules Python programmers follow
# Run it with:  python 01_hello_agent.py
# ==========================================================================

print("Hello Agent!")

# concept 1: what is a variable in python?

agent_name = "Caramel AI" # str
version = 1 # int
is_ready = True # bool

print(agent_name)
print(version)

# concept 2: what is f-string in python?
print("I am Caramel AI, running bootcamp version 1")
print("I am " + agent_name + ", running bootcamp version " + str(version)) # hard way
print("I am {agent_name}, running bootcamp version {version}")
print(f"I am {agent_name}, running bootcamp version {version}")

# concept 3: changing a variable
mood = "curious"
print(f"{agent_name} feels {mood}")

mood = "confident"
print(f"{agent_name} now feels {mood}.")

# PEP 8 Python Enhancement Proposal 8
# 1. Use snake_case for variable names
# 2. Use 4 spaces for indentation
# 3. put spaces around operators ("+", "-", "*", */) and after commas
# 4. choose descriptive variable names: `agent_name` instead of `a`, `version` instead of `v`, etc.


# ==========================================================================
# 🏋️  PRACTICE ACTIVITIES  —  variables & f-strings
# --------------------------------------------------------------------------
# Write your code below each task, then run:  python 01_hello_agent.py
#
# 1. Create three variables about yourself: your_name (str), lucky_number
#    (int), and likes_coffee (bool). Print each one.
# 2. Use ONE f-string to print:
#       "Hi, I'm <your_name> and my lucky number is <lucky_number>."
# 3. Reassign lucky_number to a new value and print it again — this proves
#    a variable can change over time.
# 4. Print the type of each variable, e.g.  print(type(your_name)).
# 5. BONUS: rebuild the sentence from task 2 using '+' concatenation instead
#    of an f-string. Remember to wrap the number with str().
# ==========================================================================