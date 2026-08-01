import streamlit as st
from PyPDF2 import PdfReader
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-flash-latest")

st.set_page_config(
    page_title="AI Career & Learning Mentor",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AI Career & Learning Mentor")
st.markdown("""
## 👋 Welcome!

This AI-powered application helps students with:

✅ Resume Analysis

✅ Career Guidance

✅ Learning Roadmap

✅ Internship Suggestions

✅ AI Chatbot
""")
st.divider()

st.sidebar.title("🎓 Features")

option = st.sidebar.selectbox(
    "Choose a Feature",
    [
        "Resume Analyzer",
        "Career Guidance",
        "Learning Roadmap",
        "Internship Finder",
        "AI Chatbot"
    ]
)

# ---------------- Resume Analyzer ----------------

if option == "Resume Analyzer":

    st.header("📄 Resume Analyzer")

    uploaded_file = st.file_uploader(
        "Upload your Resume (PDF)",
        type=["pdf"]
    )

    if uploaded_file is not None:

        reader = PdfReader(uploaded_file)

        resume_text = ""

        for page in reader.pages:
            text = page.extract_text()
            if text:
                resume_text += text

        st.success("Resume uploaded successfully!")
        st.balloons()

        st.subheader("Extracted Resume Text")

        st.text_area(
            "Resume",
            resume_text,
            height=300
        )

        score = 80

        st.subheader("📊 ATS Resume Score")

        st.progress(score)

        st.write(f"Score: {score}/100")

        if score >= 80:
            st.success("Excellent Resume!")
        elif score >= 60:
            st.warning("Good Resume. Add more projects.")
        else:
            st.error("Needs Improvement.")

# ---------------- Career Guidance ----------------

elif option == "Career Guidance":

    st.header("🎯 AI Career Guidance")

    question = st.text_area("Ask your career question")

    if st.button("Get AI Guidance"):

        if question:

            with st.spinner("🤖 AI is thinking..."):

                response = model.generate_content(question)

            st.success("Response Generated!")

            with st.expander("📄 View AI Response"):
                st.write(response.text)

        else:
            st.warning("Please enter a question.")
# ---------------- Learning Roadmap ----------------
elif option == "Learning Roadmap":

    st.header("📚 Learning Roadmap")

    skill = st.text_input(
        "Enter a skill",
        placeholder="Example: Python, Machine Learning, Data Science"
    )

    if st.button("Generate Roadmap"):

        if skill:

            with st.spinner("Generating roadmap..."):

                prompt = f"""
Create a detailed learning roadmap for {skill}.

Include:
1. Beginner topics
2. Intermediate topics
3. Advanced topics
4. Best free resources
5. Projects to build
6. Interview preparation tips
"""

                response = model.generate_content(prompt)

            st.success("Roadmap Generated!")
            st.balloons()

            with st.expander("📄 View Learning Roadmap"):
                st.write(response.text)

        else:
            st.warning("Please enter a skill.")


# ---------------- Internship Finder ----------------

elif option == "Internship Finder":

    st.header("💼 Internship Finder")

    skill = st.text_input("Enter your skills")

    if st.button("Find Internships"):

        if skill:

            prompt = f"""
Suggest internships for a student with skills in {skill}.

Mention:
1. Companies
2. Internship platforms
3. Skills required
4. Tips to get selected
"""

            response = model.generate_content(prompt)

            st.success("Internship Suggestions Ready!")

            with st.expander("💼 View Internship Suggestions"):
                st.write(response.text)

        else:
            st.warning("Please enter your skills.")
# ---------------- AI Chatbot ----------------
elif option == "AI Chatbot":

    st.header("🤖 AI Chatbot")

    prompt = st.text_area("Ask anything")

    if st.button("Send"):

        if prompt:

            response = model.generate_content(prompt)

            st.success("AI Response")

            with st.expander("🤖 View Answer"):
                st.write(response.text)

        else:
            st.warning("Please enter a prompt.")

    st.markdown("---")
    st.caption("🎓 Developed by Asma Siddiqua")
    st.caption("AI Career & Learning Mentor | 2026")