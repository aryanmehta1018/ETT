import streamlit as st
import json
import os
import pandas as pd
import matplotlib.pyplot as plt

from backend.resume_parser import extract_text
from backend.skill_extractor import extract_skills_with_llm
from backend.matcher import match_skills

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])

if uploaded_file:

    # ------------------ RESUME TEXT ------------------
    resume_text = extract_text(uploaded_file)

    st.subheader("Extracted Resume Text")
    st.text_area("Resume Content", resume_text, height=250)

    # ------------------ SKILL EXTRACTION ------------------
    with st.spinner("Analyzing with AI..."):
        extracted_skills = extract_skills_with_llm(resume_text)

    st.subheader("Extracted Skills")
    st.write(extracted_skills)

    # ------------------ JOB ROLE ------------------
    with open("data/job_roles.json") as f:
        job_roles = json.load(f)

    job_role = st.selectbox("Select Job Role", list(job_roles.keys()))

    # ------------------ MATCHING ------------------
    if st.button("Match Skills"):

        required_skills = job_roles[job_role]
        result = match_skills(extracted_skills, required_skills)

        st.subheader("📊 Dashboard")

        matched = result["matched_skills"]
        missing = result["missing_skills"]

        # ------------------ KPI ------------------
        st.metric("Match Percentage", f"{result['match_percentage']}%")

        # ------------------ CHARTS ------------------
        col1, col2 = st.columns(2)

        # -------- PIE CHART --------
        with col1:
            st.subheader("Skill Coverage")

            labels = ['Matched', 'Missing']
            sizes = [len(matched), len(missing)]

            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
            st.pyplot(fig1)

        # -------- BAR CHART --------
        with col2:
            st.subheader("Skill Breakdown")

            data = []

            for skill in matched:
                data.append([skill, "Matched"])

            for skill in missing:
                data.append([skill, "Missing"])

            df_chart = pd.DataFrame(data, columns=["Skill", "Status"])

            counts = df_chart.groupby(["Skill", "Status"]).size().unstack(fill_value=0)

            fig2, ax2 = plt.subplots()
            counts.plot(kind="bar", ax=ax2)

            plt.xticks(rotation=45, ha='right')
            st.pyplot(fig2)

        # ------------------ SKILL LIST ------------------
        col3, col4 = st.columns(2)

        with col3:
            st.subheader("✅ Matched Skills")
            st.write(matched)

        with col4:
            st.subheader("❌ Missing Skills")
            st.write(missing)

        # ------------------ TOP MISSING SKILLS ------------------
        st.subheader("🚨 Top Missing Skills")

        if missing:
            top_missing = missing[:5]
            st.warning(", ".join(top_missing))
        else:
            st.success("No missing skills 🎉")

        # ------------------ EXPORT CSV ------------------
        os.makedirs("output", exist_ok=True)

        data = []

        for skill in matched:
            data.append([job_role, skill, "Matched"])

        for skill in missing:
            data.append([job_role, skill, "Missing"])

        df = pd.DataFrame(data, columns=["Job Role", "Skill", "Status"])
        df.to_csv("output/dashboard_data.csv", index=False)

        st.success("Dashboard data exported to output/dashboard_data.csv")