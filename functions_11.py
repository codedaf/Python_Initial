#Functions:
#Example de  Python function that validates a username and password

def login(username, password):
    # Check if the username and password meet the constraints
    if not (username.isalpha() and len(username) <= 6):
        return "Error: Username must contain only letters and be at most 6 characters long."
    if not (password.isalnum() and len(password) <= 6):
        return "Error: Password must contain letters and numbers and be at most 6 characters long."

    # Here would go the logic to verify the username and password in a database or some other authentication system
    # In this example, we just return a success message if the username and password are valid
    if username == "user" and password == "pas123":
        return "Login successful."
    else:
        return "Incorrect username or password."

# Example of using the function
username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

result = login(username_input, password_input)
print(result)