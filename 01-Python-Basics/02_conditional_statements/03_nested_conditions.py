# ================================================
# 1. NESTED CONDITIONS (Authentication & Roles)
# ================================================
# Checking login status first, then checking role permission inside it.

is_logged_in = True
user_rule = "admin"

print("\n----- USER PERMISSION CHECK -----")

if is_logged_in:
    print("User is authenticated.")

    # Inner / Nested Condition
    if user_rule == "admin":
        print("Access Level: Full Admin Access Granted.")
    elif user_rule == "student":
        print("Access Level: Student Portal Access Granted.")
    else:
        print("Access Level: Guest Access Only.")
else:
    print("Access Denied: Please log in first.")

# ================================================
# NESTED GUARDRAIL CHECK (AI SYSTEM)
# ================================================

# Validating system readiness before excuting an AI task.
has_api_key = True
server_online = True
user_balance = 15.50    #US

print("\n----- AI SYSTEM PRE-CHECK -----")

if has_api_key:
    if server_online:
        if user_balance > 0:
            print("System Status: All checked passed! Excuting AI task...")
        print("Excution Blocked! Low account balance.")
    else:
        print("Execution Blocked: AI Server is currently offline.")
else:
    print("Execution Blocked: Valid Api key required.")