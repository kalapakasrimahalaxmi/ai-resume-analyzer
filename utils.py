import pdfplumber
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


# 📄 Extract text from PDF
def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


# 📊 ATS Score logic
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


# 🤖 AI Feedback (Gemini)
def get_ai_feedback(text):
    try:
        # SAFE API KEY USAGE
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

        model = genai.GenerativeModel("gemini-1.5-flash")

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