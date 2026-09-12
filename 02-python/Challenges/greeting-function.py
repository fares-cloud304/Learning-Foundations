# Challenge 16: Greeting Function
# Phase: 2 - Python Programming
# Lesson: 7 - Functions

def greet(name, greeting="Hello"):
    """Returns a greeting string, defaulting to Hello if no greeting is provided."""
    return f"{greeting}, {name}!"

# Testing the function
# Test 1: Using the default greeting
print(greet("Fares"))

# Test 2: Overriding the default greeting
print(greet("Fares", "Whats Up"))

# CLOUD ENGINEERING CONTEXT:
# Default parameters are heavily used in cloud automation. For example:
# def scan_aws_region(region="us-east-1"):
# If the user doesn't specify a region, the script safely defaults to Virginia.