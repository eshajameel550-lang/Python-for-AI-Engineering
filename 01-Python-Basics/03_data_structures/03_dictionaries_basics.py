# ===========================================
# 1. DICTIONARY CREATION & ACCESSING VALUES
# ===========================================
# Dictionaries store data in Key-Value pairs in curly braces {}

# AI Agent Metadeta Profile
agent_profile = {
    "name" : "EvolveX Receptionist",
    "version" : 2.0,
    "role" : "Customer Support",
    "active" : "True"
}

print("\n----- DICTIONARY BASICS & ACCESSING -----")
print(f"Agent Name: {agent_profile['name']}")
print(f"Agent Role: {agent_profile['role']}")

# Using .get() method (Safe Access - doesn't crash if key is missing)
tempreture = agent_profile.get("tempreture", 0.7)
print(f"Retrieved Tempreture (Safe Check): {tempreture}")

# =============================================
# 2. MODIFYING & ADDING NEW KEYS
# =============================================

print("\n----- UPDATING DICTIONARY -----")

# Adding a new Key-Value pair
agent_profile["max_tokens"] = 2048

# Updating an existing value
agent_profile["active"] = "False"

print(f"Updated Agent Profile: {agent_profile} ")

# ==============================================
# 3. DICTIONARY METHODS (Keys, Values, Items)
# ==============================================

print("\n----- DICTIONARY KEYS & VALLUES -----")

# Extracting all keys, values and pairs
print(f"Keys: {list(agent_profile.keys())}")
print(f"Values: {list(agent_profile.values())}")

# Iterating through Key-Values pairs
print("\nIterating through Profile:")
for key, value in agent_profile.items():
    print(f"    -{key}: {value}")

