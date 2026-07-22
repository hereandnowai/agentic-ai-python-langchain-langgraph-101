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

print("Hello Agent!")  # shows the words Hello Agent! on the screen

# concept 1: what is a variable in python?

agent_name = "Caramel AI" # str
version = 1 # int
is_ready = True # bool

print(agent_name)  # shows the value stored in agent_name (Caramel AI)
print(version)  # shows the value stored in version (1)

# concept 2: what is f-string in python?
print("I am Caramel AI, running bootcamp version 1")  # shows this exact sentence as plain text
print("I am " + agent_name + ", running bootcamp version " + str(version)) # hard way
print("I am {agent_name}, running bootcamp version {version}")  # shows the curly braces as-is because there is no f in front
print(f"I am {agent_name}, running bootcamp version {version}")  # the f lets the braces get filled in with the real values

# concept 3: changing a variable
mood = "curious"  # puts the word curious into a box named mood
print(f"{agent_name} feels {mood}")  # shows a sentence with the name and mood filled in

mood = "confident"  # replaces the old mood with the word confident
print(f"{agent_name} now feels {mood}.")  # shows the sentence again with the new mood

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