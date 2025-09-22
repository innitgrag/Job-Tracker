# app.py - CORRECTED VERSION
import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="Cold Email Generator", page_icon="📧", layout="centered")

# --- Sidebar: User profile ---
st.sidebar.header("Your Profile")
name = st.sidebar.text_input("Full name", value="Akshiti Garg")
email = st.sidebar.text_input("Contact email", value="akshitigarg1224@gmail.com")
phone = st.sidebar.text_input("Phone", value="+91-8949031109")
linkedin = st.sidebar.text_input("LinkedIn URL", value="")
github = st.sidebar.text_input("GitHub URL", value="")

st.sidebar.markdown("---")
st.sidebar.caption("These details auto-fill at the bottom of the email.")

# --- Preset company data ---
COMPANIES = {
    "Google": {
        "industry": "Technology",
        "size": "100,000+ employees",
        "followers": "29M+ LinkedIn followers",
        "salary": "₹15-45 LPA",
        "category": "Product-based",
        "focus": "search technology and cloud computing",
        "specialties": ["AI/ML", "Cloud Computing", "Search", "Mobile"],
        "news": "expanding AI capabilities and cloud infrastructure",
        "hq": "Mountain View, CA"
    },
    "Microsoft": {
        "industry": "Technology",
        "size": "220,000+ employees",
        "followers": "20M+ LinkedIn followers",
        "salary": "₹12-40 LPA",
        "category": "Product-based",
        "focus": "cloud computing and productivity software",
        "specialties": ["Azure", "Office 365", "Windows", "AI"],
        "news": "major investments in AI and cloud services",
        "hq": "Redmond, WA"
    },
    "Amazon": {
        "industry": "E-commerce & Cloud",
        "size": "1.5M+ employees",
        "followers": "28M+ LinkedIn followers",
        "salary": "₹18-50 LPA",
        "category": "Product-based",
        "focus": "e-commerce and cloud infrastructure",
        "specialties": ["AWS", "E-commerce", "Logistics", "AI"],
        "news": "expanding AWS services and retail innovation",
        "hq": "Seattle, WA"
    },
    "Meta": {
        "industry": "Social Media & Technology",
        "size": "86,000+ employees",
        "followers": "5M+ LinkedIn followers",
        "salary": "₹20-55 LPA",
        "category": "Product-based",
        "focus": "social media and metaverse technologies",
        "specialties": ["Social Media", "VR/AR", "AI", "Mobile"],
        "news": "heavy investment in metaverse and AI research",
        "hq": "Menlo Park, CA"
    },
    "Netflix": {
        "industry": "Entertainment & Streaming",
        "size": "12,000+ employees",
        "followers": "3M+ LinkedIn followers",
        "salary": "₹25-60 LPA",
        "category": "Product-based",
        "focus": "streaming entertainment and content recommendation",
        "specialties": ["Streaming", "Content", "Recommendation Systems", "Big Data"],
        "news": "expanding global content and improving recommendation algorithms",
        "hq": "Los Gatos, CA"
    },
}

subject_templates = [
    "Passionate BITS Pilani Grad Seeking Software Engineering Opportunities at {company}",
    "Full-Stack Developer from BITS Pilani - Ready to Contribute to {company}",
    "Software Engineer with Production Experience - Interested in {company} Opportunities",
    "BITS Pilani EEE Grad with Strong Tech Stack - Exploring Roles at {company}",
    "Full-Stack Engineer from BITS Pilani - Excited About {company} Opportunities",
    "Software Developer with 400+ LeetCode Solutions - Interested in {company}",
    "Production-Ready Developer from BITS Pilani Seeking Opportunities at {company}",
]

intro_templates = [
    "I hope this email finds you well. My name is {name}, and I am a recent B.E. (Hons.) graduate in Electrical and Electronics Engineering from BITS Pilani, Hyderabad Campus (CGPA: 7.92). I'm particularly drawn to {company}'s {focus} and would love to contribute to your mission.",
    "I'm {name}, a recent graduate from BITS Pilani, Hyderabad Campus (EEE, CGPA: 7.92). Having researched {company}'s innovative work in {focus}, I'm excited about the possibility of joining your team.",
]

experience_block = """I bring hands-on experience as a Software Developer Intern at Piramal Finance Limited, where I:
• Implemented 6+ frontend and backend modules using React.js, TypeScript, and Spring Boot
• Integrated 10+ REST APIs and collaborated with cross-functional teams for 3+ production releases
• Built custom monitoring solutions that reduced issue resolution time

Previously, at Cognix Technologies, I developed a Flutter-based food tracking app that reduced manual logging effort by 30% and accelerated feature delivery by 25%."""

tech_block = """My technical stack includes C++, Java, SQL, Node.js, React.js, Spring Boot, and experience with scalable full-stack applications. I have strong foundations in DSA, OOP, OS, DBMS, and System Design."""

