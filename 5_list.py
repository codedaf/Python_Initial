
# Create a list of fruits
fruits = ["apple", "banana", "grape", "orange"]

# Access the first element of the list
first_fruit = fruits[0]
print("The first fruit is:", first_fruit)

# Access the last element of the list
last_fruit = fruits[-1]
print("The last fruit is:", last_fruit)

# Print the entire list
print("All fruits in the list:")
for fruit in fruits:
    print(fruit)


# Adding and removing elements from a list
# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Add a number to the end of the list
numbers.append(6)
print("List after adding 6:", numbers)

# Remove the first element from the list
first_number = numbers.pop(0)
print("First number removed:", first_number)
print("List after removing the first element:", numbers)

# Remove a specific number from the list
numbers.remove(3)
print("List after removing number 3:", numbers)




#Sorting a list of numbers
# Create an unordered list of numbers
numbers = [5, 2, 8, 1, 3]

# Sort the list in ascending order
numbers.sort()
print("List sorted in ascending order:", numbers)

# Sort the list in descending order
numbers.sort(reverse=True)
print("List sorted in descending order:", numbers)

# Create a list sorted in reverse order
reversed_numbers = sorted(numbers, reverse=True)
print("List sorted in reverse order:", reversed_numbers)



#Sorting a list of numbers
# Create an unordered list of numbers
numbers = [5, 2, 8, 1, 3]

# Sort the list in ascending order
numbers.sort()
print("List sorted in ascending order:", numbers)

# Sort the list in descending order
numbers.sort(reverse=True)
print("List sorted in descending order:", numbers)

# Create a list sorted in reverse order
reversed_numbers = sorted(numbers, reverse=True)
print("List sorted in reverse order:", reversed_numbers)
