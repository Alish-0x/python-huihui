# Nested Dictionaries
my_family = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": { 
        "name": "Sofia",
        "year": 2007
    }
}
print(my_family)

print(my_family["child1"]["name"])  

#loop through nested dictionarys
for child, details in my_family.items():
    print(child)
    for key, value in details.items():
        print(f"  {key}: {value}")