Lesson 8 Notes: Lists, Tuples, & Comprehensions
Phase: 2 - Python Programming
Status: ✅ Completed

1. Lists (The Dynamic Collection)
A list holds multiple items in order. Lists are mutable — you can add, remove, or change items after creation.

Syntax & Access
ports = [22, 80, 443, 3389]ports[0]   # 22 (First item)ports[-1]  # 3389 (Last item)ports[1:3] # [80, 443] (Slicing: index 1 up to, NOT including, 3)
Key Methods
.append(item): Adds an item to the very end.
.remove(item): Removes the first matching item.
.sort(): Sorts the list in place (alphabetically or numerically).
.reverse(): Reverses the order.
len(list): Returns the total count of items.
Cloud Use Case
Lists store IP addresses, open ports, user lists, and scan results. You build them dynamically with .append() inside a for loop, then process them.

2. Tuples (The Immutable Collection)
Tuples are like lists, but they cannot be changed (immutable). Once created, you cannot add or remove items.

Syntax
python

coordinates = (10, 20)
rgb_color = (255, 128, 0)
Why use Tuples over Lists?
Data Protection: If data should NEVER change, a tuple protects it from accidental modification.
Performance: Tuples are slightly faster than lists and use less memory.
Function Returns: Functions that return multiple values automatically return a tuple.
Cloud Use Case
In security scripts, a function might return (status, message, risk_score). The caller can unpack the tuple, but cannot accidentally modify the underlying data structure.

Rule of Thumb
Lists []: For collections that grow/shrink (e.g., building a list of open ports).
Tuples (): For fixed-length records (e.g., an IP and Port pair).
3. List Comprehensions (The Python Superpower)
List comprehensions create lists concisely in a single readable line, replacing multi-line for loops.

Basic Syntax (Transformation)
python

# Normal way:
doubled = []
for x in range(5):
    doubled.append(x * 2)

# Comprehension way:
doubled = [x * 2 for x in range(5)]
# Result: [0, 2, 4, 6, 8]
Advanced Syntax (Filtering)
You can add an if statement at the end to filter items.

python

ports = [22, 80, 443, 3389, 8080]

# Only keep ports less than 1024 (Well-known ports)
safe_ports = [port for port in ports if port < 1024]
# Result: [22, 80, 443]
Cloud Use Case
Comprehensions are incredibly powerful for security filtering.

python

# Filter out only suspicious IPs from a massive list
suspicious_ips = [ip for ip in all_ips if is_suspicious(ip)]
Instead of writing a 5-line loop with an if and an .append(), you do it in one clean line. This is what separates beginner Python from professional Python.