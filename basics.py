#Week 3 - Python Data Types
#Rodo's first Python basics file

#Strings - text, always in quotes
name = "Rodo"

#Integers - whole numbers, no decimals
age = 48

#Floats - numbers with decimals
height = 1.86

#Booleans - True or false values
is_developer = True

#Let's see them all!
print (name)
print (age)
print (height)
print (is_developer)

#Let's check their types
print (type(name))
print (type(age))
print (type(height))
print (type(is_developer))

# Combining strings together - called "concatenation"
print ("My name is " + name + " and I am " + str(age) + " years old.")

# A cleaner way to do this is with an "f-string"
print (f"My name is {name} and I am {age} years old.")
print (f"I am {height} tall and a {is_developer} developer.")

print (f"Hello {name}")

# Math operations 
a = 10
b = 3
print (F"Addition: {a + b}")
print (f"Subtraction: {a - b}")
print (f"Multiplication: {a * b}")
print (f"Division: {a / b}")
print (f"Floor Division: {a // b}")
print (f"Remainder: {a % b}")
print (f"Power: {a ** b}")