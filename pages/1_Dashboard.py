import streamlit as st

st.set_page_config(
    page_title="Dashboard",
    page_icon="🏠",
    layout="wide"
)

# ---------------- Banner ----------------

try:
    st.image("images/banner.jpg", use_container_width=True)
except:
    st.info("Banner image not found.")

# ---------------- Title ----------------

st.title("🏠 AI Career & Learning Mentor")

st.write("Welcome to your personal AI Career Assistant.")
st.write("Use the modules below to improve your career.")

st.divider()

# ---------------- Dashboard ----------------

st.subheader("📊 Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🔥 Learning Streak", "14 Days")

with col2:
    st.metric("📄 Resume Score", "86%")

with col3:
    st.metric("💼 Internship Matches", "12")

with col4:
    st.metric("🎯 Career Readiness", "78%")

st.divider()

# ---------------- AI Features ----------------

st.subheader("🚀 AI Features")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📄 Resume Analyzer", use_container_width=True):
        st.switch_page("pages/2_Resume_Analyser.py")

    if st.button("📚 Learning Roadmap", use_container_width=True):
        st.switch_page("pages/4_Learning_Roadmap.py")

with col2:
    if st.button("🎯 Career Guidance", use_container_width=True):
        st.switch_page("pages/3_Career_Guidance.py")

    if st.button("🤖 AI Chatbot", use_container_width=True):
        st.switch_page("pages/6_AI_Chatbot.py")

with col3:
    if st.button("💼 Internship Finder", use_container_width=True):
        st.switch_page("pages/5_Internship_Finder.py")

    if st.button("🚪 Logout", use_container_width=True):
        st.session_state.logged_in = False
        st.switch_page("app.py")

st.divider()

# ---------------- Career Readiness ----------------

st.subheader("🎯 Career Readiness")

st.progress(78)

st.success("Current Career Readiness: 78%")

st.info("Continue learning AI, Python and Projects to reach 100%.")

st.divider()

# ---------------- Learning Roadmap ----------------

st.subheader("📚 Learning Roadmap")

st.checkbox("Python Programming", value=True)
st.checkbox("Machine Learning", value=True)
st.checkbox("Deep Learning")
st.checkbox("Generative AI")
st.checkbox("Build AI Projects")
st.checkbox("Interview Preparation")

st.divider()

# ---------------- Available Features ----------------

st.subheader("🚀 Available Features")

left, right = st.columns(2)

with left:
    st.success("📄 Resume Analyzer")
    st.success("🎯 Career Guidance")
    st.success("📚 Learning Roadmap")

with right:
    st.success("💼 Internship Finder")
    st.success("🤖 AI Chatbot")

st.divider()

# ---------------- About Developer ----------------

st.subheader("👩‍💻 About Developer")

st.info("""
**Asma Siddiqua**

🎓 B.Tech CSE (AI & ML)

🏫 Bharat Institute of Engineering & Technology

💡 Passionate about AI, Machine Learning and Python.
""")

col1, col2 = st.columns(2)

with col1:
    st.link_button(
        "💻 GitHub",
        "https://github.com/asmasiddiqua789-dev"
    )

with col2:
    st.link_button(
        "💼 LinkedIn",
        "https://www.linkedin.com/in/asma-siddiqua-7451b83a5/"
    )

st.divider()

st.caption("© 2026 AI Career & Learning Mentor")
st.caption("Developed by Asma Siddiqua")