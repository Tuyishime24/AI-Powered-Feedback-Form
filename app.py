import streamlit as st
from datetime import datetime

# -----------------------------
# GLOBAL CONFIG & THEME HELPERS
# -----------------------------

st.set_page_config(
    page_title="AI Powered Feedback Form",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Basic institution themes (logo text + colors + banner image description)
INSTITUTION_THEMES = {
    "Default": {
        "logo_text": "AI Powered Feedback Form",
        "primary_color": "#4E33E5",
        "accent_color": "#02D653",
        "banner_gradient": "linear-gradient(135deg, #1E88E5, #42A5F5)",
        "bg_tone": "#F5F7FB",
        "banner_image_desc": "Abstract AI and analytics background",
    },
    "University of Kigali": {
        "logo_text": "AI Powered Feedback Form",
    	"primary_color": "#003366",      # dark blue title / brand
    	"accent_color": "#02D653",
    	"banner_gradient": "linear-gradient(135deg, #d4f7d4, #b4e3b4)",  # light green banner
    	"bg_tone": "#4a4a4a",            # gray background
    	"banner_image_desc": "Abstract AI and analytics background",

    },
    "Kigali Teaching Hospital": {
        "logo_text": "AI Powered Feedback Form",
    	"primary_color": "#003366",      # dark blue title / brand
    	"accent_color": "#02D653",
    	"banner_gradient": "linear-gradient(135deg, #d4f7d4, #b4e3b4)",  # light green banner
    	"bg_tone": "#4a4a4a",            # gray background
    	"banner_image_desc": "Abstract AI and analytics background",
   },
    "Rwanda Tourism Board": {
        "logo_text": "AI Powered Feedback Form",
    	"primary_color": "#003366",      # dark blue title / brand
    	"accent_color": "#02D653",
    	"banner_gradient": "linear-gradient(135deg, #d4f7d4, #b4e3b4)",  # light green banner
    	"bg_tone": "#4a4a4a",            # gray background
    	"banner_image_desc": "Abstract AI and analytics background",
   },
}


def get_theme():
    inst = st.session_state.get("institution_name", "Default")
    if inst in INSTITUTION_THEMES:
        return INSTITUTION_THEMES[inst]
    return INSTITUTION_THEMES["Default"]


def inject_base_styles():
    theme = get_theme()
    primary = theme["primary_color"]
    accent = theme["accent_color"]
    bg = theme["bg_tone"]

    st.markdown(
        f"""
        <style>
        body {{
            background-color: {bg} !important;   /* gray */
            color: #E8F5E9;                      /* default text white */
        }}
        .main {{
            background-color: {bg};
            color: #ffffff;
        }}

        .top-nav {{
    	    display: flex;
    	    align-items: center;
    	    justify-content: space-between;
    	    padding: 0.6rem 1rem 0.4rem 1rem;
            background-color: #00897b;      /* teal/green professional */
    	    border-bottom: 1px solid #00695c;
    	    position: sticky;
    	    top: 0;
    	    z-index: 999;
        }}
        .top-nav-left {{
            display: flex;
            align-items: center;
            gap: 0.6rem;
        }}
        .logo-badge {{
            width: 38px;
            height: 38px;
            border-radius: 10px;
            background: {primary};
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: 700;
            font-size: 18px;
        }}
        .logo-text-main {{
            font-size: 20px;
            font-weight: 700;
            color: #ffffff;
        }}
        .logo-text-sub {{
            font-size: 11px;
            font-weight: 400;
            color: #e0e0e0;
            margin-top: -2px;
        }}
        .top-nav-right {{
            display: flex;
            align-items: center;
            gap: 0.8rem;
            font-size: 13px;
            color: #ffffff;
        }}
        .nav-link {{
            padding: 0.3rem 0.7rem;
            border-radius: 999px;
            cursor: pointer;
            color: #ffffff;
            text-decoration: none;
        }}
        .nav-link-active {{
            background-color: {primary}33;
            color: #ffffff;
            font-weight: 600;
        }}
        .nav-button-primary {{
            padding: 0.3rem 0.9rem;
            border-radius: 999px;
            background-color: {primary};
            color: white;
            font-weight: 600;
            font-size: 13px;
            text-decoration: none;
        }}
        .nav-button-outline {{
            padding: 0.3rem 0.9rem;
            border-radius: 999px;
            border: 1px solid {primary};
            color: #ffffff;
            font-weight: 600;
            font-size: 13px;
            text-decoration: none;
        }}

        .hero-banner {{
            border-radius: 20px;
            padding: 2.5rem 2.5rem 2rem 2.5rem;
            background: {theme["banner_gradient"]};  /* light green */
            color: #ffffff;
            position: relative;
            overflow: hidden;
        }}
        .hero-title {{
            font-size: 34px;
            font-weight: 800;
            margin-bottom: 0.4rem;
            color: #003366;                     /* dark blue title */
        }}
        .hero-subtitle {{
            font-size: 16px;
            max-width: 640px;
            opacity: 0.95;
            color: #ffffff;
        }}
        .hero-pill {{
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            background: #ffffff20;
            border-radius: 999px;
            padding: 0.2rem 0.75rem;
            font-size: 11px;
            margin-bottom: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: #ffffff;
        }}
        .hero-cta-container {{
            margin-top: 1.4rem;
            display: flex;
            flex-wrap: wrap;
            gap: 0.7rem;
        }}
        .hero-cta {{
            border-radius: 999px;
            padding: 0.55rem 1.1rem;
            font-size: 13px;
            border: none;
            cursor: pointer;
        }}
        .hero-cta-primary {{
            background-color: #FFFFFF;
            color: {primary};
            font-weight: 700;
        }}
        .hero-cta-secondary {{
            background-color: #ffffff10;
            color: #FFFFFF;
            font-weight: 600;
            border: 1px solid #ffffff40;
        }}
        .hero-cta-tertiary {{
            background-color: #ffffff00;
            color: #FFFFFF;
            font-weight: 500;
            border: 1px dashed #ffffff60;
        }}
        .hero-badge-metrics {{
            position: absolute;
            top: 1.5rem;
            right: 2.5rem;
            background: #00000020;
            padding: 0.8rem 1rem;
            border-radius: 14px;
            backdrop-filter: blur(12px);
            font-size: 11px;
            color: #ffffff;
        }}

        .metric-label {{
            text-transform: uppercase;
            font-size: 10px;
            opacity: 0.8;
            color: #ffffff;
        }}
        .metric-value {{
            font-size: 16px;
            font-weight: 700;
            color: #ffffff;
        }}

        .section-title {{
            font-size: 20px;
            font-weight: 700;
            margin-bottom: 0.2rem;
            color: #ffffff;
        }}
        .section-subtitle {{
            font-size: 13px;
            color: #f0f0f0;
            margin-bottom: 0.7rem;
        }}

        .card-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
            gap: 0.9rem;
        }}
        .info-card {{
            background-color: #5a5a5a;
            border-radius: 14px;
            padding: 0.9rem 0.9rem 0.85rem 0.9rem;
            box-shadow: 0 2px 6px rgba(15, 23, 42, 0.25);
            border: 1px solid #707070;
            color: #ffffff;
        }}
        .info-card-title {{
            font-size: 14px;
            font-weight: 700;
            margin-bottom: 0.1rem;
            color: #ffffff;
        }}
        .info-card-tag {{
            font-size: 11px;
            text-transform: uppercase;
            color: {accent};
            margin-bottom: 0.15rem;
        }}
        .info-card-body {{
            font-size: 12px;
            color: #f5f5f5;
        }}

        .pill-tab-bar {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.4rem;
            margin-bottom: 0.5rem;
        }}
        .pill-tab {{
            padding: 0.25rem 0.7rem;
            border-radius: 999px;
            background-color: #606060;
            font-size: 11px;
            cursor: pointer;
            color: #ffffff;
        }}
        .pill-tab-active {{
            background-color: {primary};
            color: #FFFFFF;
            font-weight: 600;
        }}

        .accent-badge {{
            display: inline-flex;
            align-items: center;
            padding: 0.18rem 0.6rem;
            border-radius: 999px;
            background-color: {accent}33;
            color: {accent};
            font-size: 10px;
            text-transform: uppercase;
            letter-spacing: 0.06em;
        }}

        .subsection-header {{
            font-size: 14px;
            font-weight: 600;
            margin-top: 0.1rem;
            margin-bottom: 0.15rem;
            color: #ffffff;
        }}
        .subsection-text {{
            font-size: 12px;
            color: #f0f0f0;
        }}

        .kpi-card {{
            background-color: #5a5a5a;
            border-radius: 14px;
            padding: 0.9rem;
            border: 1px solid #707070;
            color: #ffffff;
        }}
        .kpi-label {{
            font-size: 11px;
            text-transform: uppercase;
            color: #e0e0e0;
        }}
        .kpi-value {{
            font-size: 20px;
            font-weight: 800;
            color: #ffffff;
        }}
        .kpi-sub {{
            font-size: 11px;
            color: #00C853;
        }}

        .soft-panel {{
            background-color: #5a5a5a;
            border-radius: 18px;
            padding: 1.1rem 1rem;
            border: 1px solid #707070;
            box-shadow: 0 1px 4px rgba(15, 23, 42, 0.3);
            color: #ffffff;
        }}
        .soft-panel-title {{
            font-size: 15px;
            font-weight: 700;
            margin-bottom: 0.25rem;
            color: #ffffff;
        }}
        .soft-panel-text {{
            font-size: 12px;
            color: #f0f0f0;
        }}
        .soft-chip {{
            display: inline-flex;
            align-items: center;
            border-radius: 999px;
            padding: 0.2rem 0.55rem;
            font-size: 11px;
            background-color: #606060;
            color: #ffffff;
            margin-right: 0.3rem;
            margin-bottom: 0.2rem;
        }}
        .soft-chip-positive {{
            background-color: #E8F5E9;
            color: #2E7D32;
        }}
        .soft-chip-negative {{
            background-color: #FFEBEE;
            color: #C62828;
        }}
        .soft-chip-neutral {{
            background-color: #E3F2FD;
            color: #1565C0;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


# -----------------------------
# SESSION STATE (AUTH & ROUTING)
# -----------------------------

if "is_logged_in" not in st.session_state:
    st.session_state.is_logged_in = False

if "institution_name" not in st.session_state:
    st.session_state.institution_name = "Default"

if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

if "about_tab" not in st.session_state:
    st.session_state.about_tab = "Overview"

if "create_form_tab" not in st.session_state:
    st.session_state.create_form_tab = "Get Started"

if "my_forms_tab" not in st.session_state:
    st.session_state.my_forms_tab = "View Created Forms"

if "key_findings_tab" not in st.session_state:
    st.session_state.key_findings_tab = "Key Strengths"

if "dashboard_tab" not in st.session_state:
    st.session_state.dashboard_tab = "Overview Summary"

if "reports_tab" not in st.session_state:
    st.session_state.reports_tab = "Select Feedback Form"

if "share_tab" not in st.session_state:
    st.session_state.share_tab = "Select Form"


def go(page_name: str):
    st.session_state.current_page = page_name


# -----------------------------
# TOP NAVIGATION BAR
# -----------------------------

def render_top_nav():
    inject_base_styles()
    theme = get_theme()
    logo_text = theme["logo_text"]

    nav_items = [
        ("Home", "home"),
        ("About", "about"),
        ("Dashboard", "dashboard"),
        ("Create Form", "create_form"),
        ("My Forms", "my_forms"),
        ("Key Findings", "key_findings"),
        ("Reports", "reports"),
        ("Share", "share"),
        ("Settings", "settings"),
    ]

    st.markdown('<div class="top-nav">', unsafe_allow_html=True)

    # Left side (Logo)
    st.markdown('<div class="top-nav-left">', unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="logo-badge">AI</div>
        <div>
            <div class="logo-text-main">{logo_text}</div>
            <div class="logo-text-sub">AI-powered institutional feedback</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # Right side (navigation)
    st.markdown('<div class="top-nav-right">', unsafe_allow_html=True)
    cols = st.columns(len(nav_items) + 2)
    for idx, (label, page_key) in enumerate(nav_items):
        active_class = (
            "nav-link nav-link-active"
            if st.session_state.current_page == page_key
            else "nav-link"
        )
        if cols[idx].button(label, key=f"topnav_{page_key}"):
            go(page_key)
        cols[idx].markdown(
            f'<span class="{active_class}" ></span>', unsafe_allow_html=True
        )

    # Login / Logout
    if not st.session_state.is_logged_in:
        if cols[-2].button("Login"):
            go("login")
        if cols[-1].button("Sign up"):
            go("signup")
    else:
        cols[-2].markdown(
            f'<span style="font-size:12px;color:#607D8B;">{st.session_state.institution_name}</span>',
            unsafe_allow_html=True,
        )
        if cols[-1].button("Logout"):
            st.session_state.is_logged_in = False
            st.session_state.institution_name = "Default"
            go("home")

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.write("")  # slight spacing


# -----------------------------
# PAGE: HOME (LANDING)
# -----------------------------

def page_home():
    theme = get_theme()

    st.markdown(
        f"""
        <div class="hero-banner">
            <div class="hero-badge-metrics">
                <div class="metric-label">Live snapshot</div>
                <div class="metric-value">4.3 / 5</div>
                <div style="font-size:11px;color:#C8E6C9;">▲ +0.6 vs last term</div>
                <div style="margin-top:0.4rem;font-size:11px;">
                    Response rate: <b>72%</b> • Active forms: <b>12</b>
                </div>
            </div>
            <div class="hero-pill">
                <span>AI-Powered Feedback System</span>
                <span style="opacity:0.8;">Institutions • Analytics • Insight</span>
            </div>
            <div class="hero-title">Transform feedback into actionable insights</div>
            <div class="hero-subtitle">
                Collect, analyze, and interpret institutional feedback using AI — turning opinions into smart, data-driven decisions for universities, hospitals, public agencies, and more.
            </div>
            <div class="hero-cta-container">
                <button class="hero-cta hero-cta-primary" onclick="window.scrollTo(0, document.body.scrollHeight);">
                    🔵 Get Started
                </button>
                <button class="hero-cta hero-cta-secondary">
                    🟢 Create Feedback Form
                </button>
                <button class="hero-cta hero-cta-tertiary">
                    🟠 View Dashboard
                </button>
            </div>
            <div style="position:absolute;bottom:1.1rem;right:2.4rem;font-size:11px;opacity:0.85;">
                Background: {theme["banner_image_desc"]}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    st.markdown('<div class="section-title">Why institutions trust this platform</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">AI elevates feedback from raw scores to clear, human-readable insight that leaders can act on immediately.</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="card-grid">', unsafe_allow_html=True)
    cols = st.columns(3)
    with cols[0]:
        st.markdown(
            """
            <div class="info-card">
                <div class="info-card-tag">AI-designed forms</div>
                <div class="info-card-title">Professional forms in minutes</div>
                <div class="info-card-body">
                    Describe what you want to evaluate and automatically generate clean, well-structured feedback forms tailored to your institution.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with cols[1]:
        st.markdown(
            """
            <div class="info-card">
                <div class="info-card-tag">Instant interpretation</div>
                <div class="info-card-title">Beyond percentages and averages</div>
                <div class="info-card-body">
                    Move from raw numbers to clear strengths, gaps, and priorities using AI-powered analysis that explains what the feedback actually means.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with cols[2]:
        st.markdown(
            """
            <div class="info-card">
                <div class="info-card-tag">Executive-ready reports</div>
                <div class="info-card-title">Reporting without manual work</div>
                <div class="info-card-body">
                    Generate polished dashboards and narrative reports that can be shared with leadership in a single click.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")
    st.markdown('<div class="section-title">Institutional snapshot</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">A quick overview of current performance across active feedback initiatives.</div>',
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            """
            <div class="kpi-card">
                <div class="kpi-label">Overall satisfaction</div>
                <div class="kpi-value">4.3 / 5</div>
                <div class="kpi-sub">▲ +0.6 vs last term</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class="kpi-card">
                <div class="kpi-label">Response rate</div>
                <div class="kpi-value">72%</div>
                <div class="kpi-sub">▲ Above institutional target</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            """
            <div class="kpi-card">
                <div class="kpi-label">Active feedback forms</div>
                <div class="kpi-value">12</div>
                <div class="kpi-sub">● On track this cycle</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# -----------------------------
# PAGE: ABOUT
# -----------------------------

ABOUT_TABS = [
    "Overview",
    "Purpose",
    "Problem Addressed",
    "AI-Based Approach",
    "Key Components",
    "Application Areas",
    "Expected Benefits",
    "Data Privacy & Ethics",
    "Vision",
]


def render_pill_tabs(current_key: str, options, state_field: str):
    st.markdown('<div class="pill-tab-bar">', unsafe_allow_html=True)
    cols = st.columns(len(options))
    for idx, opt in enumerate(options):
        cls = "pill-tab pill-tab-active" if opt == current_key else "pill-tab"
        if cols[idx].button(opt, key=f"{state_field}_{opt}"):
            st.session_state[state_field] = opt
        cols[idx].markdown(f'<span class="{cls}"></span>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


def page_about():
    theme = get_theme()
    st.markdown(
        f"""
        <div class="hero-banner" style="margin-bottom:1.2rem;background:{theme["banner_gradient"]};">
            <div class="hero-pill">
                <span>📘 About the AI-Powered Feedback System</span>
            </div>
            <div class="hero-title">Understand the story behind the system</div>
            <div class="hero-subtitle">
                An intelligent, AI-enabled platform that transforms traditional surveys into meaningful insight for institutional improvement and accountability.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="accent-badge">Explore by topic</div>', unsafe_allow_html=True)
    render_pill_tabs(
        st.session_state.about_tab,
        ABOUT_TABS,
        "about_tab",
    )

    st.markdown('<div class="soft-panel">', unsafe_allow_html=True)
    tab = st.session_state.about_tab

    if tab == "Overview":
        st.markdown(
            """
            <div class="soft-panel-title">Overview</div>
            <div class="soft-panel-text">
                The AI-Powered Feedback System for Institutions is a digital platform designed to help organizations collect, analyze, and interpret feedback in a smarter and more meaningful way.
                By integrating artificial intelligence, it goes beyond traditional surveys and converts raw responses into actionable insights that support informed decision-making.
            </div>
            """,
            unsafe_allow_html=True,
        )
    elif tab == "Purpose":
        st.markdown(
            """
            <div class="soft-panel-title">Purpose of the system</div>
            <div class="soft-panel-text">
                The main purpose is to address the limitations of tools that only present numeric scores without interpretation.
                This system provides meaningful explanation of feedback data, supports institutional improvement through AI-driven insights, reduces manual analysis effort, and enables data-driven planning and accountability.
            </div>
            """,
            unsafe_allow_html=True,
        )
    elif tab == "Problem Addressed":
        st.markdown(
            """
            <div class="soft-panel-title">Problem addressed</div>
            <div class="soft-panel-text">
                Many institutions rely on survey tools that show only numbers or averages, lack contextual interpretation, and do not generate recommendations.
                Manual analysis of large volumes of feedback is time-consuming and error-prone, making it difficult for decision-makers to identify clear actions.
            </div>
            """,
            unsafe_allow_html=True,
        )
    elif tab == "AI-Based Approach":
        st.markdown(
            """
            <div class="soft-panel-title">Our AI-based approach</div>
            <div class="soft-panel-text">
                The system uses AI to analyze both quantitative and qualitative feedback, detect patterns and trends, and identify strengths and weaknesses.
                It generates clear, human-readable recommendations and displays insights through interactive dashboards and reports so feedback is collected, understood, and acted upon.
            </div>
            """,
            unsafe_allow_html=True,
        )
    elif tab == "Key Components":
        st.markdown(
            """
            <div class="soft-panel-title">Key components of the system</div>
            <div class="soft-panel-text">
                <span class="subsection-header">AI-Assisted Form Generation</span><br/>
                Automatically creates professional feedback forms based on user-defined objectives.<br/><br/>
                <span class="subsection-header">Automated Feedback Analysis</span><br/>
                Interprets responses with AI models to extract meaningful insights.<br/><br/>
                <span class="subsection-header">Recommendation Engine</span><br/>
                Provides actionable improvement suggestions tailored to each institution.<br/><br/>
                <span class="subsection-header">Dashboard & Visualization</span><br/>
                Displays real-time analytics, trends, and performance indicators.<br/><br/>
                <span class="subsection-header">Reporting Module</span><br/>
                Generates customized, downloadable reports ready for decision-making.
            </div>
            """,
            unsafe_allow_html=True,
        )
    elif tab == "Application Areas":
        st.markdown(
            """
            <div class="soft-panel-title">Application areas</div>
            <div class="soft-panel-text">
                The platform is adaptable across multiple sectors, including government institutions, educational organizations, healthcare facilities, private sector companies, non-governmental organizations, and tourism or hospitality institutions.
            </div>
            """,
            unsafe_allow_html=True,
        )
    elif tab == "Expected Benefits":
        st.markdown(
            """
            <div class="soft-panel-title">Expected benefits</div>
            <div class="soft-panel-text">
                Institutions benefit from improved service quality and stakeholder satisfaction, faster and more accurate feedback interpretation, and enhanced transparency.
                The system promotes better planning, evidence-based decisions, and continuous improvement driven by AI-generated insights.
            </div>
            """,
            unsafe_allow_html=True,
        )
    elif tab == "Data Privacy & Ethics":
        st.markdown(
            """
            <div class="soft-panel-title">Data privacy & ethics</div>
            <div class="soft-panel-text">
                The system is designed with data privacy and responsible AI principles in mind, ensuring feedback is handled securely with a focus on improvement rather than individual identification.
                Anonymity and confidentiality are preserved to encourage honest, high-quality responses.
            </div>
            """,
            unsafe_allow_html=True,
        )
    elif tab == "Vision":
        st.markdown(
            """
            <div class="soft-panel-title">Vision</div>
            <div class="soft-panel-text">
                The vision is to empower institutions with intelligent tools that transform feedback into meaningful action.
                The platform aims to drive continuous improvement and sustainable development through responsible and impactful use of AI.
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------
# PAGE: LOGIN / SIGNUP
# -----------------------------

def page_login():
    st.markdown(
        """
        <div class="section-title">Welcome back</div>
        <div class="section-subtitle">Sign in to access your institution’s AI-powered feedback workspace.</div>
        """,
        unsafe_allow_html=True,
    )
    with st.form("login_form"):
        email = st.text_input("Institutional email")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")
        if submitted:
            if email and password:
                st.session_state.is_logged_in = True
                # preserve institution if set via signup; otherwise default
                if "institution_name" not in st.session_state or not st.session_state.institution_name:
                    st.session_state.institution_name = "Default"
                st.success("Logged in successfully.")
                go("home")
            else:
                st.error("Please enter both email and password.")


def page_signup():
    st.markdown(
        """
        <div class="section-title">Create institutional workspace</div>
        <div class="section-subtitle">Register your institution to begin collecting, analyzing, and reporting feedback with AI.</div>
        """,
        unsafe_allow_html=True,
    )
    with st.form("signup_form"):
        inst_name = st.text_input("Institution name")
        sector = st.selectbox(
            "Sector",
            [
                "Education",
                "Healthcare",
                "Government",
                "Private sector",
                "NGO",
                "Tourism and hospitality",
                "Other",
            ],
        )
        email = st.text_input("Administrator email")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Sign up")
        if submitted:
            if inst_name and email and password:
                st.session_state.is_logged_in = True
                st.session_state.institution_name = inst_name
                st.success("Institution workspace created and logged in.")
                go("home")
            else:
                st.error("Please complete all required fields.")


# -----------------------------
# PAGE: CREATE FORM
# -----------------------------

CREATE_FORM_TABS = [
    "Enter Institution Details",
    "Use AI to Generate Form",
    "Customize the Form",
    "Save and Publish",
    "Get Started",
]


def page_create_form():
    st.markdown(
        """
        <div class="section-title">Create AI-powered feedback form</div>
        <div class="section-subtitle">
            Design and generate professional feedback forms quickly and easily using AI. 
            This page allows institutions to create customized forms that collect meaningful feedback aligned with their goals.
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_pill_tabs(
        st.session_state.create_form_tab,
        CREATE_FORM_TABS,
        "create_form_tab",
    )

    tab = st.session_state.create_form_tab

    if tab == "Enter Institution Details":
        st.markdown(
            """
            <div class="soft-panel">
                <div class="soft-panel-title">Enter institution details</div>
                <div class="soft-panel-text">
                    Provide basic information such as institution name, sector, and department so the system can tailor the feedback form appropriately.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("")
        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Institution name", value=st.session_state.institution_name)
            st.selectbox(
                "Sector",
                [
                    "Education",
                    "Healthcare",
                    "Government",
                    "Private sector",
                    "NGO",
                    "Tourism and hospitality",
                ],
            )
        with col2:
            st.text_input("Department or unit")
            st.text_input("Country / City", value="Kigali, Rwanda")
        st.text_area("Brief description of feedback context")

    elif tab == "Use AI to Generate Form":
        st.markdown(
            """
            <div class="soft-panel">
                <div class="soft-panel-title">Use AI to generate the form</div>
                <div class="soft-panel-text">
                    Enter a short prompt explaining what you want to evaluate. The system will automatically generate clear, relevant, and professional feedback questions.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        prompt = st.text_area("Describe what you want to evaluate", height=100)
        if st.button("Generate form with AI"):
            st.info("AI has generated a professional feedback form structure (placeholder).")

    elif tab == "Customize the Form":
        st.markdown(
            """
            <div class="soft-panel">
                <div class="soft-panel-title">Customize the form</div>
                <div class="soft-panel-text">
                    Edit generated questions, choose question types, and organize sections to match your institutional needs.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("")
        st.text_input("Form title", value="Course Evaluation – Semester 1")
        st.text_area("Introduction / instructions to respondents", height=80)
        st.multiselect(
            "Question types to include",
            ["Rating scale", "Multiple choice", "Short text", "Long text", "Matrix questions"],
            default=["Rating scale", "Short text"],
        )
        st.text_area("Sample questions", value="1. How satisfied are you with...\n2. What should be improved...")

    elif tab == "Save and Publish":
        st.markdown(
            """
            <div class="soft-panel">
                <div class="soft-panel-title">Save and publish</div>
                <div class="soft-panel-text">
                    Once satisfied, save the form and share it with your target audience for feedback collection.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("")
        col1, col2 = st.columns(2)
        with col1:
            st.checkbox("Mark form as active", value=True)
            st.date_input("Feedback collection start date", value=datetime.today())
        with col2:
            st.date_input("Feedback collection end date")
            st.text_input("Target audience (e.g. students, patients, staff)")

        if st.button("Save form"):
            st.success("Form saved successfully (demo).")
        if st.button("Save and publish"):
            st.success("Form saved and marked as published (demo).")

    elif tab == "Get Started":
        st.markdown(
            """
            <div class="soft-panel">
                <div class="soft-panel-title">Get started</div>
                <div class="soft-panel-text">
                    Start by entering your feedback objective and let AI create a smart, well-structured form for you. 
                    Use the steps below to generate, preview, and save your form.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("")
        st.text_input("Feedback objective", placeholder="Example: Evaluate teaching quality in first-year courses")
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Create Form (AI)"):
                st.info("AI is generating your form (demo).")
        with col2:
            if st.button("Preview"):
                st.info("Showing a preview of the generated form (demo).")
        with col3:
            if st.button("Save"):
                st.success("Generated form saved (demo).")


# -----------------------------
# PAGE: MY FORMS
# -----------------------------

MY_FORMS_TABS = [
    "View Created Forms",
    "Edit Forms",
    "Share Forms",
    "Track Responses",
    "Analyze Feedback",
    "Archive & Manage",
]


def page_my_forms():
    st.markdown(
        """
        <div class="section-title">My Forms</div>
        <div class="section-subtitle">
            View, manage, and organize all feedback forms you have created. 
            From here, you can edit forms, monitor responses, and access analysis results easily.
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_pill_tabs(
        st.session_state.my_forms_tab,
        MY_FORMS_TABS,
        "my_forms_tab",
    )

    tab = st.session_state.my_forms_tab

    st.markdown('<div class="soft-panel">', unsafe_allow_html=True)

    if tab == "View Created Forms":
        st.markdown(
            """
            <div class="soft-panel-title">View created forms</div>
            <div class="soft-panel-text">
                See a list of all feedback forms you have created, including titles, status, and creation dates.
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("")
        st.table(
            {
                "Form title": ["Course Evaluation – Year 1", "Patient Satisfaction Survey", "Staff Engagement Pulse"],
                "Status": ["Active", "Closed", "Draft"],
                "Created on": ["2025-03-10", "2025-02-20", "2025-04-01"],
            }
        )

    elif tab == "Edit Forms":
        st.markdown(
            """
            <div class="soft-panel-title">Edit forms</div>
            <div class="soft-panel-text">
                Update questions, sections, or form details before or after publishing, depending on your institution’s policies.
            </div>
            """,
            unsafe_allow_html=True,
        )
        form_selected = st.selectbox(
            "Select a form to edit",
            [
                "Course Evaluation – Year 1",
                "Patient Satisfaction Survey",
                "Staff Engagement Pulse",
            ],
        )
        st.text_area(f"Edit form: {form_selected}", height=120)

    elif tab == "Share Forms":
        st.markdown(
            """
            <div class="soft-panel-title">Share forms</div>
            <div class="soft-panel-text">
                Generate shareable links to distribute forms to students, patients, clients, staff, or other respondents.
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.selectbox("Select a form to share", ["Course Evaluation – Year 1", "Patient Satisfaction Survey"])
        st.text_input("Shareable link", value="https://example.com/feedback/12345")
        st.button("Copy link")

    elif tab == "Track Responses":
        st.markdown(
            """
            <div class="soft-panel-title">Track responses</div>
            <div class="soft-panel-text">
                View the number of responses collected for each form in real time.
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.table(
            {
                "Form title": ["Course Evaluation – Year 1", "Patient Satisfaction Survey"],
                "Responses": [128, 64],
                "Last response": ["2025-03-30", "2025-03-27"],
            }
        )

    elif tab == "Analyze Feedback":
        st.markdown(
            """
            <div class="soft-panel-title">Analyze feedback</div>
            <div class="soft-panel-text">
                Access AI-powered analysis showing strengths, weaknesses, and recommendations based on collected feedback.
            </div>
            """,
            unsafe_allow_html=True,
        )
        form_selected = st.selectbox("Select a form", ["Course Evaluation – Year 1", "Patient Satisfaction Survey"])
        st.info(f"AI analysis summary for {form_selected} (demo placeholder).")

    elif tab == "Archive & Manage":
        st.markdown(
            """
            <div class="soft-panel-title">Archive and manage forms</div>
            <div class="soft-panel-text">
                Organize legacy or completed forms by archiving them while keeping results accessible for reporting and trend analysis.
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.checkbox("Show archived forms")
        st.text_area("Notes on archiving policies", height=80)

    st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------
# PAGE: KEY FINDINGS
# -----------------------------

KEY_FINDINGS_TABS = [
    "Key Strengths",
    "Key Challenges / Weaknesses",
    "Major Trends",
    "AI Insights",
    "Decision Suggestions",
    "Summary",
]


def page_key_findings():
    st.markdown(
        """
        <div class="section-title">Key Findings</div>
        <div class="section-subtitle">
            High-level insights that summarize what feedback is saying about your institution’s performance, strengths, and improvement needs.
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_pill_tabs(
        st.session_state.key_findings_tab,
        KEY_FINDINGS_TABS,
        "key_findings_tab",
    )
    tab = st.session_state.key_findings_tab

    st.markdown('<div class="soft-panel">', unsafe_allow_html=True)

    if tab == "Key Strengths":
        st.markdown(
            """
            <div class="soft-panel-title">Key strengths</div>
            <div class="soft-panel-text">
                Areas where the institution is performing well based on feedback trends and positive responses.
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("")
        st.markdown(
            """
            <span class="soft-chip soft-chip-positive">High satisfaction with teaching quality</span>
            <span class="soft-chip soft-chip-positive">Strong patient care and communication</span>
            <span class="soft-chip soft-chip-positive">Responsive support services</span>
            """,
            unsafe_allow_html=True,
        )

    elif tab == "Key Challenges / Weaknesses":
        st.markdown(
            """
            <div class="soft-panel-title">Key challenges and weaknesses</div>
            <div class="soft-panel-text">
                Recurring issues or concerns that require focused attention or improvement.
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("")
        st.markdown(
            """
            <span class="soft-chip soft-chip-negative">Delays in administrative processes</span>
            <span class="soft-chip soft-chip-negative">Limited feedback channels for staff</span>
            <span class="soft-chip soft-chip-negative">Inconsistent communication on changes</span>
            """,
            unsafe_allow_html=True,
        )

    elif tab == "Major Trends":
        st.markdown(
            """
            <div class="soft-panel-title">Major trends</div>
            <div class="soft-panel-text">
                Common patterns across responses, such as satisfaction levels, service quality, and engagement.
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("")
        st.markdown(
            """
            <span class="soft-chip soft-chip-neutral">Upward trend in overall satisfaction</span>
            <span class="soft-chip soft-chip-neutral">Stable engagement rates</span>
            <span class="soft-chip soft-chip-neutral">Improvement requests for digital services</span>
            """,
            unsafe_allow_html=True,
        )

    elif tab == "AI Insights":
        st.markdown(
            """
            <div class="soft-panel-title">AI insights</div>
            <div class="soft-panel-text">
                Automatically generated interpretations that explain what the feedback means in simple, clear language.
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("")
        st.info("AI observation: Satisfaction is strong in core services, but communication and timeliness remain critical priorities (demo).")

    elif tab == "Decision Suggestions":
        st.markdown(
            """
            <div class="soft-panel-title">Decision suggestions</div>
            <div class="soft-panel-text">
                AI-supported suggestions that help leaders decide where to focus resources and interventions.
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("")
        st.markdown(
            """
            - Prioritize improving communication on timelines and service changes.  
            - Introduce regular check-ins with key stakeholders to validate improvements.  
            - Invest in digital channels to reduce administrative delays.
            """,
            unsafe_allow_html=True,
        )

    elif tab == "Summary":
        st.markdown(
            """
            <div class="soft-panel-title">Key findings summary</div>
            <div class="soft-panel-text">
                The Key Findings section transforms raw feedback data into clear, meaningful insights that help institutions understand their performance and plan effective actions.
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("")
        st.markdown(
            """
            <span class="soft-chip soft-chip-positive">Overall sentiment: Generally positive</span>
            <span class="soft-chip soft-chip-negative">Priority area: Communication and processes</span>
            <span class="soft-chip soft-chip-neutral">Next step: Implement and track interventions</span>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------
# PAGE: DASHBOARD
# -----------------------------

DASHBOARD_TABS = [
    "Overview Summary",
    "Feedback Analytics",
    "Overall Satisfaction Visual",
    "Response Distribution Chart",
    "Trends Over Time",
    "Strengths vs Weaknesses",
    "Text Feedback Insights",
    "AI Insights Panel",
    "Actionable Recommendations",
]


def page_dashboard():
    st.markdown(
        """
        <div class="section-title">Dashboard</div>
        <div class="section-subtitle">
            A real-time overview of feedback performance and AI-generated insights, helping institutions monitor responses and support data-driven decisions.
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_pill_tabs(
        st.session_state.dashboard_tab,
        DASHBOARD_TABS,
        "dashboard_tab",
    )
    tab = st.session_state.dashboard_tab

    if tab == "Overview Summary":
        st.markdown(
            """
            <div class="section-title">KPI summary cards</div>
            <div class="section-subtitle">A quick snapshot of feedback activities across your institution.</div>
            """,
            unsafe_allow_html=True,
        )
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown(
                """
                <div class="kpi-card">
                    <div class="kpi-label">Overall satisfaction</div>
                    <div class="kpi-value">4.3</div>
                    <div class="kpi-sub">▲ +0.6 vs last term</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with c2:
            st.markdown(
                """
                <div class="kpi-card">
                    <div class="kpi-label">Response rate</div>
                    <div class="kpi-value">72%</div>
                    <div class="kpi-sub">▲ Above target</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with c3:
            st.markdown(
                """
                <div class="kpi-card">
                    <div class="kpi-label">Active forms</div>
                    <div class="kpi-value">12</div>
                    <div class="kpi-sub">● On track</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with c4:
            st.markdown(
                """
                <div class="kpi-card">
                    <div class="kpi-label">Open issues</div>
                    <div class="kpi-value">5</div>
                    <div class="kpi-sub">⚠ Requires follow-up</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    elif tab == "Feedback Analytics":
        st.markdown(
            """
            <div class="section-title">Feedback analytics</div>
            <div class="section-subtitle">
                High-level distribution of responses across satisfaction levels and key dimensions.
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.info("Analytics charts placeholder – integrate with real charts in production.")

    elif tab == "Overall Satisfaction Visual":
        st.markdown(
            """
            <div class="section-title">Overall satisfaction visual</div>
            <div class="section-subtitle">
                Visual representation of overall satisfaction scores across forms.
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.info("Satisfaction bar/pie chart placeholder – integrate with visualization library.")

    elif tab == "Response Distribution Chart":
        st.markdown(
            """
            <div class="section-title">Response distribution</div>
            <div class="section-subtitle">
                Distribution of responses across rating scales and question groups.
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.info("Response distribution chart placeholder.")

    elif tab == "Trends Over Time":
        st.markdown(
            """
            <div class="section-title">Trends over time</div>
            <div class="section-subtitle">
                Time-based trends in satisfaction, response rate, and engagement.
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.info("Line chart placeholder for time-series trends.")

    elif tab == "Strengths vs Weaknesses":
        st.markdown(
            """
            <div class="section-title">Strengths vs weaknesses</div>
            <div class="section-subtitle">
                Side-by-side visual comparison of areas performing well and areas needing improvement.
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.info("Side-by-side bar chart placeholder.")

    elif tab == "Text Feedback Insights":
        st.markdown(
            """
            <div class="section-title">Text feedback insights</div>
            <div class="section-subtitle">
                Visualized summaries of qualitative comments such as themes or sentiment.
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.info("Word cloud or sentiment distribution placeholder.")

    elif tab == "AI Insights Panel":
        st.markdown(
            """
            <div class="section-title">AI insights panel</div>
            <div class="section-subtitle">
                Smart box summarizing key AI observations for leadership.
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.info("AI highlight: Service experience is strong, but communication timeliness requires urgent attention (demo).")

    elif tab == "Actionable Recommendations":
        st.markdown(
            """
            <div class="section-title">Actionable recommendations</div>
            <div class="section-subtitle">
                Prioritized list of actions indicating what to do and which issues are urgent.
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            - Urgent: Reduce queue times and administrative delays in key departments.  
            - High priority: Improve communication of service changes and timelines.  
            - Medium priority: Expand digital self-service options to reduce manual requests.
            """,
            unsafe_allow_html=True,
        )


# -----------------------------
# PAGE: REPORTS
# -----------------------------

REPORTS_TABS = [
    "Select Feedback Form",
    "Select Date Range / Filters",
    "Generate AI Report",
    "View & Download Report",
]


def page_reports():
    st.markdown(
        """
        <div class="section-title">Reports</div>
        <div class="section-subtitle">
            Generate clear, professional reports from collected feedback to support decision-making and accountability.
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_pill_tabs(
        st.session_state.reports_tab,
        REPORTS_TABS,
        "reports_tab",
    )
    tab = st.session_state.reports_tab

    st.markdown('<div class="soft-panel">', unsafe_allow_html=True)

    if tab == "Select Feedback Form":
        st.markdown(
            """
            <div class="soft-panel-title">Select feedback form</div>
            <div class="soft-panel-text">
                Choose the form you want to generate the report for.
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.selectbox("Feedback form", ["Course Evaluation – Year 1", "Patient Satisfaction Survey"])

    elif tab == "Select Date Range / Filters":
        st.markdown(
            """
            <div class="soft-panel-title">Select date range and filters</div>
            <div class="soft-panel-text">
                Narrow down the data by department, service, or time period to create focused reports.
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.date_input("From")
        st.date_input("To")
        st.text_input("Department / service filter")
        st.text_input("Additional filter (optional)")

    elif tab == "Generate AI Report":
        st.markdown(
            """
            <div class="soft-panel-title">Generate AI report</div>
            <div class="soft-panel-text">
                The system automatically analyzes responses and prepares a structured, narrative report.
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Generate report"):
            st.success("AI report generated (demo).")

    elif tab == "View & Download Report":
        st.markdown(
            """
            <div class="soft-panel-title">View and download report</div>
            <div class="soft-panel-text">
                Access the fully formatted report and export it as PDF, Excel, or shareable link.
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.info("Report preview placeholder (executive summary, key findings, and detailed sections).")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.button("Download PDF")
        with col2:
            st.button("Download Excel")
        with col3:
            st.button("Copy shareable link")

    st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------
# PAGE: SHARE
# -----------------------------

SHARE_TABS = [
    "Select Form",
    "Share Options",
    "Access Settings",
]


def page_share():
    st.markdown(
        """
        <div class="section-title">Share feedback forms</div>
        <div class="section-subtitle">
            Distribute forms through links, QR codes, or email, with flexible access settings.
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_pill_tabs(
        st.session_state.share_tab,
        SHARE_TABS,
        "share_tab",
    )
    tab = st.session_state.share_tab

    st.markdown('<div class="soft-panel">', unsafe_allow_html=True)

    if tab == "Select Form":
        st.markdown(
            """
            <div class="soft-panel-title">Select feedback form</div>
            <div class="soft-panel-text">
                Choose which feedback form you want to share.
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.selectbox("Feedback form", ["Course Evaluation – Year 1", "Patient Satisfaction Survey"])

    elif tab == "Share Options":
        st.markdown(
            """
            <div class="soft-panel-title">Share options</div>
            <div class="soft-panel-text">
                Share via direct link, QR code, or email for convenient access.
            </div>
            """,
            unsafe_allow_html=True,
        )
        link = st.text_input("Shareable link", value="https://example.com/feedback/12345")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.button("🔗 Copy link")
        with col2:
            st.button("📱 Generate QR code")
        with col3:
            st.text_input("Email addresses (comma-separated)")
            st.button("✉ Send via email")

    elif tab == "Access Settings":
        st.markdown(
            """
            <div class="soft-panel-title">Access settings</div>
            <div class="soft-panel-text">
                Define who can access the form and how responses are collected.
            </div>
            """,
            unsafe_allow_html=True,
        )
        access_mode = st.radio("Access mode", ["Open (anyone with the link)", "Restricted (only invited users)"])
        if access_mode == "Restricted (only invited users)":
            st.text_input("Authorized domains or user list")
        st.checkbox("Allow anonymous responses", value=True)
        st.checkbox("Prevent multiple submissions from same user", value=False)

    st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------
# PAGE: SETTINGS
# -----------------------------

def page_settings():
    st.markdown(
        """
        <div class="section-title">Settings</div>
        <div class="section-subtitle">
            Configure institution theme, search, and general preferences.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.text_input("Search", placeholder="Search institution, forms, or reports")

    st.markdown("### Institution theme")
    inst = st.selectbox("Select institution", list(INSTITUTION_THEMES.keys()), index=0)
    if st.button("Apply theme"):
        st.session_state.institution_name = inst
        st.success("Institution theme updated.")


# -----------------------------
# ROUTER
# -----------------------------

render_top_nav()

page = st.session_state.current_page

if page == "home":
    page_home()
elif page == "about":
    page_about()
elif page == "create_form":
    page_create_form()
elif page == "my_forms":
    page_my_forms()
elif page == "key_findings":
    page_key_findings()
elif page == "dashboard":
    page_dashboard()
elif page == "reports":
    page_reports()
elif page == "share":
    page_share()
elif page == "settings":
    page_settings()
elif page == "login":
    page_login()
elif page == "signup":
    page_signup()
else:
    page_home()
