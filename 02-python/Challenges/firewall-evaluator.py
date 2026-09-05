# Challenge 13: Firewall Rule Evaluator
# Phase: 2 - Python Programming
# Lesson: 5 - Conditionals

source_ip = input("What is your IP address? ")
dest_port = input("What port is listening? ")
protocol = input("Are you using TCP or UDP? ")

# Rule 1: Block RDP entirely (Massive security risk)
if dest_port == "3389":
    print("🚫 BLOCKED: RDP (Port 3389) is a massive security risk!")

# Rule 2: Block SSH from external networks 
# (Only allow SSH if it originates from our safe 192.168.x.x internal network)
elif dest_port == "22" and not source_ip.startswith("192.168"):
    print("🚫 BLOCKED: SSH from external networks is forbidden!")

# Rule 3: Allow standard web traffic
# (Parentheses are critical here to prevent UDP port 80 from slipping through)
elif (dest_port == "80" or dest_port == "443") and protocol == "TCP":
    print("✅ ALLOWED: Standard web traffic over TCP.")

# Rule 4: Default Deny (If it doesn't match a safe rule, block it)
else:
    print("🚫 BLOCKED: Traffic does not match any safe firewall rules.")

# CLOUD ENGINEERING CONTEXT:
# This is exactly how AWS Network ACLs and Security Groups work.
# They evaluate rules from top to bottom until a match is found.
# The "Default Deny" (the else block) is the most important rule in 
# cybersecurity—if traffic isn't explicitly allowed, it is dropped.