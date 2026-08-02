import streamlit as st
from gemini import model

st.set_page_config(
    page_title="Learning Roadmap",
    page_icon="📚",
    layout="wide"
)

st.title("📚 AI Learning Roadmap")

st.write("Generate a personalized learning roadmap for any technology.")

technology = st.text_input(
    "Enter a Technology",
    placeholder="Python, Machine Learning, AI, Data Science..."
)

if st.button("🗺️ Generate Roadmap"):

    if technology:

        with st.spinner("Generating Roadmap..."):

            prompt = f"""
You are an AI Learning Mentor.

Create a complete learning roadmap for {technology}.

Include:

1. Beginner Topics

2. Intermediate Topics

3. Advanced Topics

4. Best Free Resources

5. Recommended Projects

6. Certifications

7. Interview Preparation

8. Final Tips

Provide the roadmap in a clear step-by-step format.
"""

            response = model.generate_content(prompt)

        st.success("✅ Roadmap Generated Successfully!")

        st.markdown(response.text)

    else:
        st.warning("Please enter a technology.")

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