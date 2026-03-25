#While loop - runs as long as condition is True

attempts = 0
while attempts < 5:
    print(f"Attempt {attempts + 1} of 5")
    attempts += 1
print("Done!")

#DANGER - never run this!
while True:
    print("I will never stop...")