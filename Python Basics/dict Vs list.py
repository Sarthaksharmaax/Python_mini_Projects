# 🧠 WHEN TO USE LIST vs DICT IN PYTHON
# 🔹 USE LIST when:
#
# 👉 You care about order
# 👉 You access items by position (index)
# 👉 Data is simple & sequential
#
# ✅ LIST — Examples
# names = ["Aman", "Riya", "Neha"]
# print(names[0])   # Aman
#
#
# Use list when:
#
# Order matters
#
# Duplicates allowed
#
# You loop often
#
# Index-based access
#
# Real-life use:
#
# Todo items
#
# Steps in a process
#
# Scores list
#
# API response arrays
#
# 🔹 USE DICT when:
#
# 👉 You need key → value mapping
# 👉 Fast lookup by name/key
# 👉 Data has meaningful labels
#
# ✅ DICT — Examples
# student = {
#     "name": "Aman",
#     "age": 22,
#     "marks": 85
# }
#
# print(student["name"])  # Aman
#
#
# Use dict when:
#
# You need instant lookup
#
# Each value has a label
#
# Data represents an object/entity
#
# Real-life use:
#
# User profiles
#
# Configuration settings
#
# Database rows
#
# JSON data
#
# ⚡ PERFORMANCE DIFFERENCE (VERY IMPORTANT)
# Operation	List	Dict
# Search by value	❌ Slow (O(n))	✅ Fast (O(1))
# Access	Index	Key
# Structure	Sequence	Mapping
# 🎯 GOLDEN RULE (MEMORIZE)
#
# If you ask “what is this value?” → use DICT
# If you ask “what comes next?” → use LIST
#
# 🧪 REAL COMPARISON
# ❌ Wrong
# student = ["Aman", 22, 85]
#
#
# You forget what 22 means 😬
#
# ✅ Correct
# student = {
#     "name": "Aman",
#     "age": 22,
#     "marks": 85
# }
#
#
# Clear and safe ✔
#
# 🔥 COMBINED USE (MOST REAL PROJECTS)
# students = [
#     {"name": "Aman", "marks": 85},
#     {"name": "Riya", "marks": 92}
# ]
#
#
# 📌 List → collection
# 📌 Dict → structure
#
# 🚫 COMMON BEGINNER MISTAKES
#
# ❌ Using list when keys are needed
# ❌ Using dict when order doesn’t matter
# ❌ Storing unrelated values in lists
#
# 🎯 INTERVIEW ONE-LINE ANSWER
#
# “Lists are ordered collections accessed by index, while dictionaries are key-value mappings optimized for fast lookups.”
#
# If you want next:
#
# List vs tuple vs set vs dict
#
# Real interview trick questions
#
# Data structure decision tree
#
# Just say next 🚀
