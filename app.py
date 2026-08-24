import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="SecureView Pulse",
    page_icon="🛡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------
# Load Dataset
# -------------------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv(
        "dataset/final_security_logs.csv",
        parse_dates=["Timestamp"]
    )

df = load_data()
# ==========================================================
# PROFESSIONAL CYBERSECURITY CSS
# ==========================================================

st.markdown("""
<style>

/* ---------------- MAIN APP ---------------- */

.stApp{
    background-color:#0B1120;
}

/* Hide Streamlit Header & Footer */

header{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

/* ---------------- SIDEBAR ---------------- */

section[data-testid="stSidebar"]{
    background:#111827;
    border-right:1px solid #334155;
}

/* Sidebar text */

section[data-testid="stSidebar"] *{
    color:white !important;
}

/* ---------------- TITLES ---------------- */

.title{
    color:white;
    font-size:38px;
    font-weight:700;
}

.subtitle{
    color:#CBD5E1;
    font-size:17px;
}

/* ---------------- CARDS ---------------- */

.card{

    background:#1E293B;

    padding:18px;

    border-radius:15px;

    border:1px solid #334155;

    color:white;

}

/* KPI Cards */

.kpi-card{

    background:#1E293B;

    padding:20px;

    border-radius:16px;

    border:1px solid #334155;

    text-align:center;

    color:white;

}

/* ---------------- STATUS ---------------- */

.status-green{

    color:#22C55E;

    font-weight:bold;

}

.status-blue{

    color:#38BDF8;

    font-weight:bold;

}

.status-red{

    color:#EF4444;

    font-weight:bold;

}

.status-orange{

    color:#F59E0B;

    font-weight:bold;

}

/* ---------------- BUTTONS ---------------- */

.stButton>button{

    width:100%;

    height:44px;

    border-radius:12px;

    background:#1E293B;

    color:white;

    border:1px solid #334155;

    font-weight:600;

    transition:0.3s;

}

.stButton>button:hover{

    background:#2563EB;

    border:1px solid #38BDF8;

    color:white;

}

/* ---------------- TABLE ---------------- */

[data-testid="stDataFrame"]{

    border-radius:15px;

    overflow:hidden;

}
/* ==========================================================
   PROFESSIONAL NAVIGATION
   ========================================================== */

.nav-title {
    color: #94A3B8 !important;
    font-size: 12px !important;
    font-weight: 700 !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    margin-top: 18px !important;
    margin-bottom: 8px !important;
}

section[data-testid="stSidebar"] .stButton > button {
    background: transparent !important;
    color: #CBD5E1 !important;
    border: 1px solid transparent !important;
    text-align: left !important;
    padding: 10px 14px !important;
    margin: 3px 0 !important;
    border-radius: 10px !important;
    font-size: 15px !important;
    font-weight: 500 !important;
    height: 42px !important;
    transition: all 0.2s ease !important;
}

section[data-testid="stSidebar"] .stButton > button:hover {
    background: #1E293B !important;
    color: #FFFFFF !important;
    border: 1px solid #334155 !important;
}

.sidebar-brand {
    text-align: center;
    padding: 12px 5px 18px 5px;
}

.sidebar-brand h2 {
    color: #FFFFFF !important;
    font-size: 22px !important;
    margin: 0 !important;
}

.sidebar-brand p {
    color: #94A3B8 !important;
    font-size: 12px !important;
    margin-top: 5px !important;
}

.sidebar-status {
    background: #162033;
    border: 1px solid #26354A;
    border-radius: 10px;
    padding: 12px;
    margin-top: 18px;
}

.sidebar-status-title {
    color: #FFFFFF !important;
    font-weight: 600 !important;
    font-size: 14px !important;
}

.sidebar-status-value {
    color: #22C55E !important;
    font-size: 13px !important;
    font-weight: 600 !important;
}

</style>
""", unsafe_allow_html=True)
# ==========================================================
# SESSION STATE
# ==========================================================

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

# ==========================================================
# TOP HEADER
# ==========================================================

