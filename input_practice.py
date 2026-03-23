# User inputs - asking the user for information

name = input("What is your name? ")
age = input("How old are you? ")
city = input ("Where do you live? ")

print(f"Nice to meet you, {name}!")
print(f"You are {age} years old and live in {city}.")

# input () always returns a string - even numbers!
year = int(input("What year were you born? "))
age_calculated = 2026 - year
print(f"So you were born in {year}!")
print(f"That means you have been on this planet for {age_calculated} years!")