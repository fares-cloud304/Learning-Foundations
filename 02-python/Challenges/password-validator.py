# Challenge 09: Password Validator
# Phase: 2 - Python Programming
# Lesson: 4 - Control Flow & Logic

# Get user input
password = input("Enter your password: ")

# Check conditions using Comparison and Logical operators
# 1. len() >= 8 (Comparison: Greater than or equal to)
# 2. any(char.isdigit()) checks for at least one number
# 3. any(char.isalpha()) checks for at least one letter
# 'and' is the Logical Operator ensuring ALL conditions must be True

if len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
    print("Password is strong")
else:
    print("Password is weak")

# CLOUD ENGINEERING CONTEXT:
# Writing custom security validation logic like this is exactly how cloud engineers
# enforce IAM (Identity and Access Management) password policies in AWS or Azure.
# You are building the same logic AWS uses when it says "Password must be 8 chars,
# contain a number, and contain a symbol."