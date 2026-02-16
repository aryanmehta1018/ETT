import streamlit as st
import json
import os

from backend.resume_parser import extract_text
from backend.skill_extractor import extract_skills_with_llm
from backend.matcher import match_skills

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])

if uploaded_file:

    
    resume_text = extract_text(uploaded_file)

    st.subheader("Extracted Resume Text")
    st.text_area("Resume Content", resume_text, height=250)

    
    with st.spinner("Analyzing with AI..."):
        extracted_skills = extract_skills_with_llm(resume_text)

    st.subheader("Extracted Skills")
    st.write(extracted_skills)

    
    with open("data/job_roles.json") as f:
        job_roles = json.load(f)

    job_role = st.selectbox("Select Job Role", list(job_roles.keys()))

    if st.button("Match Skills"):

        required_skills = job_roles[job_role]
        result = match_skills(extracted_skills, required_skills)

        st.subheader("Match Results")
        st.write(f"Match Percentage: {result['match_percentage']}%")
        st.write("Matched Skills:", result["matched_skills"])
        st.write("Missing Skills:", result["missing_skills"])

        
        import csv

        os.makedirs("output", exist_ok=True)

        with open("output/dashboard_data.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Job Role", job_role])
            writer.writerow(["Match Percentage", result["match_percentage"]])
            writer.writerow(["Matched Skills", ", ".join(result["matched_skills"])])
            writer.writerow(["Missing Skills", ", ".join(result["missing_skills"])])

        st.success("Dashboard data exported to output/dashboard_data.csv")
