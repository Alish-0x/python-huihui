#although tuples are unchangeable ,there is a workaround to update a tuple by converting it to a list and then back to a tuple


x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)


#adding elements to a tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

#removing elements from a tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)


#deleting a tuple
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) 