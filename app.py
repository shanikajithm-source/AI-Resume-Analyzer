import streamlit as st
import pdfplumber

# Page Settings
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄"
)

st.title("🚀 AI Resume Analyzer")

# Job Role Selection
st.subheader("🎯 Select Target Job Role")

job_role = st.selectbox(
    "Choose a role",
    [
        "Data Analyst",
        "Data Scientist",
        "Python Developer"
    ]
)

# Upload Resume
uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    # Extract Resume Text
    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text

    # Display Resume Content
    st.subheader("📄 Resume Content")

    st.text_area(
        "Extracted Text",
        text,
        height=250
    )

    # Master Skills Database
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

    # Find Skills Present in Resume
    found_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    # Display Skills
    st.subheader("✅ Skills Found")

    if found_skills:
        for skill in found_skills:
            st.write(f"✔️ {skill}")
    else:
        st.warning("No skills found.")

    # Role-Based Skills
    job_skills = {

        "Data Analyst": [
            "Python",
            "SQL",
            "Excel",
            "Power BI",
            "Tableau",
            "Data Analysis"
        ],

        "Data Scientist": [
            "Python",
            "Machine Learning",
            "Pandas",
            "NumPy",
            "Scikit-learn",
            "SQL"
        ],

        "Python Developer": [
            "Python",
            "Git",
            "GitHub",
            "Docker",
            "AWS",
            "SQL"
        ]
    }

    # Selected Role
    st.subheader("🎯 Selected Role")
    st.info(job_role)

    required_skills = job_skills[job_role]

    matched_skills = []

    for skill in required_skills:
        if skill.lower() in text.lower():
            matched_skills.append(skill)

    # ATS Score
    ats_score = int(
        (len(matched_skills) / len(required_skills)) * 100
    )

    st.subheader("📊 ATS Score")

    st.progress(ats_score)

    st.success(
        f"Your ATS Score is {ats_score}/100"
    )

    # Resume Strength
    st.subheader("🏆 Resume Strength")

    if ats_score >= 90:
        st.success("Excellent Resume")
    elif ats_score >= 70:
        st.info("Good Resume")
    elif ats_score >= 50:
        st.warning("Average Resume")
    else:
        st.error("Needs Improvement")

    # Missing Skills
    missing_skills = []

    for skill in required_skills:
        if skill not in matched_skills:
            missing_skills.append(skill)

    st.subheader("❌ Missing Skills")

    if missing_skills:
        for skill in missing_skills:
            st.write(f"❌ {skill}")
    else:
        st.success("No missing skills found!")

    # Company Match Scores
    st.subheader("🏢 Company Match Scores")

    companies = {

        "Google": [
            "Python",
            "Machine Learning",
            "Git",
            "AWS",
            "Docker"
        ],

        "Infosys": [
            "Python",
            "SQL",
            "Excel",
            "Git"
        ],

        "TCS": [
            "Python",
            "SQL",
            "Git",
            "Java"
        ],

        "Deloitte": [
            "Python",
            "Power BI",
            "Excel",
            "SQL"
        ]
    }

    company_scores = {}

    for company, company_skills in companies.items():

        matched = 0

        for skill in company_skills:
            if skill in found_skills:
                matched += 1

        score = int(
            (matched / len(company_skills)) * 100
        )

        company_scores[company] = score

        st.write(f"{company}: {score}%")

    # Suggestions
    st.subheader("💡 Skills Recommended To Learn")

    recommendations = []

    for skill in missing_skills:
        recommendations.append(skill)

    if recommendations:
        for skill in recommendations:
            st.write(f"📌 Learn {skill}")
    else:
        st.success("Great! No recommendations.")

    # Download Report
    st.subheader("📥 Download Resume Report")

    report = f"""
AI RESUME ANALYZER REPORT

Selected Role:
{job_role}

ATS Score:
{ats_score}/100

Skills Found:
{', '.join(found_skills)}

Missing Skills:
{', '.join(missing_skills)}

Company Match Scores:
Google: {company_scores['Google']}%
Infosys: {company_scores['Infosys']}%
TCS: {company_scores['TCS']}%
Deloitte: {company_scores['Deloitte']}%

Recommended Skills:
{', '.join(recommendations)}
"""

    st.download_button(
        label="📄 Download Report",
        data=report,
        file_name="resume_report.txt",
        mime="text/plain"
    )