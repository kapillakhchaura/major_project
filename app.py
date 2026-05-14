
import streamlit as st
from landing_page import landing_page

if "menu" not in st.session_state:
    st.session_state["menu"] = "AI Assistant"
# ==============================
# Database Initialization
# ==============================

from database import init_db
init_db()

# ==============================
# Core Modules
# ==============================

from auth import auth_page, forgot_password_ui

# ==============================
# Import Views
# ==============================

from admin_views import (
    admin_dashboard_view,
    admin_all_reports_view,
    admin_manage_users_view,
    admin_settings_view
)

from user_views import (
    user_generate_report_view,
    user_profile_view,
    user_my_reports_view,
    ai_chatbot_view,
    upload_report_view   # ✅ ye add hona chahiye
)

# ==============================
# Page Config
# ==============================

st.set_page_config(
    page_title="AI Doctor",
    layout="wide",
    page_icon="🩺"
)
# ==============================
# 🎨 COMPACT UI STYLE
# ==============================

st.markdown("""
<style>

/* Top spacing कम */
.block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
}

/* Chart height fix */
.stPlotlyChart {
    height: 300px !important;
}

/* Dataframe compact */
.css-1d391kg {
    padding: 0px;
}

/* Sidebar spacing */
section[data-testid="stSidebar"] {
    padding-top: 1rem;
}

/* Cards (future use) */
.card {
    background-color: #111827;
    padding: 12px;
    border-radius: 10px;
    border: 1px solid #374151;
}

</style>
""", unsafe_allow_html=True)

# ==============================
# Session Initialization
# ==============================

if "auth" not in st.session_state:
    st.session_state["auth"] = {
        "logged_in": False,
        "username": None,
        "role": None
    }
if "show_forgot" not in st.session_state:
    st.session_state["show_forgot"] = False


# ==============================
# AUTH SECTION (LOGIN / FORGOT)
# ==============================

if not st.session_state["auth"]["logged_in"]:

    # 🔥 STEP 1: Show Landing Page
    if not st.session_state.get("show_auth", False):
        landing_page()
        st.stop()

    # 🔥 STEP 2: Show Auth Page
    auth_page()
    st.stop()

# ==============================
# Sidebar Header
# ==============================

st.sidebar.title("🩺 AI Doctor")

username = st.session_state["auth"].get("username")
role = st.session_state["auth"].get("role")

st.sidebar.write(f"👤 Logged in as: **{username}**")
st.sidebar.write(f"🔐 Role: **{role}**")

# Logout Button
if st.sidebar.button("🚪 Logout"):
    st.session_state["auth"] = {
        "logged_in": False,
        "username": None,
        "role": None
    }
    st.rerun()

st.sidebar.divider()

# ==============================
# ADMIN PANEL
# ==============================

if role == "admin":

    menu = st.sidebar.radio(
        "Admin Menu",
        [
            "Dashboard",
            "All Reports",
            "Manage Users",
            "Settings"
        ]
    )

    if menu == "Dashboard":
        admin_dashboard_view()

    elif menu == "All Reports":
        admin_all_reports_view()

    elif menu == "Manage Users":
        admin_manage_users_view()

    elif menu == "Settings":
        admin_settings_view()


# ==============================
# USER PANEL
# ==============================

elif role == "user":

    menu_list = [
        "AI Assistant",
        "Generate Report",
        "My Reports",
        "Upload Report",   # 👈 ADD
        "Profile"
    ]

    menu = st.sidebar.radio(
        "User Menu",
        menu_list,
        index=menu_list.index(st.session_state["menu"])
    )

    # 🔥 sync menu
    st.session_state["menu"] = menu

    # 🔥 render views
    if menu == "AI Assistant":
        ai_chatbot_view()

    elif menu == "Generate Report":
        user_generate_report_view()

    elif menu == "My Reports":
        user_my_reports_view()

    # 👇 🔥 YE SABSE IMPORTANT ADD HAI
    elif menu == "Upload Report":
        upload_report_view()

    elif menu == "Profile":
        user_profile_view()

# ==============================
# Invalid Role
# ==============================

else:
    st.error("Invalid role detected.")