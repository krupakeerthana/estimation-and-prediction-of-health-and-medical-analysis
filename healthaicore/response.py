def generate_response(pipeline, prompt: str) -> str:
    output = pipeline(prompt, max_new_tokens=100, do_sample=True)[0]['generated_text']
    return output.strip()
