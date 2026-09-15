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
    .badge-row { margin-bottom: 1.5rem; }
    .tag-pill {
        display: inline-block;
        background-color: #eef3f9;
        color: #1f4e79;
        padding: 0.3rem 0.9rem;
        border-radius: 999px;
        margin: 0.2rem 0.3rem 0.2rem 0;
        font-size: 0.8rem;
        font-weight: 600;
        letter-spacing: 0.02em;
    }
    .headline {
        font-size: 1.6rem;
        font-weight: 600;
        color: #1a1a1a;
        margin: 0.4rem 0 1rem 0;
        line-height: 1.3;
    }
    .headline .accent { color: #1f4e79; }
    .stat-card {
        background-color: #f7f9fb;
        border-radius: 12px;
        padding: 1.1rem 1rem;
        text-align: left;
        border: 1px solid #e6ebf1;
        height: 100%;
    }
    .stat-number { font-size: 1.7rem; font-weight: 700; color: #1f4e79; }
    .stat-label { font-size: 0.8rem; color: #666; margin-top: 0.2rem; }
    .section-title {
        border-bottom: 2px solid #1f4e79;
        padding-bottom: 0.3rem;
        margin-top: 2.5rem;
        margin-bottom: 1.2rem;
    }
    .project-card {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 1.4rem 1.6rem;
        margin-bottom: 1.3rem;
        border: 1px solid #e6ebf1;
        border-left: 5px solid #1f4e79;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }
    .project-title { font-size: 1.2rem; font-weight: 700; margin-bottom: 0.5rem; }
    .project-row { margin: 0.35rem 0; font-size: 0.95rem; }
    .project-row b { color: #1f4e79; }
    .timeline-item {
        border-left: 3px solid #1f4e79;
        padding-left: 1.2rem;
        margin-bottom: 1.6rem;
        position: relative;
    }
    .timeline-item::before {
        content: "";
        position: absolute;
        left: -7px;
        top: 4px;
        width: 11px;
        height: 11px;
        border-radius: 50%;
        background-color: #1f4e79;
    }
    .timeline-role { font-weight: 700; font-size: 1.05rem; }
    .timeline-org { color: #555; font-size: 0.9rem; margin-bottom: 0.3rem; }
    a { color: #1f4e79; }
    div.stButton > button, div.stDownloadButton > button {
        background-color: #1f4e79;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 0.5rem 1.3rem;
        font-weight: 600;
    }
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
        st.image(str(photo_path), width=200)
    else:
        st.info("Add your photo at assets/profile.jpg")

with col_intro:
    st.markdown(
        '<span class="tag-pill">OPERATIONS</span><span class="tag-pill">BUSINESS ANALYSIS</span>'
        '<span class="tag-pill">MARKET ENTRY STRATEGY</span><span class="tag-pill">POWER BI</span>',
        unsafe_allow_html=True,
    )
    st.title("Chandni Choudhary")
    st.markdown(
        '<div class="headline">Turning operational problems into '
        '<span class="accent">data-driven, evidence-backed decisions.</span></div>',
        unsafe_allow_html=True,
    )
    st.write(
        "Operations major with a Marketing minor at Fortune Institute of International Business (FIIB), New Delhi. "
        "Prior industry experience as an Operations Manager at Shree Ganesh Dyeing, Mumbai, and current work building "
        "a data-driven market entry scoring tool for the México–India Business Council. Comfortable with Python, "
        "Power BI, Excel and HTML/CSS, targeting analyst roles where data, structure and business decision-making meet."
    )
    st.markdown(f"[LinkedIn]({LINKEDIN}) &nbsp;|&nbsp; [GitHub]({GITHUB_REPO})")

    resume_path = Path("assets/resume.docx")
    if resume_path.exists():
        with open(resume_path, "rb") as f:
            st.download_button(
                label="⬇ Download Resume",
                data=f,
                file_name="Chandni_Choudhary_Resume.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            )
    else:
        st.caption("Resume: add assets/resume.docx to enable download")

st.write("")

stat_cols = st.columns(4)
stats = [
    ("4", "Projects", "Analytics, operations & strategy work"),
    ("1", "Live Tool", "MIBC Market Entry Intelligence Tool"),
    ("Power BI + Python", "Toolkit", "Dashboards, DAX, data verification"),
    ("2025–27", "PGDM Operations", "Fortune Institute of Int'l Business"),
]
for col, (num, label, sub) in zip(stat_cols, stats):
    with col:
        st.markdown(
            f"""
            <div class="stat-card">
            <div class="stat-number">{num}</div>
            <div><b>{label}</b></div>
            <div class="stat-label">{sub}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ---------- Skills ----------
st.markdown('<h2 class="section-title">Skills</h2>', unsafe_allow_html=True)

skill_groups = {
    "Domain & Business": ["Operations Management", "Market Entry Strategy", "Business Analysis", "Project Management"],
    "Analytics": ["Excel", "Power BI", "DAX", "RFM Segmentation"],
    "Digital & AI Tools": ["Python", "HTML/CSS", "AI-Assisted Development"],
}

for group, skills in skill_groups.items():
    st.markdown(f"**{group}**")
    st.markdown("".join(f'<span class="tag-pill">{s}</span>' for s in skills), unsafe_allow_html=True)

# ---------- Projects ----------
st.markdown('<h2 class="section-title">Projects</h2>', unsafe_allow_html=True)

projects = [
    {
        "title": "📈 MIBC Market Entry Intelligence Tool",
        "problem": "MIBC advisors needed a structured way to assess Mexican brand readiness to enter the Indian market.",
        "contribution": "Sourced and independently verified all underlying data; AI assisted with the code implementation.",
        "tools": ["Weighted Scoring Model", "HTML5/CSS3/JavaScript", "Netlify"],
        "output": "Live web app covering 7 Indian cities and 9+ product categories.",
        "evidence": "https://market-entry-intelligence-v5.netlify.app",
        "evidence_label": "View live tool",
    },
    {
        "title": "🗂️ Wakefit North India Retail Expansion — PM Capstone (Group 6)",
        "problem": "Plan Wakefit's North India offline retail expansion; manage a stakeholder-unavailability crisis mid-project.",
        "contribution": "Project Manager — led the Charter, WBS/Gantt, Network Diagram, and the M5 risk register & mitigation plan.",
        "tools": ["WBS", "Critical Path Method", "Risk Mitigation Planning"],
        "output": "All milestones delivered on schedule despite a 2-week stakeholder unavailability.",
        "evidence": f"{GITHUB_REPO}/tree/main/evidence/wakefit-pm-capstone",
        "evidence_label": "View project files",
    },
    {
        "title": "✈️ TQMSS Airline Operational Quality Dashboard",
        "problem": "Diagnose where airline service quality was breaking down, using 5,000 flight records.",
        "contribution": "Built the Power BI dashboard, selected the KPIs, and wrote the management insights.",
        "tools": ["Power BI", "KPI Benchmarking", "Quality Management"],
        "output": "Identified a 23-point on-time performance gap, pinpointed to one carrier's operations at one airport.",
        "evidence": f"{GITHUB_REPO}/tree/main/evidence/tqmss-airline-dashboard",
        "evidence_label": "View project files",
    },
    {
        "title": "🚗 AUTO-MOTIVE Sales & Service Dashboard (Learning Team 2)",
        "problem": "Understand which car models, regions, and service factors drive sales, satisfaction, and complaints.",
        "contribution": "Decomposition tree and key-driver analysis within the team's Power BI dashboard.",
        "tools": ["Power BI", "Star Schema", "DAX Measures"],
        "output": "Analyzed 201 car sales (₹336.61M); flagged one model as high-risk and one region driving the majority of sales.",
        "evidence": f"{GITHUB_REPO}/tree/main/evidence/auto-motive-dashboard",
        "evidence_label": "View project files",
    },
]

for p in projects:
    tools_html = "".join(f'<span class="tag-pill">{t}</span>' for t in p["tools"])
    st.markdown(
        f"""
        <div class="project-card">
        <div class="project-title">{p['title']}</div>
        <div class="project-row"><b>Problem:</b> {p['problem']}</div>
        <div class="project-row"><b>My contribution:</b> {p['contribution']}</div>
        <div class="project-row">{tools_html}</div>
        <div class="project-row"><b>Output:</b> {p['output']}</div>
        <div class="project-row"><a href="{p['evidence']}" target="_blank">{p['evidence_label']} →</a></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------- Experience ----------
st.markdown('<h2 class="section-title">Experience</h2>', unsafe_allow_html=True)

experience = [
    {
        "role": "Corporate Intern",
        "org": "México–India Business Council (MIBC) / IM Global — April 2026 onward, Delhi/Mumbai hybrid",
    },
    {
        "role": "Operations Manager",
        "org": "Shree Ganesh Dyeing, Mumbai — prior to PGDM",
    },
]
for e in experience:
    st.markdown(
        f"""
        <div class="timeline-item">
        <div class="timeline-role">{e['role']}</div>
        <div class="timeline-org">{e['org']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------- Education ----------
st.markdown('<h2 class="section-title">Education</h2>', unsafe_allow_html=True)
st.markdown("**PGDM (Operations)**, Fortune Institute of International Business (FIIB), New Delhi — Batch 2025–27")

# ---------- Footer ----------
st.markdown('<h2 class="section-title">Get in Touch</h2>', unsafe_allow_html=True)
st.markdown(f"[LinkedIn]({LINKEDIN}) &nbsp;|&nbsp; [GitHub Portfolio Repository]({GITHUB_REPO})")
