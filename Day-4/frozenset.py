# Frozenset - a frozenset is an immutable version of a set
# Once a frozenset is created, you cannot change its items, add or remove items

# Creating a frozenset - use the frozenset() function
thisset = frozenset({"apple", "banana", "cherry"})
print(thisset)


# Looping through a frozenset
for x in thisset:
    print(x)