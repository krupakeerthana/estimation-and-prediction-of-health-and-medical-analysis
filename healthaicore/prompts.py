def chat_prompt(user_input: str) -> str:
    return f"Medical question: {user_input}"

def prediction_prompt(symptoms: str) -> str:
    return f"Given the symptoms: {symptoms}, what possible diseases could the patient have?"

def treatment_prompt(condition: str) -> str:
    return f"Suggest a treatment plan for: {condition}"
