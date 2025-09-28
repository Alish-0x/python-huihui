#global variables can be used by everyone , both inside and outside of functions
x = "awesome"
def myfunc():
    print("Python is " + x)
myfunc()


# if the variable is created inside a function, it is local and can only be used inside that function


y = "great"
def myfunc():
    x = "fantastic"
    print("Python is " + x)
myfunc()
print(y)  
