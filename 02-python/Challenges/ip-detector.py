# Suspicious IP Detector
# Phase: 2 - Python Programming

log = input("Paste your log here: ")
log = log.strip(" ")
parts = log.split(" ")
ip = parts[1]

# Split the IP address by dots to analyze the network origin
octets = ip.split(".")
first_octet = octets[0] # Fixed: use octets[0], not parts[0]!

# Check if the IP belongs to private RFC 1918 internal networks
if first_octet == "192" or first_octet == "10":
    print(f"✅ IP {ip} is from a safe internal network.")
else:
    print(f"🚨 ALERT: IP {ip} is from an external network! Potential breach!")

# Output log length for debugging
log_length = len(log)
print(f"Log length is {log_length}")