st.markdown("""
<div style="
background:#111827;
padding:15px 25px;
border-radius:15px;
border:1px solid #334155;
margin-bottom:20px;
">

<div style="
display:flex;
justify-content:space-between;
align-items:center;
">

<div>

<h2 style="
color:white;
margin-bottom:3px;
">
🛡 SecureView Pulse
</h2>

<p style="
color:#94A3B8;
margin-top:0px;
">
AI-Powered Cybersecurity Monitoring Platform
</p>

</div>

<div style="text-align:right;">

<p style="margin:0;color:#22C55E;font-weight:bold;">
🤖 AI Engine : ACTIVE
</p>

<p style="margin:0;color:#38BDF8;font-weight:bold;">
☁ Cloud : READY
</p>

</div>

</div>

</div>
""", unsafe_allow_html=True)

# ==========================================================
# TOP NAVIGATION
# ==========================================================

nav1,nav2,nav3,nav4=st.columns(4)

with nav1:
    if st.button("Dashboard",use_container_width=True):
        st.session_state.page="Dashboard"

with nav2:
    if st.button("Analytics",use_container_width=True):
        st.session_state.page="Analytics"

with nav3:
    if st.button("AI Summary",use_container_width=True):
        st.session_state.page="AI Summary"

with nav4:
    if st.button("Reports",use_container_width=True):
        st.session_state.page="Reports"

st.write("")

# ==========================================================
# MAIN LAYOUT
# ==========================================================

left,right=st.columns([1,4])

# ==========================================================
# LEFT SIDEBAR
# ==========================================================

with left:

    st.markdown("""
<div class="card">

<h4 style="color:white;">
Navigation
</h4>

</div>
""",unsafe_allow_html=True)

    st.write("")

    if st.button("🏠 Dashboard",use_container_width=True):
        st.session_state.page="Dashboard"

    if st.button("📊 Analytics",use_container_width=True):
        st.session_state.page="Analytics"

    if st.button("🛡 Threat Intelligence",use_container_width=True):
        st.session_state.page="Threat Intelligence"

    if st.button("🚨 Live Monitoring",use_container_width=True):
        st.session_state.page="Live Monitoring"

    if st.button("📋 Reports",use_container_width=True):
        st.session_state.page="Reports"

    if st.button("ℹ About",use_container_width=True):
        st.session_state.page="About"

    st.write("")

    st.markdown("""
<div class="card">

<h4 style="color:white;">
Search Events
</h4>

</div>
""",unsafe_allow_html=True)

    search=st.text_input(
        "",
        placeholder="Search Username / Threat..."
    )

# ==========================================================
# RIGHT PANEL
# ==========================================================

with right:

    page=st.session_state.page

# ==========================================================
# DASHBOARD PAGE
# ==========================================================

def dashboard_page():
    search = st.text_input(
    "🔎 Search Security Events",
    placeholder="Search username, IP, threat type, CVE, MITRE ID..."
)

if search:
    filtered_df = df[
        df.astype(str)
        .apply(
            lambda x: x.str.contains(
                search,
                case=False,
                na=False
            )
        )
        .any(axis=1)
    ]
