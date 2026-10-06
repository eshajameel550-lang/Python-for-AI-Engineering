# ==========================================
# 1. LAMBDA FUNCTIONS (One-line Functions)
# ==========================================
# Syntax: lambda arguments: expression

# Regular function vs Lambda function comparison
def regular_clean_text(text: str) -> str:
    return text.strip().lower()

# Equivalent Lambda Function
clean_text = lambda text: text.strip().lower()

print("--- 1. LAMBDA FUNCTION DEMO ---")
raw_input = "   Hello AI World!   "
print(f"Original: '{raw_input}'")
print(f"Cleaned with Lambda: '{clean_text(raw_input)}'")


# ==========================================
# 2. USING map() WITH LAMBDA (Batch Processing)
# ==========================================
# map(function, iterable) applies a function to every item in a list.

raw_prompts = [
    "  summarize ARTICLE ",
    "   translate to URDU  ",
    " extract KEYWORDS  "
]

print("\n--- 2. BATCH CLEANING WITH map() ---")

# Apply cleaning lambda to all prompts at once
cleaned_prompts = list(map(lambda p: p.strip().lower(), raw_prompts))

for i, prompt in enumerate(cleaned_prompts, start=1):
    print(f"Cleaned Prompt #{i}: '{prompt}'")


# ==========================================
# 3. LIST COMPREHENSION (Pythonic Alternative to map)
# ==========================================
# In modern Python, list comprehensions are often preferred for readability.

print("\n--- 3. LIST COMPREHENSION EQUIVALENT ---")

# Calculating character length for each prompt
prompt_lengths = [len(p) for p in cleaned_prompts]
print(f"Prompt Lengths: {prompt_lengths}")