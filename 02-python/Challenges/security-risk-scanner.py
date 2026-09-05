# Challenge 12: Security Risk Scanner
# Phase: 2 - Python Programming
# Lesson: 5 - Conditionals

role = input("Enter your role (admin/user): ")
mfa = input("Has MFA? (True/False): ")
login_days = int(input("Days since last login: "))

# Convert string input to Python Boolean
if mfa == "True":
    mfa = True
else:
    mfa = False

# Security Risk Logic (Ordered from most severe to least)
if role == "admin" and mfa == False:
    print("🔴 CRITICAL RISK: Admin must have MFA enabled!")
elif login_days > 90:
    print("🟠 HIGH RISK: Abandoned accounts are goldmines for attackers.")
elif role == "admin" and mfa == True:
    print("🟡 MEDIUM RISK: Admins are high-value targets even with MFA.")
else:
    print("🟢 LOW RISK: Standard secure user.")

# Formatted Report
print("\n---- SECURITY REPORT ----")
print(f"Role: {role}")
print(f"MFA Enabled: {mfa}")
print(f"Days since last login: {login_days}")

# CLOUD ENGINEERING CONTEXT:
# This exact decision tree is how AWS IAM Access Analyzer works.
# It checks identity conditions (role, MFA, last activity) and assigns
# a risk score to flag vulnerable accounts before attackers find them.