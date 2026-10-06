# =================================================
# MINI PROJECT: Smart AI Knowledge Base Simulator
# =================================================
# Manages documents chunks, unique tags, and metadata querying.

print("\n----- AI KNOWLEDGE BASE & METADETA SYSTEM -----")

# 1. Knowledge Base Data Structure (List of Dictionaries)
knowledge_base = [
    {
        "doc_id" : "doc_101",
        "title" : "Introduction to RAG",
        "content" : "Retrieval-Augmented Generation improves LLM response accuracy.",
        "tags" : {"ai", "tags", "llm", "ai"},    # Set auto-removes duplicates
        "metadata" : {"author": "Esha", "views": 120}
    },
    {
        "doc_id" : "doc_102",
        "title" : "Python Data Structures",
        "content" : "List, Dictionaries and Sets are core of AI pipelines.",
        "tags" : {"python", "data", "basics", "python"},   # Set auto-removes duplicates
        "metadata" : {"author": "Esha", "views": 250}
    }
]

# 2. Extracting All Unique Tags Across Knowledge Base using Sets
all_unique_tags = set()
for doc in knowledge_base:
    all_unique_tags.update(doc["tags"])

print(f"Total Document Loaded: {len(knowledge_base)}")
print(f"Global Unique Tags Identified: {all_unique_tags}")
print("-" * 50)

# 3. Querying / Filtering Knowledge Base By Tag
search_tag = "python"
print(f"\n----- Searching Documents For Tag: {search_tag}...-----")

matching_docs = []
for doc in knowledge_base:
    if search_tag in doc["tags"]:
        matching_docs.append(doc)

# Display Search Results
if matching_docs:
    print(f"\nFound {len(matching_docs)} matching document(s):")
    for result in matching_docs:
        print(f" - ID: {result['doc_id']} | Title: {result['title']}")
        print(f"   Author: {result['metadata']['author']} | Views: {result['metadata']['views']}")
        print(f"   Content Preview: {result['content']}")
else:
    print("No matching documents found.")

print("\n" + "=" * 50)
print("Knowledge Base Processing Complete.")
print("=" * 50)