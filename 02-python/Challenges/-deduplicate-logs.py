# Challenge 22: Deduplicate Logs
# Phase: 2 - Python Programming
# Lesson: 8 - Lists, Tuples, & Comprehensions

def deduplicate_logs(log_list):
    """
    Takes a list of log strings, removes duplicates, 
    and sorts them chronologically by timestamp.
    """
    # Step 1: Remove duplicates using set()
    # A Set is a mathematical collection that CANNOT hold duplicate values.
    # By converting our list to a set, Python instantly deletes the copies.
    # We immediately convert it back to a list so we can sort it later.
    unique_logs = list(set(log_list))
    
    # Step 2: Sort by timestamp
    # Because our logs start with a time string (e.g., "10:00..."), 
    # Python's default alphabetical sort will perfectly sort them by time.
    unique_logs.sort()
    
    # Step 3: Return the clean, ordered list
    return unique_logs

# --- TEST IT ---
logs = [
    "10:00 SSH LOGIN",
    "09:00 PORT SCAN",
    "10:00 SSH LOGIN", # Duplicate!
    "08:00 PING"
]

clean_logs = deduplicate_logs(logs)
print(clean_logs)
# Output: ['08:00 PING', '09:00 PORT SCAN', '10:00 SSH LOGIN']
# Notice: The duplicate "10:00 SSH LOGIN" is gone, and they are in time order!

# CLOUD ENGINEERING CONTEXT:
# AWS CloudWatch often sends duplicateB duplicate logs if there's a network retry.
# Security engineers use this exact pattern (set -> list -> sort) to clean 
# massive log files before analyzing them for threats, saving hours of processing time.