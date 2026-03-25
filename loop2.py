# While loop for user input validation
password = ""

while password != "baires123":
    password = input("Enter the secret password: ")
    if password != "baires123":
        print("Wrong! Try again.")
              
print("Access granted! Welcome Rodo!")