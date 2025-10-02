# Removing Items from a Set - `remove()` or `discard()` method
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# Using `discard()`
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#`pop()` method - removes a random item
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

#`clear()` method - empties the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#`del` keyword - deletes the set completely
thisset = {"apple", "banana", "cherry"}
del thisset

