# unpacking a tuple
fruits = ("apple", "banana", "cherry")
a, b, c = fruits
print(a)
print(b)
print(c)


# unpacking with asterisk - to assign remaining values to a list
fruits = ("apple", "banana", "cherry", "orange", "kiwi")
a, b, *c = fruits
print(a)
print(b)
print(c)


# unpacking with asterisk in different positions
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "mango")
*a, b, c = fruits
print(a)
print(b)
print(c)
