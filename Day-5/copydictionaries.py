# Copying a dictionary

# Using the `copy` method
original_dict = {
    "name": "Alice",
    "age": 28,
    "city": "Los Angeles"
}
copied_dict = original_dict.copy()
print("Original Dictionary:", original_dict)
print("Copied Dictionary using copy():", copied_dict)   

# Using the `dict` constructor
another_copied_dict = dict(original_dict)
print("Copied Dictionary using dict():", another_copied_dict)
