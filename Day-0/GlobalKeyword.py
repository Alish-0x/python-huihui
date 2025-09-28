#we can use the global keyword to modify a global variable inside a function

def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)

# it can also be change the value of a global variable inside a function
x = "awesome"
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x) 