# Changing dictionary items 
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "job": "Developer",
    "salary": 70000
}
print(my_dict)

# Change the value of "age" to 31
my_dict["age"] = 31
print(my_dict)  

#`update` method to change multiple items at once
my_dict.update({"city": "San Francisco", "job": "Senior Developer"})
print(my_dict)

