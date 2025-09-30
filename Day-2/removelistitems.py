#remove items - remove an item from the list
thislist = ["apple", "banana", "cherry"]
print("Original list:", thislist)
thislist.remove("banana")
print("After removing 'banana':", thislist)

#pop items - remove an item at the specified index (or the last item if no index is specified) using the pop() method
popped_item = thislist.pop(1)
print("After popping item at index 1:", thislist)
print("Popped item:", popped_item)


#del keyword - removes specificed index
del thislist[0]
print("after del item:", thislist)

#clear list - remove all items from the list using the clear() method
thislist.clear()
print("After clearing the list:", thislist)