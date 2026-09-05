# Challenge 11: Grade Calculator
# Phase: 2 - Python Programming
# Lesson: 5 - Conditionals

grade = int(input("Please enter your grade here: "))

if grade >= 90:
    print("Congrats you got an A")
elif grade >= 80:
    print("Congrats you got a B")
elif grade >= 70:
    print("Congrats you got a C")
elif grade >= 60:
    print("Congrats you got a D!")
else:
    print("You got an F and have failed your exams")

# CLOUD ENGINEERING CONTEXT:
# This exact logic is used in AWS CloudWatch Alarms.
# Instead of grades, you check CPU utilization:
# if cpu >= 90: critical_alert(), elif cpu >= 70: warning_alert(), etc.