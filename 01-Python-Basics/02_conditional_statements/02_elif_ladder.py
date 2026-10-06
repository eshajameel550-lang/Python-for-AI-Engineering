# ===========================================
# 1. MULTI-CONDITION EVALUATION (ELIF LADDER)
# ===========================================
# Evaluate conditions sequently from top to buttom.
# Stops at FIRST condidtion that evaluates to True.

student_marks = 78

print("\n----- STUDENT GRADE EVALUATION -----")
if student_marks >= 90:
    grade = "A+"
elif student_marks >= 80:
    grade = "A"
elif student_marks >= 70:
    grade = "B"
elif student_marks >= 60:
    grade = "C"
else:
    grade = "F"
print(f"Marks: {student_marks} | Grade: {grade}")

# ==============================================
# 2. AI ROUTING SYSTEM
# ==============================================
# Routing requests to different AI models based on input token length.

input_tokens = 3500

print("\n----- AI MODEL ROUTER -----")
if input_tokens <= 1000:
    selected_model = "Lightweight Model (Fast & Cheap)"
elif input_tokens <= 4000:
    selected_model = "Standard Balanced Model (General Tasks)"
elif input_tokens <= 8000:
    selected_model = "High-context Model (Complex Reasoning)"
else: 
    input_token = "Ultra-Large Model / Custom Fine-Tuned"

print(f"Input Tokens Count: {input_tokens}")
print(f"Routed To: {selected_model}")

