# Boolean represents either True or False

'''
when you compare two values, the expression is evaluated and Python returns the Boolean answer:
print(10 > 9)   # True
print(10 == 9)  # False
print(10 < 9)   # False
'''

a = 10
b = 9
if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")

#we can also use the bool() function to evaluate any value, and give us True or False in return

print(bool("Hello"))  # True
print(bool(15))       # True
print(bool(0))        # False

# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.


# Functions can Return a Boolean
def myFunction() :
    return True 
print(myFunction())  
if myFunction():
    print("YES!")
else:
    print("NO!")

#python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type
x = 200
print(isinstance(x, int))  # True
y = "Hello"
print(isinstance(y, int))  # False
