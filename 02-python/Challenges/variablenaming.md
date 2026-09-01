Challenge 04: Variable Naming Rules
Phase: 2 - Python Programming
Lesson: 2 - Variables and Data Types
Status: ✅ Completed

Objective
Identify which variable names are valid in Python and understand the underlying rules.

The Test Cases
2cool ❌
_private ✅
my-var ❌
camelCase ✅
class ✅ (Technically, but practically a trap)
Rules Extracted
No leading numbers: Variables cannot start with a digit (0-9).
No dashes/hyphens: Python interprets - as a minus sign. Use underscores _ instead.
The class trap: While technically accepted by the interpreter, class is a reserved keyword. Using it as a variable name will overwrite Python's ability to create classes, breaking your code.
Cloud Engineering Context
In Python, the standard naming convention is snake_case (e.g., s3_bucket_name, is_instance_running), not camelCase. Following PEP 8 (Python's style guide) makes your automation scripts readable for other cloud engineers.