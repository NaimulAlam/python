# String Data Type

# Litereal Assignment
import math
first = "Naim"
last = "Hero"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# Constructor Function
# pizza = str('Mozzerela')
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatination
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting (adding) a number to a string
decade = str(2000)
print(type(decade))
print(decade)

statement = "I am " + first + ", I love music from the " + decade + "s."
print(statement)

multiline = '''
   I am trying to write multiple line, 
                                      aren't you?
'''
print(multiline)

# Escaping special characters \t for tab \n for a new lines \ - is for escaping
sentence = 'I\'m back at work!\t Hey!\n\nWhere\'s this at\\located?'
print(sentence)

# String Methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("you", "u"))
print(multiline)

print(len(multiline))
multiline += "                              "
multiline = "                              " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))


# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$2".rjust(4))
print("Muffin".ljust(16, ".") + "$3".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))


# String index values
print(first[0])
print(first[-1])
print(first[1:-1])  # range values
print(first[1:])  # range till end of string

# Some methods return boolean data ( true/false)
print(first.startswith("N"))
print(first.endswith("M"))  # case sensitive

# Boolean Data type
newvalue = True
x = bool(False)
print(type(x))
print(isinstance(newvalue, bool))

# Numeric Date Types

# Integer Type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float type
gpa = 4.63
y = float(3.1415)
print(type(gpa))
print(isinstance(y, float))

# Complex Type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in functions for numbers
print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))

print(round(gpa, 1))

# math modules ( import should be at top, auto format also puch it to top as well)
# import math

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string to a number

zipcode = "1000"
zip_value = int(zipcode)
print(type(zip_value))

# Error if we attmpt to cast a string to a number (incorrect data type)
# zip_value = int("CTG")
