import streamlit as st
import pandas as pd
import plotly.express as px
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Use GPT-2, no token needed
MODEL_NAME = "gpt2"

@st.cache_resource(show_spinner=True)
def load_model_pipeline():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
    return pipeline("text-generation", model=model, tokenizer=tokenizer)

generator = load_model_pipeline()

def generate_response(prompt: str) -> str:
    # GPT-2 does not need special prompt formatting
    output = generator(prompt, max_new_tokens=100, do_sample=True)[0]['generated_text']
    return output.strip()

# Prompt templates (can keep same or simplify)
def chat_prompt(user_input: str) -> str:
    return f"Medical question: {user_input}"

def prediction_prompt(symptoms: str) -> str:
    return f"Given the symptoms: {symptoms}, what possible diseases could the patient have?"

def treatment_prompt(condition: str) -> str:
    return f"Suggest a treatment plan for: {condition}"

sample_data = pd.DataFrame({
    "Date": pd.date_range(start="2025-06-01", periods=10),
    "Heart Rate": [72, 74, 75, 76, 74, 73, 77, 79, 76, 75],
    "Blood Pressure": [120, 122, 121, 119, 118, 121, 123, 124, 125, 123],
    "Glucose": [95, 96, 98, 97, 99, 100, 98, 97, 96, 95]
})

st.set_page_config(page_title="HealthAI", layout="wide")
st.title("🧠 HealthAI: Intelligent Healthcare Assistant")

section = st.sidebar.selectbox(
    "Choose Feature",
    ["Patient Chat", "Disease Prediction", "Treatment Plans", "Health Analytics"]
)

if section == "Patient Chat":
    st.header("🗣️ Patient Chat")
    query = st.text_input("Ask a medical question:")
    if st.button("Submit") and query:
        with st.spinner("Generating response..."):
            prompt = chat_prompt(query)
            response = generate_response(prompt)
            st.success(response)

elif section == "Disease Prediction":
    st.header("🔍 Disease Prediction")
    symptoms = st.text_area("Describe your symptoms (e.g., headache, fever, fatigue):")
    if st.button("Predict") and symptoms:
        with st.spinner("Predicting possible diseases..."):
            prompt = prediction_prompt(symptoms)
            response = generate_response(prompt)
            st.info(response)
            st.warning("⚠️ This is NOT a substitute for professional medical advice.")

elif section == "Treatment Plans":
    st.header("💊 Treatment Plans")
    condition = st.text_input("Enter diagnosed condition:")
    if st.button("Get Treatment Plan") and condition:
        with st.spinner("Generating treatment plan..."):
            prompt = treatment_prompt(condition)
            response = generate_response(prompt)
            st.info(response)
            st.warning("⚠️ Always consult a doctor before starting any treatment.")

elif section == "Health Analytics":
    st.header("📊 Health Analytics Dashboard")

    st.subheader("📈 Heart Rate")
    st.plotly_chart(px.line(sample_data, x="Date", y="Heart Rate", title="Heart Rate Trend"))

    st.subheader("🩸 Blood Pressure")
    st.plotly_chart(px.line(sample_data, x="Date", y="Blood Pressure", title="Blood Pressure Trend"))

    st.subheader("🍬 Glucose Levels")
    st.plotly_chart(px.line(sample_data, x="Date", y="Glucose", title="Glucose Trend"))

    st.subheader("📌 Summary")
    st.dataframe(sample_data.set_index("Date"))
