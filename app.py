import streamlit as st
import pdfplumber

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄")

st.title("🚀 AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    # Extract text
    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

    # Show Resume Content
    st.subheader("📄 Resume Content")
    st.text_area("Extracted Text", text, height=250)

    # Skills Database
    skills = [
        "Python",
        "SQL",
        "Machine Learning",
        "Pandas",
        "NumPy",
        "Scikit-learn",
        "Git",
        "GitHub",
        "Firebase",
        "Edge Impulse",
        "Data Analysis",
        "Jupyter",
        "Power BI",
        "Excel",
        "AWS",
        "Docker",
        "Tableau",
        "Java",
        "C",
        "C++"
    ]

    # Find Skills
    found_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    st.subheader("✅ Skills Found")

    for skill in found_skills:
        st.write(f"✔️ {skill}")

    # ATS Score
    ats_score = int((len(found_skills) / len(skills)) * 100)

    st.subheader("📊 ATS Score")
    st.progress(ats_score)

    st.success(f"Your ATS Score is {ats_score}/100")

    # Missing Skills
    missing_skills = []

    for skill in skills:
        if skill not in found_skills:
            missing_skills.append(skill)

    st.subheader("❌ Missing Skills")

    if len(missing_skills) == 0:
        st.success("No missing skills found!")
    else:
        for skill in missing_skills:
            st.write(f"❌ {skill}")

    # Resume Feedback
    st.subheader("📝 Resume Feedback")

    if ats_score >= 80:
        st.success("Excellent Resume! Ready for most internships and entry-level jobs.")
    elif ats_score >= 60:
        st.warning("Good Resume. Add more industry-relevant skills.")
    else:
        st.error("Resume needs improvement.")

    # Company Match Score
    st.subheader("🏢 Company Match Scores")

    google_skills = ["Python", "SQL", "Machine Learning", "AWS", "Docker"]
    infosys_skills = ["Python", "SQL", "Excel", "Git"]
    tcs_skills = ["Python", "SQL", "Git", "Java"]
    deloitte_skills = ["Python", "Excel", "Power BI", "SQL"]

    def calculate_match(company_skills):
        matched = 0

        for skill in company_skills:
            if skill in found_skills:
                matched += 1

        return int((matched / len(company_skills)) * 100)

    google_score = calculate_match(google_skills)
    infosys_score = calculate_match(infosys_skills)
    tcs_score = calculate_match(tcs_skills)
    deloitte_score = calculate_match(deloitte_skills)

    st.write(f"Google Match: {google_score}%")
    st.write(f"Infosys Match: {infosys_score}%")
    st.write(f"TCS Match: {tcs_score}%")
    st.write(f"Deloitte Match: {deloitte_score}%")

    # Suggestions
    st.subheader("💡 Suggested Skills To Learn")

    suggestions = []

    high_value_skills = [
        "Power BI",
        "AWS",
        "Docker",
        "Tableau",
        "Excel"
    ]

    for skill in high_value_skills:
        if skill not in found_skills:
            suggestions.append(skill)

    if suggestions:
        for skill in suggestions:
            st.write(f"📌 Learn {skill}")
    else:
        st.success("Amazing! You already have all recommended skills.")

    # Download Report
    st.subheader("📥 Download Resume Report")

    report = f"""
AI RESUME ANALYZER REPORT

ATS Score: {ats_score}/100

Skills Found:
{', '.join(found_skills)}

Missing Skills:
{', '.join(missing_skills)}

Google Match: {google_score}%
Infosys Match: {infosys_score}%
TCS Match: {tcs_score}%
Deloitte Match: {deloitte_score}%

Suggested Skills:
{', '.join(suggestions)}
"""

    st.download_button(
        label="Download Report",
        data=report,
        file_name="resume_report.txt",
        mime="text/plain"
    )