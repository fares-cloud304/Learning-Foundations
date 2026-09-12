# Cloud Billing Anomaly Detector
# Phase: 2 - Python Programming (Lessons 1-6)

string = input("Please paste the string here: ")
string = string.strip(" ")
servers = string.split(",")

total_cost = 0
hacked_count = 0
safe_count = 0

for server_data in servers:
    server_data = server_data.split(":")
    server_name = server_data[0]
    price = float(server_data[1])
    total_cost = total_cost + price
    
    if price > 5.00:
        hacked_count = hacked_count + 1
        print(f"🚨 ALERT: {server_name} cost is ${price}! Crypto-miner detected!")
    else:
        safe_count = safe_count + 1

if hacked_count > 0:
    escalation = "PAGE ON-CALL TEAM NOW"
else:
    escalation = "Billing is normal. Go back to sleep."

print(f"\n--- BILLING REPORT ---")
print(f"Total Cost: ${total_cost:.2f}")
print(f"Safe Servers: {safe_count}")
print(f"Hacked Servers: {hacked_count}")
print(f"Decision: {escalation}")