# python has two primitive loops - while loop and for loop

# while loop
i = 1
while i <= 5:
    print(i)
    i += 1  

#break statement - to exit the loop
j = 1
while j <= 10:
    if j == 6:
        break
    print(j)
    j += 1

#continue statement
k = 1
while k <= 10:
    if k % 2 == 0:
        k += 1
        continue
    print(k)
    k += 1


#else statement with while loop - executes when the loop condition becomes false
n = 1
while n <= 5:
    print(n)
    n += 1
else:
    print("Loop ended")
