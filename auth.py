import streamlit as st
from database import add_user, verify_user, get_user, update_password, user_exists


# ==============================
# AUTH PAGE (LOGIN + REGISTER)
# ==============================

def auth_page():

    st.markdown("""
    <style>

    /* 🔥 REMOVE TOP SPACE */
    .block-container {
        padding-top: 0rem !important;
        margin-top: 0rem !important;
    }

    /* 🔥 REMOVE HEADER SPACE */
    header {
        visibility: hidden;
    }

    /* 🔥 REMOVE EXTRA GAP */
    section.main > div {
        padding-top: 0rem !important;
    }

    /* Background */
    body {
        background: linear-gradient(135deg, #0f172a, #020617);
    }

    /* Card UI */
    .auth-card {
        background: rgba(17, 24, 39, 0.85);
        backdrop-filter: blur(15px);
        padding: 35px;
        border-radius: 20px;
        border: 1px solid #374151;
        box-shadow: 0 20px 40px rgba(0,0,0,0.6);
    }

    /* Inputs */
    .stTextInput>div>div>input {
        border-radius: 10px;
        padding: 10px;
    }

    /* Buttons */
    .stButton>button {
        border-radius: 10px;
        height: 40px;
        font-size: 16px;
        background: linear-gradient(90deg,#6366f1,#8b5cf6);
        color: white;
        border: none;
        transition: 0.3s;
    }

    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(90deg,#4f46e5,#7c3aed);
    }

    </style>
    """, unsafe_allow_html=True)

    left, center, right = st.columns([1, 2, 1])

    with center:

        st.markdown('<div class="auth-card">', unsafe_allow_html=True)

        st.markdown("""
        <h2 style='text-align:center; font-size:32px;'>
        🩺 SMART HEALTH DIAGNOSIS SYSTEM
        </h2>

        <p style='text-align:center; color:#9ca3af;'>
        Smart AI Powered Health System
        </p>
        """, unsafe_allow_html=True)

        tab1, tab2 = st.tabs(["Login", "Register"])

        # ======================
        # LOGIN
        # ======================
        with tab1:
            st.markdown("### 🔐 Login")

            username = st.text_input("👤 Username", key="login_user")
            password = st.text_input("🔑 Password", type="password", key="login_pass")

            role = st.radio("Login as", ["user", "admin"], horizontal=True)

            if st.button("🚀 Login", use_container_width=True, key="login_btn"):
                verified_role = verify_user(username, password)

                if verified_role and verified_role == role:
                    st.session_state["auth"] = {
                        "logged_in": True,
                        "username": username,
                        "role": verified_role
                    }
                    st.success("Login successful")
                    st.rerun()
                else:
                    st.error("Invalid credentials")

            # Forgot toggle
            if st.button("🔑 Forgot Password", use_container_width=True):
                st.session_state["show_forgot"] = not st.session_state.get("show_forgot", False)

            if st.session_state.get("show_forgot", False):
                forgot_password_ui()

        # ======================
        # REGISTER
        # ======================
        with tab2:
            st.markdown("### 📝 Create Account")

            new_user = st.text_input("👤 Username", key="reg_user")
            new_pass = st.text_input("🔑 Password", type="password", key="reg_pass")
            role_select = st.selectbox("🎭 Role", ["user", "admin"])

            st.markdown("### 🔐 Security Question")

            sec_q = st.selectbox("Select Question", [
                "Your first pet name?",
                "Your favorite teacher?",
                "Your birth city?",
                "Your best friend name?"
            ])

            sec_ans = st.text_input("Answer")

            if st.button("✨ Create Account", use_container_width=True):

                if not new_user or not new_pass or not sec_ans:
                    st.warning("Please fill all fields")
                    return

                if user_exists(new_user):
                    st.error("⚠ Username already taken")
                    return

                try:
                    add_user(new_user, new_pass, role_select, sec_q, sec_ans)
                    st.success("✅ Account created successfully")
                except Exception as e:
                    st.error(f"Error: {e}")

        st.markdown("</div>", unsafe_allow_html=True)


# ==============================
# FORGOT PASSWORD UI
# ==============================

def forgot_password_ui():

    st.divider()
    st.subheader("🔐 Reset Password")

    username = st.text_input("Enter Username", key="fp_user")

    if username:

        user = get_user(username)

        if not user:
            st.error("User not found")
            return

        # ✅ Safe tuple extraction
        try:
            security_question = user[3]
            security_answer = user[4]
        except:
            st.error("User data corrupted")
            return

        st.info(f"Security Question: {security_question}")

        answer = st.text_input("Your Answer", key="fp_ans")
        new_password = st.text_input("New Password", type="password", key="fp_new_pass")

        if st.button("Reset Password", key="reset_btn"):

            if not answer or not new_password:
                st.warning("Fill all fields")
                return

            if answer.lower().strip() == security_answer.lower().strip():
                update_password(username, new_password)

                st.success("Password reset successful ✅")

                # 🔁 Hide form after reset
                st.session_state["show_forgot"] = False

            else:
                st.error("Wrong answer ❌")