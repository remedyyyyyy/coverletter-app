import streamlit as st
from datetime import datetime
from docx import Document

st.set_page_config(page_title="Cover Letter Generator", layout="centered")

st.title("📄 Smart Cover Letter Generator")

with st.form("cover_letter_form"):
    company = st.text_input("Company Name")
    position = st.text_input("Job Title / Position")
    jd = st.text_area("Paste Job Description Here", height=200)

    submitted = st.form_submit_button("Generate Cover Letter")

if submitted:
    today = datetime.now().strftime("%-d %B %Y")
    jd_lower = jd.lower()
    keywords = ["quality", "inspection", "iqc", "oqc", "iso", "report", "data"]
    include_internship = any(k in jd_lower for k in keywords)

    paragraph2 = (
        "During my Quality Engineering Internship at VS Industry Sdn. Bhd., I gained practical experience in establishing and maintaining quality standards. "
        "I successfully conducted over 150 IQC inspections on materials such as resin and raw materials, keeping defect rates under 2%. "
        "I also performed OQC checks to ensure 100% on-time delivery and supported ISO 9001:2015 documentation efforts, aligning well with your responsibilities."
    ) if include_internship else (
        "As a Mechanical Engineering graduate, I bring a solid foundation in quality practices, inspection routines, and strong communication skills that I believe will make me a valuable addition to your team."
    )

    letter = f"""Norfatin Hazirah Mohd Idris
Johor Bahru, Johor
014-6887244
norfatinhazirahmohdidris@yahoo.com
linkedin.com/in/fatin-04-20

Hiring Manager
{company}

{today}

Application for {position} Position

Dear Hiring Manager,

I am writing to express my keen interest in the {position} position at {company}. As a recent Mechanical Engineering graduate with a foundation in quality control, machine maintenance, and a proactive approach to problem-solving, I am confident in my ability to contribute effectively to your team.

{paragraph2}

I am also adept at data management and reporting, having maintained accurate quality records using Microsoft Dynamics SL and Excel with 99% accuracy during my internship. Additionally, I am proficient in Microsoft Office, AutoCAD, and Fusion 360, and am eager to learn and adapt to new technologies and systems.

I am a fast learner, able to work under pressure, and possess excellent communication skills. Thank you for considering my application. I have attached my resume for your review and welcome the opportunity to discuss how my skills and enthusiasm can benefit {company}.

Sincerely,
Norfatin Hazirah Mohd Idris
+6014-6887244"""

    st.success("✅ Cover letter generated!")
    st.text_area("📄 Your Cover Letter:", letter, height=400)

    doc = Document()
    for line in letter.split("\n"):
        doc.add_paragraph(line)
    doc.save("cover_letter.docx")

    with open("cover_letter.docx", "rb") as file:
        st.download_button("⬇ Download .docx", file, file_name="Cover_Letter.docx")
