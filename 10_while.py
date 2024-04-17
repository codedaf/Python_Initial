#Printing numbers from 1 to 5 using a while loop
# Initialize a counter
counter = 1

# Use a while loop to print numbers from 1 to 5
while counter <= 5:
    print(counter)
    counter += 1

 
# Calculating the sum of the first n numbers using a while loop
    # Ask the user to input a number
n = int(input("Enter a positive integer: "))

# Initialize variables
sum = 0
counter = 1

# Use a while loop to calculate the sum of the first n numbers
while counter <= n:
    sum += counter
    counter += 1

# Print the sum
print("The sum of the first", n, "numbers is:", sum)


#Guessing a randomly generated number using a while loop
import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize variables
attempts = 0
guessed = False

# Use a while loop to allow the user to guess the number
while not guessed:
    guess = int(input("Guess the secret number (between 1 and 100): "))
    attempts += 1
    
    if guess == secret_number:
        print("Congratulations! You guessed the secret number in", attempts, "attempts.")
        guessed = True
    elif guess < secret_number:
        print("The secret number is higher.")
    else:
        print("The secret number is lower.")
