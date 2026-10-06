# ========================================
# MINI PROJECT: Smart AI Assistant Configuration
# ========================================

print("\n----- WELCOME TO AI WORKSPACE CONFIGURATOR -----")

# 1. Collecting User Input (String Manipulation & Sanitization)
dev_name = input("Enter your name: ").strip().title()
bot_name = input("Enter your custom AI Agent name: ").strip().capitalize()
daily_tokens_str = input("Enter estimated daily token usage (e.g., 50000): ")

# 2. Type Casting (Converting string input to integer for math calculations)
daily_tokens = int(daily_tokens_str)

# 3. Arithmetic & Comparision Operators
monthly_tokens = daily_tokens * 30
yearly_tokens = daily_tokens * 365
is_heavy_user = daily_tokens > 100000       # Comparision operator returning Boolean

# 4. Final Formatted Report (Using f-strings & Advanced Formatting)
print("\n" + "=" * 45)
print("         AI AGENT DEPLOYMENT SUMMARY         ")
print("=" * 45)
print(f"Developer Name  : {dev_name}")
print(f"Agent Name  : {bot_name}")
print(f"Daily_Tokens  : {daily_tokens:,}")
print(f"Monthly Tokens  : {monthly_tokens:}")
print(f"Yearly Tokens  : {yearly_tokens:}")
print(f"Heavy Workload?  : {is_heavy_user}")
print("=" * 45)
print("Status: Agent successfully configured & ready!")