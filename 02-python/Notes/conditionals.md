Lesson 5 Notes: Conditionals (Making Decisions)
Phase: 2 - Python Programming
Status: ✅ Completed

Core Concept: if / elif / else
Conditionals give your script a brain. Instead of just running top-to-bottom, the script can evaluate data and choose different paths based on the results.

The Structure
if: The first condition to check. Mandatory.
elif: (Else-If) The next condition if the first was False. You can stack as many elifs as needed.
else: The fallback. If NOTHING above was True, do this. Has no condition.
The 3 Golden Rules
The Colon : — Every if, elif, and else line MUST end with a colon.
Indentation (4 spaces) — The code underneath MUST be indented. This is how Python knows what code belongs to the condition. Un-indenting tells Python the block is over.
else has no condition — You never write else == True. It just catches everything that slipped past the if and elifs.
Truthy and Falsy Values
In Python, conditions don't strictly need to be True or False. Python evaluates other values as "Falsy":

False
0 (Zero)
"" (Empty string)
[] (Empty list)
None (No data)
Everything else is considered "Truthy". This is useful for quick checks like if user_input: (which triggers if the string is not empty).

Logical Operators in Conditionals
and: Both conditions must be True. (e.g., if role == "admin" and mfa == True:)
or: At least one condition must be True. (e.g., if port == 80 or port == 443:)
not: Flips the condition. (e.g., if not source_ip.startswith("192.168"): — triggers if it's an external IP)
Warning: Be careful with and / or precedence. Use parentheses to be explicit: (port == 80 or port == 443) and protocol == "TCP"

Nested Conditionals
You can put an if statement inside another if statement. Example: First check if user is admin, then inside that, check if they have MFA.

Rule: Avoid nesting too deep (more than 2-3 levels). It makes code hard to read. Usually, combining conditions with and/or is cleaner.
Cloud Engineering Context
The "Default Deny" pattern is the most important conditional concept in cloud security. Your else block should almost always block or reject traffic, because if data doesn't explicitly match your safe rules, it should be treated as a threat.