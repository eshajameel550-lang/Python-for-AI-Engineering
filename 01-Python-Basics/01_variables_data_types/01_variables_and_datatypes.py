# =========================================
#  1. MULTIPLE VARIALBE ASSIGNMENT 
# =========================================

name, age, field, is_student = "Esha Jameel", 18, "Computer Science", True

print("\n----- MULTIPLE ASSIGNMENT -----")
print(f"Name: {name}, Age: {age}, Field: {field}")

# ==========================================
# 2. CHECKING DATA TYPES WITH TYPE()
# ==========================================

print("\n---- CHECK DATA TYPES -----")
print("Name Type:", type(name))               # str
print("Age Type:", type(age))                 # int
print("Is_student Type:", type(is_student))   # bool

# ==========================================
# 3. DAYNAMIC TYPING & VARIBLE RE-ASSIGNMENT
# ==========================================

# Pthon allows variable types to change dynamically
print("\n----- VARIABLE RE-ASSIGNMENT-----")
score = 96
print(f"Score: {score}, Type: {type(score)}")

# Re-assigning a string value to the same variable
score = "Excellent"
print(f"Updated Score Value: {score}, Type: {type(score)}")

# ===========================================
# 4. SWAPPING VARIABLES (PYTHONIC WAY)
# ===========================================

print(f"\n ----- SWAPPING VARIABLE -----")

# Swapping variable without using a third value
a = 6
b = 18
print("----- WITHOUT USING A THIRD VALUE -----")
print(f"Before Swap: a = {a}, b = {b}")
a, b = b, a
print(f"After Swap: a = {a}, b = {b}")

# Swapping variables with using a third value
x = 78
y = 43
print("----- WITH USING A THIRD VALUE -----")
print(f"Before Swap: x = {x}, y = {y}")
temp = x
x = y
y = temp
print(f"After Swapping: x = {x}, y = {y}")

