# ==========================================
# MINI PROJECT: AI Agent Tool Execution Engine
# ==========================================
# Simulates how an AI Agent dynamically routes user intent to specific python functions.

print("--- AI AGENT TOOL EXECUTION ENGINE ---\n")

# 1. Defining Available Agent Tools
def search_knowledge_base(query: str, limit: int = 2) -> list:
    """Tool: Searches vector database for relevant documents."""
    print(f"[TOOL EXECUTED]: Searching for '{query}' (Limit: {limit})")
    return ["Doc 1: RAG Architecture Overview", "Doc 2: Vector Embeddings Guide"]

def calculate_tokens(*texts: str) -> int:
    """Tool: Calculates total estimated tokens across multiple texts."""
    total_words = sum(len(text.split()) for text in texts)
    estimated_tokens = int(total_words * 1.3)
    print(f"[TOOL EXECUTED]: Calculated total tokens for {len(texts)} text block(s).")
    return estimated_tokens

def format_llm_payload(prompt: str, **settings) -> dict:
    """Tool: Formats model API configurations."""
    print(f"[TOOL EXECUTED]: Formatting API payload with model settings.")
    return {"prompt": prompt, "config": settings}


# 2. Master Tool Execution Engine Router
def execute_agent_tool(tool_function, *args, **kwargs):
    """
    Higher-order function that takes a tool function and its 
    dynamic arguments (*args, **kwargs), executes it safely, and logs results.
    """
    print(f"\n---> Triggering Tool: '{tool_function.__name__}'")
    try:
        result = tool_function(*args, **kwargs)
        return {"status": "success", "output": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}


# 3. Simulating AI Agent Tool Calls
print("1. Testing Knowledge Base Search Tool:")
res1 = execute_agent_tool(search_knowledge_base, "Agentic Workflows", limit=1)
print(f"Result: {res1}")

print("\n2. Testing Token Counter Tool:")
res2 = execute_agent_tool(calculate_tokens, "Functions make code modular.", "Args and Kwargs allow dynamic input.")
print(f"Result: {res2}")

print("\n3. Testing LLM Payload Builder Tool:")
res3 = execute_agent_tool(
    format_llm_payload, 
    "Explain Python decorators", 
    model="gemini-2.0-flash", 
    temperature=0.2, 
    max_tokens=2048
)
print(f"Result: {res3}")

print("\n" + "=" * 50)
print("Tool Execution Engine Operations Completed.")
print("=" * 50)