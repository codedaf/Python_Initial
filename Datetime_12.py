import datetime

# Get the current date and time
current_date_time = datetime.datetime.now()

# Print the current date and time
print("Current date and time:", current_date_time)

# Get only the current date
current_date = datetime.date.today()

# Print the current date
print("Current date:", current_date)

# Create a specific date
specific_date = datetime.date(2023, 12, 31)

# Print the specific date
print("Specific date:", specific_date)

# Get the day of the week for a specific date
day_of_week = specific_date.strftime("%A")

# Print the day of the week
print("Day of the week for the specific date:", day_of_week)
