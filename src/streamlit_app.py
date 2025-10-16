import streamlit as st
import pandas as pd
import numpy as np
import requests
import json
import os
import sys
from datetime import datetime
from pathlib import Path

# Error handling and logging setup
def handle_error(error, context="Application"):
    """Centralized error handling function"""
    error_msg = f"{context}: {str(error)}"
    st.error(f"⚠️ {error_msg}")
    return None

def safe_load_image(image_path, caption="", width=None):
    """Safely load images with comprehensive error handling for Hugging Face Spaces"""
    try:
        # Check multiple possible paths for Hugging Face Spaces
        possible_paths = [
            image_path,
            image_path.replace("src/assets/", "assets/"),
            image_path.replace("src/assets/", "/app/assets/"),
            image_path.replace("src/assets/", "./assets/"),
            os.path.join(os.getcwd(), image_path)
        ]
        
        working_path = None
        for path in possible_paths:
            if os.path.exists(path):
                working_path = path
                break
        
        if not working_path:
            # Don't show error in HF Spaces, just skip
            return False
            
        if width and isinstance(width, int):
            st.image(working_path, caption=caption, width=width)
        else:
            st.image(working_path, caption=caption, width="stretch")
        return True
        
    except Exception as e:
        # Silently handle errors in Hugging Face Spaces
        return False

# Verify required directories exist (silently for HF Spaces)
try:
    assets_dirs = ["src/assets", "assets", "./assets", "/app/assets"]
    assets_found = any(Path(d).exists() for d in assets_dirs)
    # Don't show errors in Hugging Face Spaces deployment
except Exception as e:
    # Silently handle directory check errors
    pass

