Lesson 2 Notes: Variables and Data Types
Phase: 2 - Python Programming
Status: ✅ Completed

Core Concept: Dynamic Typing
Python is a dynamically typed language. This means you do not have to declare the data type of a variable when you create it (unlike languages like C++ or Java). Python automatically figures out the type based on the data you assign to it.

Example: x = 10 (Python automatically knows x is an integer).
The 4 Fundamental Data Types
1. Integer (int)
What it is: Whole numbers, positive or negative, without a decimal point.
Cloud Example: Counting the number of EC2 instances, port numbers (e.g., port = 443).
2. Float (float)
What it is: Numbers that contain a decimal point. Used for precision.
Cloud Example: CPU utilization percentages (e.g., cpu_load = 74.5), cloud billing costs (e.g., price = 0.023).
3. String (str)
What it is: Text data. Must be wrapped in single (') or double (") quotes.
Cloud Example: IP addresses (e.g., ip = "192.168.1.1"), S3 bucket names, instance IDs.
4. Boolean (bool)
What it is: Represents one of two values: True or False. (Note the capital letters!).
Cloud Example: Checking if a server is running (is_active = True), checking if a firewall rule exists (is_encrypted = False).
Variable Naming Rules
When creating variables in Python, you must follow these strict rules:

Can contain letters, numbers, and underscores (_).
Cannot start with a number (e.g., 2servers is illegal, server_2 is fine).
Cannot contain spaces or hyphens (use _ instead).
Cannot use Python reserved keywords (like class, if, for, True).
Best Practice: Python uses snake_case for variables (e.g., my_cloud_server), not camelCase.