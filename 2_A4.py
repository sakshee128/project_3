listSize = int(input("Enter the list size:"))
a = set([input(f"Enter element {i} in set a:") for i in range(listSize)])
b = set([input(f"Enter element {i} in set b:") for i in range(listSize)])

# Add new element in list b
b.add(6)
print(f"b after adding 6 is {b}")

# remove element in list b
b.remove(6)
print(f"b after removing 6 is {b}")

#length of list a
print(f"Length of list a is {len(a)}")

# if element present in the list
print(4 in a)

# Union of sets
print(f"Union of sets is {a|b}")

# intersection of sets
print(f"Intersection of sets is {a&b}")

# Difference of sets
print(f"Difference of sets is {a-b}")

# Subset of sets
print(f"Subset of sets is {a^b}")