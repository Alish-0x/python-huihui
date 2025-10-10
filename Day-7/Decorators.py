# Decorators - its lets add extra functionality to an existing function, without changing its structure.
#A decorator is a function that takes another function as input and returns a new function.

#Basic Decorator 
def changecase(func):
    def myinner():
        return func().upper()
    return myinner
@changecase
def myfun():
    return "hello world"
print(myfun())

# `@changecase` is equivalent to `myfun = changecase(myfun)` where myfun is passed as an argument to changecase function.
# So when we call myfun(), it actually calls the inner function myinner() defined inside changecase, which in turn calls the original myfun() and modifies its output to uppercase.

#multiple decorators calls - a decorators can be called multiple times by using multiple @decorator_name above the function definition.
def changecase1(func):
    def myinner1():
        return func().upper()
    return myinner1
@changecase
def myfun1():
    return "hello world"

@changecase
def otherfun():
    return "huhui huihui"

print(myfun1())
print(otherfun())


#Decorator with arguments - functions that take arguments can also be decorated by passing those arguments to wrapper function.
def chnaegcase(func):
    def myinner(name):
        return func(name).upper()
    return myinner
@chnaegcase
def function(nam):
    return f"hello {nam}"
print(function("john"))


#`*args` and `**kwargs` - its used to solve the problem of passing variable number of arguments to a decorated function ,it allows to pass any number of positional and keyword arguments to the wrapper function.
def changecasee(func):
    def myinnerr(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return myinnerr
@changecasee
def myfun2(na, ms):
    return f"hello {na}, {ms}"
print(myfun2("john", "how are you?"))


#decorator with arguments - it accepts their owm args by adding another wrapper function.
def chngcse(n):
    def changecasee(func):
        def myinner():
            if n == 1:
                a = func().upper()
            else:
                a = func().lower()
            return a
        return myinner
    return changecasee
@chngcse(2)
def myfun3():
    return "Hello World"
print(myfun3())


#multiple decorators 
def star(func):
    def inner():
        return "*" + func() + "*"
    return inner
def percent(func):
    def inner():
        return "%" + func() + "%"
    return inner
@star
@percent
def myfun4():
    return "hello"
print(myfun4())


#preserving function metadata - function is decorated, its metadata like name and docstring are lost. 

#normally a fnunctifon name can be returned with the __name__ attribute 
def myfun5():
    return "hello"
print(myfun5.__name__)  # Output: myfun5
#but when decorated, it returns the name of the inner function instead of the original function.
def changecaseee(func):
    def myinnerrr():
        return func().upper()
    return myinnerrr
@changecaseee
def myfun6():
    return "hello"
print(myfun6.__name__)  # Output: myinnerrr

#To preserve the original function's metadata, we can use the functools.wraps decorator from the functools module.
import functools
def changecaseeee(func):
    @functools.wraps(func)
    def myinnerrrr():
        return func().upper()
    return myinnerrrr
@changecaseeee
def myfun7():
    return "hello"
print(myfun7.__name__)  # Output: myfun7

#By using @functools.wraps(func), the inner function myinnerrrr now correctly reflects the metadata of the original function myfun7.