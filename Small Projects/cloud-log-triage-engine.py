# Cloud Access Log Triage Engine
# Phase: 2 - Python Programming (Lessons 1-6 Cumulative Project)

raw_string = input("Please paste your string here: ")
raw_string = raw_string.strip(" ")
parts = raw_string.split(" ")

user_admin = parts[0]
ip_messy = parts[1]
events_messy = parts[2]

# Parse the key:value pairs
user = user_admin.split(":")[1]
ip = ip_messy.split(":")[1]
events_raw = events_messy.split(":")[1]

# Split events into a list
events = events_raw.split(",")

# Accumulator: Count the FAIL events
fail_count = 0
for event in events:
    if event == "FAIL":
        fail_count = fail_count + 1

# Network Threat Logic: Double the score if IP is external
if not ip.startswith("192.168"):
    threat_score = fail_count * 2
else:
    threat_score = fail_count

# Priority Decision Matrix
if threat_score >= 5:
    priority = "CRITICAL"
elif threat_score >= 2:
    priority = "HIGH"
else:
    priority = "LOW"

# Incident Report
print(f"------INCIDENT REPORT------")
print(f"User is: {user}")
print(f"IP address is: {ip}")
print(f"Fail count is: {fail_count}")
print(f"Threat score is: {threat_score} so the priority is: {priority}")