# tuples in python are immutable lists,
# meaning they cannot be changed after creation.
# They are defined using parentheses ().

point = (12.5, 48.1)  # makes a fixed pair of numbers and stores it in point
color = (255, 200, 0)  # makes a fixed group of three numbers and stores it in color
person = ("Priya", 30, "savings")  # makes a fixed group of three details and stores it in person

print("point:", point)  # shows the point pair
print("color:", color)  # shows the color group

print(point[0]) # access first element
print(color[1]) # access second element
print(person[-1]) # access last element

name, age, account_type = person # unpacking a tuple into variables
print(f"name: {name}, age: {age}, account_type: {account_type}")  # shows the three unpacked details in a sentence

# what is a function in python?
# fun
def min_and_max(a, b):  # makes a helper that takes two numbers
    """Returns the minimum and maximum of two numbers."""
    if a < b:  # check whether the first number is smaller than the second
        return a, b  # gives back the smaller one first, then the larger one
    return b, a  # otherwise gives back b first, then a

low, high = min_and_max(9, 4)  # runs the helper and unpacks its two answers into low and high
print(f"low: {low}, high: {high}")  # shows the smaller and larger numbers


# sets in python are unordered collections of unique elements.
# They are defined using curly braces {}.
# it automatically removes duplicates and does not maintain order.

tags = {"loan", "priority", "loan", "kyc", "priority"}  # makes a set, which keeps only one of each word
print("tags:", tags) # duplicates are removed

print("loan" in tags) # check if an element is in the set
print("car" in tags) # check if an element is not in the set

tags.add("verified") # add an element to the set
print("tags after adding 'verified':", tags)
tags.add("loan") # adding an existing element does nothing
print("tags after adding 'loan' again:", tags)
tags.discard("kyc") # remove an element from the set
print("tags after discarding 'kyc':", tags)

raw_words = ["yes", "no", "yes", "maybe", "no", "yes"]  # makes a list with several repeated words
unique_words = list(set(raw_words)) # convert list to set to remove duplicates, then back to list
print("unique_words:", unique_words)  # shows the list of words with repeats removed

skills_needed = {"python", "sql", "apis"}  # makes a set of the skills a job needs
skills_have = {"python", "excel", "apis"}  # makes a set of the skills a person already has
print("\nin BOTH (intersection):", skills_needed & skills_have)  # shows only the skills found in both sets
print("in EITHER (union):", skills_needed | skills_have)  # shows every skill from both sets combined
print("needed but MISSING: ", skills_needed - skills_have)  # shows needed skills the person does not have yet


# ==========================================================================
# 🏋️  PRACTICE ACTIVITIES  —  tuples & sets
# --------------------------------------------------------------------------
# Write your code below each task, then run:  python 04_tuples_and_sets.py
#
# 1. Make a tuple  person = ("Asha", 27, "current")  and unpack it into
#    three variables in ONE line, then print them.
# 2. Try to change  person[0] = "Ravi".  Read the error message — why does
#    a tuple not allow this? (Write your answer as a comment.)
# 3. Given  nums = [3, 3, 1, 2, 2, 3], use a set to find the UNIQUE values.
# 4. Two sets: a = {"python", "sql"}, b = {"sql", "excel"}.  Print the values
#    in BOTH (&), in EITHER (|), and only in 'a' (-).
# 5. Write a function  first_and_last(items)  that returns the first and last
#    element of a list as a tuple.
# ==========================================================================