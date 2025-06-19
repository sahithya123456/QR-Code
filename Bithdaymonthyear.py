from datetime import datetime

# Take birth date input
birth_date_input = input("Enter your birth date (YYYY-MM-DD): ")

# Convert input to datetime
birth_date = datetime.strptime(birth_date_input, "%Y-%m-%d")

# Calculate age directly
today = datetime.today()
age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

# Display age
print(f"Your age is {age} years.")