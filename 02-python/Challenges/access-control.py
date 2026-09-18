# Challenge 24: Access Control List (ACL)
# Phase: 2 - Python Programming
# Lesson: 9 - Dictionaries & Sets

# Nested Dictionary: Users mapped to their roles and permissions
users = {
    "alice": {"role": "admin", "permissions": ["read", "write", "delete"]},
    "bob": {"role": "viewer", "permissions": ["read"]}
}

def can_perform_action(users_dict, username, action):
    """
    Checks if a specific user has permission to perform a specific action.
    Returns True if allowed, False if denied or user doesn't exist.
    """
    # Step 1: Check if the user exists in the dictionary
    if username in users_dict:
        # Step 2: Dig into the nested dictionary to get their permissions list
        allowed_actions = users_dict[username]["permissions"]
        
        # Step 3: Check if the requested action is in that list
        if action in allowed_actions:
            return True
        else:
            return False
    else:
        # User doesn't exist
        return False

# --- TEST IT ---
print(can_perform_action(users, "alice", "write"))  # True (admin can write)
print(can_perform_action(users, "bob", "write"))    # False (viewer cannot write)
print(can_perform_action(users, "bob", "read"))     # True (viewer can read)
print(can_perform_action(users, "hacker", "read"))  # False (unknown user)

# CLOUD ENGINEERING CONTEXT:
# This is exactly how AWS IAM (Identity and Access Management) works under the hood.
# When you make an API call, AWS checks your user dictionary, finds your 
# attached policies (permissions list), and verifies if the requested 
# action (like "s3:GetObject") is in that list. If not, it returns AccessDenied.