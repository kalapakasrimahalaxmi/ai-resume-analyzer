import streamlit as st
from utils import extract_text_from_pdf, calculate_ats_score, get_ai_feedback, calculate_job_match

# 🎨 Page config
st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

# 🎨 Custom UI Styling
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

h1 {
    color: #38bdf8;
    text-align: center;
    font-size: 40px;
}

h2, h3 {
    color: #22c55e;
}

.block-container {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 12px;
}

.stFileUploader {
    background-color: #1e293b;
    border-radius: 10px;
    padding: 10px;
}

.stButton button {
    background: linear-gradient(90deg, #22c55e, #38bdf8);
    color: white;
    border-radius: 8px;
    border: none;
    padding: 10px 20px;
}

p {
    color: #e2e8f0;
}

body {
    overflow-x: hidden;
}
</style>
""", unsafe_allow_html=True)

# 🚀 Title
st.markdown("<h1>🚀 AI Resume Analyzer</h1>", unsafe_allow_html=True)

# 📄 Upload resume
uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    st.success("✅ File uploaded successfully!")

    # 📄 Extract text
    text = extract_text_from_pdf(uploaded_file)

    # 📊 ATS Score
    ats_score = calculate_ats_score(text)

    st.subheader("📊 ATS Score")
    st.progress(ats_score / 100)
    st.write(f"**Score: {ats_score}/100**")

    # 📌 Job Description (optional feature)
    job_desc = st.text_area("📌 Paste Job Description (optional)")

    if job_desc:
        match = calculate_job_match(text, job_desc)

        st.subheader("🎯 Job Match Score")
        st.progress(match / 100)
        st.write(f"Match: {match}%")

    # 🤖 AI Feedback
    st.subheader("🤖 AI Feedback")

    with st.spinner("Analyzing resume using AI..."):
        feedback = get_ai_feedback(text)

    st.success("Analysis complete!")
    st.write(feedback)