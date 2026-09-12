# Challenge 17: CIDR to IP List Generator
# Phase: 2 - Python Programming
# Lesson: 7 - Functions

def generate_ips(network):
    """
    Takes a /24 network string (e.g., "192.168.1.0/24") 
    and returns a list of all 256 host IPs.
    """
    # Step 1: Split the network by "/" to separate the IP and the CIDR
    parts = network.split("/")
    
    # Step 2: The IP is parts[0]. Split it by "." to get the octets
    octets = parts[0].split(".")
    
    # Step 3: Get the base network (first 3 octets with a dot at the end)
    base = f"{octets[0]}.{octets[1]}.{octets[2]}."
    
    # Step 4: Create an empty list to hold the generated IPs
    ip_list = []
    
    # Step 5: Loop from 0 to 255
    for i in range(256):
        # Combine the base with the current number
        new_ip = base + str(i)
        # Add it to the list using .append()
        ip_list.append(new_ip)
        
    # Step 6: Return the list
    return ip_list

# --- TEST IT ---
network_input = "192.168.1.0/24"
all_ips = generate_ips(network_input)

# Print the first 5 and last 5 to prove it works
print(f"Total IPs generated: {len(all_ips)}")
print(f"First 5: {all_ips[0:5]}")
print(f"Last 5: {all_ips[251:256]}")

# CLOUD ENGINEERING CONTEXT:
# This is exactly how cloud engineers iterate through VPC subnets to 
# find available IP addresses or scan an entire network range for 
# unpatched servers. In a real AWS script, you would use the 
# boto3 EC2 client to check if each IP is already assigned.