# ==========================================
# 1. TUPLES (Immutable Data Structure)
# ==========================================
# Tuples use parameters () and CANNOT be changed after creation.

# AI MODEL Configuration (Fixed Settings)
model_config = ("gemini-2.0-flash", 0.7, 4096)      # (model, temreture, max-tokens)

print("\n----- TUPLE OPERATIONS -----")
print(f"Full Config Tuple: {model_config}")
print(f"Model Name (Index 0): {model_config[0]}")
print(f"Tempreture (Index 1): {model_config[1]}")

# Tuple Unpacking (Extracting values into variables directly)
model_name, temp, max_tokens = model_config
print(f"Unpacked -> Model: {model_name}, Temp: {temp}")

# Trying to modify a tuple will give an error:
# model_config[1] = 0.9  # TypeError: 'tuple' object does not support item assignment

# ============================================
# 2. SETS (Unique & Unorderd Collection)
# ============================================
# Sets uses carly braces {} and automatically remove dublicate items.

# Raw list with repeated AI tags
raw_tags = ["python", "ai", "llm", "python", "prompt", "ai", "agent"]

# Converting list to set to remove dublicates
unique_tags = set(raw_tags)

print("\n----- SET OPERATIONS -----")
print(f"Orignal List (with dublicates): {raw_tags}")
print(f"Unique Set (dublicated removed): {unique_tags}")

# Adding & Removing from Set
unique_tags.add("rag")
unique_tags.discard("llm")
print(f"Updated Set: {unique_tags}")

# Set Membership Check (Extremely Fast Lookups)
print(f"Is 'python' in tags?: {'python' in unique_tags}")