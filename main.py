
from dotenv import load_dotenv

load_dotenv()
import streamlit as st
import os
from PIL import Image
import pdf2image
import google.generativeai as gmai
import PyPDF2 as pdf


gmai.configure(api_key=os.getenv("API_KEY"))


def get_gemini_responce(input):
    model=gmai.GenerativeModel("gemini-pro")
    responce=model.generate_content(input)
    return responce.text

def input_pdf_setup(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page1 in range(len(reader.pages)):
        page=reader.pages[page1]
        text+=str(page.extract_text())
    return text



st.set_page_config(page_title="ATS Resume",page_icon=":smiley:",layout="wide")
st.header("ATS(Applications Tracking System) Resume")
input_text = st.text_area(
'job' , placeholder="Enter the job description here", key="input", height=200)
uploaded_file = st.file_uploader('upload', type=['pdf'],help="Upload your resume here")    

if uploaded_file is not None:
    st.write("Uploaded")
    
sumbit1=st.button("Tell me my chances")
sumbit2=st.button("Tell me my chances with prompt")
sumbit3=st.button("Tell me my chances with prompt and pdf")
sumbit4=st.button("Tell me my chances with prompt and pdf and job description")

input_prompt1 = """
As an experienced HR professional with  expertise across various career fields, 
your task is to review the provided resume in comparison to the job description for those profiles.
 Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job role."""


input_prompt2 = """
Your are experienced in every field, you would like to know how the provided resume can be tailored to better match the job description for these profiles.
"""
input_prompt_3 = """
"You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of every field and extensive knowledge of ATS functionality.
 Your task is to evaluate the resume against the provided job description and provide the percentage of match.
 First, the output should be presented as a percentage, 
 followed by the missing keywords, and finally, share your overall thoughts on the match."""


input_prompt_4 = """
As a seasoned HR professional with broad expertise spanning various career domains, your role involves evaluating the provided resume vis-à-vis the job description. Please identify the software applications outlined in the job description and specify their respective purposes."""

if sumbit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        responce=get_gemini_responce(input_prompt1)
        st.write(responce)
    
    else:
        st.write("Please upload the resume")
elif sumbit2:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        responce=get_gemini_responce(input_prompt2)
        st.write(responce)    
    else:
        st.write("Please upload the resume")
elif sumbit3:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        responce=get_gemini_responce(input_prompt_3)
        st.write(responce)    
    else:
        st.write("Please upload the resume")

elif sumbit4:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        responce=get_gemini_responce(input_prompt_4)
        st.write(responce)    
    else:
        st.write("Please upload the resume")
