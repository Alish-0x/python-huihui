#`copy()` creates a shallow copy of the list
thislist = ["banana", "Orange", "Kiwi", "cherry"]
mylist = thislist.copy()
print(mylist)   

#`list()` also creates a copy of the list
thislist = ["banana", "Orange", "Kiwi", "cherry"]
mylist = list(thislist)
print(mylist)

#`:` operator also creates a copy of the list
thislist = ["banana", "Orange", "Kiwi", "cherry"]
mylist = thislist[:]
print(mylist)

#Note: You cannot copy a list simply by typing `mylist = thislist`, because: `mylist` will only be a reference to `thislist`, and changes made in `mylist` will automatically also be made in `thislist`.