else:
    filtered_df = df.copy()

    st.markdown("""
    <h2 style="color:white;">
    🏠 Dashboard
    </h2>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p style="color:#CBD5E1;">
    Real-Time Threat Monitoring & AI Security Analytics
    </p>
    """, unsafe_allow_html=True)

    st.write("")

    total_events = len(df)

    ai_threats = (df["Prediction"] == "Anomaly").sum()

    critical = (df["Threat_Priority"] == "Critical").sum()

    high = (df["Threat_Priority"] == "High").sum()

    avg_risk = round(df["Risk_Score"].mean(), 1)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(f"""
        <div class="kpi-card">
        <h2 style="color:#38BDF8;">{total_events}</h2>
        <p>Total Events</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="kpi-card">
        <h2 style="color:#EF4444;">{ai_threats}</h2>
        <p>AI Detected Threats</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="kpi-card">
        <h2 style="color:#F59E0B;">{critical}</h2>
        <p>Critical Threats</p>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown(f"""
        <div class="kpi-card">
        <h2 style="color:#22C55E;">{avg_risk}</h2>
        <p>Average Risk Score</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    c1, c2 = st.columns(2)
    
    # ==========================================================
    # THREAT PRIORITY DISTRIBUTION
    # ==========================================================

    with c1:

        priority = (
            df["Threat_Priority"]
            .value_counts()
            .reset_index()
        )

        priority.columns = ["Priority", "Count"]

        fig = px.pie(
            priority,
            names="Priority",
            values="Count",
            hole=0.55,
            title="Threat Priority Distribution"
        )

        fig.update_layout(
            paper_bgcolor="#1E293B",
            plot_bgcolor="#1E293B",
            font_color="white",
            legend_font_color="white",
            title_font_size=18
        )

        st.plotly_chart(fig, use_container_width=True)
        

    # ==========================================================
    # THREAT TYPE ANALYSIS
    # ==========================================================

    with c2:

        threat = (
            df["Threat_Type"]
            .value_counts()
            .reset_index()
        )

        threat.columns = ["Threat", "Count"]

        fig = px.bar(
            threat,
            x="Threat",
            y="Count",
            color="Threat",
            title="Threat Type Analysis"
        )

        fig.update_layout(
            paper_bgcolor="#1E293B",
            plot_bgcolor="#1E293B",
            font_color="white",
            showlegend=False,
            title_font_size=18
        )

        st.plotly_chart(fig, use_container_width=True)
     # ==========================================================
    # RISK SCORE TIMELINE
    # ==========================================================

    st.write("")

    timeline = df.sort_values("Timestamp")

    fig = px.line(
        timeline,
        x="Timestamp",
        y="Risk_Score",
        color="Prediction",
        title="Risk Score Timeline"
    )

    fig.update_layout(
        paper_bgcolor="#1E293B",
        plot_bgcolor="#1E293B",
        font_color="white",
        title_font_size=18
    )

    st.plotly_chart(fig, use_container_width=True)
    # ==========================================================
# RECENT ALERTS
# ==========================================================

st.subheader("🚨 Recent Alerts")

alerts = filtered_df.sort_values(
    "Timestamp",
    ascending=False
)

st.dataframe(
    alerts[
        [
            "Timestamp",
            "Threat_Type",
            "Threat_Priority",
            "Risk_Score",
            "Recommendation"
        ]
    ].head(10),
    use_container_width=True,
    hide_index=True
)
# ==========================================================
# AI SECURITY SUMMARY
# ==========================================================

st.write("")

left, right = st.columns([2, 1])

with left:

    total = len(filtered_df)

    anomalies = (
        filtered_df["Prediction"] == "Anomaly"
    ).sum()

    critical = (
        filtered_df["Threat_Priority"] == "Critical"
    ).sum()

    common_threat = (
        filtered_df["Threat_Type"].mode()[0]
        if not filtered_df.empty
        else "N/A"
    )

    avg_risk = round(
        filtered_df["Risk_Score"].mean(),
        1
    )

    st.markdown(f"""
    <div class="card">

    <h3 style="color:#38BDF8;">
    🤖 AI Threat Summary
    </h3>

    <hr>

    <p style="color:white;font-size:17px;">

    ✔ Total Events Analysed : <b>{total}</b><br><br>

    ✔ AI Detected Threats : <b>{anomalies}</b><br><br>

    ✔ Critical Threats : <b>{critical}</b><br><br>

    ✔ Most Common Threat : <b>{common_threat}</b><br><br>

    ✔ Average Risk Score : <b>{avg_risk}</b>

    </p>

    </div>
    """, unsafe_allow_html=True)


with right:

    st.markdown("""
    <div class="card">

    <h3 style="color:#22C55E;">
    🛡 AI Recommendation
    </h3>

    <hr>

    <p style="color:white;">

    • Investigate Critical Events

    <br><br>

    • Monitor High Risk Assets

    <br><br>

    • Review MITRE Mapping

    <br><br>

    • Validate IOC Indicators

    <br><br>

    • Apply Security Patches

    </p>

    </div>
    """, unsafe_allow_html=True)
    # ==========================================================
# MITRE & CVE
# ==========================================================

st.write("")

c1, c2 = st.columns(2)

with c1:

    mitre = (
        filtered_df["MITRE_ID"]
        .value_counts()
        .reset_index()
    )

    mitre.columns = ["MITRE", "Count"]

    fig = px.bar(
        mitre,
        x="MITRE",
        y="Count",
        title="MITRE ATT&CK Techniques"
    )

    fig.update_layout(
        paper_bgcolor="#1E293B",
        plot_bgcolor="#1E293B",
        font_color="white"
    )

    st.plotly_chart(fig, use_container_width=True)


with c2:

    cve = (
        filtered_df["CVE_ID"]
        .value_counts()
        .reset_index()
    )

    cve.columns = ["CVE", "Count"]

    fig = px.bar(
        cve,
        x="CVE",
        y="Count",
        title="CVE Intelligence"
    )

    fig.update_layout(
        paper_bgcolor="#1E293B",
        plot_bgcolor="#1E293B",
        font_color="white"
    )

    st.plotly_chart(fig, use_container_width=True)
    # ==========================================================
# IOC FEED
# ==========================================================

st.subheader("🦠 Indicators of Compromise")

st.dataframe(
    filtered_df[
        [
            "IOC",
            "Threat_Type",
            "Threat_Priority",
            "MITRE_ID",
            "CVE_ID"
        ]
    ].head(10),
    use_container_width=True,
    hide_index=True
)
# ==========================================================
# SECURITY EVENTS
# ==========================================================

st.subheader("📋 Security Events")

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)

