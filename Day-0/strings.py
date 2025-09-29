#strings are surrounded by either single quotation marks, or double quotation marks.

#"hello" is the same as 'hello'

print("hello")  
print('hello')


#can use quotes inside quotes if they are different
print("It's a beautiful day")
print('He said "Hello"')


#assigning strings to variables
greeting = "Hello"
print(greeting)


#multiline strings using triple quotes [''' or """]
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


#strings are arrays
#square brackets can be used to access elements of the string
c = "welcome"
print(c[2])

#looping through a string

for z in "hardwork":
    print(z)

    #string length
    #get length of string using len() function

    az = "Hello World"
    print(len(az))

#check string
#use keyword 'in' to check if a certain phrase or character is present in a string
lol = "everythings is free if you know where to look"
print("free" in lol)        

# using in if statement

lol = "everythings is free if you know where to look"
if "free" in lol:
    print("yes, 'free' is present")

#check if NOT present
#use keyword "not in"

lol = "everythings is free if you know where to look"
print("expensive" not in lol)


