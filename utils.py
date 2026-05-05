import pdfplumber
import streamlit as st
import google.generativeai as genai


# 🔐 Get API key from Streamlit Secrets
api_key = st.secrets.get("YOUR_GEMINI_API_KEY")

if not api_key:
    raise ValueError("❌ GEMINI_API_KEY not found in Streamlit Secrets")

genai.configure(api_key=api_key)


# 📄 Extract text from PDF
def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text


# 📊 ATS Score calculation
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


# 🤖 AI Feedback (Gemini)
def get_ai_feedback(text):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")

        prompt = f"""
        You are an expert ATS resume reviewer.

        Analyze this resume and provide:
        - ATS Score (0-100)
        - Strengths
        - Weaknesses
        - Improvements

        Resume:
        {text}
        """

        response = model.generate_content(prompt)
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