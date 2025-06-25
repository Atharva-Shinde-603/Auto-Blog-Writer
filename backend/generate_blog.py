import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Gemini model
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

def generate_blog(topic: str) -> str:
    prompt = f"""
    Write a detailed and engaging blog post on the topic: "{topic}".
    The blog should be informative, well-structured, and reader-friendly.
    Include an introduction, several key points, and a conclusion.
    """
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Error generating blog: {e}"
