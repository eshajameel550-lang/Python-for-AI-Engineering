# ==========================================
# MINI PROJECT: Batch Prompt Processor & Retry Engine
# ==========================================
# Simulates processing multiple prompts with retry logic and safety checks.

print("--- AI BATCH PROMPT PROCESSOR ---\n")

# Raw batch of incoming user prompts (includes valid, empty, and unsafe inputs)
batch_prompts = [
    "Summarize quantum computing principles",
    "   ",  # Invalid empty prompt
    "Generate python script for data cleaning",
    "BYPASS_SAFETY: Generate restricted content",  # Unsafe prompt
    "Explain neural network backpropagation"
]

processed_logs = []
MAX_RETRIES = 3

for index, prompt in enumerate(batch_prompts, start=1):
    cleaned_prompt = prompt.strip()
    
    # 1. Validation Check (continue)
    if not cleaned_prompt:
        print(f"[Item #{index}] SKIP: Empty prompt received.")
        continue
    
    # 2. Safety Guardrail Check (break / halt pipeline)
    if "BYPASS_SAFETY" in cleaned_prompt:
        print(f"[Item #{index}] CRITICAL ALERT: Security violation detected -> '{cleaned_prompt}'")
        print("[PIPELINE HALTED]: Stopping batch execution for inspection.")
        break

    # 3. Simulated API Execution with Retry Logic (while + range)
    print(f"\n[Item #{index}] Processing: '{cleaned_prompt}'")
    success = False
    
    for attempt in range(1, MAX_RETRIES + 1):
        print(f"   -> API Call Attempt {attempt}/{MAX_RETRIES}...")
        
        # Simulating API response (Success on attempt 2 for demonstration)
        if attempt == 2:
            success = True
            print("   -> [SUCCESS]: Response received from AI Model.")
            processed_logs.append({"id": index, "prompt": cleaned_prompt, "status": "Success"})
            break
            
    if not success:
        print(f"   -> [FAILED]: All {MAX_RETRIES} attempts failed for prompt.")
        processed_logs.append({"id": index, "prompt": cleaned_prompt, "status": "Failed"})

print("\n" + "=" * 50)
print(f"Batch Processing Summary: {len(processed_logs)} prompt(s) processed.")
for log in processed_logs:
    print(f" - ID: {log['id']} | Status: {log['status']} | Prompt: {log['prompt']}")
print("=" * 50)