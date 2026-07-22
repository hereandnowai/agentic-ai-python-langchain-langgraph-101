# what is a list in python?
# A list is a collection of items in a particular order.

# part 1: creating a list
account_types = ["savings", "current", "loan", "credit card"]  # makes a list holding four kinds of accounts
print(f"complete list: {account_types}")  # shows the whole list on the screen
print(f"length of the list: {len(account_types)}")  # shows how many items are in the list

mixed_list = ["Alice", 34, True, 15000.0]  # a list can hold different kinds of things at once
print(f"mixed list: {mixed_list}")  # shows that mixed list

basket = []  # makes an empty list with nothing in it yet
print(f"empty list: {basket}")  # shows the empty list

# part 2: accessing list items
print(f"first item: {account_types[0]}")  # shows the first item (counting starts at 0)
print(f"last item: {account_types[-1]}")  # shows the last item (-1 means the end)
print(f"first three items: {account_types[0:3]}")  # shows items 0, 1 and 2 (a slice)
print(f"last two items: {account_types[-2:]}")  # shows the final two items

# part 3: modifying list items
account_types[0] = "premium savings" # replacing the first item
print(f"modified list: {account_types}")  # shows the list after the change

account_types.append("fixed deposit") # adding a new item at the end
print(f"list after appending: {account_types}")  # shows the longer list

account_types.insert(1, "business account") # adding a new item at a specific index
print(f"list after inserting: {account_types}")  # shows the list with the new item in the middle

account_types.extend(["student account", "retirement account"]) # adding multiple items at the end
print(f"list after extending: {account_types}")  # shows the list with both new items added

removed = account_types.pop() # removing the last item
print(f"removed item: {removed}")  # shows which item was taken off the end
print(f"list after popping: {account_types}")  # shows the list without that item

account_types.sort() # sorting the list in ascending order
print(f"sorted list: {account_types}")  # shows the list now in A-to-Z order

account_types.sort(reverse=True) # sorting the list in descending order
print(f"sorted list in descending order: {account_types}")  # shows the list now in Z-to-A order

account_types.reverse() # reversing the order of the list
print(f"reversed list: {account_types}")  # shows the list flipped end to end

numbers = [5, 2, 9, 1, 7]  # makes a list of five numbers
numbers.sort() # sorting the list of numbers in ascending order
print(f"sorted numbers: {numbers}")  # shows the numbers from smallest to biggest
print(f"sorted copy of numbers: {sorted(numbers)}") # creating a sorted copy of the list

print(f"sum of numbers: {sum(numbers)}")  # adds all the numbers together and shows the total
print(f"min number: {min(numbers)}")  # shows the smallest number
print(f"max number: {max(numbers)}")  # shows the biggest number

print("original numbers list:", numbers)  # shows the numbers list is still there unchanged

print("loan" in account_types) # checking if an item exists in the list
print(account_types.index("loan")) # getting the index of an item in the list
print(account_types.count("loan")) # counting the occurrences of an item in the list

for i, account in enumerate(account_types):  # goes through the list giving each item and its position number
    print(f"index: {i}, account type: {account}")  # shows the position number and the item

# part 4: copying a list
a = [1, 2, 3]  # makes a list of three numbers
b = a # b is a reference to the same list as a
b.append(4)  # adds 4 to the list (this also changes a, since they are the same list)
print(f"a: {a}, b: {b}") # both a and b will show

c = a.copy() # c is a copy of the list a
c.append(5)  # adds 5 only to the copy, not to the original
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

