# ==========================================
# 1. ITERATING OVER A LIST
# ==========================================
# For loops allow us to process items in a sequence one by one.

prompts_queue = [
    "Generate a summary of the article",
    "Translate the summary into French",
    "Extract key action items",
    "Format output as JSON"
]

print("--- 1. PROCESSING PROMPT QUEUE ---")

# Iterating through each item in the list
for prompt in prompts_queue:
    print(f"Processing Task: {prompt}")


# ==========================================
# 2. USING range() FOR INDEXING & ITERATION
# ==========================================
# range(start, stop, step) generates numbers in sequence.

print("\n--- 2. API RETRY ATTEMPTS (range) ---")

# Simulating API retry attempts (1 to 3)
max_retries = 3

for attempt in range(1, max_retries + 1):
    print(f"API Call Attempt #{attempt} of {max_retries}...")


# ==========================================
# 3. ENUMERATE (Tracking Index & Value Together)
# ==========================================
# enumerate() gives us both the loop count (index) and the item value.

print("\n--- 3. TRACKING INDEX WITH ENUMERATE ---")

for index, prompt in enumerate(prompts_queue, start=1):
    print(f"Step {index}: {prompt}")