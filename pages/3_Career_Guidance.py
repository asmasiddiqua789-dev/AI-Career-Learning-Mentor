import streamlit as st
from gemini import model

st.set_page_config(
    page_title="Career Guidance",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 AI Career Guidance")

st.write("Ask any career-related question and get AI-powered guidance.")

career_question = st.text_area(
    "Ask your question",
    placeholder="Example: How can I become an AI Engineer?"
)

if st.button("🚀 Get Career Guidance"):

    if career_question:

        with st.spinner("Thinking..."):

            prompt = f"""
You are an expert AI Career Mentor.

Answer the following question in a structured format.

Question:
{career_question}

Include:

1. Explanation

2. Skills Required

3. Career Opportunities

4. Salary Range

5. Learning Roadmap

6. Certifications

7. Final Advice
"""

            response = model.generate_content(prompt)

        st.success("✅ AI Guidance Ready!")

        st.markdown(response.text)

    else:
        st.warning("Please enter your question.")

st.divider()

st.subheader("👩‍💻 About Developer")

st.info("""
**Asma Siddiqua**

🎓 B.Tech CSE (AI & ML)

🏫 Bharat Institute of Engineering & Technology

💡 Passionate about Artificial Intelligence, Machine Learning and Python.
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
st.caption("Developed by Asma Siddiqua")