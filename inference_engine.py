from rules import rules

def diagnose(user_conditions):

    matched_solutions = []

    for rule in rules:
        if all(condition in user_conditions for condition in rule["conditions"]):
            matched_solutions.append(rule["solution"])

    if matched_solutions:
        return matched_solutions
    else:
        return ["No solution found in knowledge base. Contact technician."]