# ========================================
# 1. IMPLICIT TYPE CASTING (Automatic)
# ========================================

# Python converts smaller data types to larger data types to prevent data loss.
num_int = 34
num_float = 7.8

# Integer + Float = Float
total = num_int + num_float

print("\n----- IMPLICIT CASTING -----")
print(f"Value of Total: {total}")
print(f"Data Type of Total: {type(total)}")     #Output: float

# ========================================
# 2. EXPLICIT TYPE CASTING (Manual)
# ========================================

# Manualy converts data types using build-in-functions: str(), float(), int()

print("\n----- EXPLICIT CASTING -----")

# String to Integer
num_str = "500"
converted_int = int(num_str)
print(f"Converted Str to Int: {converted_int + 50}")

# Float to Integer
num_float = 99.77
converted_int = int(num_float)
print(f"Converted float {num_float} to Int: {converted_int}")

# Integer/ Float String
age = 20
converted_str = str(age)
print(f"Converted Int to String: 'I am' + conveted_str -> " + "I am " +  converted_str)
print(f"Types of converted_str: {type(converted_str)}")

# =========================================
# 3. BOOLEAN CASTING (bool())
# =========================================
# Empty or zero values evaluate to False; non-zero/non-empty evaluate to True.

print("\n----- BOOLEAN CASTING -----")
print("bool(0):", bool(0))
print("bool(10):", bool(10))
print("bool(''):", bool(''))
print("bool('Hello'):", bool('Hello'))

