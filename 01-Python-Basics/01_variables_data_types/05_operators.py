# =========================================
# 1. ARITHMETIC OPERATORS
# =========================================
# Basic mathematical operations

a = 5
b = 8

print("\n----- ARITHMETIC OPERATORS -----")
print(f"Addition ({a} + {b}): {a + b}")
print(f"Subtraction ({a} - {b}): {a - b}")
print(f"Multiplication ({a} * {b}): {a * b}")
print(f"Standard Divition ({a} / {b}): {a / b}")
print(f"Floor Division ({a} // {b}): {a // b}")
print(f"Modulus / Remainder ({a} % {b}): {a % b}")
print(f"Exponentiation / Power ({a} + {b}): {a + b}")
print(f"Addition ({a} ** {b}): {a ** b}")

# ============================================
# 2. COMPARISION OPERATORS
# ============================================
# Compares two values and returns a Boolean (True/False)

x = 65
y = 34

print("\n----- COMPARISION OPERTORS -----")
print(f"Is x equal to y? ({x} == {y}): {x == y}")
print(f"Is x is not equal to y? ({x} != {y}): {x != y}")
print(f"Is x greater than y? ({x} > {y}): {x > y}")
print(f"Is x less than y? ({x} < {y}): {x < y}")
print(f"Is x greater than or equal to y? ({x} >= {y}): {x >= y}")
print(f"Is x less than or equal to y? ({x} <= {y}): {x <= y}")

# =============================================
# 3. LOGICAL OPERATORS
# =============================================
# Used to combine conditional statements 

has_degree = True
has_experience = False

print("\n----- LOGICAL OPERATORS-----")

print(f"Eligible for Senior Role (Degree AND Experice): {has_degree and has_experience}")
print(f"Eligible for Entry Role (Degree OR Experice): {has_degree or has_experience}")
print(f"Inverted Degree Status (NOT): {not has_experience}")




