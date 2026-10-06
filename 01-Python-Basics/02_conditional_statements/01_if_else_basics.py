# ============================================
# 1. SIMPLE IF STATEMENT
# ============================================
# Execute code block ONLY if the condition is the True.

user_score = 85
passing_score = 50

print("\n----- SIMPLE IF STATEMENT -----")
if user_score >= passing_score:
    print("Status: Passed!")
    print("Congratulations on completing the assignment.")

# =============================================
# 2. IF-ELSE STATEMENT
# =============================================
# Handles both True & False outcomes.

api_key_provided = False
print("\n----- IF-ELSE-STATEMENT ------")
if api_key_provided:
    print("Access granted: Connecting to AI Services...")
else:
    print("Access Denied: Missing Api Key!")

# ==============================================
# 3. THRESHOLD CHECK WITH OPERATORS
# ==============================================
# Evaluating numeric limits (e.g., Token limits or Server load)

token_usage = 4500
token_limit = 5000

print("\n----- THRESHOLD EVALUATION -----")
if token_usage > token_limit:
    print("Alert! Daily token limit exceeded! Halting execution.")
else:
    remaining_tokens = token_limit - token_usage
    print(f"Usage Normal: {remaining_tokens} remaining tokens for today.")
