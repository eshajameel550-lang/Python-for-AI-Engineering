# ==========================================
# MINI PROJECT: AI Dataset Loader & System Logger
# ==========================================
# Safely loads JSON dataset files, logs processing errors to a text file,
# and outputs structured pipeline analytics.

import json
from datetime import datetime

LOG_FILE = "pipeline_errors.log"

def log_error(error_message: str) -> None:
    """Appends timestamped error messages to a local log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] ERROR: {error_message}\n")

def load_and_process_prompts(file_path: str) -> list:
    """Safely reads and processes prompts from a JSON dataset."""
    print(f"--- Loading Dataset: '{file_path}' ---")
    processed_prompts = []
    
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            prompts = data.get("prompts", [])
            
            for item in prompts:
                # Extract prompt text safely
                prompt_text = item.get("text", "").strip()
                if prompt_text:
                    processed_prompts.append(prompt_text)

    except FileNotFoundError:
        err_msg = f"Dataset file '{file_path}' not found."
        print(f"[FAILED]: {err_msg}")
        log_error(err_msg)

    except json.JSONDecodeError:
        err_msg = f"Invalid JSON syntax in file '{file_path}'."
        print(f"[FAILED]: {err_msg}")
        log_error(err_msg)

    else:
        print(f"[SUCCESS]: Successfully processed {len(processed_prompts)} prompt(s).")

    finally:
        print("[STATUS]: Pipeline attempt completed.\n")

    return processed_prompts

# ==========================================
# TEST EXECUTION PIPELINE
# ==========================================

# 1. Create a dummy valid dataset file for testing
sample_dataset = {
    "prompts": [
        {"id": 1, "text": "Explain RAG architecture with vector databases."},
        {"id": 2, "text": "   "}, # Blank prompt
        {"id": 3, "text": "How do agentic workflows handle tool calling?"}
    ]
}

with open("valid_dataset.json", "w", encoding="utf-8") as f:
    json.dump(sample_dataset, f, indent=4)

# 2. Test Execution 1: Valid Dataset
valid_prompts = load_and_process_prompts("valid_dataset.json")
print(f"Valid Prompts Extracted: {valid_prompts}\n")

# 3. Test Execution 2: Missing Dataset (Triggers FileNotFoundError + Logging)
missing_prompts = load_and_process_prompts("non_existent_file.json")

print("=" * 50)
print(f"Check '{LOG_FILE}' in your sidebar to view logged errors.")
print("=" * 50)