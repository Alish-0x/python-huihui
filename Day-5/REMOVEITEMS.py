# Removing items

# `pop` method to remove a specific item by key
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "job": "Developer",
    "salary": 50000,
    "email": "john.doe@example.com",
    "phone": "123-456-7890"
}   
print(my_dict)
my_dict.pop("age")
print(my_dict)

# `popitem` method to remove the last inserted item
my_dict.popitem()
print(my_dict)

# `del` statement to remove an item by key
del my_dict["city"]
print(my_dict)

# `clear` method to empty the dictionary
my_dict.clear()
print(my_dict)