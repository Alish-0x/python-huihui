#loop a list

#loop through a list using a for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#loop through a list using a while loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1  

#loop through the index numbers of a list
for i in range(len(fruits)):
    print(fruits[i])

#using list comprehension to loop through a list - it is a short hand for loop
[print(fruit) for fruit in fruits]