projects_block = """• PG Pal: Full-stack platform with secure authentication and advanced filtering (pg-pal.vercel.app)
• Jobify: Job matching platform connecting recruiters and candidates"""

closing_templates = [
    "I would welcome the opportunity to discuss how my technical skills and passion for software development can contribute to {company}'s continued innovation. Thank you for your time.",
    "I'm excited about the possibility of contributing to {company}'s projects and would love to discuss how my skills align with your team's needs. Thank you for your consideration.",
]

st.title("📧 Cold Email Generator (with Company Research)")
st.caption("Create personalized, research-backed cold emails in minutes.")

# --- Company Selection ---
col1, col2 = st.columns([2,1])
with col1:
    company = st.selectbox("Select a company", options=list(COMPANIES.keys()) + ["Custom"])
with col2:
    variants = st.number_input("Variants", min_value=1, max_value=5, value=3, step=1)

custom_company = {}
if company == "Custom":
    st.markdown("### Enter custom company details")
    cc1, cc2 = st.columns(2)
    with cc1:
        custom_company["name"] = st.text_input("Company name", value="Acme Corp")
        custom_company["industry"] = st.text_input("Industry", value="Technology")
        custom_company["size"] = st.text_input("Company size", value="1000+ employees")
        custom_company["followers"] = st.text_input("LinkedIn followers", value="N/A")
    with cc2:
        custom_company["salary"] = st.text_input("Salary range", value="₹8-25 LPA")
        custom_company["category"] = st.text_input("Category", value="Product-based")
        custom_company["focus"] = st.text_input("Focus area", value="innovative technology solutions")
        custom_company["hq"] = st.text_input("Headquarters", value="Unknown")
    custom_company["specialties"] = st.text_input("Specialties (comma-separated)", value="Software Development, Technology").split(",")
    custom_company["news"] = st.text_input("Recent news (optional)", value="growth and innovation")

# Pick company data
if company != "Custom":
    data = COMPANIES[company]
    company_name = company
else:
    data = custom_company
    company_name = custom_company.get("name", "")

# --- Show Research Card ---
st.markdown("### Company Research")
with st.container(border=True):
    st.write(f"**Company:** {company_name}")
    st.write(f"**Industry:** {data.get('industry','')} | **Category:** {data.get('category','')}")
    st.write(f"**Size:** {data.get('size','')} | **HQ:** {data.get('hq','')}")
    st.write(f"**LinkedIn:** {data.get('followers','')} | **Salary Range:** {data.get('salary','')}")
    st.write(f"**Focus:** {data.get('focus','')}")
    st.write(f"**Specialties:** {', '.join(data.get('specialties', [])[:3])}")
    if data.get('news'):
        st.write(f"**Recent news:** {data.get('news')}")

st.markdown("---")

# Hiring manager
hiring_manager = st.text_input("Hiring manager (optional)", value="Hiring Manager")

# Generate button
if st.button("Generate Emails"):
    emails = []
    for i in range(variants):
        subject = random.choice(subject_templates).format(company=company_name)
        intro = random.choice(intro_templates).format(name=name, company=company_name, focus=data.get('focus',''))
        specialties = ", ".join(data.get('specialties', [])[:3])
        closing = random.choice(closing_templates).format(company=company_name)

        body = f"""Dear {hiring_manager},

{intro}

I am writing to express my interest in software engineering opportunities at {company_name}.

**Company Research Insights:**
I'm impressed by {company_name}'s position as a leading {data.get('category','')} company with {data.get('size','')} and {data.get('followers','')}. Your specialization in {specialties} aligns with my technical background.

**Experience & Skills:**
{experience_block}

**Technical Expertise:**
{tech_block}

**Notable Projects:**
{projects_block}

**Problem-Solving Foundation:**
I have solved 400+ problems on LeetCode, demonstrating strong algorithmic thinking.

{closing}

Best regards,
{name}
📧 {email}
📱 {phone}
💼 LinkedIn: {linkedin}
🔗 GitHub: {github}"""

        emails.append((subject, body))

    st.success(f"Generated {len(emails)} email(s)")

    for idx, (subject, body) in enumerate(emails, start=1):
        st.markdown(f"#### Version {idx}")
        st.text_input("Subject", value=subject, key=f"sub_{idx}")
        st.text_area("Body", value=body, height=420, key=f"body_{idx}")
        fname = f"cold_email_{company_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}_v{idx}.txt"
        # FIXED: Added proper file_name parameter
        st.download_button("Download .txt", data=f"SUBJECT: {subject}\n\n{body}", file_name=fname, mime="text/plain")
        st.markdown("---")

st.info("Tip: Edit the text above before downloading to fine-tune for each role.")
