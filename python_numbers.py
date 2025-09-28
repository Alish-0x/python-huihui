#there are three types of numbers in python
#int
#float
#complex 


x = 5           #int
y = 5.5         #float
z = 3 + 5j      #complex

print(type(x))
print(type(y))
print(type(z))

#int

a = 1
b = 35656222554887711
c = -3255522
print(type(a))
print(type(b))
print(type(c))

#float
d = 1.10
e = 1.0
f = -35.59
print(type(d))
print(type(e))
print(type(f))

#complex - 'j' is used as an imaginary part
g = 3+5j
h = 5j
i = -5j
print(type(g))
print(type(h))
print(type(i))



#Type Conversion
#convert from one type to another 

x = 1    #int
y = 2.8  #float
z = 1j   #complex

a = float(x)   #convert int to float
b = int(y)     #convert float to int
c = complex(x) #convert int to complex
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

#complex num cannot be converted to another type 
