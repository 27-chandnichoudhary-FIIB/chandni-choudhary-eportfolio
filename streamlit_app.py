import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Chandni Choudhary | Portfolio",
    page_icon="📊",
    layout="wide",
)

# ---------- Style ----------
st.markdown(
    """
    <style>
    .main { padding-top: 1.5rem; }
    h1, h2, h3 { font-family: 'Georgia', serif; }
    .headline { font-size: 1.15rem; color: #4a4a4a; margin-top: -0.5rem; }
    .section-title {
        border-bottom: 2px solid #1f4e79;
        padding-bottom: 0.3rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .project-card {
        background-color: #f7f9fb;
        border-radius: 10px;
        padding: 1.2rem 1.5rem;
        margin-bottom: 1.2rem;
        border-left: 4px solid #1f4e79;
    }
    .skill-pill {
        display: inline-block;
        background-color: #e8eef5;
        color: #1f4e79;
        padding: 0.25rem 0.75rem;
        border-radius: 999px;
        margin: 0.2rem;
        font-size: 0.85rem;
    }
    a { color: #1f4e79; }
    </style>
    """,
    unsafe_allow_html=True,
)

GITHUB_REPO = "https://github.com/27-chandnichoudhary-FIIB/chandni-choudhary-eportfolio"
LINKEDIN = "https://linkedin.com/in/chandnichoudhary"

# ---------- Header ----------
col_photo, col_intro = st.columns([1, 3])

with col_photo:
    photo_path = Path("assets/profile.jpg")
    if photo_path.exists():
        st.image(str(photo_path), width=180)
    else:
        st.info("Add your photo at assets/profile.jpg")

with col_intro:
    st.title("Chandni Choudhary")
    st.markdown(
        '<div class="headline">PGDM Operations Student | Market Entry Strategy &amp; Business Analysis | Data-Driven Decision Making</div>',
        unsafe_allow_html=True,
    )
    st.write(
        "Operations major with a Marketing minor at Fortune Institute of International Business (FIIB), New Delhi. "
        "Prior industry experience as an Operations Manager at Shree Ganesh Dyeing, Mumbai, and current work building "
        "a data-driven market entry scoring tool for the México–India Business Council. Comfortable with Python, "
        "Power BI, Excel and HTML/CSS, targeting analyst roles where data, structure and business decision-making meet."
    )
    st.markdown(f"[LinkedIn]({LINKEDIN}) &nbsp;|&nbsp; [GitHub]({GITHUB_REPO})")

# ---------- Skills ----------
st.markdown('<h2 class="section-title">Skills</h2>', unsafe_allow_html=True)

skill_groups = {
    "Domain & Business": ["Operations Management", "Market Entry Strategy", "Business Analysis", "Project Management"],
    "Analytics": ["Excel", "Power BI", "DAX", "RFM Segmentation"],
    "Digital & AI Tools": ["Python", "HTML/CSS", "AI-Assisted Development"],
}

for group, skills in skill_groups.items():
    st.markdown(f"**{group}**")
    st.markdown("".join(f'<span class="skill-pill">{s}</span>' for s in skills), unsafe_allow_html=True)

# ---------- Projects ----------
st.markdown('<h2 class="section-title">Projects</h2>', unsafe_allow_html=True)

projects = [
    {
        "title": "MIBC Market Entry Intelligence Tool",
        "problem": "MIBC advisors needed a structured way to assess Mexican brand readiness to enter the Indian market.",
        "contribution": "Sourced and independently verified all underlying data; AI assisted with the code implementation.",
        "tools": "Weighted composite scoring model (Demand Readiness 40%, Regulatory Ease 35%, Distributor Readiness 25%); HTML5/CSS3/JavaScript, Netlify.",
        "output": "Live web app covering 7 Indian cities and 9+ product categories.",
        "evidence": "https://market-entry-intelligence-v5.netlify.app",
        "evidence_label": "View live tool",
    },
    {
        "title": "Wakefit North India Retail Expansion — PM Capstone (Group 6)",
        "problem": "Plan Wakefit's North India offline retail expansion; manage a stakeholder-unavailability crisis mid-project.",
        "contribution": "Project Manager — led the Charter, WBS/Gantt, Network Diagram, and the M5 risk register & mitigation plan.",
        "tools": "PM methodology — WBS, critical path method (CPM), risk mitigation planning.",
        "output": "All milestones delivered on schedule despite a 2-week stakeholder unavailability.",
        "evidence": f"{GITHUB_REPO}/tree/main/evidence/wakefit-pm-capstone",
        "evidence_label": "View project files",
    },
    {
        "title": "TQMSS Airline Operational Quality Dashboard",
        "problem": "Diagnose where airline service quality was breaking down, using 5,000 flight records.",
        "contribution": "Built the Power BI dashboard, selected the KPIs, and wrote the management insights.",
        "tools": "Power BI; KPI benchmarking (OTP%, delay severity, cancellations, baggage handling).",
        "output": "Identified a 23-point on-time performance gap, pinpointed to one carrier's operations at one airport.",
        "evidence": f"{GITHUB_REPO}/tree/main/evidence/tqmss-airline-dashboard",
        "evidence_label": "View project files",
    },
    {
        "title": "AUTO-MOTIVE Sales & Service Dashboard (Learning Team 2)",
        "problem": "Understand which car models, regions, and service factors drive sales, satisfaction, and complaints.",
        "contribution": "Decomposition tree and key-driver analysis within the team's Power BI dashboard.",
        "tools": "Power BI, star-schema data model, DAX measures.",
        "output": "Analyzed 201 car sales (₹336.61M); flagged one model as high-risk and one region driving the majority of sales.",
        "evidence": f"{GITHUB_REPO}/tree/main/evidence/auto-motive-dashboard",
        "evidence_label": "View project files",
    },
]

for p in projects:
    st.markdown(
        f"""
        <div class="project-card">
        <h4>{p['title']}</h4>
        <p><b>Problem:</b> {p['problem']}</p>
        <p><b>My contribution:</b> {p['contribution']}</p>
        <p><b>Approach & tools:</b> {p['tools']}</p>
        <p><b>Output:</b> {p['output']}</p>
        <p><a href="{p['evidence']}" target="_blank">{p['evidence_label']} →</a></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------- Experience ----------
st.markdown('<h2 class="section-title">Experience</h2>', unsafe_allow_html=True)
st.markdown(
    """
    - **Corporate Internship Programme (CIP), México–India Business Council (MIBC) / IM Global** — April 2026 onward, Delhi/Mumbai hybrid
    - **Operations Manager, Shree Ganesh Dyeing, Mumbai** — prior to PGDM
    """
)

# ---------- Education ----------
st.markdown('<h2 class="section-title">Education</h2>', unsafe_allow_html=True)
st.markdown("**PGDM (Operations)**, Fortune Institute of International Business (FIIB), New Delhi — Batch 2025–27")

# ---------- Footer ----------
st.markdown('<h2 class="section-title">Get in Touch</h2>', unsafe_allow_html=True)
st.markdown(f"[LinkedIn]({LINKEDIN}) &nbsp;|&nbsp; [GitHub Portfolio Repository]({GITHUB_REPO})")
