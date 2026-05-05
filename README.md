📄 AI Resume Analyzer (ATS Score + AI Feedback)

An AI-powered web application that analyzes resumes, extracts text from PDF files, and evaluates them against ATS (Applicant Tracking System) standards. It provides an ATS score along with AI-generated improvement feedback to help users optimize their resumes for better job opportunities.

🚀 Live Demo
https://ai-resume-analyzer-grizd4ysnpqpzgwkuiqhms.streamlit.app

📌 Features:
📄 Upload resume in PDF format
🔍 Automatic text extraction using PDF parser
📊 ATS Score evaluation (0–100)
🤖 AI-powered resume feedback
💡 Suggestions to improve skills, formatting & keywords
⚡ Instant results in a clean UI

🧠 Tech Stack:
Python 🐍
Streamlit (Frontend UI)
pdfplumber (PDF text extraction)
Google Gemini API (AI feedback)
Git & GitHub (Version control)

📂 Project Structure:
ai-resume-analyzer/
│
├── app.py              # Main Streamlit application
├── utils.py            # Resume processing + AI logic
├── requirements.txt    # Dependencies
├── .gitignore          # Ignored files
└── README.md

⚙️ How It Works:
User uploads a resume(PDF)
System extracts text from resume
ATS scoring algorithm evaluates structure & keywords
AI model generates improvement suggestions
Results are displayed in an interactive dashboard

🛠️ Installation (Run Locally):
1. Clone the repository
git clone https://github.com/kalapakasrimahalaxmi/ai-resume-analyzer.git
cd ai-resume-analyzer

2. Install dependencies
pip install -r requirements.txt

3. Run the app
streamlit run app.py

🔐 Environment Variables:

Create a .env file:

GEMINI_API_KEY=your_api_key_here

Or for Streamlit Cloud:

GEMINI_API_KEY = "your_api_key_here"

📊 Example Output:
ATS Score: 82/100
Feedback:
Add more technical keywords
Improve project descriptions
Use action verbs (built, developed, designed)
Optimize formatting for ATS readability

🎯 Use Cases:
* Job seekers optimizing resumes
* Students applying for internships
* Career guidance & resume improvement
* HR screening simulation

💡 Future Improvements:
* Resume vs Job Description matching
* Multi-language resume support
* Downloadable improved resume PDF
* Skill gap analysis dashboard

👨‍💻 Author

Kalapaka Sri Mahalaxmi
BTech Computer Science Engineering
Passionate about AI, Data Science & Web Development

⭐ Show Support

If you like this project:

⭐ Star the repository
🍴 Fork it
🔁 Share with others
