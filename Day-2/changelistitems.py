#change list items - change a specific items value or range of items values

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blueberry"
print(thislist)
thislist[0:2] = ["blackcurrant", "watermelon"]
print(thislist)

#we can also insert items without replacing the existing values using the insert() method
thislist.insert(2, "orange")
print(thislist)