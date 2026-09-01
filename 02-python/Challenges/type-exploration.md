Challenge 06: Type Exploration Rules
Phase: 2 - Python Programming
Lesson: 2 - Variables and Data Types
Status: ✅ Completed

Objective
Research and document what happens when Python mixes different data types.

The Experiments (Conducted in Python REPL)
Test 1: Adding Int and Float
>>> print(type(5 + 2.5))<class 'float'>
Rule (Upward Promotion): When you do math with an int and a float, Python automatically promotes the result to a float. It will never downgrade a float to an int because it refuses to lose decimal data (like turning 7.5 into 7).

Test 2: Comparing Int and String
python

>>> print(5 == "5")
False
Rule (Strict Typing): Python does not guess. Even if a number and a string look identical to a human, they are fundamentally different types. An int is for math; a str is for text.

Test 3: Comparing Int and Float
python

>>> print(5 == 5.0)
True
Rule: Python considers integers and floats with the same numerical value to be equal, because of the "upward promotion" rule mentioned above.

Test 4: The Boolean Secret
python

>>> print(type(True + 1))
<class 'int'>
Rule (Booleans are Integers): Under the hood, True is just the number 1, and False is 0. You can actually do math with them!

Cloud Engineering Context
Understanding these rules prevents massive bugs in cloud scripts. If an AWS API returns the number of servers as the string "5", and you try to do 5 + 1, Python will crash with a TypeError. You must convert it to an int first. Also, using True/False math is a clever trick engineers use to count how many servers failed a security check (e.g., failed_checks = is_unencrypted + is_public).