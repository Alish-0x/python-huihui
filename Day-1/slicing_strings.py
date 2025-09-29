#slicing strings
#return a range of characters by using the slice syntax
#specify the start index and the end index, separated by a colon, to return a part of the string

a = "quick brown fox"
print(a[4:8]) #index 8 is not included 

#slice from the start index 
print(a[4:]) #index 4 to the end so everything will be printed unlike where the end index is specified

#slice from the beginning 
print(a[:8])
#slice from the beginning to the end
print(a[:])

#negative indexing
print(a[-3:]) #last 3 characters


