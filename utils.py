import pdfplumber
import streamlit as st
from google import genai


# 🔐 Gemini Client (NEW SDK)
client = genai.Client(api_key=st.secrets["YOUR_GEMINI_API_KEY"])


# 📄 Extract text from PDF
def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text


# 📊 ATS Score (basic keyword logic)
def calculate_ats_score(text):
    keywords = [
        "python", "java", "c++", "machine learning", "data science",
        "sql", "projects", "internship", "experience", "skills",
        "django", "flask", "react", "ai", "deep learning"
    ]

    text = text.lower()
    score = 0

    for keyword in keywords:
        if keyword in text:
            score += 10

    return min(score, 100)


# 🤖 AI Feedback (Gemini - NEW SDK)
def get_ai_feedback(text):
    try:
        response = client.models.generate_content(
            model="models/gemini-1.5-flash",
            contents=f"""
You are an expert ATS resume reviewer.

Analyze the resume and provide:

1. ATS Score (0–100)
2. Strengths
3. Weaknesses
4. Improvements

Resume:
{text}
"""
        )

        return response.text

    except Exception as e:
        return f"Error generating AI feedback: {str(e)}"


# 🎯 Job Match Score
def calculate_job_match(resume_text, job_desc):
    resume_text = resume_text.lower()
    job_desc = job_desc.lower()

    resume_words = set(resume_text.split())
    job_words = set(job_desc.split())

    if not job_words:
        return 0

    match = len(resume_words.intersection(job_words))
    score = (match / len(job_words)) * 100

    return min(int(score), 100)