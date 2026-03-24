#if/else making decisions in Python
age = int(input("How old are you? "))
if age >= 18:
    print("Mojitos for you my friend!")
else:
    print("Sorry my friend, your options are water, orange juice or milk..." )

# elif - multiple conditions
score = float(input("What is your score on the device? "))
if score <= 0.5:
    print("You can continue, drive safely!")
elif score > 0.5 and score <= 0.8:
    print("Sir, you need to stop driving, until you alcohol level is under the legal limit. You can stay here or in jail, your choice.")
elif score > 0.8 and score <= 1.0:
    print ("Sir, you just won a free night in our fine and confortable jail, please turn around...")
else:
    print("Well, well, well... how can you stay on your feet, sir.")


#if / elif difference - if statements are independent(parallels), while elif statements are dependent(continuos) or mutally exclusive. 
#If you have multiple conditions that can be true at the same time, you should use if statements. 
#If you have multple conditions that are mutually exclusive, you should use elif statements.

score = 0.6

# With separte ifs - prints TWO messages
if score > 0.5:
    print("above 0.5")
if score > 0.3:
    print("above 0.3")

# With elif - prints ONE message

if score > 0.5:
    print("above 0.5")
elif score > 0.3:
    print("above 0.3")