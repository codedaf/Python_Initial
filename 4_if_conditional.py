# Basic If statement
x = 10
if x > 5:
    print("x is greater than 5")

# If-else statement
y = 3
if y % 2 == 0:
    print("y is even")
else:
    print("y is odd")


# If-elif-else statement
z = 7
if z < 0:
    print("z is negative")
elif z == 0:
    print("z is zero")
else:
    print("z is positive")

# Nested If statement
a = 15
if a > 10:
    if a % 2 == 0:
        print("a is greater than 10 and even")
    else:
        print("a is greater than 10 and odd")

# User login example with if conditionals
username = "user123"
password = "password123"

input_username = input("Enter username: ")
input_password = input("Enter password: ")

if input_username == username and input_password == password:
    print("Login successful!")
else:
    print("Invalid username or password. Please try again.")
