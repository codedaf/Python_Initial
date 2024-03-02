# Creating and accessing elements in a dictionary

# Create a dictionary of student names and their corresponding ages
student_ages = {"Alice": 20, "Bob": 22, "Charlie": 21}

# Accessing elements in the dictionary
print("Alice's age:", student_ages["Alice"])
print("Bob's age:", student_ages["Bob"])
print("Charlie's age:", student_ages["Charlie"])





# Iterating over key-value pairs in a dictionary
# Create a dictionary of car brands and their corresponding prices
car_prices = {"Toyota": 20000, "Honda": 22000, "Ford": 25000}

# Iterating over key-value pairs in the dictionary
print("Car Prices:")
for brand, price in car_prices.items():
    print(f"{brand}: ${price}")



#  Modifying and adding elements to a dictionary
    
    # Create an empty dictionary
phone_numbers = {}

# Add phone numbers to the dictionary
phone_numbers["Alice"] = "555-1234"
phone_numbers["Bob"] = "555-5678"
phone_numbers["Charlie"] = "555-9012"

# Modify Alice's phone number
phone_numbers["Alice"] = "555-4321"

# Print all phone numbers in the dictionary
print("Phone Numbers:")
for name, number in phone_numbers.items():
    print(f"{name}: {number}")
