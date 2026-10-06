# ========================================
# 1. STRING SLICING & INDEXING
# ========================================
# Indexing starts form 0. Negative indexing starts from the end (-1).

text = "AI Engineering"

print("\n----- STRING SLICING & INDEXING -----")
print(f"Original Text: {text}")
print(f"First Character (index 0): {text[0]}")
print(f"Last Character (index -1): {text[-1]}")
print(f"Sliced Substring (0 to 2): {text[0:2]}")    # Extract 'AI'
print(f"Slice form 3 to end:  {text[3:]}")              # Extract 'Engineering'

# ========================================
# 2. COMMAN STRING METHODS
# ========================================

raw_input = "   Python Programming  "
print("\n----- STRING METHODS ------")
print(f"Raw Input: {raw_input}")
print(f"Uppercase: {raw_input.upper()}")
print(f"Capitalized: {raw_input.capitalize}")
print(f"Stiped Spaces: {raw_input.strip()}")
print(f"Replace Words: {raw_input.replace('Python', 'Java')}")

# ========================================
# 3. STRING SPLITING & JOINING
# ========================================

skills_str = "Python, Data Analytics, Machine Learning, AI"

# Spliting string into the list
skills_list = skills_str.split(", ")

print("\n----- SPLIT & JOIN -----")
print(f"String to List: {skills_list}")

# Joining list back into a single string with a separator
joined_skills = " | ".join(skills_str)
print(f"List of String: {joined_skills}")

# ===========================================
# 4. ADVANCED F-STRING FORMATTING
# ===========================================

model_name = "Gimini"
accuracy = 0.945435

print("\n----- STRING FORMATING -----")
# Rounding float numbers inside f-strings (.2f = 2 decimal places)
print(f"Model: {model_name} | Accuracy: {accuracy: .2%}")
print(f"Rounded Accuracy: {accuracy: .2f}")