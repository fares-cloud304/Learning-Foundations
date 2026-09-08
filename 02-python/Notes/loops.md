Lesson 6 Notes: Loops (for & while)
Phase: 2 - Python Programming
Status: ✅ Completed

Core Concept: Why Loops?
Scripts without loops run top-to-bottom once and stop. Loops allow your code to repeat automatically. This is the foundation of automation: processing 1000 log files, checking 50 ports, or retrying a failed API call.

1. The for Loop (Iterating over a collection)
Used when you know exactly how many times you want to loop, or when you want to go through a collection item-by-item.

Syntax: Looping through a List
ports = [22, 80, 443, 3389]for port in ports:    print(port)
port is a temporary variable that holds the current item.
The loop runs 4 times because there are 4 items in the list.
Syntax: Looping with range()
If you just want to repeat something X times, or generate numbers:

python

for i in range(5):
    print(i) # Prints 0, 1, 2, 3, 4
range(5) generates numbers from 0 up to (but NOT including) 5.
range(1, 6) generates 1, 2, 3, 4, 5.
range(0, 10, 2) generates 0, 2, 4, 6, 8 (Step by 2).
2. The while Loop (Looping until a condition is met)
Used when you DON'T know exactly how many times it will run. It keeps going as long as a condition is True.

Syntax
python

attempts = 0
while attempts < 3:
    print("Trying again...")
    attempts += 1
Warning: If you forget to change the condition (like attempts += 1), it will run forever! This is called an Infinite Loop and will crash your program.
3. Loop Control Statements
Sometimes you need to change how the loop runs mid-execution.

break: Instantly kills the loop entirely. You jump out.
Use Case: You find a critical threat in a list of logs, so you stop searching and trigger an alert immediately.
continue: Skips the rest of the current loop iteration and jumps to the next one.
Use Case: You are processing logs and hit an empty line. You use continue to skip it and move to the next log without crashing.
Cloud Engineering Context
for loops are your daily driver for parsing data. When you pull a list of 100 EC2 instances from AWS, you use a for loop to check the security settings of each one.
while loops are essential for retry logic. If an AWS API fails due to a network blip, you use a while loop to retry 3 times before giving up.
break is crucial for performance. If you are scanning 10,000 servers for a specific vulnerability, once you find it, you break out of the loop instead of scanning the remaining 9,999 servers.
text

