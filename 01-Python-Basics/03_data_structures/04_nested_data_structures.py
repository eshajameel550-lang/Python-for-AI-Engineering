# ================================================
# 1. LIST OF DICTIONARIES (AI Chat History / Logs)
# ================================================
# Common structure for storing user queries and model responses.

chat_history = [
    {"role": "user", "message": "Explain RAG architecture"},
    {"role": "assistant", "message": "RAG connects LLMs with external knowledge bases."},
    {"role": "user", "message": "Give me Python example."}
]

print("\n----- 1. LIST OF DICTIONARIES -----")
print(f"First message role: {chat_history[0]['role']}")
print(f"First message text: {chat_history[0]['message']}")

# Iterating through chat messages
print("\nFormatted Chat Log:")
for chat in chat_history:
    print(f"[{chat['role'].upper()}]: {chat['message']}")

# =====================================================
# 2. DICTIONARY OF LISTS & NESTED DICTS (API Playload)
# =====================================================
# Representing a complex LLM response payload.

api_response = {
    "status": 200,
    "model_info" : {
        "name": "gimini-2.0-flash",
        "provider": "Google"
    },
    "data": {
        "prompt_tokens": 150,
        "completion_tokens": 45,
        "tags": ["python", "ai", "data-structures"]
    }
}

print("\n----- 2. COMPLEX NESTED DICTIONARY -----")
# Extracting nested values step-by-step

model_name = api_response["model_info"]["name"]
completion_tokens = api_response["data"]["completion_tokens"]
first_tag = api_response["data"]["tags"][0]

print(f"Model Used: {model_name}")
print(f"Completion Tokens: {completion_tokens}")
print(f"Primary Tag: {first_tag}")

