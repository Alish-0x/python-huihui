# for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

#looping through a string
for c in "banana":
    print(c)

#using break statement to exit the loop
for x in fruits:
    if x == "banana":
        break
    print(x)

#using continue statement
for x in fruits:
    if x == "banana":
        continue
    print(x)

#using range() function
for i in range(6):
    print(i)

#else in for loop - executes when the loop is finished
for i in range(6):
    print(i)
else:
    print("Loop ended")

#nested for loop
adj = ["red", "big", "tasty"]
for a in adj:
    for f in fruits:
        print(a, f)

#using pass statement - does nothing, used as a placeholder
for x in fruits:
    pass  # Placeholder for future 