# ==========================================================
# ANALYTICS PAGE
# ==========================================================

def analytics_page():

    st.markdown("""
    <h2 style='color:white;'>📊 Threat Analytics</h2>
    <p style='color:#CBD5E1;'>
    Advanced analysis of cybersecurity threats and AI predictions.
    </p>
    """, unsafe_allow_html=True)

    st.write("")

    col1, col2 = st.columns(2)

    # ----------------------------------------------------
    # Severity Distribution
    # ----------------------------------------------------

    with col1:

        severity = (
            df["Severity"]
            .value_counts()
            .reset_index()
        )

        severity.columns = ["Severity", "Count"]

        fig = px.bar(
            severity,
            x="Severity",
            y="Count",
            color="Severity",
            title="Severity Distribution"
        )

        fig.update_layout(
            paper_bgcolor="#1E293B",
            plot_bgcolor="#1E293B",
            font_color="white",
            showlegend=False
        )

        st.plotly_chart(fig, use_container_width=True)

    # ----------------------------------------------------
    # Protocol Distribution
    # ----------------------------------------------------

    with col2:

        protocol = (
            df["Protocol"]
            .value_counts()
            .reset_index()
        )

        protocol.columns = ["Protocol", "Count"]

        fig = px.pie(
            protocol,
            names="Protocol",
            values="Count",
            hole=0.55,
            title="Protocol Distribution"
        )

        fig.update_layout(
            paper_bgcolor="#1E293B",
            plot_bgcolor="#1E293B",
            font_color="white"
        )

        st.plotly_chart(fig, use_container_width=True)

    st.write("")

    # ----------------------------------------------------
    # Device OS Analysis
    # ----------------------------------------------------

    os_data = (
        df["Device_OS"]
        .value_counts()
        .reset_index()
    )

    os_data.columns = ["Device", "Count"]

    fig = px.bar(
        os_data,
        x="Device",
        y="Count",
        color="Device",
        title="Device Operating System Analysis"
    )

    fig.update_layout(
        paper_bgcolor="#1E293B",
        plot_bgcolor="#1E293B",
        font_color="white",
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)

    st.write("")

    # ----------------------------------------------------
    # Confidence Score Distribution
    # ----------------------------------------------------

    fig = px.histogram(
        df,
        x="Confidence_Score",
        nbins=20,
        title="AI Confidence Score Distribution"
    )

    fig.update_layout(
        paper_bgcolor="#1E293B",
        plot_bgcolor="#1E293B",
        font_color="white"
    )

    st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# AI SUMMARY PAGE
# ==========================================================

