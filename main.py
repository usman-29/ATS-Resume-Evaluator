import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

load_dotenv()  # load all our environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_repsonse(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text


def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

# Prompt Template


input_prompt = """
You are a highly skilled ATS (Applicant Tracking System) specialized in evaluating resumes for technical roles, including software engineering, data science, AI engineer. Your goal is to assess a given resume against a provided job description.

1. Carefully analyze the resume and job description for matching skills, experience, and qualifications.
2. Identify missing keywords or skills relevant to the job role.
3. Offer practical advice to improve the resume for a competitive job market.

Your evaluation should be highly accurate and provide constructive feedback. Return the results in a JSON format with the following structure:

I want the response in one single string with this structure:
{{
  "JD Match": "<matching percentage>",
  "MissingKeywords": ["list of missing keywords"],
  "ProfileSummary": "<short summary of the profile>"
}}
"""

# streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader(
    "Upload Your Resume", type="pdf", help="Please uplaod the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        response = get_gemini_repsonse(input_prompt)
        st.subheader(response)
