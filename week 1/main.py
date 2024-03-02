import math

print()
print("Hello World! This is Luna typing python :) 😁👍")

value1 = 1
value2 = 2
string1 = "Hello I am a string"
value3 = 1

#This is a coment

#This is Addistion (+)
print("1 + 2 = " + str(1 + 2))

#This is Subtraction (-)
#use str() to convert to string
print("2 - 1 = " + str(value2 - value1))

#This is Multiplication (*)
print("2 * 5 = " + str(2 * 5))

#This is Divition (/)
print("2 / 2 = " + str(value2 / value2))

#This primts a blank line
print()

#This is printing the type of the values
print("Both " + str(2.5) + " and " + str(2.0) + " is " + str(type(2.0)))
print("This text like this '" + string1 + "' is a " + str(type(string1)))
print("And single numbers like " + str(value1) + " is a " + str(type(value1)))

if (value1 == value3):
  print("1 = 1")
else:
  print("1 != 1")

#another blank line for style
print()

a = 2
b = 4

print("a scured =", a**2)
print("b scured =", b**2)
c = math.sqrt(a**2 + b**2)
print("The Scuareroot of a and b is", c)
