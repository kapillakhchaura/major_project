import streamlit as st

def landing_page():

    # =========================
    # NAVBAR
    # =========================
    st.markdown("""
    <style>

    /* 🔥 SCROLL CARD */
    .scroll-card {
        height:220px;
        overflow-y:auto;
        padding:18px;
        border-radius:16px;
        background: rgba(30, 41, 59, 0.6);
        border:1px solid rgba(148,163,184,0.2);
        backdrop-filter: blur(10px);
        transition: all 0.35s ease;
        position: relative;
    }

    /* 🔥 HOVER POPUP EFFECT */
    .scroll-card:hover {
        transform: translateY(-10px) scale(1.03);
        border:1px solid #8b5cf6;
        box-shadow:0 20px 40px rgba(139,92,246,0.5);
        background: rgba(30, 41, 59, 0.9);
    }

    /* 🔥 EXTRA GLOW BORDER */
    .scroll-card::before {
        content: "";
        position: absolute;
        inset: 0;
        border-radius:16px;
        opacity: 0;
        transition: 0.3s;
    }

    .scroll-card:hover::before {
        opacity: 1;
        box-shadow: inset 0 0 20px rgba(139,92,246,0.4);
    }

    /* 🔥 SCROLLBAR */
    .scroll-card::-webkit-scrollbar {
        width: 6px;
    }
    .scroll-card::-webkit-scrollbar-thumb {
        background: #6366f1;
        border-radius: 10px;
    }

    /* 🔥 TITLE COLORS */
    .card-title-blue { color:#60a5fa; }
    .card-title-purple { color:#a78bfa; }
    .card-title-green { color:#34d399; }

    /* 🔥 GOOGLE FONT */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
    }

    /* 🔥 BACKGROUND */
    body {
        background: linear-gradient(135deg, #020617, #0f172a, #1e293b);
    }

    /* 🔥 CONTAINER */
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 1rem !important;
    }

    /* 🔥 HERO */
    .hero-title {
        text-align:center;
        font-size:42px;
        font-weight:700;
        color:#f1f5f9;
    }

    .hero-sub1 {
        text-align:center;
        font-size:16px;
        color:#94a3b8;
    }

    /* 🔥 BUTTON */
    .stButton>button {
        background: linear-gradient(90deg,#6366f1,#8b5cf6);
        color:white;
        border-radius:12px;
        height:45px;
        font-size:16px;
        transition:0.3s;
    }

    .stButton>button:hover {
        transform: scale(1.05);
    }

    /* 🔥 FOOTER */
    .footer-box {
        background: linear-gradient(90deg,#16a34a,#15803d);
        padding:15px;
        border-radius:12px;
        text-align:center;
        color:white;
        font-weight:500;
    }

    </style>
    """, unsafe_allow_html=True)

   
    # =========================
    # HERO SECTION
    # =========================
    st.markdown("""
    <div class="hero-title">🧠 Smart Health Diagnosis System</div>
    <div class="hero-sub1">
    AI-powered system for disease detection, risk analysis & report generation
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([5,1])

    with col1:
        st.markdown("### 🩺 AI Doctor System")

    with col2:
        if st.button("🔐 Login / Signup"):
            st.session_state["show_auth"] = True
            st.rerun()
    

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="scroll-card">
        <h4 style="color:#60a5fa;">🧠 AI Prediction</h4>
        <p>Detect diseases instantly using advanced AI algorithms trained on medical datasets. 
        Our system analyzes symptoms, patient inputs, and clinical patterns to provide 
        accurate early-stage predictions for multiple diseases like Diabetes, Heart, and Kidney disorders.

        ✔ Fast AI-based diagnosis  
        ✔ Early risk detection  
        ✔ Supports multiple diseases  
        ✔ Improves preventive healthcare</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="scroll-card">
        <h4 style="color:#a78bfa;">📄 Smart Reports</h4>
        <p>Generate professional medical reports automatically with structured insights. 
        The system creates downloadable PDF reports including patient details, 
        risk scores, AI predictions, and medical recommendations.

        ✔ Instant PDF generation  
        ✔ Clean & professional format  
        ✔ Includes risk score & category  
        ✔ Easy to download & share with doctors</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="scroll-card">
        <h4 style="color:#34d399;">📊 Risk Analysis</h4>
        <p>Understand your health condition with intelligent risk scoring. 
        Our AI evaluates your data and categorizes it into Low, Moderate, 
        or High risk levels with visual indicators and insights.

        ✔ Accurate risk percentage  
        ✔ Visual dashboards & graphs  
        ✔ Personalized health insights  
        ✔ Helps in better decision making</p>
        </div>
        """, unsafe_allow_html=True)
    # st.markdown("<hr>", unsafe_allow_html=True)


   

    # st.markdown("<hr>", unsafe_allow_html=True)

    # =========================
    # FEATURES
    # =========================
    st.markdown("<h2>🚀 What This System Does</h2>", unsafe_allow_html=True)


    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="scroll-card">
        <h4 style="color:#60a5fa;">🧠 Early Disease Detection</h4>
        <p>Detect potential diseases at an early stage using advanced AI-driven analysis. 
        The system evaluates your symptoms, medical inputs, and health patterns to identify risks 
        before they become severe. This helps in timely medical intervention and better prevention.

        ✔ Identifies early warning signs  
        ✔ Reduces chances of late diagnosis  
        ✔ Helps in preventive healthcare  
        ✔ Supports multiple disease detection  </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="scroll-card">
        <h4 style="color:#a78bfa;">📊 Health Monitoring & Insights</h4>
        <p>Continuously monitor your health condition with intelligent tracking and data analysis. 
        The system provides detailed insights into your health trends and risk levels over time, 
        helping you understand your body better and make informed lifestyle decisions.

        ✔ Tracks health trends over time  
        ✔ Provides real-time insights  
        ✔ Personalized health analysis  
        ✔ Helps maintain long-term wellness  </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="scroll-card">
        <h4 style="color:#34d399;">📄 Smart Medical Reports</h4>
        <p>Generate comprehensive medical reports enriched with AI insights and structured data. 
        These reports include predictions, risk scores, and health summaries that can be easily 
        shared with doctors for better diagnosis and consultation.

        ✔ Detailed and structured reports  
        ✔ Includes prediction & risk score  
        ✔ Easy to download and share  
        ✔ Improves doctor consultation process  </p>
        </div>
        """, unsafe_allow_html=True)

    # st.markdown("<hr>", unsafe_allow_html=True)

    # =========================
    # HOW IT WORKS
    # =========================
    st.markdown("""
    <div style="
    background: linear-gradient(135deg,#020617,#0f172a);
    padding:25px;
    border-radius:15px;
    border:1px solid #374151;
    box-shadow:0 10px 30px rgba(0,0,0,0.6);
    ">

    <h2 style="
    font-size:28px;
    background: linear-gradient(90deg,#22c55e,#4ade80);
    -webkit-background-clip: text;
    color: transparent;
    margin-bottom:20px;
    text-align:center;
    ">
    ⚙️ How It Works
    </h2>

    <div style="display:flex;flex-wrap:wrap;gap:20px;">

    <!-- Step 1 -->
    <div class="scroll-card" style="flex:1;min-width:220px;">
    <h4 style="color:#60a5fa;">1️⃣ Input Data</h4>
    <p style="color:#9ca3af;">
    Enter your symptoms or medical values such as glucose, BP, or age.
    Provide accurate inputs for better AI analysis.
    </p>
    </div>

    <!-- Step 2 -->
    <div class="scroll-card" style="flex:1;min-width:220px;">
    <h4 style="color:#a78bfa;">2️⃣ AI Analysis</h4>
    <p style="color:#9ca3af;">
    Our AI model processes your input using trained machine learning algorithms 
    to detect hidden patterns and predict possible diseases.
    </p>
    </div>

    <!-- Step 3 -->
    <div class="scroll-card" style="flex:1;min-width:220px;">
    <h4 style="color:#f59e0b;">3️⃣ Risk Detection</h4>
    <p style="color:#9ca3af;">
    The system calculates a risk score and categorizes it into 
    Low, Moderate, or High risk levels with insights.
    </p>
    </div>

    <!-- Step 4 -->
    <div class="scroll-card" style="flex:1;min-width:220px;">
    <h4 style="color:#22c55e;">4️⃣ Report Generation</h4>
    <p style="color:#9ca3af;">
    Generate a professional medical report instantly with prediction results, 
    risk score, and recommendations.
    </p>
    </div>

    </div>

    </div>
    """, unsafe_allow_html=True)
    # =========================
    # ABOUT PROJECT
    # =========================
    # st.markdown("## 👨‍💻 About Project")

    
    st.markdown("""
    <div style="
    background: linear-gradient(135deg,#1f2937,#111827);
    padding:25px;
    border-radius:15px;
    border:1px solid #374151;
    box-shadow:0 10px 25px rgba(0,0,0,0.5);
    ">

    <h2 style="
    text-align:center;
    background: linear-gradient(90deg,#6366f1,#8b5cf6);
    -webkit-background-clip: text;
    color: transparent;
    margin-bottom:20px;
    ">
    👨‍💻 About This Project
    </h2>

    <div style="display:flex;gap:20px;flex-wrap:wrap;">

    <!-- Technology -->
    <div style="
    flex:1;
    min-width:250px;
    padding:18px;
    background:#111827;
    border-radius:12px;
    border:1px solid #374151;
    ">

    <h3 style="color:#34d399;">💡 Technology</h3>

    <p style="color:#9ca3af;">
    Built using modern technologies focused on AI and healthcare solutions.
    </p>

    <ul style="color:#9ca3af; margin-top:10px;">
    <li>Python & Streamlit for frontend</li>
    <li>Machine Learning models</li>
    <li>Healthcare datasets for training</li>
    <li>Real-time prediction system</li>
    </ul>

    </div>

    <!-- Developer -->
    <div style="
    flex:1;
    min-width:250px;
    padding:18px;
    background:#111827;
    border-radius:12px;
    border:1px solid #374151;
    ">

    <h3 style="color:#f59e0b;">👨‍🎓 Developer</h3>

    <p style="color:#9ca3af;">
    Developed as a Final Year Major Project with focus on AI in healthcare.
    </p>

    <ul style="color:#9ca3af; margin-top:10px;">
    <li>Developer: Kapil Lakhchaura</li>
    <li>Project Type: Final Year Major</li>
    <li>Domain: AI + Healthcare</li>
    <li>Goal: Early disease detection</li>
    </ul>

    </div>

    </div>

    </div>
    """, unsafe_allow_html=True)