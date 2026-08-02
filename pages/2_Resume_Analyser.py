import streamlit as st
from PyPDF2 import PdfReader
from gemini import model

st.set_page_config(
    page_title="Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")

st.write("Upload your resume and get an AI-powered ATS analysis.")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    reader = PdfReader(uploaded_file)

    resume_text = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            resume_text += text

    st.success("✅ Resume uploaded successfully!")

    with st.expander("📄 View Resume"):
        st.write(resume_text)

    if st.button("🚀 Analyze Resume"):

        with st.spinner("Analyzing Resume..."):

            prompt = f"""
You are an ATS Resume Expert.

Analyze this resume.

Provide:

1. ATS Score (out of 100)

2. Strengths

3. Missing Skills

4. Weaknesses

5. Improvement Suggestions

6. Final Recommendation

Resume:

{resume_text}
"""

            response = model.generate_content(prompt)

        st.success("✅ Analysis Completed!")

        st.markdown(response.text)

st.divider()

st.subheader("👩‍💻 About Developer")

st.info("""
**Asma Siddiqua**

🎓 B.Tech CSE (AI & ML)

🏫 Bharat Institute of Engineering & Technology
""")

col1, col2 = st.columns(2)

with col1:
    st.link_button(
        "💻 GitHub",
        "https://github.com/asmasiddiqua789-dev",
        use_container_width=True
    )

with col2:
    st.link_button(
        "💼 LinkedIn",
        "https://www.linkedin.com/in/asma-siddiqua-7451b83a5/",
        use_container_width=True
    )

st.divider()

st.caption("© 2026 AI Career & Learning Mentor")