# Looping through a dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "job": "Developer",
    "salary": 50000,
    "email": "john.doe@example.com",
    "phone": "123-456-7890"
}
# Loop through keys
for key in my_dict:
    print(key)

# Loop through values
for value in my_dict.values():
    print(value)

# Loop through key-value pairs
for key, value in my_dict.items():
    print(key, value)