# Challenge 20: List Operations
# Phase: 2 - Python Programming
# Lesson: 8 - Lists, Tuples, & Comprehensions

# Step 1: Create a list of 5 ports
ports = [443, 22, 8080, 80, 3389]
print(f"Original list: {ports}")

# Step 2: Add one port to the end
ports.append(3306) # MySQL port
print(f"After append:  {ports}")

# Step 3: Remove one port
ports.remove(3389) # Removing dangerous RDP port
print(f"After remove:  {ports}")

# Step 4: Sort the list
ports.sort()
print(f"After sort:    {ports}")

# Step 5: Print the length
print(f"Total ports:   {len(ports)}")

# CLOUD ENGINEERING CONTEXT:
# Managing lists of ports is essential for configuring AWS Security Groups.
# You use .append() to open a new port, .remove() to close a vulnerable one,
# and .sort() to make the firewall rules readable for auditing.