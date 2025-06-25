import google.generativeai as genai

# Configure Gemini API key
genai.configure(api_key="AIzaSyB8QovhbvubJEdfDcQI0e2Q--Fj_wGZhB0")

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
