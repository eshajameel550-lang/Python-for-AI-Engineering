# ==========================================
# 1. BASIC WHILE LOOP (Counter Driven)
# ==========================================
# Executes as long as the condition remains True.

print("--- 1. TOKEN LIMIT COUNTER ---")

current_tokens = 0
max_token_limit = 500
chunk_size = 100

while current_tokens < max_token_limit:
    current_tokens += chunk_size
    print(f"Processed chunk. Current total tokens: {current_tokens}/{max_token_limit}")

print("Token limit reached! Stopping batch processing.")


# ==========================================
# 2. STATE DRIVEN WHILE LOOP (Flags / Conditions)
# ==========================================
# Simulating an API polling or status checker.

print("\n--- 2. SIMULATED JOB STATUS POLL ---")

import time

job_completed = False
attempts = 0

while not job_completed:
    attempts += 1
    print(f"Checking job status... Attempt #{attempts}")
    
    # Simulating that job finishes on attempt 3
    if attempts == 3:
        job_completed = True
        print("[SUCCESS]: AI Model generation completed!")