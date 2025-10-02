# Adding Items to a Set - `add()` method
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# Adding multiple items to a set - `update()` method
thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
print(thisset)

# Adding items from a list to a set
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# Adding items from a tuple to a set
thisset = {"apple", "banana", "cherry"}
mytuple = ("kiwi", "orange")
thisset.update(mytuple)
print(thisset)