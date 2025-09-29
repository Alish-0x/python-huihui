#modifying strings

#upper case
#The upper() method returns the string in upper case
a = "hello world"
print(a.upper())


#lower case
#The lower() method returns the string in lower case
b = "HELLO WORLD"
print(b.lower())

#remove whitespace
#The strip() method removes any whitespace from the beginning or the end
c = "   hello world   "
print(c.strip()) 

#replace string
#The replace() method replaces a string with another string
d = "hello world"
print(d.replace("h", "j")) #replaces h with j

#split string
#The split() method splits the string into substrings if it finds instances of the separator
e = "hello,world"
print(e.split(",")) 
#returns ['hello', 'world'] as a list