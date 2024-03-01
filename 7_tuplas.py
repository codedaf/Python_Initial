
"""
Tuples in Python are primarily used for the following reasons:
Immutability: Tuples are immutable, meaning once created, they cannot be modified. This can be useful when you need to ensure that data does not change during program execution.
Efficiency: Tuples are more efficient in terms of performance compared to lists, especially when it comes to iterations and accessing elements. This is because tuples are optimized for read-only operations.
Packing and Unpacking: Tuples allow you to pack multiple values into a single data entity. They also make it easy to unpack values into individual variables, which can be useful in functions that return multiple values.
Usage in dictionaries: Tuples can be used as keys in Python dictionaries, whereas lists cannot due to their mutability. This makes tuples useful when you need to create a composite key in a dictionary.
Ordered sequences: Although tuples are immutable, they maintain the order of elements, just like lists. This means you can access tuple elements in the same order they were added.
In summary, tuples are useful in situations where you need immutable and efficient data, such as representing simple data structures or as keys in dictionaries. Their immutability provides an additional guarantee of data integrity in certain situations.
"""

#Creating a tuple and accessing its elements
# Create a tuple of coordinates

coordinate = (10, 20)
# Accessing elements of the tuple
x = coordinate[0]
y = coordinate[1]

print("X coordinate:", x)
print("Y coordinate:", y)


# Create a tuple representing a person's information
person = ("John", 30, "New York")
# Unpack the tuple into variables
name, age, city = person

print("Name:", name)
print("Age:", age)
print("City:", city)


#Returning multiple values from a function using a tuple

# Function to calculate the area and perimeter of a rectangle
def calculate_rectangle_properties(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

# Call the function and unpack the returned tuple
rectangle_area, rectangle_perimeter = calculate_rectangle_properties(5, 3)

print("Area of the rectangle:", rectangle_area)
print("Perimeter of the rectangle:", rectangle_perimeter)
