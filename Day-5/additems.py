# Adding new items
my_dict = {
    "name": "John",
    "age": 25,
    "city": "Norway",   
    "job": "Developer"

}
print(my_dict)  

#ADD ITEMS
my_dict["salary"] = 50000
print(my_dict)

#`update` method to add multiple items at once
my_dict.update({"email": "john.doe@example.com", "phone": "123-456-7890"})
print(my_dict)