def ai_summary_page():

    st.markdown("""
    <h2 style='color:white;'>🤖 AI Security Summary</h2>
    <p style='color:#CBD5E1;'>
    Artificial Intelligence based Threat Detection and Risk Assessment
    </p>
    """, unsafe_allow_html=True)

    st.write("")

    total_events = len(df)
    anomalies = (df["Prediction"] == "Anomaly").sum()
    normal = (df["Prediction"] == "Normal").sum()
    critical = (df["Threat_Priority"] == "Critical").sum()
    high = (df["Threat_Priority"] == "High").sum()
    avg_risk = round(df["Risk_Score"].mean(), 2)
    avg_conf = round(df["Confidence_Score"].mean(), 2)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Total Events", total_events)

    with c2:
        st.metric("AI Threats Detected", anomalies)

    with c3:
        st.metric("Average Risk Score", avg_risk)

    st.write("")

    left, right = st.columns(2)

    # =====================================================
    # AI Prediction Distribution
    # =====================================================

    with left:

        prediction = (
            df["Prediction"]
            .value_counts()
            .reset_index()
        )

        prediction.columns = ["Prediction", "Count"]

        fig = px.pie(
            prediction,
            names="Prediction",
            values="Count",
            hole=0.55,
            title="AI Prediction Distribution"
        )

        fig.update_layout(
            paper_bgcolor="#1E293B",
            plot_bgcolor="#1E293B",
            font_color="white"
        )

        st.plotly_chart(fig, use_container_width=True)

    # =====================================================
    # Threat Priority
    # =====================================================

    with right:

        priority = (
            df["Threat_Priority"]
            .value_counts()
            .reset_index()
        )

        priority.columns = ["Priority", "Count"]

        fig = px.bar(
            priority,
            x="Priority",
            y="Count",
            color="Priority",
            title="Threat Priority Summary"
        )

        fig.update_layout(
            paper_bgcolor="#1E293B",
            plot_bgcolor="#1E293B",
            font_color="white",
            showlegend=False
        )

        st.plotly_chart(fig, use_container_width=True)

    st.write("")

    st.subheader("📋 AI Assessment Summary")

    st.success(f"""
✔ AI analysed **{total_events}** security events.

✔ **{anomalies}** events were classified as anomalies.

✔ Average Confidence Score : **{avg_conf}**

✔ Average Risk Score : **{avg_risk}**
""")

    st.warning(f"""
⚠ Critical Threats : **{critical}**

⚠ High Priority Threats : **{high}**

Immediate investigation is recommended for all Critical events.
""")

    st.info("""
### 🤖 AI Recommendations

• Continue real-time monitoring.

• Investigate Critical and High threats first.

• Monitor repeated IOC indicators.

• Review MITRE ATT&CK mappings.

• Apply available security patches for affected systems.

• Improve endpoint monitoring for suspicious activities.
""")

    st.subheader("📄 AI Detection Results")

    st.dataframe(

        df[
            [
                "Timestamp",
                "Prediction",
                "Confidence_Score",
                "Risk_Score",
                "Threat_Priority",
                "Recommendation"
            ]
        ],

        use_container_width=True,

        hide_index=True

    )

# ==========================================================
# THREAT INTELLIGENCE PAGE
# ==========================================================

def threat_intelligence_page():

    st.markdown("""
    <h2 style='color:white;'>🛡 Threat Intelligence</h2>
    <p style='color:#CBD5E1;'>
    Cyber Threat Intelligence, MITRE ATT&CK Framework and CVE Analysis
    </p>
    """, unsafe_allow_html=True)

    st.write("")

    left,right=st.columns(2)

    # ======================================================
    # MITRE ATT&CK
    # ======================================================

    with left:

        mitre=(
            df["MITRE_ID"]
            .value_counts()
            .reset_index()
        )

        mitre.columns=["MITRE","Count"]

        fig=px.bar(
            mitre,
            x="MITRE",
            y="Count",
            color="MITRE",
            title="MITRE ATT&CK Techniques"
        )

        fig.update_layout(
            paper_bgcolor="#1E293B",
            plot_bgcolor="#1E293B",
            font_color="white",
            showlegend=False
        )

        st.plotly_chart(fig,use_container_width=True)

    # ======================================================
    # CVE Distribution
    # ======================================================

    with right:

        cve=(
            df["CVE_ID"]
            .value_counts()
            .reset_index()
        )

        cve.columns=["CVE","Count"]

        fig=px.pie(
            cve,
            names="CVE",
            values="Count",
            hole=.55,
            title="CVE Intelligence"
        )

        fig.update_layout(
            paper_bgcolor="#1E293B",
            plot_bgcolor="#1E293B",
            font_color="white"
        )

        st.plotly_chart(fig,use_container_width=True)

    st.write("")

    st.subheader("🎯 Threat Intelligence Feed")

    st.dataframe(

        df[
            [
                "Threat_Type",
                "MITRE_ID",
                "CVE_ID",
                "IOC",
                "Recommendation"
            ]
        ],

        use_container_width=True,

        hide_index=True

    )

    st.write("")

    st.subheader("🧠 AI Threat Recommendations")

    st.success("""
✔ Monitor IOC activities continuously.

✔ Investigate Critical Threats immediately.

✔ Patch systems affected by known CVEs.

✔ Review MITRE ATT&CK mapped techniques.

✔ Strengthen endpoint monitoring.

✔ Enable continuous log collection.
""")

    st.warning("""
High-risk indicators should be escalated to the Security Operations Center (SOC) for further investigation.
""")

