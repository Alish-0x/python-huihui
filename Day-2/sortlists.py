#`sort()` sort alphanumerically and ascending by default

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


#descending order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(reverse = True)
print(thislist) 

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#custom function - sort by length of the values
def myfunc(n):
    return len(n)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = myfunc)
print(thislist)

#case insensitive sort
thislist = ["banana", "Orange", "kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#reverse() - reverses the current sorting order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


