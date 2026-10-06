# ==========================================
# 1. WRITING & READING TEXT FILES
# ==========================================
# Using 'with open()' automatically handles closing files safely.

log_filename = "ai_agent_activity.log"

print("--- 1. WRITING & READING TEXT FILES ---")

# Writing to a text file ('w' mode creates or overwrites)
with open(log_filename, "w", encoding="utf-8") as file:
    file.write("[LOG 101]: System initialized successfully.\n")
    file.write("[LOG 102]: Connected to vector database.\n")

print(f"Log written to '{log_filename}' successfully.")

# Appending new log entry ('a' mode)
with open(log_filename, "a", encoding="utf-8") as file:
    file.write("[LOG 103]: Prompt batch processed.\n")

# Reading from the text file ('r' mode)
print("\nReading Log File Contents:")
with open(log_filename, "r", encoding="utf-8") as file:
    content = file.read()
    print(content)


# ==========================================
# 2. WORKING WITH JSON FILES (API Payloads & Configs)
# ==========================================
# JSON is the standard format for AI API requests, models, and metadata.

import json

json_filename = "agent_config.json"

config_data = {
    "agent_name": "EvolveX Support Bot",
    "model": "gemini-2.0-flash",
    "temperature": 0.3,
    "tools_enabled": ["knowledge_base", "calculator"]
}

print("--- 2. WRITING & READING JSON DATA ---")

# Saving dictionary as a formatted JSON file
with open(json_filename, "w", encoding="utf-8") as json_file:
    json.dump(config_data, json_file, indent=4)

print(f"Configuration saved to '{json_filename}'.")

# Reading JSON file back into a Python Dictionary
with open(json_filename, "r", encoding="utf-8") as json_file:
    loaded_config = json.load(json_file)

print("\nLoaded JSON Config into Python Dict:")
print(f"Agent Name: {loaded_config['agent_name']}")
print(f"Model Used: {loaded_config['model']}")
print(f"Enabled Tools: {loaded_config['tools_enabled']}")