# Page configuration with Hugging Face Spaces compatibility
try:
    st.set_page_config(
        page_title="Bhumika Patel | Software Developer & Data Analyst",
        page_icon="👩‍💻",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
except Exception as e:
    # Silently handle config errors in Hugging Face Spaces
    pass

# Safe Lottie animation loader
def load_lottie_url(url: str):
    """Safely load Lottie animation with comprehensive error handling"""
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            return r.json()
        else:
            return None
    except requests.RequestException as e:
        handle_error(e, "Lottie Animation Loading")
        return None
    except json.JSONDecodeError as e:
        handle_error(e, "Lottie JSON Parsing")
        return None
    except Exception as e:
        handle_error(e, "Lottie Animation")
        return None

# Advanced fallback animation
fallback_animation = {
    "v": "5.5.9",
    "fr": 60,
    "ip": 0,
    "op": 120,
    "w": 500,
    "h": 500,
    "nm": "Code Animation",
    "ddd": 0,
    "assets": [],
    "layers": [{
        "ddd": 0,
        "ind": 1,
        "ty": 4,
        "nm": "Shape",
        "sr": 1,
        "ks": {
            "o": {"a": 0, "k": 100},
            "r": {"a": 1, "k": [
                {"i": {"x": [0.833], "y": [0.833]}, "o": {"x": [0.167], "y": [0.167]}, "t": 0, "s": [0]},
                {"t": 120, "s": [360]}
            ]},
            "p": {"a": 0, "k": [250, 250, 0]},
            "a": {"a": 0, "k": [0, 0, 0]},
            "s": {"a": 1, "k": [
                {"i": {"x": [0.833, 0.833, 0.833], "y": [0.833, 0.833, 0.833]}, "o": {"x": [0.167, 0.167, 0.167], "y": [0.167, 0.167, 0.167]}, "t": 0, "s": [100, 100, 100]},
                {"i": {"x": [0.833, 0.833, 0.833], "y": [0.833, 0.833, 0.833]}, "o": {"x": [0.167, 0.167, 0.167], "y": [0.167, 0.167, 0.167]}, "t": 60, "s": [120, 120, 100]},
                {"t": 120, "s": [100, 100, 100]}
            ]}
        },
        "ao": 0,
        "shapes": [{
            "ty": "gr",
            "it": [
                {"ty": "rc", "p": {"a": 0, "k": [0, 0]}, "s": {"a": 0, "k": [100, 100]}, "r": {"a": 0, "k": 20}},
                {"ty": "st", "c": {"a": 0, "k": [0.4, 0.9, 1, 1]}, "o": {"a": 0, "k": 100}, "w": {"a": 0, "k": 6}},
                {"ty": "fl", "c": {"a": 0, "k": [0.1, 0.2, 0.4, 0.8]}, "o": {"a": 0, "k": 80}},
                {"ty": "tr", "p": {"a": 0, "k": [0, 0]}, "a": {"a": 0, "k": [0, 0]}, "s": {"a": 0, "k": [100, 100]}, "r": {"a": 0, "k": 0}, "o": {"a": 0, "k": 100}}
            ]
        }],
        "ip": 0,
        "op": 120,
        "st": 0,
        "bm": 0
    }]
}

# Ultra-Modern CSS with Advanced Animations
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap');
    
    * {
        font-family: 'Space Grotesk', sans-serif;
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    /* Advanced Animated Mesh Background */
    .main {
        background: #0a0a0f;
        position: relative;
        overflow-x: hidden;
    }
    
    .main::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: 
            radial-gradient(circle at 20% 50%, rgba(120, 119, 198, 0.2) 0%, transparent 50%),
            radial-gradient(circle at 80% 80%, rgba(138, 43, 226, 0.2) 0%, transparent 50%),
            radial-gradient(circle at 40% 20%, rgba(0, 191, 255, 0.1) 0%, transparent 50%);
        pointer-events: none;
        z-index: 0;
    }
    
    /* Static Grid Lines */
    .grid-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            linear-gradient(rgba(100, 255, 218, 0.02) 1px, transparent 1px),
            linear-gradient(90deg, rgba(100, 255, 218, 0.02) 1px, transparent 1px);
        background-size: 50px 50px;
        pointer-events: none;
        z-index: 0;
    }
    
    /* Name Loading Animation - Stable */
    @keyframes nameReveal {
        0% {
            opacity: 0;
            transform: translateY(20px);
        }
        100% {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Holographic Text Effect - Smooth Gradient */
    .holographic-text {
        background: linear-gradient(45deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        background-size: 200% 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        filter: drop-shadow(0 0 10px rgba(102, 126, 234, 0.3));
        animation: smoothGradient 6s ease-in-out infinite;
    }
    
    @keyframes smoothGradient {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    /* Cyber Hero Header - Stable */
    .cyber-hero {
        font-size: clamp(3rem, 8vw, 6rem);
        font-weight: 800;
        text-align: center;
        margin: 0;
        position: relative;
        animation: nameReveal 1s ease-out forwards;
        opacity: 0;
    }
    
    /* Neon Subtitle - Gentle Glow */
    .neon-subtitle {
        font-size: clamp(1.2rem, 3vw, 2rem);
        text-align: center;
        color: #64ffda;
        text-shadow: 0 0 10px rgba(100, 255, 218, 0.5);
        font-family: 'JetBrains Mono', monospace;
        letter-spacing: 0.1em;
        animation: gentleGlow 4s ease-in-out infinite;
    }
    
    @keyframes gentleGlow {
        0%, 100% { text-shadow: 0 0 10px rgba(100, 255, 218, 0.5); }
        50% { text-shadow: 0 0 20px rgba(100, 255, 218, 0.7), 0 0 30px rgba(100, 255, 218, 0.3); }
    }
    
    /* 3D Section Headers - Static */
    .section-3d {
        font-size: clamp(2rem, 5vw, 3.5rem);
        font-weight: 800;
        margin: 60px 0 40px 0;
        position: relative;
        display: inline-block;
    }
    
    .section-3d::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 10%;
        width: 80%;
        height: 4px;
        background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
        border-radius: 2px;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    /* Glassmorphic Cards with 3D Transform */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(20px) saturate(180%);
        border-radius: 20px;
        padding: 35px;
        margin: 25px 0;
        border: 1px solid rgba(255, 255, 255, 0.08);
        box-shadow: 
            0 8px 32px 0 rgba(31, 38, 135, 0.37),
            inset 0 1px 0 0 rgba(255, 255, 255, 0.1);
        transition: all 0.5s cubic-bezier(0.23, 1, 0.320, 1);
        position: relative;
        overflow: hidden;
        transform-style: preserve-3d;
    }
    
    .glass-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, 
            transparent 30%, 
            rgba(100, 255, 218, 0.1) 50%, 
            transparent 70%);
        transform: rotate(45deg);
        transition: 0.6s;
    }
    
    .glass-card:hover {
        transform: translateY(-8px) scale(1.01);
        border-color: rgba(100, 255, 218, 0.4);
        box-shadow: 
            0 15px 40px rgba(100, 255, 218, 0.2),
            0 0 30px rgba(102, 126, 234, 0.15),
            inset 0 1px 0 0 rgba(255, 255, 255, 0.15);
        transition: all 0.4s cubic-bezier(0.23, 1, 0.320, 1);
    }
    
    .glass-card:hover::before {
        left: 150%;
    }
    
    /* Magnetic Hover Effect for Project Cards */
    .project-magnetic {
        background: rgba(255, 255, 255, 0.04);
        backdrop-filter: blur(15px);
        border-radius: 25px;
        padding: 40px;
        margin: 30px 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.4s cubic-bezier(0.23, 1, 0.320, 1);
        position: relative;
        overflow: hidden;
        cursor: pointer;
    }
    
    .project-magnetic::after {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(102, 126, 234, 0.2) 0%, transparent 70%);
        transform: translate(-50%, -50%);
        transition: width 0.6s, height 0.6s;
    }
    
    .project-magnetic:hover::after {
        width: 500px;
        height: 500px;
    }
    
    .project-magnetic {
        animation: gentleFloat 8s ease-in-out infinite;
    }
    
    .project-magnetic:hover {
        transform: translateY(-12px) scale(1.02);
        border-color: rgba(102, 126, 234, 0.5);
        box-shadow: 
            0 20px 50px rgba(102, 126, 234, 0.25),
            0 0 40px rgba(138, 43, 226, 0.2);
        transition: all 0.4s cubic-bezier(0.23, 1, 0.320, 1);
    }
    
    @keyframes gentleFloat {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-5px); }
    }
    
    /* Animated Tech Tags */
    .tech-bubble {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.8), rgba(118, 75, 162, 0.8));
        color: white;
        padding: 8px 18px;
        border-radius: 25px;
        font-size: 0.85rem;
        margin: 6px 6px 6px 0;
        display: inline-block;
        font-weight: 600;
        position: relative;
        overflow: hidden;
        transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    .tech-bubble::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        background: rgba(255, 255, 255, 0.3);
        border-radius: 50%;
        transform: translate(-50%, -50%);
        transition: width 0.4s, height 0.4s;
    }
    
    .tech-bubble:hover {
        transform: translateY(-5px) scale(1.15);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.5);
    }
    
    .tech-bubble:hover::before {
        width: 200px;
        height: 200px;
    }
    
    /* Skill Progress - Smooth Gradient */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #667eea, #764ba2, #f093fb) !important;
        background-size: 200% 100%;
        box-shadow: 0 2px 10px rgba(102, 126, 234, 0.3);
        animation: smoothProgress 4s ease-in-out infinite;
    }
    
    @keyframes smoothProgress {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    /* Contact Cards with Lift Effect */
    .contact-lift {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 35px;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
    }
    
    .contact-lift::before {
        content: '';
        position: absolute;
        inset: 0;
        border-radius: 20px;
        padding: 2px;
        background: linear-gradient(45deg, #667eea, #764ba2, #f093fb);
        -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
        -webkit-mask-composite: xor;
        mask-composite: exclude;
        opacity: 0;
        transition: opacity 0.4s;
    }
    
    .contact-lift:hover {
        transform: translateY(-15px) scale(1.05);
        box-shadow: 0 20px 50px rgba(100, 255, 218, 0.3);
    }
    
    .contact-lift:hover::before {
        opacity: 1;
    }
    
    /* Experience Timeline Effect */
    .timeline-card {
        background: rgba(255, 255, 255, 0.04);
        backdrop-filter: blur(12px);
        border-radius: 20px;
        padding: 30px;
        margin: 20px 0;
        border-left: 4px solid #64ffda;
        transition: all 0.4s ease;
        position: relative;
    }
    
    .timeline-card::before {
        content: '';
        position: absolute;
        left: -12px;
        top: 50%;
        transform: translateY(-50%);
        width: 20px;
        height: 20px;
        background: #64ffda;
        border-radius: 50%;
        box-shadow: 0 0 15px rgba(100, 255, 218, 0.5);
    }
    
    .timeline-card:hover {
        transform: translateX(15px);
        border-left-width: 6px;
        box-shadow: 0 10px 40px rgba(100, 255, 218, 0.2);
    }
    
    /* Smooth Separator */
    .cyber-divider {
        height: 2px;
        background: linear-gradient(90deg, 
            transparent 0%, 
            rgba(100, 255, 218, 0.3) 25%, 
            rgba(102, 126, 234, 0.6) 50%, 
            rgba(100, 255, 218, 0.3) 75%, 
            transparent 100%);
        margin: 50px 0;
        position: relative;
        background-size: 300% 100%;
        animation: smoothDivider 8s ease-in-out infinite;
    }
    
    @keyframes smoothDivider {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #667eea, #764ba2);
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(102, 126, 234, 0.5);
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #764ba2, #f093fb);
    }
    
    /* Text Reveal Animation */
    .reveal-text {
        animation: revealUp 1s ease-out forwards;
        opacity: 0;
    }
    
    @keyframes revealUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Gentle Icon Glow */
    .icon-glow {
        margin-top: 40px;
        transition: all 0.3s ease;
        display: inline-block;
        animation: iconBreath 6s ease-in-out infinite;
    }
    
    .icon-glow:hover {
        filter: drop-shadow(0 0 20px rgba(100, 255, 218, 0.6));
        transform: scale(1.15);
        animation-play-state: paused;
    }
    
    @keyframes iconBreath {
        0%, 100% { 
            filter: drop-shadow(0 0 5px rgba(100, 255, 218, 0.3));
            transform: scale(1);
        }
        50% { 
            filter: drop-shadow(0 0 10px rgba(100, 255, 218, 0.5));
            transform: scale(1.05);
        }
    }
    
    /* Hide Streamlit header and footer */
    .stApp > header {
        display: none;
    }
    
    #MainMenu {
        display: none;
    }
    
    footer {
        display: none;
    }
    
    .stApp > footer {
        display: none;
    }
</style>

<div class="grid-overlay"></div>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    .main, .stApp {
        background-color: #0A0A0A;
    }
    # h1, h2, h3 {
    #     color: #00D4FF;
    #     border-left: 4px solid #00D4FF;
    #     padding-left: 10px;
    # }
    p, div {
        color: #E0E0E0;
    }
    </style>
    """, unsafe_allow_html=True)

# Hero Section with Animated Name
st.markdown('''
    <h1 class="cyber-hero" data-text="BHUMIKA PATEL">
        <span style="color: #fff;">BHUMIKA</span> 
        <span class="holographic-text">PATEL</span>
    </h1>
''', unsafe_allow_html=True)

st.markdown('<p class="neon-subtitle">Software Developer | Data Analyst | Problem Solver</p>', unsafe_allow_html=True)

st.markdown("""
<div class="reveal-text" style="text-align: center; margin: 40px 0; max-width: 700px; margin-left: auto; margin-right: auto;">
    <p style="font-size: 1.3rem; color: #ccd6f6; line-height: 1.8; font-weight: 300;">
    A dedicated software developer specializing in <span style="color: #64ffda; font-weight: 600;">data-driven solutions</span> and 
    <span style="color: #667eea; font-weight: 600;">innovative applications</span>. Passionate about leveraging technology to solve 
    complex problems and create impactful solutions that drive business growth and user engagement.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Cyber Divider
# Professional Photo Section
st.markdown('<div class="cyber-divider"></div>', unsafe_allow_html=True)

# Horizontal layout for photo and intro
photo_col1, photo_col2 = st.columns([1, 2], gap="large")

with photo_col1:
    st.markdown("""
    <style>
    .photo-frame-static {
        padding: 6px;
        background: linear-gradient(45deg, #667eea, #764ba2, #f093fb);
        border-radius: 15px;
        display: inline-block;
        box-shadow: 0 8px 25px rgba(100, 255, 218, 0.3);
        margin: 20px 0;
    }
    </style>
    <div style="text-align: center;">
        <div class="photo-frame-static">
    """, unsafe_allow_html=True)
    
    # Display the professional photo sideways with proper parameters
    safe_load_image("src/assets/Bhumika_Photo.jfif", 
                   caption="Bhumika Patel", 
                   width=300)
    
    st.markdown("""
        </div>
    </div>
    """, unsafe_allow_html=True)

with photo_col2:
    st.markdown("""
    <div style="margin: 40px 0;">
        <h2 style="color: #64ffda; margin-bottom: 20px; font-weight: 600; font-size: 2.2rem;">👩‍💻 Meet Bhumika Patel</h2>
        <div style="padding: 25px; background: rgba(255, 255, 255, 0.05); border-radius: 15px; border-left: 4px solid #64ffda;">
            <h3 style="color: #667eea; margin-bottom: 15px;">About Me</h3>
            <p style="color: #ccd6f6; font-size: 1.1rem; line-height: 1.8; margin-bottom: 15px;">
                A dedicated software developer and data analyst with expertise in AI/ML, hackathon winner, and technical leader passionate about creating innovative solutions.
            </p>
            <p style="color: #8892b0; font-size: 1rem; font-style: italic; margin-top: 20px;">
                ✨ "Passionate about creating innovative solutions that make a difference"
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="cyber-divider"></div>', unsafe_allow_html=True)

# Skills Section
st.markdown('<h2 class="section-3d"><span style="color: #64ffda;">🛠</span> Technical Skills</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown("""
    <div class="glass-card">
        <h3>💻 Software Development</h3>
        <ul>
            <li><b>Full-Stack Development</b> (Frontend & Backend)</li>
            <li><b>Web Application Development</b> with modern frameworks</li>
            <li><b>Database Design & Management</b> (SQL & NoSQL)</li>
            <li><b>RESTful API Development</b> & Integration</li>
            <li><b>Version Control</b> with Git & GitHub</li>
            <li><b>Agile Development</b> methodologies</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="glass-card">
        <h3>📊 Data Analytics</h3>
        <ul>
            <li><b>Data Analysis & Visualization</b> with Python/R</li>
            <li><b>Statistical Analysis</b> & Business Intelligence</li>
            <li><b>Machine Learning</b> & Predictive Modeling</li>
            <li><b>SQL Database Querying</b> & Data Mining</li>
            <li><b>Dashboard Creation</b> with Power BI/Tableau</li>
            <li><b>Data Cleaning</b> & ETL processes</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="glass-card">
        <h3>🔧 Tools & Technologies</h3>
        <ul>
            <li><b>Languages:</b> Python, Java, JavaScript, SQL, R</li>
            <li><b>Frameworks:</b> React, Node.js, Django, Flask</li>
            <li><b>Tools:</b> VS Code, Git, Docker, Jupyter, Power BI</li>
            <li><b>Libraries:</b> Pandas, NumPy, Scikit-learn, TensorFlow</li>
            <li><b>Databases:</b> MySQL, PostgreSQL, MongoDB</li>
            <li><b>Cloud:</b> AWS, Azure, Google Cloud Platform</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Skills Proficiency
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### <span style='color: #64ffda;'>📊</span> Skill Proficiency", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("**🐍 Python**")
    st.progress(0.85)
    st.markdown("**☕ Java**")
    st.progress(0.75)

with col2:
    st.markdown("**📊 Data Analysis**")
    st.progress(0.80)
    st.markdown("**💾 SQL**")
    st.progress(0.78)

with col3:
    st.markdown("**⚙️ Machine Learning**")
    st.progress(0.72)
    st.markdown("**🌐 Web Development**")
    st.progress(0.75)

with col4:
    st.markdown("**📚 Git/GitHub**")
    st.progress(0.70)
    st.markdown("**☁️ Cloud Platforms**")
    st.progress(0.68)

st.markdown('<div class="cyber-divider"></div>', unsafe_allow_html=True)

# Projects Section
st.markdown('<h2 class="section-3d"><span style="color: #667eea;">🏆</span> Award-Winning Projects & Innovations</h2>', unsafe_allow_html=True)

# Featured Projects Layout
col1, col2, col3 = st.columns(3, gap="medium")

# -------- Project 1: Financial Fraud Detection API - Execute 4.0 TOP 6 --------
with col1:
    st.markdown("""
    <div class="project-magnetic">
        <h3 style="color: #64ffda;">🔒 Financial Fraud Detection API</h3>
        <p style="color: #8892b0; font-size: 1.1rem; line-height: 1.7; margin: 20px 0;">
            <strong>🏆 TOP 6 Achievement in Execute 4.0 Hackathon, Delhi Technical University (DTU)</strong><br>
            Advanced machine learning-powered API for real-time financial fraud detection and risk assessment.
        </p>
        <div style="margin: 20px 0;">
            <span class="tech-bubble">Machine Learning</span><span class="tech-bubble">Python</span>
            <span class="tech-bubble">API Development</span><span class="tech-bubble">Fraud Detection</span>
            <span class="tech-bubble">Hugging Face</span>
        </div>
        <div style="margin-top: 25px;">
            <h4 style="color: #64ffda; margin-bottom: 15px;">✨ Key Features</h4>
            <ul style="color: #ccd6f6; line-height: 2;">
                <li>🔍 Real-time fraud detection algorithms</li>
                <li>📊 Advanced risk scoring system</li>
                <li>⚡ High-performance API endpoints</li>
                <li>🎯 Precision-focused ML models</li>
                <li>📈 Interactive fraud analytics dashboard</li>
                <li>🏆 Award-winning solution architecture</li>
            </ul>
        </div>
        <a href="https://huggingface.co/spaces/bhumika007/Fraud_Detection_API_excecute4_Part2" target="_blank" style="color:#64ffda; text-decoration:none; font-weight:bold;">🚀 Live Demo on Hugging Face</a>
    </div>
    """, unsafe_allow_html=True)

# -------- Project 2: AI Health Assistant - HACK SRIT 2025 --------
with col2:
    st.markdown("""
    <div class="project-magnetic">
        <h3 style="color: #667eea;">🏥 AI Health Assistant</h3>
        <p style="color: #8892b0; font-size: 1.1rem; line-height: 1.7; margin: 20px 0;">
            <strong>🚀 HACK SRIT 2025 Project - SRIT Jabalpur (May 10-11, 2025)</strong><br>
            Intelligent healthcare AI assistant providing personalized medical insights and health recommendations.
        </p>
        <div style="margin: 20px 0;">
            <span class="tech-bubble">Artificial Intelligence</span><span class="tech-bubble">Healthcare</span>
            <span class="tech-bubble">Machine Learning</span><span class="tech-bubble">NLP</span>
            <span class="tech-bubble">Hugging Face</span>
        </div>
        <div style="margin-top: 25px;">
            <h4 style="color: #667eea; margin-bottom: 15px;">✨ Key Features</h4>
            <ul style="color: #ccd6f6; line-height: 2;">
                <li>🧠 AI-powered health diagnostics</li>
                <li>📊 Personalized health recommendations</li>
                <li>💬 Natural language processing interface</li>
                <li>📈 Health data visualization</li>
                <li>⚡ Real-time symptom analysis</li>
                <li>🏆 Hackathon innovation showcase</li>
            </ul>
        </div>
        <a href="https://huggingface.co/spaces/bhumika007/AI_health" target="_blank" style="color:#667eea; text-decoration:none; font-weight:bold;">🚀 Live Demo on Hugging Face</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# -------- Project 3: Helmet & License Plate Detection - Major College Project --------
with col3:
    st.markdown("""
    <div class="project-magnetic">
        <h3 style="color: #f093fb;">🏏 Helmet & License Plate Detection</h3>
        <p style="color: #8892b0; font-size: 1.1rem; line-height: 1.7; margin: 20px 0;">
            <strong>🎓 Major College Project</strong><br>
            Advanced computer vision system for automated traffic safety monitoring and license plate recognition using deep learning.
        </p>
        <div style="margin: 20px 0;">
            <span class="tech-bubble">Computer Vision</span><span class="tech-bubble">Deep Learning</span>
            <span class="tech-bubble">YOLO</span><span class="tech-bubble">OpenCV</span>
            <span class="tech-bubble">Hugging Face</span>
        </div>
        <div style="margin-top: 25px;">
            <h4 style="color: #f093fb; margin-bottom: 15px;">✨ Key Features</h4>
            <ul style="color: #ccd6f6; line-height: 2;">
                <li>🎯 Real-time helmet detection for riders</li>
                <li>📷 Automated license plate recognition</li>
                <li>🚦 Traffic safety compliance monitoring</li>
                <li>📊 Advanced object detection algorithms</li>
                <li>⚡ High-accuracy YOLO implementation</li>
                <li>🎓 Academic excellence demonstration</li>
            </ul>
        </div>
        <a href="https://huggingface.co/spaces/bhumika007/Helmet-License-Plate-Detection" target="_blank" style="color:#f093fb; text-decoration:none; font-weight:bold;">🚀 Live Demo on Hugging Face</a>
    </div>
    """, unsafe_allow_html=True)


st.markdown('<div class="cyber-divider"></div>', unsafe_allow_html=True)

# Achievements Showcase Section
st.markdown('<h2 class="section-3d"><span style="color: #f093fb;">🏆</span> Leadership & Innovation Showcase</h2>', unsafe_allow_html=True)

# Create two columns for achievements
achievement_col1, achievement_col2 = st.columns(2, gap="large")

with achievement_col1:
    st.markdown("""
    <div class="glass-card">
        <h3 style="color: #64ffda; text-align: center; margin-bottom: 20px;">👩‍💼 Professional Profile</h3>
    </div>
    """, unsafe_allow_html=True)
    
    safe_load_image("src/assets/Bhumika_Photo.jfif", 
                   caption="Bhumika Patel - Software Developer & Data Analyst")
    
    st.markdown("""
    <div class="glass-card" style="margin-top: 20px; padding: 20px;">
        <ul style="color: #ccd6f6; line-height: 1.8;">
            <li>✅ <strong>Passionate technologist</strong> with expertise in AI/ML</li>
            <li>✅ <strong>Award-winning developer</strong> in competitive hackathons</li>
            <li>✅ <strong>Technical leader</strong> driving innovation in healthcare and fintech</li>
            <li>✅ <strong>Problem solver</strong> with focus on real-world impact</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with achievement_col2:
    st.markdown("""
    <div class="glass-card">
        <h3 style="color: #667eea; text-align: center; margin-bottom: 20px;">🎤 Leadership in Action</h3>
    </div>
    """, unsafe_allow_html=True)
    
    safe_load_image("src/assets/Presentation_Leadership_hackSRIT.jfif", 
                   caption="Presenting at HACK SRIT 2025 - Technical Leadership")
    
    st.markdown("""
    <div class="glass-card" style="margin-top: 20px; padding: 20px;">
        <ul style="color: #ccd6f6; line-height: 1.8;">
            <li>✅ <strong>Public speaking</strong> and technical presentation skills</li>
            <li>✅ <strong>Team leadership</strong> in competitive hackathon environments</li>
            <li>✅ <strong>Project management</strong> and stakeholder communication</li>
            <li>✅ <strong>Innovation showcase</strong> with live demonstrations</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="cyber-divider"></div>', unsafe_allow_html=True)

# Experience Section
st.markdown('<h2 class="section-3d"><span style="color: #f093fb;">💼</span> Professional Experience</h2>', unsafe_allow_html=True)

exp_col1, exp_col2 = st.columns(2, gap="large")

with exp_col1:
    st.markdown("""
    <div class="timeline-card">
        <h3><span style='color: #667eea;'>👨‍💻</span> TechCorp Solutions | Software Developer</h3>
        <p><strong>Jan 2023 - Present</strong> | Mumbai, India</p>
        <h4>🎯 Key Responsibilities</h4>
        <ul>
            <li>Developed and maintained <strong>full-stack web applications</strong> using modern frameworks</li>
            <li>Implemented <strong>data analytics solutions</strong> for business intelligence</li>
            <li>Collaborated with <strong>cross-functional teams</strong> to deliver high-quality software</li>
            <li>Optimized <strong>database performance</strong> and reduced query execution time by 40%</li>
            <li>Led <strong>code reviews</strong> and mentored junior developers</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="timeline-card">
        <h3><span style='color: #64ffda;'>👨‍💻</span> DataInsights Analytics | Data Analyst</h3>
        <p><strong>Jun 2021 - Dec 2022</strong> | Pune, India</p>
        <h4>🎯 Key Achievements</h4>
        <ul>
            <li>Analyzed <strong>large datasets</strong> to identify business trends and insights</li>
            <li>Created <strong>interactive dashboards</strong> using Power BI and Tableau</li>
            <li>Implemented <strong>predictive models</strong> for customer behavior analysis</li>
            <li>Automated <strong>data processing workflows</strong> reducing manual effort by 60%</li>
            <li>Collaborated with <strong>stakeholders</strong> to translate business requirements into technical solutions</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with exp_col2:
    st.markdown("""
    <div class="timeline-card">
        <h3><span style='color: #64ffda;'>👨‍💻</span> InnovateTech | Junior Software Engineer</h3>
        <p><strong>Aug 2020 - May 2021</strong> | Bangalore, India</p>
        <h4>🎯 Key Responsibilities</h4>
        <ul>
            <li>Developed <strong>web applications</strong> using Java Spring Boot and React</li>
            <li>Designed and implemented <strong>RESTful APIs</strong> for mobile and web clients</li>
            <li>Participated in <strong>agile development</strong> processes and daily standups</li>
            <li>Conducted <strong>unit testing</strong> and debugging to ensure code quality</li>
            <li>Collaborated with <strong>senior engineers</strong> on architecture decisions</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
st.markdown('<div class="cyber-divider"></div>', unsafe_allow_html=True)

st.markdown('<h2 class="section-3d"><span style="color: #00f2fe;">📚</span> Courses & Certifications</h2>', unsafe_allow_html=True)

# Create columns for courses
course_col1, course_col2 = st.columns(2, gap="large")

with course_col1:
    # Basics of Python - Springboard
    st.markdown("""
    <div class="glass-card">
        <h3 style="color: #64ffda;">🐍 Basics of Python</h3>
        <p style="color: #8892b0; margin: 10px 0;"><strong>Springboard</strong></p>
        <div style="margin: 15px 0;">
            <span class="tech-bubble">Python</span>
            <span class="tech-bubble">Programming Fundamentals</span>
            <span class="tech-bubble">Coding</span>
            <span class="tech-bubble">Development</span>
        </div>
        <ul style="color: #ccd6f6; line-height: 1.8; margin: 15px 0;">
            <li>✅ Successfully completed <strong>comprehensive Python course</strong></li>
            <li>✅ Mastered <strong>Python fundamentals</strong> and syntax</li>
            <li>✅ Hands-on experience with <strong>practical coding exercises</strong></li>
            <li>✅ Built strong foundation for <strong>advanced programming</strong></li>
        </ul>
        <a href="https://drive.google.com/file/d/1PPBFguEliZgMx81E7I4dTkk9-OwWte2W/view?usp=drive_link" 
           target="_blank" 
           style="color: #64ffda; text-decoration: none; font-weight: bold; display: inline-block; margin-top: 10px;">
           📄 View Certificate
        </a>
    </div>
    """, unsafe_allow_html=True)

    # Object Oriented Programming using Python
    st.markdown("""
    <div class="glass-card">
        <h3 style="color: #667eea;">⚙️ Object Oriented Programming using Python</h3>
        <p style="color: #8892b0; margin: 10px 0;"><strong>Professional Certification</strong></p>
        <div style="margin: 15px 0;">
            <span class="tech-bubble">Python</span>
            <span class="tech-bubble">OOP</span>
            <span class="tech-bubble">Programming</span>
            <span class="tech-bubble">Software Design</span>
        </div>
        <ul style="color: #ccd6f6; line-height: 1.8; margin: 15px 0;">
            <li>✅ Advanced <strong>Object-Oriented Programming</strong> concepts</li>
            <li>✅ Expertise in <strong>Python class design</strong> patterns</li>
            <li>✅ Proficiency in <strong>inheritance and polymorphism</strong></li>
            <li>✅ Enhanced <strong>software architecture</strong> skills</li>
        </ul>
        <a href="https://drive.google.com/file/d/1VpakzRDauRF3-f-yoe5p3iixysP6ruQN/view?usp=sharing" 
           target="_blank" 
           style="color: #667eea; text-decoration: none; font-weight: bold; display: inline-block; margin-top: 10px;">
           📄 View Certificate
        </a>
    </div>
    """, unsafe_allow_html=True)

with course_col2:
    # E-Cell DTU E-SUMMIT Achievement
    st.markdown("""
    <div class="glass-card">
        <h3 style="color: #f093fb;">🏆 E-SUMMIT '25 TOP 6 Achievement</h3>
        <p style="color: #8892b0; margin: 10px 0;"><strong>E-Cell DTU, SabPaisa, and cellDTU</strong></p>
        <div style="margin: 15px 0;">
            <span class="tech-bubble">Entrepreneurship</span>
            <span class="tech-bubble">Innovation</span>
            <span class="tech-bubble">Competition</span>
            <span class="tech-bubble">Leadership</span>
        </div>
        <ul style="color: #ccd6f6; line-height: 1.8; margin: 15px 0;">
            <li>✅ Achieved <strong>TOP 6 position</strong> in prestigious E-SUMMIT '25</li>
            <li>✅ Demonstrated <strong>innovative thinking</strong> and problem-solving</li>
            <li>✅ Competed with <strong>top entrepreneurial talent</strong> nationwide</li>
            <li>✅ Recognition from <strong>leading industry partners</strong></li>
            <li>✅ Enhanced <strong>business development</strong> and pitching skills</li>
        </ul>
        <a href="https://drive.google.com/file/d/1JtOSuIYjJaL_yyehXujJXqjqbYbP-AiR/view?usp=drive_link" 
           target="_blank" 
           style="color: #f093fb; text-decoration: none; font-weight: bold; display: inline-block; margin-top: 10px;">
           📄 View Certificate
        </a>
    </div>
    """, unsafe_allow_html=True)

    # HACK SRIT 2025 Achievement
    st.markdown("""
    <div class="glass-card">
        <h3 style="color: #00f2fe;">🚀 HACK SRIT 2025 Participant</h3>
        <p style="color: #8892b0; margin: 10px 0;"><strong>SRIT Jabalpur</strong></p>
        <div style="margin: 15px 0;">
            <span class="tech-bubble">Hackathon</span>
            <span class="tech-bubble">Coding</span>
            <span class="tech-bubble">Innovation</span>
            <span class="tech-bubble">Team Work</span>
        </div>
        <ul style="color: #ccd6f6; line-height: 1.8; margin: 15px 0;">
            <li>✅ Participated in <strong>prestigious hackathon</strong> competition</li>
            <li>✅ Developed <strong>innovative tech solutions</strong> under time pressure</li>
            <li>✅ Collaborated with <strong>skilled development teams</strong></li>
            <li>✅ Enhanced <strong>rapid prototyping</strong> abilities</li>
            <li>✅ Demonstrated <strong>problem-solving</strong> in competitive environment</li>
        </ul>
        <a href="https://drive.google.com/file/d/1aRObwFQJsKuafk8rSMqq2em1HHGMQ7Vn/view?usp=drive_link" 
           target="_blank" 
           style="color: #00f2fe; text-decoration: none; font-weight: bold; display: inline-block; margin-top: 10px;">
           📄 View Certificate
        </a>
    </div>
    """, unsafe_allow_html=True)

# IIITDMJ Programming Club Certificate
st.markdown("""
<div class="project-magnetic" style="margin-top: 20px;">
    <h3 style="color: #764ba2;">🏆 36-Hour Programming Intensive</h3>
    <p style="color: #8892b0; margin: 10px 0;"><strong>Programming Club of IIITDMJ PDPM IIITDM Jabalpur</strong></p>
    <div style="margin: 15px 0;">
        <span class="tech-bubble">Programming</span>
        <span class="tech-bubble">Competitive Coding</span>
        <span class="tech-bubble">Team Collaboration</span>
        <span class="tech-bubble">Problem Solving</span>
        <span class="tech-bubble">Algorithms</span>
    </div>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 20px 0;">
        <div>
            <h4 style="color: #64ffda; margin-bottom: 10px;">🎯 Program Highlights</h4>
            <ul style="color: #ccd6f6; line-height: 1.8;">
                <li>✅ <strong>36-hour intensive</strong> in-person programming workshop</li>
                <li>✅ Hands-on experience with <strong>competitive programming</strong></li>
                <li>✅ Collaborated in <strong>team-based challenges</strong></li>
                <li>✅ Prestigious <strong>IIITDMJ recognition</strong></li>
                <li>✅ Enhanced <strong>algorithmic thinking</strong> abilities</li>
            </ul>
        </div>
        <div>
            <h4 style="color: #667eea; margin-bottom: 10px;">💡 Skills Acquired</h4>
            <ul style="color: #ccd6f6; line-height: 1.8;">
                <li>• Advanced problem-solving techniques</li>
                <li>• Efficient algorithm implementation</li>
                <li>• Time-constrained programming</li>
                <li>• Team collaboration and leadership</li>
                <li>• Code optimization strategies</li>
            </ul>
        </div>
    </div>
    <a href="https://drive.google.com/file/d/1QC7ISV0pINplCW4JsiqhVaN17cMyJ-qS/view?usp=sharing" 
       target="_blank" 
       style="color: #764ba2; text-decoration: none; font-weight: bold; display: inline-block; margin-top: 10px;">
       📄 View Certificate
    </a>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="cyber-divider"></div>', unsafe_allow_html=True)

# Contact Section
st.markdown('<h2 class="section-3d"><span style="color: #64ffda;">📞</span> Let\'s Connect</h2>', unsafe_allow_html=True)

contact_col1, contact_col2, contact_col3, contact_col4 = st.columns(4, gap="medium")

with contact_col1:
    st.markdown("<div class='icon-glow' style='font-size: 3rem;'>📱</div>", unsafe_allow_html=True)
    st.markdown("### Phone")
    st.markdown("**+91 (900) 1234567**")

with contact_col2:
    st.markdown("<div class='icon-glow' style='font-size: 3rem;'>📧</div>", unsafe_allow_html=True)
    st.markdown("### Email")
    st.markdown("**bhumika.patel.dev@gmail.com**")

with contact_col3:
    st.markdown("<div class='icon-glow' style='font-size: 3rem;'>💼</div>", unsafe_allow_html=True)
    st.markdown("### GitHub")
    st.markdown("**[github.com/bhumika-patel](https://github.com/bhumika-patel)**")

with contact_col4:
    st.markdown("<div class='icon-glow' style='font-size: 3rem;'>🔗</div>", unsafe_allow_html=True)
    st.markdown("### LinkedIn")
    st.markdown("**[Bhumika Patel](https://www.linkedin.com/in/bhumika-patel-dev)**")
