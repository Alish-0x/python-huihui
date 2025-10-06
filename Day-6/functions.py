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


#Arbitrary keyword arguments - using **kwargs to accept variable number of named arguments
def my_function(**kid):
    print("His last name is " + kid["lname"])   
my_function(fname = "Tobias", lname = "Refsnes")


#Default parameter value - if no argument is provided, the default is used
def greet_with_default(name="Guest"):
    print(f"Hello, {name}!")


#Return values - functions can return values using the `return` statement
def add(a, b):
    return a + b
result = add(5, 3)
print("Sum:", result)

#pass statement - used as a placeholder for future code
def placeholder_function():
    pass

#positional-only arguments - arguments that must be specified by position
def positional_only_function(name, /, age):
    print(f"{name} is {age} years old.")
positional_only_function("Jane", 28)

#keyword-only arguments - arguments that must be specified by name
def keyword_only_function(*, name, age):
    print(f"{name} is {age} years old.")
keyword_only_function(name="John", age=30)

#combine positional-only and keyword-only arguments
def combined_function(name, /, age, *, city):
    print(f"{name} is {age} years old and lives in {city}.")
combined_function("Alice", 25, city="New York")

#recursive functions - functions that call themselves
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print("Factorial of 5:", factorial(5))