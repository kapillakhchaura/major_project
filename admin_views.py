# admin_views.py

import streamlit as st
import pandas as pd
import plotly.express as px
from prediction import get_feature_importance
from database import (
    get_all_reports,
    get_all_users,
    get_risk_distribution,
    get_average_risk,
    get_monthly_trend,
    get_top_high_risk
)

# ---------------- Dashboard ----------------
def admin_dashboard_view():

    st.title("📊 AI Smart Admin Dashboard")

    reports = get_all_reports()
    users = get_all_users()

    if not reports:
        st.warning("No data available")
        return

    # =========================
    # 📦 DataFrame
    # =========================
    df = pd.DataFrame(
        reports,
        columns=[
            "ID",
            "Username",
            "Disease",
            "Result",
            "PDF Path",
            "Created At",
            "Risk Score",
            "Risk Category"
        ]
    )

    df["Created At"] = pd.to_datetime(df["Created At"])

    # =========================
    # 🎯 KPI CARDS
    # =========================
    st.markdown("### 🚀 Key Insights")

    total_users = len(set(df["Username"]))
    total_reports = len(df)
    avg_risk = round(df["Risk Score"].mean(), 2)
    high_risk = df[df["Risk Category"] == "High Risk"].shape[0]

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("👥 Users", total_users)
    c2.metric("📄 Reports", total_reports)
    c3.metric("📊 Avg Risk", f"{avg_risk}%")
    c4.metric("🚨 High Risk", high_risk)

    st.divider()

    # =========================
    # 📊 Charts Row 1
    # =========================
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🎯 Risk Distribution")
        dist = df.groupby("Risk Category").size().reset_index(name="Count")

        fig1 = px.pie(
            dist,
            values="Count",
            names="Risk Category",
            color_discrete_sequence=px.colors.sequential.RdBu
        )
        st.plotly_chart(fig1, use_container_width=True, height=300)
    with col2:
        st.subheader("🦠 Disease Cases")
        disease_count = df["Disease"].value_counts().reset_index()
        disease_count.columns = ["Disease", "Count"]

        fig2 = px.bar(
            disease_count,
            x="Disease",
            y="Count",
            color="Disease",
            text_auto=True
        )
        st.plotly_chart(fig2, use_container_width=True, height=100)
    st.divider()

    # =========================
    # 📊 Charts Row 2
    # =========================
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("📈 Avg Risk per Disease")

        avg = df.groupby("Disease")["Risk Score"].mean().reset_index()

        fig3 = px.bar(
            avg,
            x="Disease",
            y="Risk Score",
            color="Disease"
        )
        st.plotly_chart(fig3, use_container_width=True, height=100)
    with col4:
        st.subheader("📅 Monthly Trend")

        monthly = df.groupby(df["Created At"].dt.to_period("M"))["Risk Score"].mean().reset_index()
        monthly["Created At"] = monthly["Created At"].astype(str)

        fig4 = px.line(
            monthly,
            x="Created At",
            y="Risk Score",
            markers=True
        )
        st.plotly_chart(fig4, use_container_width=True, height=150)
    st.divider()

    # =========================
    # 🌍 MAP (Demo)
    # =========================
    st.subheader("🌍 Risk Map (Demo)")

    df["lat"] = 20 + (df.index * 0.5)
    df["lon"] = 77 + (df.index * 0.5)

    fig_map = px.scatter_mapbox(
        df,
        lat="lat",
        lon="lon",
        color="Risk Score",
        size="Risk Score",
        hover_name="Disease",
        zoom=3,
        mapbox_style="carto-darkmatter"
    )

    st.plotly_chart(fig_map, use_container_width=True, height=100)
    st.divider()

    # =========================
    # 🔝 Top High Risk
    # =========================
    st.subheader("🚨 Top High Risk Cases")

    top = df.sort_values("Risk Score", ascending=False).head(10)
    st.dataframe(top, use_container_width=True)

    st.divider()

    # =========================
    # 📝 Recent Reports
    # =========================
    st.subheader("📝 Recent Reports")
    st.dataframe(df.tail(10), height=200)
    st.divider()

    # =========================
    # 🧠 AI Explainability
    # =========================
    st.subheader("🧠 AI Model Explainability")

    disease_choice = st.selectbox(
        "Select Model",
        ["Diabetes", "Heart Disease", "Kidney Disease"]
    )

    features, importances = get_feature_importance(disease_choice)

    df_imp = pd.DataFrame({
        "Feature": features,
        "Importance": importances
    })

    fig_imp = px.bar(
        df_imp.sort_values(by="Importance", ascending=True),
        x="Importance",
        y="Feature",
        orientation="h"
    )

    st.plotly_chart(fig_imp, use_container_width=True)


# ---------------- All Reports ----------------
def admin_all_reports_view():
    st.title("📄 All Reports")

    reports = get_all_reports()

    if not reports:
        st.info("No reports available.")
        return

    df = pd.DataFrame(
        reports,
        columns=[
            "ID",
            "Username",
            "Disease",
            "Result",
            "PDF Path",
            "Created At",
            "Risk Score",
            "Risk Category"
        ]
    )

    st.dataframe(df)


# ---------------- Manage Users ----------------
def admin_manage_users_view():
    st.title("👥 Manage Users")

    users = get_all_users()

    if not users:
        st.info("No users found.")
        return

    df = pd.DataFrame(
        users,
        columns=["Username", "Role", "Created At"]
    )

    st.dataframe(df)


# ---------------- Settings ----------------
def admin_settings_view():
    st.title("⚙ Admin Settings")
    st.write("Future configuration options will appear here.")