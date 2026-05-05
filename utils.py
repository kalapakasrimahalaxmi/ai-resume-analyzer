import pdfplumber
import google.generativeai as genai

# 🔑 Replace with your Gemini API key
genai.configure(api_key="AIzaSyDz4zzLru3CdLZ4_2BDypYVSPkwP0TaE6k")


# 📄 Extract text from PDF
def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


# 📊 Simple ATS score logic
def calculate_ats_score(text):
    keywords = [
        "python", "java", "c++", "machine learning", "data science",
        "sql", "projects", "internship", "experience", "skills"
    ]

    score = 0
    text = text.lower()

    for keyword in keywords:
        if keyword in text:
            score += 10

    return min(score, 100)


# 🤖 AI feedback using Gemini (FREE)
def get_ai_feedback(text):
    try:
        import google.generativeai as genai

        genai.configure(api_key="AIzaSyDz4zzLru3CdLZ4_2BDypYVSPkwP0TaE6k")

        # 🔍 Automatically pick a working model
        models = genai.list_models()
        model_name = None

        for m in models:
            if "generateContent" in m.supported_generation_methods:
                model_name = m.name
                break

        if not model_name:
            return "No compatible model found."

        model = genai.GenerativeModel(model_name)

        prompt = f"""
        You are an expert resume reviewer.

        Analyze this resume and provide:
        - ATS Score (out of 100)
        - Strengths
        - Weaknesses
        - Suggestions

        Resume:
        {text}
        """

        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error generating AI feedback: {str(e)}"