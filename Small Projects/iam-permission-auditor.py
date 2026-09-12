# IAM Permission Auditor
# Phase: 2 - Python Programming (Lessons 1-6 Final Project)

raw_string = input("Please paste your string here: ")
raw_string = raw_string.strip(" ")
users = raw_string.split(",")

admin_count = 0
standard_count = 0
threat_score = 0

for user_data in users:
    user_data = user_data.split(":")
    label = user_data[0]
    username = user_data[1]
    role = user_data[2]
    
    if role == "ADMIN":
        admin_count = admin_count + 1
        threat_score = threat_score + 3
        print(f"⚠️ Admin detected: {username}")
    else:
        standard_count = standard_count + 1
        
    if username.startswith("bob"):
        print(f"🚨 CRITICAL: User 'bob' has {role} access! Immediate review required!")

if threat_score > 5:
    action = "Initiate Lockdown Procedure"
else:
    action = "Permissions are acceptable"

print(f"\n--- AUDIT REPORT ---")
print(f"Admin count: {admin_count}")
print(f"Standard count: {standard_count}")
print(f"Threat Score: {threat_score}")
print(f"Action: {action}")