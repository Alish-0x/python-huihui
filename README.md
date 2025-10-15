# Python Learning Journey 🐍

A comprehensive guide covering fundamental to intermediate Python concepts, organized day-by-day.

## 📚 Table of Contents

- [Day 0: Python Basics](#day-0-python-basics)
- [Day 1: Strings and Operators](#day-1-strings-and-operators)
- [Day 2: Lists](#day-2-lists)
- [Day 3: Tuples](#day-3-tuples)
- [Day 4: Sets](#day-4-sets)
- [Day 5: Dictionaries](#day-5-dictionaries)
- [Day 6: Control Flow and Functions](#day-6-control-flow-and-functions)
- [Day 7: Decorators & range](#day-7-decorators--range)

---
## Day 0: Python Basics

### Topics Covered
- **Hello World** - Your first Python program
- **Variables** - Storing and managing data
- **Data Types** - Understanding Python's built-in types
- **Type Casting** - Converting between data types
- **Comments** - Code documentation
- **Indentation** - Python's syntax structure

### Key Concepts

#### Variables
```python
# Variable assignment
name = "Python"
age = 30
is_active = True

# Multiple assignments
x, y, z = 1, 2, 3

# Assign same value to multiple variables
a = b = c = 100

# Unpacking collections
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
```

#### Data Types
```python
# Text Type
str_var = "Hello World"

# Numeric Types
int_var = 20
float_var = 20.5
complex_var = 1j

# Sequence Types
list_var = ["apple", "banana", "cherry"]
tuple_var = ("apple", "banana", "cherry")
range_var = range(6)

# Boolean Type
bool_var = True
```

#### Global vs Local Variables
```python
# Global variable
x = "global"

def my_function():
    # Local variable
    x = "local"
    print(x)  # Prints: local

my_function()
print(x)  # Prints: global

# Using global keyword
def modify_global():
    global x
    x = "modified"
```

#### Python Numbers
```python
# Integer
x = 1

# Float
y = 2.8

# Complex
z = 1j

# Type conversion
a = float(x)  # 1.0
b = int(y)    # 2
c = complex(x) # (1+0j)
```

---

## Day 1: Strings and Operators

### Topics Covered
- **String Operations** - Manipulation and formatting
- **String Methods** - Built-in string functions
- **Escape Characters** - Special characters in strings
- **Boolean Values** - True/False logic
- **Python Operators** - Arithmetic, comparison, logical, etc.

### Key Concepts

#### String Slicing
```python
text = "Hello, World!"

# Slicing
print(text[0:5])    # "Hello"
print(text[:5])     # "Hello"
print(text[7:])     # "World!"
print(text[-5:-1])  # "orld"

# Step slicing
print(text[::2])    # "Hlo ol!"
print(text[::-1])   # "!dlroW ,olleH" (reversed)
```

#### String Modification
```python
text = "hello world"

# Upper and lower case
print(text.upper())      # "HELLO WORLD"
print(text.lower())      # "hello world"
print(text.capitalize()) # "Hello world"
print(text.title())      # "Hello World"

# Strip whitespace
text = "  Hello  "
print(text.strip())   # "Hello"
print(text.lstrip())  # "Hello  "
print(text.rstrip())  # "  Hello"

# Replace
text = "Hello World"
print(text.replace("World", "Python"))  # "Hello Python"
```

#### String Concatenation
```python
# Using + operator
first = "Hello"
last = "World"
full = first + " " + last  # "Hello World"

# Using join()
words = ["Hello", "World"]
sentence = " ".join(words)  # "Hello World"
```

#### String Formatting
```python
# f-strings (Python 3.6+)
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old")

# format() method
print("My name is {} and I am {} years old".format(name, age))

# Old style
print("My name is %s and I am %d years old" % (name, age))
```

#### Escape Characters
```python
# Common escape characters
print("Hello\nWorld")       # New line
print("Hello\tWorld")       # Tab
print("Hello\\World")       # Backslash
print("Hello\"World\"")     # Double quotes
print('Hello\'World\'')     # Single quotes
```

#### Python Operators
```python
# Arithmetic Operators
+ - * / % ** //

# Comparison Operators
== != > < >= <=

# Logical Operators
and or not

# Assignment Operators
= += -= *= /= %= //= **=

# Identity Operators
is, is not

# Membership Operators
in, not in

# Bitwise Operators
& | ^ ~ << >>
```

#### Boolean Logic
```python
# Boolean values
x = True
y = False

# Boolean operations
print(x and y)  # False
print(x or y)   # True
print(not x)    # False

# Truthy and Falsy values
bool(0)         # False
bool("")        # False
bool(None)      # False
bool([])        # False
bool(1)         # True
bool("text")    # True
```

---

## Day 2: Lists

### Topics Covered
- **Creating Lists** - List initialization
- **Accessing Items** - Indexing and slicing
- **Modifying Lists** - Changing, adding, removing items
- **List Operations** - Sorting, copying, joining
- **List Comprehension** - Elegant list creation
- **Looping Lists** - Iterating through lists

### Key Concepts

#### Python Lists
```python
# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]

# List constructor
my_list = list(("apple", "banana", "cherry"))

# Nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

#### Accessing List Items
```python
fruits = ["apple", "banana", "cherry", "orange", "kiwi"]

# Positive indexing
print(fruits[0])    # "apple"
print(fruits[2])    # "cherry"

# Negative indexing
print(fruits[-1])   # "kiwi"
print(fruits[-2])   # "orange"

# Slicing
print(fruits[1:3])  # ["banana", "cherry"]
print(fruits[:3])   # ["apple", "banana", "cherry"]
print(fruits[2:])   # ["cherry", "orange", "kiwi"]
print(fruits[-3:-1]) # ["cherry", "orange"]
```

#### Changing List Items
```python
fruits = ["apple", "banana", "cherry"]

# Change single item
fruits[1] = "blackberry"

# Change range of items
fruits[1:3] = ["blueberry", "strawberry"]

# Insert without replacing
fruits[1:2] = ["watermelon", "melon"]
```

#### Adding List Items
```python
fruits = ["apple", "banana", "cherry"]

# append() - add to end
fruits.append("orange")

# insert() - add at specific position
fruits.insert(1, "mango")

# extend() - add multiple items
fruits.extend(["kiwi", "grape"])

# Using + operator
fruits = fruits + ["pear", "plum"]
```

#### Removing List Items
```python
fruits = ["apple", "banana", "cherry", "banana"]

# remove() - remove specific value
fruits.remove("banana")  # Removes first occurrence

# pop() - remove by index
fruits.pop(1)      # Removes item at index 1
fruits.pop()       # Removes last item

# del - delete by index or slice
del fruits[0]
del fruits[0:2]

# clear() - empty the list
fruits.clear()
```

#### Looping Lists
```python
fruits = ["apple", "banana", "cherry"]

# For loop
for fruit in fruits:
    print(fruit)

# Loop with index
for i in range(len(fruits)):
    print(fruits[i])

# Using enumerate()
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# While loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
```

#### List Comprehension
```python
# Basic syntax: [expression for item in iterable]
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]

# With condition
evens = [x for x in numbers if x % 2 == 0]

# Multiple conditions
filtered = [x for x in numbers if x > 2 if x < 5]

# With if-else
result = [x if x % 2 == 0 else x*2 for x in numbers]

# Nested list comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]
```

#### Sorting Lists
```python
numbers = [3, 1, 4, 1, 5, 9, 2]

# sort() - sorts the list in-place
numbers.sort()
numbers.sort(reverse=True)

# sorted() - returns new sorted list
sorted_nums = sorted(numbers)

# Custom sorting
fruits = ["banana", "apple", "cherry"]
fruits.sort(key=len)  # Sort by length

# Reverse order
numbers.reverse()
```

#### Copying Lists
```python
original = [1, 2, 3]

# Using copy() method
copy1 = original.copy()

# Using list() constructor
copy2 = list(original)

# Using slice
copy3 = original[:]

# Shallow vs deep copy (for nested lists)
import copy
deep_copy = copy.deepcopy(original)
```

#### Joining Lists
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Using + operator
list3 = list1 + list2

# Using extend()
list1.extend(list2)

# Using loop
for item in list2:
    list1.append(item)
```

---

## Day 3: Tuples

### Topics Covered
- **Creating Tuples** - Tuple initialization
- **Accessing Tuples** - Indexing and slicing
- **Updating Tuples** - Working around immutability
- **Unpacking Tuples** - Extracting values
- **Looping Tuples** - Iteration methods
- **Joining Tuples** - Combining tuples

### Key Concepts

#### Python Tuples
```python
# Creating tuples
fruits = ("apple", "banana", "cherry")
numbers = (1, 2, 3, 4, 5)
mixed = (1, "two", 3.0, True)

# Single item tuple (comma required)
single = ("apple",)

# Tuple constructor
my_tuple = tuple(("apple", "banana", "cherry"))

# Tuples are immutable
# fruits[0] = "orange"  # This raises an error
```

#### Accessing Tuples
```python
fruits = ("apple", "banana", "cherry", "orange", "kiwi")

# Indexing
print(fruits[0])    # "apple"
print(fruits[-1])   # "kiwi"

# Slicing
print(fruits[1:3])  # ("banana", "cherry")
print(fruits[:3])   # ("apple", "banana", "cherry")
print(fruits[2:])   # ("cherry", "orange", "kiwi")
```

#### Updating Tuples
```python
# Tuples are immutable, but you can work around it
fruits = ("apple", "banana", "cherry")

# Convert to list, modify, convert back
fruits_list = list(fruits)
fruits_list[1] = "mango"
fruits = tuple(fruits_list)

# Add tuples
fruits = fruits + ("orange",)

# Remove items (by creating new tuple)
fruits = fruits[:1] + fruits[2:]
```

#### Unpacking Tuples
```python
fruits = ("apple", "banana", "cherry")

# Basic unpacking
x, y, z = fruits

# Using asterisk *
fruits = ("apple", "banana", "cherry", "orange", "kiwi")
x, y, *rest = fruits  # x="apple", y="banana", rest=["cherry", "orange", "kiwi"]

x, *middle, z = fruits  # x="apple", middle=["banana", "cherry", "orange"], z="kiwi"
```

#### Looping Tuples
```python
fruits = ("apple", "banana", "cherry")

# For loop
for fruit in fruits:
    print(fruit)

# Loop with index
for i in range(len(fruits)):
    print(fruits[i])

# Using enumerate()
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

#### Joining Tuples
```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Using + operator
tuple3 = tuple1 + tuple2

# Multiply tuples
tuple4 = tuple1 * 2  # (1, 2, 3, 1, 2, 3)
```

#### Tuple Methods
```python
numbers = (1, 2, 3, 2, 4, 2, 5)

# count() - count occurrences
print(numbers.count(2))  # 3

# index() - find first occurrence
print(numbers.index(3))  # 2
```

---

## Day 4: Sets

### Topics Covered
- **Creating Sets** - Set initialization
- **Accessing Sets** - Working with unordered collections
- **Adding Items** - Set insertion methods
- **Removing Items** - Set deletion methods
- **Joining Sets** - Set operations
- **Looping Sets** - Iteration
- **Frozen Sets** - Immutable sets

### Key Concepts

#### Python Sets
```python
# Creating sets
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}

# Set constructor
my_set = set(("apple", "banana", "cherry"))

# Sets are unordered and unique
# Duplicates are automatically removed
numbers = {1, 2, 2, 3, 3, 3}  # Results in {1, 2, 3}
```

#### Accessing Set Items
```python
fruits = {"apple", "banana", "cherry"}

# Cannot access by index (unordered)
# fruits[0]  # This raises an error

# Check if item exists
print("apple" in fruits)  # True

# Loop through items
for fruit in fruits:
    print(fruit)
```

#### Adding Set Items
```python
fruits = {"apple", "banana", "cherry"}

# add() - add single item
fruits.add("orange")

# update() - add multiple items
fruits.update(["mango", "grape"])

# Update with any iterable
fruits.update(["kiwi"], {"pear"}, ("plum",))
```

#### Removing Set Items
```python
fruits = {"apple", "banana", "cherry"}

# remove() - removes item (raises error if not found)
fruits.remove("banana")

# discard() - removes item (no error if not found)
fruits.discard("banana")

# pop() - removes random item
item = fruits.pop()

# clear() - empty the set
fruits.clear()

# del - delete the set completely
del fruits
```

#### Joining Sets
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# union() - combine sets (no duplicates)
set3 = set1.union(set2)  # {1, 2, 3, 4, 5}
set3 = set1 | set2       # Using operator

# intersection() - common elements
set3 = set1.intersection(set2)  # {3}
set3 = set1 & set2              # Using operator

# difference() - elements in first but not second
set3 = set1.difference(set2)    # {1, 2}
set3 = set1 - set2              # Using operator

# symmetric_difference() - elements in either but not both
set3 = set1.symmetric_difference(set2)  # {1, 2, 4, 5}
set3 = set1 ^ set2                      # Using operator
```

#### Set Methods
```python
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

# issubset() - check if subset
print(set1.issubset(set2))  # True

# issuperset() - check if superset
print(set2.issuperset(set1))  # True

# isdisjoint() - check if no common elements
set3 = {6, 7, 8}
print(set1.isdisjoint(set3))  # True
```

#### Looping Sets
```python
fruits = {"apple", "banana", "cherry"}

# For loop
for fruit in fruits:
    print(fruit)

# Cannot use index-based loops (unordered)
```

#### Frozen Sets
```python
# Frozen sets are immutable
fruits = frozenset(["apple", "banana", "cherry"])

# Can be used as dictionary keys
my_dict = {fruits: "fruit_set"}

# Cannot modify
# fruits.add("orange")  # This raises an error

# Can perform set operations
set1 = frozenset([1, 2, 3])
set2 = frozenset([3, 4, 5])
result = set1 | set2  # Works fine
```

---

## Day 5: Dictionaries

### Topics Covered
- **Creating Dictionaries** - Key-value pairs
- **Accessing Items** - Retrieving values
- **Changing Items** - Modifying dictionaries
- **Adding Items** - Inserting new key-value pairs
- **Removing Items** - Deleting entries
- **Looping Dictionaries** - Iteration methods
- **Copying Dictionaries** - Dictionary duplication
- **Nested Dictionaries** - Dictionaries within dictionaries

### Key Concepts

#### Python Dictionaries
```python
# Creating dictionaries
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Using dict() constructor
person = dict(name="John", age=30, city="New York")

# Empty dictionary
empty = {}
empty = dict()
```

#### Accessing Dictionary Items
```python
person = {"name": "John", "age": 30, "city": "New York"}

# Using brackets
print(person["name"])  # "John"

# Using get() method (safer)
print(person.get("name"))  # "John"
print(person.get("country", "USA"))  # Returns "USA" if key doesn't exist

# Get all keys
print(person.keys())  # dict_keys(['name', 'age', 'city'])

# Get all values
print(person.values())  # dict_values(['John', 30, 'New York'])

# Get all items (key-value pairs)
print(person.items())  # dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])
```

#### Changing Dictionary Items
```python
person = {"name": "John", "age": 30, "city": "New York"}

# Update single item
person["age"] = 31

# Update multiple items
person.update({"age": 32, "city": "Boston"})
```

#### Adding Dictionary Items
```python
person = {"name": "John", "age": 30}

# Add single item
person["city"] = "New York"

# Add multiple items
person.update({"country": "USA", "job": "Developer"})
```

#### Removing Dictionary Items
```python
person = {"name": "John", "age": 30, "city": "New York"}

# pop() - remove specific key
person.pop("age")

# popitem() - remove last inserted item
person.popitem()

# del - delete specific key
del person["city"]

# del - delete entire dictionary
del person

# clear() - empty the dictionary
person.clear()
```

#### Looping Dictionaries
```python
person = {"name": "John", "age": 30, "city": "New York"}

# Loop through keys
for key in person:
    print(key)

for key in person.keys():
    print(key)

# Loop through values
for value in person.values():
    print(value)

# Loop through items (key-value pairs)
for key, value in person.items():
    print(f"{key}: {value}")
```

#### Copying Dictionaries
```python
original = {"name": "John", "age": 30}

# Using copy() method
copy1 = original.copy()

# Using dict() constructor
copy2 = dict(original)

# Shallow vs deep copy (for nested dictionaries)
import copy
deep_copy = copy.deepcopy(original)
```

#### Nested Dictionaries
```python
# Dictionary of dictionaries
family = {
    "child1": {"name": "Emily", "age": 5},
    "child2": {"name": "Tobias", "age": 8},
    "child3": {"name": "Linus", "age": 10}
}

# Accessing nested values
print(family["child1"]["name"])  # "Emily"

# Adding nested dictionary
family["child4"] = {"name": "Sarah", "age": 3}

# Looping nested dictionaries
for person, info in family.items():
    print(f"\n{person}:")
    for key, value in info.items():
        print(f"  {key}: {value}")
```

#### Dictionary Methods Summary
```python
# clear() - Remove all elements
# copy() - Return a copy
# fromkeys() - Create dict with specified keys
# get() - Return value of specified key
# items() - Return list of tuple pairs (key, value)
# keys() - Return list of keys
# pop() - Remove element with specified key
# popitem() - Remove last inserted key-value pair
# setdefault() - Return value of key, if not exist insert with specified value
# update() - Update dictionary with key-value pairs
# values() - Return list of all values
```

---

## Day 6: Control Flow and Functions

### Topics Covered
- **If-Else Statements** - Conditional logic
- **While Loops** - Indefinite iteration
- **For Loops** - Definite iteration
- **Match Statements** - Pattern matching (Python 3.10+)
- **Functions** - Code reusability and organization

### Key Concepts

#### If-Else Statements
```python
# Basic if statement
x = 10
if x > 5:
    print("x is greater than 5")

# If-else
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

# If-elif-else
x = 5
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

# Nested if
x = 10
if x > 5:
    if x > 8:
        print("x is greater than 8")
    else:
        print("x is between 5 and 8")

# Ternary operator (one-line if-else)
x = 10
result = "Even" if x % 2 == 0 else "Odd"

# Multiple conditions
age = 25
has_license = True
if age >= 18 and has_license:
    print("Can drive")
```

#### While Loops
```python
# Basic while loop
i = 1
while i <= 5:
    print(i)
    i += 1

# While with break
i = 1
while True:
    print(i)
    if i >= 5:
        break
    i += 1

# While with continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue  # Skip when i is 3
    print(i)

# While with else (executes when condition becomes false)
i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("Loop completed")
```

#### For Loops
```python
# Loop through sequence
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop through string
for char in "Python":
    print(char)

# Loop with range()
for i in range(5):  # 0 to 4
    print(i)

for i in range(2, 10):  # 2 to 9
    print(i)

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8 (step of 2)
    print(i)

# For with break
for i in range(10):
    if i == 5:
        break
    print(i)

# For with continue
for i in range(10):
    if i == 5:
        continue
    print(i)

# For with else
for i in range(5):
    print(i)
else:
    print("Loop completed")

# Nested for loops
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")
```

#### Match Statements (Python 3.10+)
```python
# Basic match statement
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"

# Match with multiple patterns
def check_value(value):
    match value:
        case 0:
            return "Zero"
        case 1 | 2 | 3:
            return "Small number"
        case _:
            return "Other"

# Match with guards
def categorize_age(age):
    match age:
        case n if n < 0:
            return "Invalid"
        case n if n < 13:
            return "Child"
        case n if n < 20:
            return "Teenager"
        case _:
            return "Adult"
```

#### Functions
```python
# Basic function
def greet():
    print("Hello, World!")

greet()  # Call the function

# Function with parameters
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# Function with default parameters
def greet(name="World"):
    print(f"Hello, {name}!")

greet()        # Uses default
greet("Alice") # Uses provided value

# Function with return value
def add(a, b):
    return a + b

result = add(5, 3)  # result = 8

# Multiple return values
def get_info():
    name = "John"
    age = 30
    return name, age

name, age = get_info()

# Arbitrary arguments (*args)
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4, 5))  # 15

# Keyword arguments (**kwargs)
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="John", age=30, city="New York")

# Lambda functions (anonymous functions)
square = lambda x: x ** 2
print(square(5))  # 25

add = lambda x, y: x + y
print(add(3, 4))  # 7

# Lambda with map()
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))

# Lambda with filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Lambda with sorted()
points = [(1, 2), (3, 1), (5, 0)]
sorted_points = sorted(points, key=lambda point: point[1])

# Recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # 120

# Function documentation (docstrings)
def greet(name):
    """
    Greets a person with their name.
    
    Parameters:
    name (str): The name of the person to greet
    
    Returns:
    None
    """
    print(f"Hello, {name}!")
```

---

## 🎯 Quick Reference

### Common String Methods
- `upper()`, `lower()`, `capitalize()`, `title()`
- `strip()`, `lstrip()`, `rstrip()`
- `replace(old, new)`, `split(delimiter)`
- `find(substring)`, `count(substring)`
- `startswith()`, `endswith()`
- `join(iterable)`

### Common List Methods
- `append(item)`, `insert(index, item)`, `extend(iterable)`
- `remove(item)`, `pop(index)`, `clear()`
- `sort()`, `reverse()`
- `count(item)`, `index(item)`
- `copy()`

### Common Dictionary Methods
- `get(key, default)`, `keys()`, `values()`, `items()`
- `pop(key)`, `popitem()`, `clear()`
- `update(dict)`, `copy()`
- `setdefault(key, default)`

### Common Set Methods
- `add(item)`, `update(iterable)`, `remove(item)`, `discard(item)`
- `union()`, `intersection()`, `difference()`, `symmetric_difference()`
- `issubset()`, `issuperset()`, `isdisjoint()`

---

## 💡 Best Practices

1. **Use meaningful variable names**: `user_name` instead of `un`
2. **Follow PEP 8**: Python's style guide
3. **Write docstrings**: Document your functions
4. **Use list comprehensions**: More Pythonic and efficient
5. **Handle exceptions**: Use try-except blocks
6. **Use f-strings**: Modern and readable string formatting
7. **Keep functions small**: Single Responsibility Principle
8. **Use type hints**: Improve code readability (Python 3.5+)

```python
def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"
```

---



## Day 7: Decorators & range

### Topics Covered
- **Decorators** - Functions that modify other functions
- **range()** - Creating integer sequences for iteration

### Quick Overview

#### Decorators
Decorators are higher-order functions that take a function as input and return a new function (usually a wrapper) that adds behavior before or after the original function runs. Use `functools.wraps` to preserve metadata.

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before the function")
        result = func(*args, **kwargs)
        print("After the function")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
# Output:
# Before the function
# Hello, Alice!
# After the function
```

Decorators with arguments:

```python
def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hi")

greet()  # prints Hi three times
```

Common uses: logging, timing, memoization, access control, input validation.

#### range()
`range()` creates an iterable sequence of integers. It is memory-efficient and commonly used with loops.

```python
range(5)        # 0,1,2,3,4
range(2, 8)     # 2,3,4,5,6,7
range(0, 10, 2) # 0,2,4,6,8
list(range(5))  # [0,1,2,3,4]
for i in range(5):
    print(i)

# Negative step
list(range(5, 0, -1))  # [5,4,3,2,1]
```

Use `len(range(...))` to get its length, and remember it's lazy — it doesn't build the full list unless you convert it to one.

### Short Exercises (Day 7)

1) Write a decorator `timer` that prints how long a function took to run.

Answer (example):
```python
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end-start:.6f}s")
        return result
    return wrapper

@timer
def do_work(n):
    sum(i*i for i in range(n))

do_work(100000)
```

2) Using `range()`, produce the list: [10, 8, 6, 4, 2].

Answer:
```python
list(range(10, 0, -2))  # [10,8,6,4,2]
```

3) Create a decorator `count_calls` that adds an attribute `calls` to the wrapped function counting how many times it was called.

Answer (example):
```python
from functools import wraps

def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@count_calls
def ping():
    print("pong")

ping(); ping(); ping()
print(ping.calls)  # 3
```

---

**Happy Coding! 🐍✨** **huihuihui**

*Last Updated: October 10, 2025*

---
---


