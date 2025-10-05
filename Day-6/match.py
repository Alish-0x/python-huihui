#match statements - its like switch case in other languages


'''syntax:
match variable:
    case value1:
        #code block
    case value2:
        #code block
    case _:
        #default code block
'''

day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")

#combine values using pipes |
color = "red"
match color:
    case "red" | "blue":
        print("Primary color")
    case "green" | "yellow":
        print("Secondary color")
    case _:
        print("Unknown color")

#if statements as guards - incase of complex conditions
month = 4
day = 15
match month:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print       ("April")
    case 6 | 7 | 8:
        print("Summer month")
    case _:
        print("Other month")

