#Creating a set and performing basic operations

# Create a set of unique colors
colors = {"red", "green", "blue"}

# Add a new color to the set
colors.add("yellow")
print("Set after adding 'yellow':", colors)


# Remove a color from the set
colors.remove("green")
print("Set after removing 'green':", colors)

# Check if a color is in the set
print("'blue' exists in the set:", "blue" in colors)

# Iterate over the elements of the set
print("All colors in the set:")
for color in colors:
    print(color)




# Performing set operations (union, intersection, difference)
# Define two sets of numbers
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Perform union operation
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)

# Perform intersection operation
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)

# Perform difference operation
difference_set = set1.difference(set2)
print("Difference between set1 and set2:", difference_set)



#Removing duplicates from a list using a set
# Create a list with duplicate elements
numbers = [1, 2, 2, 3, 4, 4, 5, 5]

# Convert the list to a set to remove duplicates
unique_numbers = set(numbers)

print("Original list:", numbers)
print("List after removing duplicates:", list(unique_numbers))
