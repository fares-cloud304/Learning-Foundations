# Challenge 18: Log Analyzer Function
# Phase: 2 - Python Programming
# Lesson: 7 - Functions

def analyze_logs(log_list):
    """
    Takes a list of log strings and returns a dictionary 
    counting how many times each IP address appeared.
    """
    # Step 1: Create an empty dictionary to hold our counts
    ip_counts = {}
    
    # Step 2: Loop through every log in the list
    for log in log_list:
        # Step 3: Split the log by spaces to extract the IP
        parts = log.split(" ")
        ip = parts[1] # The IP is the second item (index 1)
        
        # Step 4: Check if the IP is already in our dictionary
        if ip in ip_counts:
            # It exists! Add 1 to its current count
            ip_counts[ip] += 1
        else:
            # It doesn't exist! This is the first time we see it, set count to 1
            ip_counts[ip] = 1
            
    # Step 5: Return the final dictionary
    return ip_counts

# --- TEST IT ---
# Simulate a list of raw server logs
test_logs = [
    "FAIL 10.0.0.1",
    "FAIL 192.168.1.5",
    "FAIL 10.0.0.1",
    "FAIL 10.0.0.1",
    "FAIL 203.0.113.50"
]

# Call the function and print the result
result = analyze_logs(test_logs)
print(result)

# CLOUD ENGINEERING CONTEXT:
# AWS CloudTrail logs contain thousands of API calls. Security engineers 
# use this exact dictionary pattern to count which IP addresses are 
# making the most "AccessDenied" errors to detect brute force attacks.