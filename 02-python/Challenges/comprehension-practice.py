# Challenge 21: Comprehension Practice
# Phase: 2 - Python Programming
# Lesson: 8 - Lists, Tuples, & Comprehensions

# Generate squares of numbers 1-10 that are divisible by 3
squares = [x ** 2 for x in range(1, 11) if x % 3 == 0]

print(squares) # Output: [9, 36, 81]

# CLOUD ENGINEERING CONTEXT:
# List comprehensions with conditions are incredibly powerful for 
# filtering cloud data. Example: Finding all EC2 instances that 
# are in the "running" state:
# running_instances = [i for i in instances if i['state'] == 'running']