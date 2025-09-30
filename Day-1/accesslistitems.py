#access list items
thislist = ["apple", "banana", "cherry"]
print(thislist)
print(thislist[0])
print(thislist[1])
print(thislist[2])

#we can also use negative indexing to access list items
print(thislist[-1])
print(thislist[-2])
print(thislist[-3])

#we can also use range of indexes to access multiple items in a list
print(thislist[0:2]) 
print(thislist[1:3])
print(thislist[:2])
print(thislist[1:])
print(thislist[-2:])

#check if item exists
if "apple" in thislist:
    print("Yes, 'apple' is in the list") 
if "mango" in thislist:
    print("Yes, 'mango' is in the list")
else:
    print("No, 'mango' is not in the list")