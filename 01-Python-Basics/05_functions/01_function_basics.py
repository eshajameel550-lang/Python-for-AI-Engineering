# ==========================================
# 1. BASIC FUNCTION DEFINITION & RETURN VALUES
# ==========================================
# Functions package reusable logic into clean, callable blocks.

def format_ai_prompt(user_query: str, system_role: str = "Assistant") -> str:
    """
    Formats a user query into a structured AI prompt.
    Uses Type Hinting (str -> str) for clean code standards.
    """
    formatted_prompt = f"System Role: [{system_role}]\nUser Input: '{user_query}'"
    return formatted_prompt

print("--- 1. BASIC FUNCTION CALLS ---")

# Calling with default parameter
prompt_1 = format_ai_prompt("What is Retrieval-Augmented Generation?")
print(prompt_1)

print("-" * 40)

# Calling with custom parameter
prompt_2 = format_ai_prompt("Extract all JSON data from this text.", system_role="Data Extractor")
print(prompt_2)


# ==========================================
# 2. RETURNING MULTIPLE VALUES (Tuples)
# ==========================================
# Functions can return multiple outputs at once.

def calculate_token_usage(prompt_text: str, completion_text: str):
    """Calculates approximate token count based on word length."""
    # Rough estimate: ~1.3 tokens per word
    prompt_tokens = int(len(prompt_text.split()) * 1.3)
    completion_tokens = int(len(completion_text.split()) * 1.3)
    total_tokens = prompt_tokens + completion_tokens
    
    return prompt_tokens, completion_tokens, total_tokens

print("\n--- 2. MULTIPLE RETURN VALUES ---")

p_tokens, c_tokens, total = calculate_token_usage(
    "Explain Python functions in simple terms",
    "Functions are reusable blocks of code that take inputs and return outputs."
)

print(f"Prompt Tokens: {p_tokens}")
print(f"Completion Tokens: {c_tokens}")
print(f"Total Usage: {total}")