import streamlit as st
import json
from backend.resume_parser import extract_text

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])

if uploaded_file:
    text = extract_text(uploaded_file)
    st.text_area("Extracted Resume Text", text, height=300)
