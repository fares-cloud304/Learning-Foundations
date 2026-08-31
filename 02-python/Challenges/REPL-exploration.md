Challenge 02: REPL Exploration
Phase: 2 - Python Programming
Lesson: 1 - Python Introduction & Installation
Status: ✅ Completed

Objective
Explore the Python REPL by performing math operations, string concatenation, and using the type() function to identify data types.

REPL Input & Output
Math Operations
>>> 10 + 515>>> 100 / 333.333333333333336>>> 2 ** 38
String Concatenation
python
>>> "cloud" + "Engineer"
'cloudEngineer'
>>> "Phase" + "2"
'Phase2'

>>> "cloud" + "Engineer"
'cloudEngineer'
>>> "Phase" + "2"
'Phase2'
The type() Function
python

>>> type(10)
<class 'int'>
>>> type(3.14)
<class 'float'>
>>> type("hello")
<class 'str'>
>>> type("true")
<class 'str'>
Cloud Engineering Context
Math (/, **): Cloud engineers use math operations to automate cost calculations (e.g., estimating EC2 instance hours per month) or calculate network subnet masks (using powers of 2).
Concatenation (+): Used constantly to build dynamic strings, like generating AWS S3 bucket names or constructing URLs for API requests.
The type() trap: Notice that type("true") resulted in <class 'str'>, NOT a boolean. In Python, "true" with quotes is just text. The actual boolean value is True (capitalized, no quotes). When pulling data from AWS APIs, knowing the exact data type is critical so you don't try to do math on a string!