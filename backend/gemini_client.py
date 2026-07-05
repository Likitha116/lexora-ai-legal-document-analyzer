import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load local .env (works locally)
load_dotenv()

# Try local .env first
api_key = os.getenv("GEMINI_API_KEY")

# If deployed on Streamlit Cloud, use Secrets
if not api_key:
    api_key = st.secrets.get("GEMINI_API_KEY")

# Stop if still not found
if not api_key:
    raise ValueError(
        "Gemini API key not found. Please configure GEMINI_API_KEY."
    )

# Configure Gemini
genai.configure(api_key=api_key)

# Create model
model = genai.GenerativeModel(
    "gemini-2.5-flash",
    generation_config={
        "temperature": 0.2,
        "top_p": 0.9,
        "top_k": 40,
    }
)


def generate_response(prompt):
    response = model.generate_content(prompt)
    return response.text