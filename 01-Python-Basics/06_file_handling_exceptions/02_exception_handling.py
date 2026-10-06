# ==========================================
# 1. BASIC TRY-EXCEPT BLOCK
# ==========================================
# Prevents program crash when file reading fails or key is missing.

print("--- 1. FILE & JSON EXCEPTION HANDLING ---")

import json

def load_dataset(file_path: str) -> dict:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print(f"[ERROR]: File '{file_path}' not found! Loading default empty dataset.")
        return {}
    except json.JSONDecodeError:
        print(f"[ERROR]: File '{file_path}' contains invalid JSON formatting!")
        return {}

# Testing with non-existent file
missing_data = load_dataset("non_existent_dataset.json")
print(f"Result: {missing_data}")


# ==========================================
# 2. FULL TRY-EXCEPT-ELSE-FINALLY PIPELINE
# ==========================================
# - try: Code that might raise an error
# - except: Code that handles specific errors
# - else: Code that runs ONLY if no error occurs
# - finally: Code that ALWAYS runs (cleanup tasks)

print("\n--- 2. API SIMULATION WITH FULL ERROR HANDLING ---")

def process_api_response(raw_response: str):
    print("Initiating API parsing...")
    try:
        # Simulating JSON parsing
        parsed = json.loads(raw_response)
        output_text = parsed["response"]
    except KeyNotFoundOrInvalidError := KeyError:
        print(f"[ERROR]: Missing key in API response -> {KeyNotFoundOrInvalidError}")
    except json.JSONDecodeError:
        print("[ERROR]: Malformed JSON string received from API.")
    else:
        # Runs only if try block succeeds completely
        print(f"[SUCCESS]: Parsed AI Output -> '{output_text}'")
    finally:
        # Always executes (good for closing connections/logs)
        print("[CLEANUP]: API operation finished.\n")

# Test 1: Valid Response
process_api_response('{"response": "Python Exception Handling is robust!"}')

# Test 2: Invalid Key Response
process_api_response('{"error_code": 404}')