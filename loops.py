#For loop - repeat a specific number of times.
for i in range(5):
    print(f"Round {i}")

# If you want to start from 1 instead of 0, you can use range (1, X) - where X is the number up to which you want to loop, but not including it.
for i in range(1, 6):
    print(f"Round {i}")

# Looping over a list of things
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for day in days:
    print(f"Today is {day}")

# The invisible structure--- 

    for name in ["Claude, Gemini, Rodo, ChatPPT"]:
        print(f"Hello {name}!")