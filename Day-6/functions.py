# Function to print a message - `def` keyword is used to define a function
def greet():
    print("Hello, welcome to Python functions!")

#call a function
greet()


#Arguments - functions can take inputs called parameters
def greet_user(name):
    print(f"Hello, {name}!")

#call the function with an argument
greet_user("Ak")

#number of arguments should match what the function expects

#Arbitrary arguments - using *args to accept variable number of arguments
def greet_multiple(*names):
    for name in names:
        print(f"Hello, {name}!")

#call  multiple arguments
greet_multiple("Ak", "Bob", "Charlie")

#Keyword arguments - specify arguments by name
def describe_person(name, age):
    print(f"{name} is {age} years old.")
#call with keyword arguments

describe_person(age=25, name="Alice")
