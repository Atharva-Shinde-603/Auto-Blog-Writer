import google.generativeai as genai

# ✅ Replace this with your actual Gemini API key from https://makersuite.google.com/app/apikey
genai.configure(api_key="AIzaSyB8QovhbvubJEdfDcQI0e2Q--Fj_wGZhB0")

# Initialize the model
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")


# Generate content
response = model.generate_content("Write a haiku about the sunset.")

# Print result
print("\nGenerated Haiku:\n")
print(response.text)
