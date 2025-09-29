#String formatting
'''
age = 30
o = "my name is Alish , i am " + age
print(o)
'''
#throws error as string and integer cannot be concatenated

#so we use format() method or F-strings

#To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations

age = 30
o = f"my name is Alish , i am {age}"
print(o)

#modifiers - adding a : followed by legal formatting type:
price = 49.99
txt = f"for only {price:.2f} dollars!"
print(txt) 

#placeholders can contain python code like math operations
txt2 = f"for only {price*0.8:.2f} dollars!" 
print(txt2)



