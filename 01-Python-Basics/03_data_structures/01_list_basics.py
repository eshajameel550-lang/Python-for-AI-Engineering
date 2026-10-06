# ==========================================
# 1. LIST CREATION & INDEXING 
# ==========================================
# List are ordered, mutable (changeable) collections.

# AI Prompt History List
ai_prompts = [
    "Summarize this article",
    "Translate to Spanish",
    "Write a Python function",
    "Explain quantum computing"
]

print("\n----- INITIAL LIST & INDEXING -----")
print(f"Full List: {ai_prompts}")
print(f"First List index(0): {ai_prompts[0]}")
print(f"Last List index(-1): {ai_prompts[-1]}")

# ===============================================
# 2. LIST MODIFICATION (Add & Remove)
# ===============================================

print("\n----- MODIFYING LIST -----")

#Adding new items
ai_prompts.append("Generate a JSON response")       # Append to the end
ai_prompts.insert(1, "Fix syntax error")            # insert at specific index
print(f"After Adding Items: {ai_prompts}")

# Removing Items
ai_prompts.remove("Translate to Spanish")           # Removes by value
removed_items = ai_prompts.pop()                   # Remove & returns last item
print(f"Removed Item via pop(): {removed_items}")
print(f"Current List State: {ai_prompts}")

# ================================================
# 3. LIST SLICING & HELPER FUNCTIONS
# ================================================

print("\n----- SLICING & UTILITIES -----")

# Slicing: [start: stop]
recent_prompts = ai_prompts[0:2]
print(f"Top 2 Prompts: {recent_prompts}")

# Common operations
print(f"Total Prompts Count: {len(ai_prompts)}")
print(f"Is 'Write a Python function' in lists?: {'Write a Python function' in ai_prompts}")

