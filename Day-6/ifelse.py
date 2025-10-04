# if-else statement - requires indentation
age = 20
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

#else-if (elif) statement
marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")

#else statement
ma = 65
if ma >= 60:
    print("Grade: D")
elif ma >= 50:
    print("Grade: E")
else:
    print("Grade: F")
   

#short-hand if-else (ternary operator)
num = 10
result = "Even" if num % 2 == 0 else "Odd"
print(result)

#and keyword
num1 = 15
num2 = 25
if num1 > 10 and num2 > 20:
    print("Both numbers are greater than their respective thresholds.") 

#or keyword
num3 = 5
num4 = 30
if num3 > 10 or num4 > 20:
    print("At least one number is greater than its respective threshold.")  

#not keyword
is_raining = False
if not is_raining:
    print("It's not raining, you can go outside.")  

#nested if statement
num = 45
if num > 0:
    if num % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")

#pass statement - does nothing, used as a placeholder
value = 100
if value > 50:
    pass  # Placeholder for future code

