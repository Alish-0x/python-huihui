#`+` oprator to join two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
joined_list = list1 + list2
print(joined_list)


#`extend()` method to add the elements of one list to the end of another list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)



#append elements of a tuple to a list using `extend()`
list1 = ["a", "b", "c"]
tuple1 = ("d", "e", "f")
list1.extend(tuple1)
print(list1)

#append elements of a set to a list using `extend()`
list1 = ["a", "b", "c"]
set1 = {"d", "e", "f"}
list1.extend(set1)
print(list1)