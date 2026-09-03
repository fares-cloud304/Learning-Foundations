Challenge 08: Operator Precedence
Phase: 2 - Python Programming
Lesson: 4 - Control Flow & Logic
Status: ✅ Completed

Objective
Predict the output of a mathematical expression with mixed operators, verify in Python, and explain the execution order.

The Challenge
Expression: 2 + 3 * 4 - 1

My Prediction & Verification
My Prediction: 13
Python Output: 13
Explanation of Order (Operator Precedence)
Python follows standard mathematical rules (PEMDAS/BODMAS), not strict left-to-right reading:

Multiply: 3 * 4 evaluates first -> 12
Add: 2 + 12 evaluates next -> 14
Subtract: 14 - 1 evaluates last -> 13
Key Takeaway
Multiplication (*) and Division (/) have higher precedence than Addition (+) and Subtraction (-). To override this order and force left-to-right execution, use parentheses: e.g., (2 + 3) * 4 - 1 results in 19.

Cloud Engineering Context
When calculating cloud infrastructure costs in Python (e.g., hours * rate + tax), incorrect operator precedence can lead to scripts outputting wildly wrong billing amounts. Always use parentheses to make your math explicitly clear and prevent costly logic bugs.