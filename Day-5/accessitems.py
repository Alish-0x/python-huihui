# Accessing dictionary items
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(my_dict["name"])
print(my_dict.get("age"))   
print(my_dict.keys())
print(my_dict.values())

#`items` method -make changes to the dictionary and see that the view reflects these changes
print(my_dict.items())
print(my_dict)
my_dict["age"] = 31
print(my_dict)

