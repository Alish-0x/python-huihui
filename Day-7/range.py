#range() function - it is used to return a sequence of numbers.
#its immutable meaning it cannot be changed after its created 

#creating a range - it can be called with one, two or three arguments.

#range(start, stop, step)


#call range with one argument - it generates numbers from 0 to stop-1
r = range(10)
print(r) #output: range(0, 10)

#call range with two arguments - it generates numbers from start to stop-1
r1 = range(1, 10)
print(r1) #output: range(1, 10)

#call range with three arguments - it generates numbers from start to stop-1 with a step value
r2 = range(1, 10, 2)
print(r2) #output: range(1, 10, 2)

#using range in for loop - it is commonly used in for loops to iterate over a sequence of numbers.
for i in range(5):
    print(i) #output: 0 1 2 3 4


#using list to display range - we can convert the range object to a list to see all the numbers in the range.
print(list(range(5))) #output: [0, 1, 2, 3, 4]
print(list(range(1, 10))) #output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1, 10, 2))) #output: [1, 3, 5, 7, 9]

#using negative step - we can use a negative step value to generate numbers in reverse order.
print(list(range(10, 0, -1))) #output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(list(range(10, 0, -2))) #output: [10, 8, 6, 4, 2] 

#slicing a range - we can slice a range object to get a subrange of numbers.
r3 = range(10)
print(r3[2:5]) #output: range(2, 5)
print(list(r3[2:])) #output: [2, 3, 4, 5, 6, 7, 8, 9]

#membership testing - we can use the `in` operator to check if a number is in a range.
r4 = range(10)
print(5 in r4) #output: True
print(15 in r4) #output: False

#length of a range - we can use the `len()` function to get the number of elements in a range.
r5 = range(10)
print(len(r5)) #output: 10
r6 = range(1, 10, 2)
print(len(r6)) #output: 5