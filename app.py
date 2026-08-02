import streamlit as st

st.set_page_config(
    page_title="AI Career & Learning Mentor",
    page_icon="🎓",
    layout="wide"
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------- CSS ----------

st.markdown("""
<style>

.stApp{
    background:linear-gradient(135deg,#050816,#0F172A,#111827);
}

#MainMenu, header, footer{
    visibility:hidden;
}

.block-container{
    max-width:650px;
    padding-top:40px;
}

h1,h2,h3,p,label{
    color:white !important;
}

.stTextInput input{
    background:#1B2236;
    color:white;
    border-radius:10px;
    border:1px solid #3A4668;
}

</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------

st.markdown("""
<div style="text-align:center">

<h1>🎓 AI Career & Learning Mentor</h1>

<p>Your AI-Powered Career & Learning Companion ✨</p>

</div>
""", unsafe_allow_html=True)

# ---------- LOGIN ----------

if not st.session_state.logged_in:

    st.markdown("## Welcome Back 👋")

    tab1, tab2 = st.tabs(["🔑 Login", "📝 Sign Up"])

    with tab1:

        username = st.text_input("Username")

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login", type="primary", use_container_width=True):

            if username == "admin" and password == "1234":

                st.session_state.logged_in = True

                st.switch_page("pages/1_Dashboard.py")

            else:

                st.error("Invalid Username or Password")

    with tab2:

        new_user = st.text_input("Create Username")

        new_pass = st.text_input(
            "Create Password",
            type="password"
        )

        confirm = st.text_input(
            "Confirm Password",
            type="password"
        )

        if st.button("Create Account", type="primary", use_container_width=True):

            if new_pass == confirm:

                st.success("Account Created Successfully!")

            else:

                st.error("Passwords do not match.")