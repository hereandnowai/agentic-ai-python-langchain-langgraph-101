# what is a list in python?
# A list is a collection of items in a particular order.

# part 1: creating a list
account_types = ["savings", "current", "loan", "credit card"]
print(f"complete list: {account_types}")
print(f"length of the list: {len(account_types)}")

mixed_list = ["Alice", 34, True, 15000.0]
print(f"mixed list: {mixed_list}")

basket = []
print(f"empty list: {basket}")

# part 2: accessing list items
print(f"first item: {account_types[0]}")
print(f"last item: {account_types[-1]}")
print(f"first three items: {account_types[0:3]}")
print(f"last two items: {account_types[-2:]}")

# part 3: modifying list items
account_types[0] = "premium savings" # replacing the first item
print(f"modified list: {account_types}")

account_types.append("fixed deposit") # adding a new item at the end
print(f"list after appending: {account_types}")

account_types.insert(1, "business account") # adding a new item at a specific index
print(f"list after inserting: {account_types}")

account_types.extend(["student account", "retirement account"]) # adding multiple items at the end
print(f"list after extending: {account_types}")

removed = account_types.pop() # removing the last item
print(f"removed item: {removed}")
print(f"list after popping: {account_types}")

account_types.sort() # sorting the list in ascending order
print(f"sorted list: {account_types}")

account_types.sort(reverse=True) # sorting the list in descending order
print(f"sorted list in descending order: {account_types}")

account_types.reverse() # reversing the order of the list
print(f"reversed list: {account_types}")

numbers = [5, 2, 9, 1, 7]
numbers.sort() # sorting the list of numbers in ascending order
print(f"sorted numbers: {numbers}")
print(f"sorted copy of numbers: {sorted(numbers)}") # creating a sorted copy of the list

print(f"sum of numbers: {sum(numbers)}")
print(f"min number: {min(numbers)}")
print(f"max number: {max(numbers)}")

print("original numbers list:", numbers)

print("loan" in account_types) # checking if an item exists in the list
print(account_types.index("loan")) # getting the index of an item in the list
print(account_types.count("loan")) # counting the occurrences of an item in the list

for i, account in enumerate(account_types):
    print(f"index: {i}, account type: {account}")

# part 4: copying a list
a = [1, 2, 3]
b = a # b is a reference to the same list as a
b.append(4)
print(f"a: {a}, b: {b}") # both a and b will show

c = a.copy() # c is a copy of the list a
c.append(5)
print(f"a: {a}, c: {c}") # a will not show the new item added to c


# ==========================================================================
# 🏋️  PRACTICE ACTIVITIES  —  lists
# --------------------------------------------------------------------------
# Write your code below each task, then run:  python 01_lists.py
#
# 1. Make  fruits = ["apple", "banana", "cherry"].  Append "mango" to the
#    end, insert "kiwi" at the front (index 0), then print the list.
# 2. Print just the first TWO fruits using slicing.
# 3. Sort  [5, 2, 9, 1, 7]  ascending, then sort it again descending.
# 4. From  scores = [10, 20, 30, 40], print the sum, the max, and the
#    average (sum divided by len).
# 5. Explain in a comment the difference between  b = a  and  c = a.copy().
#    Prove it: append to one and print both a and b, then a and c.
# ==========================================================================

