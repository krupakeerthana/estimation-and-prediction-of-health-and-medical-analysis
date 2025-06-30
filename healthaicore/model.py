from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

def load_model_pipeline(model_name="gpt2"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return pipeline("text-generation", model=model, tokenizer=tokenizer)