# ==========================================================
# LIVE MONITORING PAGE
# ==========================================================

def live_monitoring_page():

    st.markdown("""
    <h2 style='color:white;'>🚨 Live Monitoring</h2>
    <p style='color:#CBD5E1;'>
    Real-Time Security Monitoring and AI Threat Detection
    </p>
    """, unsafe_allow_html=True)

    st.write("")

    # ======================================================
    # LIVE STATUS CARDS
    # ======================================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.success("🟢 AI Engine\n\nActive")

    with c2:
        st.success("🟢 Threat Feed\n\nConnected")

    with c3:
        st.info("☁ Cloud\n\nAWS Ready")

    with c4:
        st.warning(f"🕒 Last Scan\n\n{df['Timestamp'].max()}")

    st.write("")

    # ======================================================
    # ACTIVE ALERTS
    # ======================================================

    st.subheader("🚨 Active Security Alerts")

    alerts = df.sort_values(
        "Risk_Score",
        ascending=False
    ).head(10)

    st.dataframe(
        alerts[
            [
                "Timestamp",
                "Threat_Type",
                "Threat_Priority",
                "Risk_Score",
                "Prediction",
                "Status"
            ]
        ],
        use_container_width=True,
        hide_index=True
    )

    st.write("")

    # ======================================================
    # LIVE RISK SCORE
    # ======================================================

    fig = px.line(
        df.sort_values("Timestamp"),
        x="Timestamp",
        y="Risk_Score",
        color="Prediction",
        title="Live Risk Score Monitoring"
    )

    fig.update_layout(
        paper_bgcolor="#1E293B",
        plot_bgcolor="#1E293B",
        font_color="white"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.write("")

    # ======================================================
    # MONITORING STATUS
    # ======================================================

    st.subheader("🛡 Monitoring Status")

    st.success("""
✔ AI Detection Engine Running

✔ Security Logs Connected

✔ Threat Intelligence Feed Active

✔ Continuous Risk Assessment Enabled

✔ Incident Monitoring Active
""")

# ==========================================================
# REPORTS PAGE
# ==========================================================

def reports_page():

    st.markdown("""
    <h2 style='color:white;'>📋 Security Reports</h2>
    <p style='color:#CBD5E1;'>
    Export and review cybersecurity monitoring reports
    </p>
    """, unsafe_allow_html=True)

    st.write("")

    total = len(df)
    anomalies = (df["Prediction"] == "Anomaly").sum()
    critical = (df["Threat_Priority"] == "Critical").sum()
    avg = round(df["Risk_Score"].mean(), 2)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Events", total)
    c2.metric("AI Threats", anomalies)
    c3.metric("Critical", critical)
    c4.metric("Average Risk", avg)

    st.write("")

    st.subheader("📄 Security Event Report")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "📥 Download Security Report",
        csv,
        file_name="Security_Report.csv",
        mime="text/csv"
    )

# ==========================================================
# ABOUT PAGE
# ==========================================================

def about_page():

    st.markdown("""
    <h2 style='color:white;'>ℹ About SecureView Pulse</h2>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("""
### 🛡 Project

SecureView Pulse is an AI-Assisted Threat Detection Dashboard developed to help cybersecurity analysts monitor, detect, and prioritize cyber threats using Machine Learning.

---

### 🤖 AI Model

Isolation Forest

---

### ⚙ Technologies

- Python
- Streamlit
- Plotly
- Pandas
- Scikit-learn

---

### 🛡 Security Frameworks

- MITRE ATT&CK
- CVE Intelligence
- IOC Analysis

---

### 📊 Features

- AI Threat Detection
- Risk Score Analysis
- Live Monitoring
- Threat Intelligence
- Analytics Dashboard
- Security Reports
""")
   # ==========================================================
# PAGE NAVIGATION
# ==========================================================

page = st.session_state.page

if page == "Dashboard":
    dashboard_page()

elif page == "Analytics":
    analytics_page()

elif page == "AI Summary":
    ai_summary_page()

elif page == "Threat Intelligence":
    threat_intelligence_page()

elif page == "Live Monitoring":
    live_monitoring_page()

elif page == "Reports":
    reports_page()

elif page == "About":
    about_page()