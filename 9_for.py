 #Printing numbers from 1 to 5 using a for loop
# Use a for loop to print numbers from 1 to 5
for i in range(1, 6):
    print(i)


#  Iterating over elements in a list using a for loop
# Define a list of fruits
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Use a for loop to iterate over each fruit and print it
for fruit in fruits:
    print(fruit)

# Calculating the sum of elements in a list using a for loop
    # Define a list of numbers
numbers = [10, 20, 30, 40, 50]

# Initialize a variable to store the sum
total = 0

# Use a for loop to iterate over each number and calculate the sum
for num in numbers:
    total += num

# Print the total sum
print("The total sum is:", total)


# Imprimir números pares del 1 al 100
for num in range(1, 101):
    if num % 2 == 0:
        print(num)
