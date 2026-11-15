
import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Meridian Workforce Intelligence | AS3",
    page_icon="📊",
    layout="wide"
)

# ---------------- CUSTOM DESIGN ----------------
st.markdown("""
<style>
.stApp {
    background-color: #F7F8FC;
}
h1, h2, h3 {
    color: #26345C;
}
[data-testid="stSidebar"] {
    background-color: #202B4A;
}
[data-testid="stSidebar"] * {
    color: white !important;
}
.metric-card {
    background: white;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #E4E7F0;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("MERIDIAN")
st.sidebar.caption("AS3 E-PORTFOLIO")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "NAVIGATION",
    [
        "Home",
        "Business Overview",
        "Revenue Model",
        "Workforce Plan",
        "Job Role Analysis",
        "Employee Lifecycle",
        "Reflection & Learning",
        "Evidence"
    ]
)

st.sidebar.markdown("---")
st.sidebar.write("**Prepared by:**")
st.sidebar.write("Nikita Joshi")
st.sidebar.write("PGDM | FIIB")
st.sidebar.caption("Academic Project | AS3")

# ---------------- HOME ----------------
if page == "Home":
    st.title("Meridian Workforce Intelligence")
    st.subheader("AS3 | Human Resource Management E-Portfolio")

    st.markdown("""
    ### The right workforce. The right business decisions.

    Welcome to my AS3 e-portfolio. This project focuses on
    designing the workforce and HR practices for Meridian
    Workforce Intelligence, an AI-powered workforce planning
    platform.

    The portfolio presents the business model, revenue plan,
    workforce structure, job role analysis, recruitment and
    employee lifecycle.
    """)

    st.image(
        "https://images.unsplash.com/photo-1552664730-d307ca884978",
        caption="Building an effective and future-ready workforce",
        use_container_width=True
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("Revenue Ambition", "₹100 Cr")
    col2.metric("Planned Workforce", "202")
    col3.metric("Business Functions", "10")

    st.info("All financial figures, customer volumes and workforce numbers in this portfolio are proposed planning assumptions, not actual business results.")

# ---------------- BUSINESS OVERVIEW ----------------
elif page == "Business Overview":
    st.title("01 | Business Overview")

    st.subheader("About Meridian")
    st.write("""
    Meridian Workforce Intelligence is an AI-powered workforce
    planning platform designed to help organisations make better
    people-related decisions.

    It helps businesses forecast employee requirements, identify
    skill gaps and decide whether to hire new employees, reskill
    existing employees or redeploy talent.
    """)

    st.subheader("The Business Challenge")
    st.write("""
    Organisations may have enough employees but still lack the
    specific skills needed for future business requirements.
    Meridian aims to solve this challenge through workforce data
    and AI-driven insights.
    """)

    st.subheader("How the Platform Creates Value")

    c1, c2, c3 = st.columns(3)
    c1.markdown("### 🔍 Forecast")
    c1.write("Predict future workforce requirements.")
    c2.markdown("### 🎯 Identify")
    c2.write("Highlight skill shortages and capability gaps.")
    c3.markdown("### 🚀 Recommend")
    c3.write("Support Hire, Reskill and Redeploy decisions.")

    st.subheader("Target Customers")
    st.write("Small and medium businesses, mid-sized organisations and large enterprises.")

# ---------------- REVENUE MODEL ----------------
elif page == "Revenue Model":
    st.title("02 | Revenue Model")
    st.write("The proposed annual revenue ambition is ₹100 crore.")

    revenue = pd.DataFrame({
        "Revenue Stream": [
            "Subscriptions",
            "Setup & Integration",
            "Consulting"
        ],
        "Revenue (₹ Crore)": [90, 8.5, 1.5]
    })

    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("Revenue Breakdown")
        st.dataframe(revenue, use_container_width=True, hide_index=True)
        st.metric("Total Revenue Ambition", "₹100 Cr")

    with col2:
        st.subheader("Revenue Contribution")
        st.bar_chart(
            revenue.set_index("Revenue Stream"),
            y="Revenue (₹ Crore)"
        )

    st.subheader("Subscription Plans")

    plans = pd.DataFrame({
        "Plan": ["Basic", "Professional", "Enterprise"],
        "Annual Price": ["₹6 lakh", "₹15 lakh", "₹30 lakh"],
        "Planned Customers": [500, 300, 50],
        "Revenue": ["₹30 Cr", "₹45 Cr", "₹15 Cr"]
    })
    st.dataframe(plans, use_container_width=True, hide_index=True)

    st.subheader("Other Revenue Activities")
    st.write("""
    - Setup and integration: ₹8.5 crore through planned implementation services.
    - Consulting: ₹1.5 crore through additional workforce planning and advisory engagements.
    """)

    st.info("These figures represent proposed business assumptions and targets.")

# ---------------- WORKFORCE PLAN ----------------
elif page == "Workforce Plan":
    st.title("03 | Workforce Plan")
    st.write("Proposed workforce structure across 10 departments.")

    workforce = pd.DataFrame({
        "Department": [
            "Engineering & Product",
            "AI & Data Science",
            "Sales & Business Development",
            "Marketing",
            "Customer Success & Support",
            "Implementation & Consulting",
            "HR",
            "Finance & Legal",
            "Operations & Admin",
            "Leadership"
        ],
        "Employees": [55, 25, 35, 12, 35, 20, 6, 5, 5, 4]
    })

    st.metric("Total Planned Employees", "202")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Department-wise Workforce")
        st.dataframe(workforce, use_container_width=True, hide_index=True)
    with col2:
        st.subheader("Workforce Distribution")
        st.bar_chart(workforce.set_index("Department"))

    st.subheader("Role of HR")
    st.write("""
    The HR team consists of 6 planned employees. HR will coordinate
    recruitment, employee development, performance management,
    workforce planning and employee experience.
    """)

# ---------------- JOB ROLE ANALYSIS ----------------
elif page == "Job Role Analysis":
    st.title("04 | Job Role Analysis")
    st.subheader("Sales & Business Development Manager")

    st.write("""
    **Role Purpose:** To acquire suitable clients, build business
    relationships and grow recurring subscription revenue.
    """)

    st.subheader("Key Result Areas (KRA)")
    kra = [
        "Build and manage a qualified sales pipeline.",
        "Acquire new customers and develop business relationships.",
        "Negotiate subscription and service contracts.",
        "Coordinate with implementation teams during client handover."
    ]
    for item in kra:
        st.write("• " + item)

    st.subheader("Key Performance Indicators (KPI)")
    kpi = [
        "Qualified sales pipeline value",
        "Opportunity-to-win conversion rate",
        "New annual contract value",
        "Client renewal rate"
    ]
    for item in kpi:
        st.write("• " + item)

    st.subheader("Knowledge, Skills and Abilities (KSA)")

    col1, col2, col3 = st.columns(3)
    col1.markdown("### Knowledge")
    col1.write("Workforce planning, HR technology and SaaS business models.")
    col2.markdown("### Skills")
    col2.write("Consultative selling, negotiation and CRM.")
    col3.markdown("### Abilities")
    col3.write("Building trust, understanding client needs and coordinating delivery.")

    st.info("Specific KPI targets should be finalised after the role is staffed and baseline performance data is available.")

# ---------------- EMPLOYEE LIFECYCLE ----------------
elif page == "Employee Lifecycle":
    st.title("05 | Recruitment & Employee Lifecycle")

    st.subheader("Recruitment Process")

    stages = [
        ("1. Attract", "Employer branding, referrals and campus recruitment."),
        ("2. Screen", "CV screening using consistent role-based criteria."),
        ("3. Assess", "Role-based work samples and competency assessment."),
        ("4. Select", "Structured interviews, scorecards and reference checks."),
        ("5. Onboard", "Day-one access, buddy support and 30/60/90-day goals.")
    ]

    for title, description in stages:
        with st.expander(title):
            st.write(description)

    st.subheader("After Joining")

    lifecycle = pd.DataFrame({
        "Stage": ["Perform", "Develop", "Reward", "Engage", "Retain"],
        "HR Practice": [
            "Clear KPIs and regular feedback",
            "Learning paths and internal mobility",
            "Fair compensation and recognition",
            "Wellbeing and employee voice",
            "Career growth and manager support"
        ]
    })
    st.dataframe(lifecycle, use_container_width=True, hide_index=True)

    st.subheader("Responsibility")
    st.write("""
    - HR: People policies, recruitment systems and employee processes.
    - Managers: Selection, role clarity, coaching and feedback.
    - Leaders: Strategic direction, capability building and retention.
    """)

# ---------------- REFLECTION ----------------
elif page == "Reflection & Learning":
    st.title("06 | Reflection & Learning")

    st.subheader("My Key Learnings")
    st.write("""
    Through this project, I developed a better understanding of
    how HR strategy connects with business objectives.

    I learned that workforce planning is not only about deciding
    how many employees an organisation needs. It also involves
    identifying the right skills, designing suitable roles and
    ensuring that employees contribute to business performance.
    """)

    st.subheader("My Contribution")
    st.write("""
    My contribution focused on understanding the business model,
    developing the workforce structure, analysing the Sales &
    Business Development Manager role and designing recruitment
    and employee lifecycle practices.
    """)

    st.subheader("Key Takeaway")
    st.success("An effective HR strategy ensures that the organisation has the right people, with the right skills, at the right time.")

# ---------------- EVIDENCE ----------------
elif page == "Evidence":
    st.title("07 | Project Evidence")

    st.write("""
    This section is reserved for supporting documents and evidence
    related to the AS3 project.
    """)

    st.subheader("Evidence Checklist")
    st.write("- AS3 presentation")
    st.write("- Revenue model and calculations")
    st.write("- Workforce planning details")
    st.write("- Job role analysis")
    st.write("- Recruitment and employee lifecycle framework")

    st.warning("Add your actual assignment screenshots, presentation and supporting documents here before final submission.")

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("Meridian Workforce Intelligence | AS3 E-Portfolio | PGDM")
