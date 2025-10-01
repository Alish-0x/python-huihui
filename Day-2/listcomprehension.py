#it offers a shorter syntax when you want to create a new list based on the values of an existing list.
fruits = ["apple", "banana", "cherry", "kiwi", "mango", "papaya"]
newlist = [ ]
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

#using list comprehension
newlist = [x for x in fruits if "a" in x]
print(newlist)

#syntax
#newlist = [expression for item in iterable if condition == True]


#condition is optional
#example without condition
newlist = [x for x in fruits]
print(newlist)  
#example with condition
newlist = [x for x in fruits if x != "apple"]
print(newlist)

#range()
newlist = [x for x in range(10)]
print(newlist)

#expression
newlist = [x.upper() for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

