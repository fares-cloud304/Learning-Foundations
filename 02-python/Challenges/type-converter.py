# Challenge 05: Type Converter
# Phase: 2 - Python Programming
# Lesson: 2 - Variables and Data Types

# Take a string number from the user
age = input("Enter a number: ")

# Convert string -> int -> multiply by 2 -> convert back to string
result = str(int(age) * 2)

# Print the final string result
print(result)

# CLOUD ENGINEERING NOTE:
# We often get data from APIs as strings. For example, AWS might return 
# "10" for the number of running instances. We must convert it to an int 
# to do math on it, then back to a str to log it or send it to a dashboard.