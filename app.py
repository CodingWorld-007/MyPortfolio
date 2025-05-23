from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Aman Joshi"
PAGE_ICON = ":wave:"
NAME = "Aman Joshi"
DESCRIPTION = """
Pursuing B.Tech CSE(Hons.) with specialization in Artificial Intelligence and Machine Learning.
"""
EMAIL = "amanjoshi9891@gmail.com"
SOCIAL_MEDIA = {
    "YouTube ▶️": "https://youtube.com/@codingworld_official",
    "LinkedIn 🔗": "https://linkedin.com/in/amanajjoshi",
    "GitHub 💻": "https://github.com/CodingWorld-007",
    "Instagram 🌐": "https://www.instagram.com/codingworld_official",
}
AWARDS = {
    "🏆 SCIENCE EXHIBITION 2023 - First Position Certification 🏆 ": "https://drive.google.com/file/d/134A0qhv7mhzzvHfVih4K-5AZfj2R2_Hm/view?usp=sharing",
    "- \t\t SCIENCE EXHIBITION 2023 - Project Video": "https://drive.google.com/file/d/1mIm4Cv70frLaPQ8hfqfIpA62l-EVUHZb/view?usp=sharing",
    "🏆 ROBO - RACE 2023 - First Position 🏆": "https://drive.google.com/file/d/13d68utRWutqhKsHzRcxXmaMLYnnSi2UX/view?usp=sharing",
    "🏆 G20 - BEST RESEARCHER AWARD 2023 - Runner Up 🏆": "https://drive.google.com/file/d/19n4EB8m11l5pG1Yb2lQGMle4PP-N6Tw3/view?usp=sharing",
}

PROJECTS = {
    "1. DATA VISUALISATION ": "https://codingworld-data-visualiser.streamlit.app/",
    "2. AI-Enhanced Chat & Image Suite: Streamlit Deployment, 2024": "https://codingworld-gemini-ai.streamlit.app/",
    "3. Digit Recognition Project, 2023": "",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=250)

with col2:
    st.markdown(f"<h1 style='color: white;'>{NAME}</h1>", unsafe_allow_html=True)

    link_url = "https://www.gehu.ac.in/"

    # Add a hyperlink to the text and apply color formatting
    description_with_link = f"<font color='black'><a href='{link_url}' target='_blank'>{DESCRIPTION}</a></font>"

    # Display the text with the hyperlink
    st.markdown(description_with_link, unsafe_allow_html=True)

    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📧", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

st.write('\n')
st.header("MORE ABOUT MY WORK")
# --- DEVELOPMENT ---
st.subheader("DEVELOPMENT")
st.write("---")
st.write(
    """
    PATENT:
    1. "TRAFFIC LIGHT GUARD": AN AUTOMATED CAR HALTING SYSTEM AT TRAFFIC LIGHT.
        - Published - 202411013629 A
        - Summary - Filed [26 Feb, 2024], 
        - a. Involves a device with cameras, sensors, and machine learning algorithms.
        - b. Detects traffic signals from a distance, adjusts car speed based on signal status.
        - c. Automatically controls brakesto ensure safe decelerationbefore the signal.
        - d. Hands back before control to the driver when the signal turn green.

    2. Intelli-Safe: Elevating Road Safety via Integrated Hardware and Machine Learning for Proactive Hazard Avoidance System.
        - Published - 202411049367 A
        - Summary - Filed [27 Jun, 2024],
        - a. Involves a system consist of Integrated cameras, sensors, and machine learning algorithms.
        - b. Detects pot holes/trench from a distance, adjusts car speed based on conditions (4 categorised conditions).
        - c. Automatically controls brakes to ensure safe deceleration before the hazard.
    
    - Under Process -
    
    3. Related to Emergency Situation, Confidential right now. 
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write("---")
st.write(
    """
- 👩‍💻 Programming: Intermediate: C, C++, Python, Java, HTML, CSS, JavaScript. Basic: MYSQL, R
- 📊 Data Visulization: Matplotlib
- 📚 Frameworks : TensorFlow, PyTorch, scikit-learn.

"""
)

# --- EDUCATION ---
st.write('\n')
st.subheader("EDUCATIONAL QUALIFICATION")
st.write("---")
st.write(
    """
    Bachelor of Technology (B.Tech) in Computer Science and Engineering
    - Specialization in Artificial Intelligence & Machine Learning
    - GRAPHIC ERA HILL UNIVERSITY, DEHRADUN
    - Sep 2022 - Jun 2026
    - Grade: 8.27
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Experience")
st.write("---")
st.write(
    """
    YouTuber (CODING WORLD)
    - YouTube  ·  Part-Time
    - Jun 2023 - Present 
    - India · Remote
"""
)

# --- Accomplishments ---
st.write('\n')
st.subheader("ACHEIVEMENTS & AWARDS")
st.write("To download the certificates for verification, please click the embedded links.")
st.write("---")
for awards, link in AWARDS.items():
    st.write(f"[{awards}]({link})")

# --- Projects ---
st.write('\n')
st.subheader("PROJECTS")
st.write("To check it, please click the embedded links below.")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
