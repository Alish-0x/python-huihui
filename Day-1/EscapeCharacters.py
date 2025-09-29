#Escape Characters - to insert characters that are illegal in a string
#\n - new line
#\t - tab
#\\ - backslash
#\' - single quote
#\" - double quote
'''
#Example 
t = "welcome to "\nPython's" world"
print(t)
#we get an error as double quotes inside a double quote string is illegal
'''

#so fix it using escape characters
t = "welcome to \"\nPython\'s\" world"
print(t)

'''
other escape characters are:
\r - carriage return
\b - backspace
\f - form feed
\v - vertical tab
\ooo - octal value
\xhh - hex value
\u - unicode value


'''