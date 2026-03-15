from questionnaire import ask_questions
from inference_engine import diagnose

print("SMART TROUBLESHOOTING SYSTEM")
print("--------------------------------")

user_conditions = ask_questions()

solutions = diagnose(user_conditions)

print("\nSuggested Solutions:")

for sol in solutions:
    print("-", sol)