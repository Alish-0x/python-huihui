#append items -add an item to the end of the list

thislist = ["apple", "banana", "cherry"]
print("Original list:", thislist)
thislist.append("orange")
print("After appending 'orange':", thislist)


#insert items - add an item at the specified index using the insert() method
thislist.insert(1, "lemon")
print("After inserting 'lemon' at index 1:", thislist)

#extend list - add the items of another list (or any iterable) to the end of the current list using the extend() method
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print("After extending with tropical fruits:", thislist)