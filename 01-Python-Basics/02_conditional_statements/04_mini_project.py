# ===================================================
# MINI PROJECT: AI Input Guardrail & Route Evaluator 
# ===================================================
# Validates user prompt safety, length, and routes it to the appropriate AI model.

print("\n----- AI PROMPT GUARDRAILS & ROUTER SYSTEM -----")

# 1. Collecting User Input 
raw_prompt = input("Enter your AI prompt: ")

# Cleaning input space errors
clean_prompt = raw_prompt.strip()
len_prompt = len(clean_prompt)

# Defining safety blocklist words (Simple Safety Guardrail)
blocked_words = ["hack", "bypass", "exploit", "steal"]

# 2. Main Decision Tree / Guardrail Checks
if not clean_prompt:
    print("\n [Error]: Empty propmt received! Please enter a valid query.")

else:
    # Check 1: Safety Guardrail (Checking for harmful words)
    has_unsafe_word = any(word in clean_prompt.lower() for word in blocked_words)

    if has_unsafe_word:
        print("\n [SECURITY ALERT]: Prompt blocked by AI Guardrail due to policy validation.")

    else:
        # Check 2: Prompt Length Validation & Routing
        print("\n [STATUS]: Safety checked passed! Evaluating route...")

        if len_prompt < 10:
            print(f"Prompt Length: {len_prompt} chars")
            print("Action: Rejected - Propmt is too short to generate a meaningful response.")

        elif len_prompt <= 200:
                    print(f"Prompt Length: {len_prompt} chars")
                    print("Route Selected: Fast/Lightweight Model (Quick Response)")

        if len_prompt < 1000:
                    print(f"Prompt Length: {len_prompt} chars")
                    print("Route Selected: Advanced Reasoning Model (Standard Processing)")
        else:
              # Nested Check for ultra-long prompts
              print(f"Prompt Length: {len_prompt} chars")
              print("Route Selected: High-Context Model")

              if len_prompt > 30000:
                print("Warning: Very large input. Text summarization layer applied before processing.")

print("\n" + "=" * 45)
print("System Execution Completed.")
print("=" * 45)  




