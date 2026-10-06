# ==========================================
# 1. CONTINUE STATEMENT (Skip & Next)
# ==========================================
# Skips the rest of the current loop iteration and moves to the next one.

prompts = ["Summarize article", "", "Translate text", "   ", "Extract keywords"]

print("--- 1. FILTERING INVALID PROMPTS (continue) ---")

for prompt in prompts:
    # Skip empty or whitespace-only prompts
    if not prompt.strip():
        print("[SKIP]: Blank prompt detected, skipping...")
        continue
    
    print(f"[PROCESSING]: Running prompt -> '{prompt}'")


# ==========================================
# 2. BREAK STATEMENT (Early Exit)
# ==========================================
# Terminates the loop immediately when a specific condition is met.

generated_responses = [
    "Here is your clear code explanation.",
    "This solution uses Python data structures.",
    "ERROR: Rate limit exceeded on API",
    "This text will never be reached."
]

print("\n--- 2. GUARDRAIL & ERROR BREAK (break) ---")

for response in generated_responses:
    if "ERROR" in response:
        print(f"[CRITICAL STOP]: Safety Guardrail triggered -> {response}")
        break  # Immediately exits the loop
    
    print(f"[OUTPUT LOGGED]: {response}")


# ==========================================
# 3. PASS STATEMENT (Placeholder)
# ==========================================
# Acts as a placeholder where code is syntactically required but no action is needed yet.

print("\n--- 3. PLACEHOLDER FOR FUTURE FEATURES (pass) ---")

for model in ["gemini-2.0-flash", "custom-fine-tuned-model"]:
    if model == "custom-fine-tuned-model":
        # TODO: Implement custom endpoint connection logic later
        pass
    else:
        print(f"[ACTIVE]: Default model selected -> {model}")