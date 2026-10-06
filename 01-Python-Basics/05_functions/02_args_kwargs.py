# ==========================================
# 1. *args (VARIABLE POSITIONAL ARGUMENTS)
# ==========================================
# *args allows a function to accept any number of positional inputs as a Tuple.

def combine_knowledge_chunks(*chunks: str) -> str:
    """Combines multiple text chunks into a single context block."""
    print(f"Received {len(chunks)} text chunks.")
    combined_context = "\n---\n".join(chunks)
    return combined_context

print("--- 1. USING *args FOR DYNAMIC INPUTS ---")

# Calling with 2 arguments
context_1 = combine_knowledge_chunks(
    "RAG enhances accuracy.",
    "Vector embeddings store text mathematically."
)
print(context_1)

print("\n" + "="*40 + "\n")

# Calling with 3 arguments
context_2 = combine_knowledge_chunks(
    "Python is the core language for AI.",
    "Functions provide modularity.",
    "Agentic workflows automate complex tasks."
)
print(context_2)


# ==========================================
# 2. **kwargs (VARIABLE KEYWORD ARGUMENTS)
# ==========================================
# **kwargs allows a function to accept dynamic key-value pairs as a Dictionary.

def call_llm_api(prompt: str, **model_params) -> dict:
    """
    Simulates calling an LLM API with flexible parameters
    like temperature, max_tokens, top_p, etc.
    """
    payload = {
        "prompt": prompt,
        "parameters": model_params  # Pack all kwargs into a dict
    }
    return payload

print("\n--- 2. USING **kwargs FOR CONFIGURATIONS ---")

# Calling with custom model parameters
api_request = call_llm_api(
    "Summarize this document",
    model="gemini-2.0-flash",
    temperature=0.7,
    max_tokens=1024,
    stream=True
)

print(f"Generated Payload:\n{api_request}")
print(f"Model Temperature: {api_request['parameters'].get('temperature')}")