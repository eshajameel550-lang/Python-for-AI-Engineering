# ===========================================
# 1. BASIC USER INPUT (Always returns string)
# ===========================================
# The input() function always collects string as a string type 

user_name = input("Enter your name: ")
print("\n------ BASIC INPUT -----")
print(f"Hello {user_name}! Type of input: {type(user_name)}")

# ===========================================
# 2. TYPE CASTING USER INPUT FOR MATH
# ===========================================
# To perform arithmetic operations, input must be explicitly converted (casted).

print("\n ----- TYPE CASTING USER INPUT -----")
age_input = input("Enter your current age: ")

# Converting string input to integer
current_age = int(age_input)
future_age = current_age + 5

print(f"In 5 years, you will be {future_age} years old")

# ============================================
# 3. MULTIPLE INPUTS & MINI CALCULATOR
# ============================================

print("\n ------ SIMPLE USER INPUT CALCULATOR -----")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

addition = num1 + num2
multipication = num1 * num2

print(f"Addition: {num1} + {num2} = {addition}")
print(f"Multiplication: {num1} + {num2} = {multipication:.2f}")

# =============================================
# 4. SANITIZING USER INPUT (.strip() & .lower())
# =============================================
# Cleaning space errors or casing before processing

print("\n----- SANITIZING INPUT ------")
raw_response = input("Do you mean to continue? (Yes/No): ")

# Cleaning spaces and converting to lowercase
clean_response = raw_response.strip().lower()

print(f"Raw Input: {raw_response}")
print(f"Cleaned Input: {clean_response}")
print(f"Is answer 'Yes'?: {clean_response == 'Yes'}")