# Challenge 23: Dictionary Practice
# Phase: 2 - Python Programming
# Lesson: 9 - Dictionaries & Sets

# Step 1: Create a dictionary mapping port numbers to service names
# We use integers for the keys (ports) and strings for the values (services)
port_map = {
    22: "SSH",
    80: "HTTP",
    443: "HTTPS"
}

# Step 2: Look up a port using the key
print(f"Port 22 is: {port_map[22]}")
print(f"Port 443 is: {port_map[443]}")

# Step 3: Safe lookup using .get() (Best Practice!)
# If you look up a port that doesn't exist, .get() returns None instead of crashing
print(f"Port 8080 is: {port_map.get(8080, 'Unknown Service')}")

# CLOUD ENGINEERING CONTEXT:
# Dictionaries are the primary data structure returned by AWS APIs (JSON).
# When you query an EC2 instance, AWS returns a dictionary of attributes.
# You use the key (like 'InstanceId' or 'State') to look up the exact 
# piece of data you need for your security automation.