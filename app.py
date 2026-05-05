import streamlit as st
from utils import extract_text_from_pdf, calculate_ats_score, get_ai_feedback

# 🎨 Page config
st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

# 🎨 Custom UI Styling
st.markdown("""
<style>
/* Background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

/* Title */
h1 {
    color: #38bdf8;
    text-align: center;
    font-size: 40px;
}

/* Subheaders */
h2, h3 {
    color: #22c55e;
}

/* Cards */
.block-container {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 12px;
}

/* File uploader */
.stFileUploader {
    background-color: #1e293b;
    border-radius: 10px;
    padding: 10px;
}

/* Button */
.stButton button {
    background: linear-gradient(90deg, #22c55e, #38bdf8);
    color: white;
    border-radius: 8px;
    border: none;
    padding: 10px 20px;
}

/* Text */
p {
    color: #e2e8f0;
}
</style>
""", unsafe_allow_html=True)

# 🚀 Title
st.markdown("<h1>🚀 AI Resume Analyzer</h1>", unsafe_allow_html=True)

# 📄 Upload
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

    # 🤖 AI Feedback
    st.subheader("🤖 AI Feedback")
    feedback = get_ai_feedback(text)
    st.write(feedback)