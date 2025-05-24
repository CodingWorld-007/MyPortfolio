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
DESCRIPTION = "Pursuing B.Tech CSE(Hons.) with specialization in Artificial Intelligence and Machine Learning."
EMAIL = "amanjoshi9891@gmail.com"

SOCIAL_MEDIA = {
    "YouTube ▶️": "https://youtube.com/@codingworld_official",
    "LinkedIn 🔗": "https://linkedin.com/in/amanajjoshi",
    "GitHub 💻": "https://github.com/CodingWorld-007",
}

AWARDS = {
    "🏆 SCIENCE EXHIBITION 2023 - First Position Certification 🏆": "https://drive.google.com/file/d/134A0qhv7mhzzvHfVih4K-5AZfj2R2_Hm/view?usp=sharing",
    "- SCIENCE EXHIBITION 2023 - Project Video": "https://drive.google.com/file/d/1mIm4Cv70frLaPQ8hfqfIpA62l-EVUHZb/view?usp=sharing",
    "🏆 ROBO - RACE 2023 - First Position 🏆": "https://drive.google.com/file/d/13d68utRWutqhKsHzRcxXmaMLYnnSi2UX/view?usp=sharing",
    "🏆 G20 - BEST RESEARCHER AWARD 2023 - Runner Up 🏆": "https://drive.google.com/file/d/19n4EB8m11l5pG1Yb2lQGMle4PP-N6Tw3/view?usp=sharing",
}

PROJECTS = {
    "1. DATA VISUALISATION": "https://codingworld-data-visualiser.streamlit.app/",
    "2. AI-Enhanced Chat & Image Suite: Streamlit Deployment, 2024": "https://codingworld-gemini-ai.streamlit.app/",
    "3. Digit Recognition Project, 2023": None,  # Marked as coming soon
}

# --- PAGE CONFIG ---
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=250)
with col2:
    st.markdown(f"<h1 style='color: white;'>{NAME}</h1>", unsafe_allow_html=True)
    description_html = f"""
    <p style='color:black; font-size:16px;'>
    <a href='https://www.gehu.ac.in/' target='_blank' style='text-decoration:none; color:black;'>{DESCRIPTION}</a>
    </p>
    """
    st.markdown(description_html, unsafe_allow_html=True)
    st.download_button("📄 Download Resume", data=PDFbyte, file_name=resume_file.name, mime="application/octet-stream")
    st.write("📧", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
num_cols = min(len(SOCIAL_MEDIA), 4)
for i, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    if i % num_cols == 0:
        cols = st.columns(num_cols)
    cols[i % num_cols].write(f"[{platform}]({link})")

# --- PATENTS / WORK ---
st.write('\n')
st.header("MORE ABOUT MY WORK")
with st.expander("📜 View Patent Details"):
    st.subheader("DEVELOPMENT")
    st.write("---")
    st.markdown("""
**1. "TRAFFIC LIGHT GUARD"**  
- Published - 202411013629 A  
- Summary - Filed [26 Feb, 2024]  
    - Involves a device with cameras, sensors, and ML algorithms  
    - Detects traffic signals from a distance  
    - Adjusts car speed based on signal status  
    - Automatically controls brakes to ensure safe deceleration before the signal  
    - Hands control back to driver when signal turns green  

**2. Intelli-Safe**  
- Published - 202411049367 A  
- Summary - Filed [27 Jun, 2024]  
    - Integrated cameras, sensors & ML for proactive pothole detection  
    - Recognizes 4 categorized road hazard conditions  
    - Automatically decelerates vehicles  

**3. Emergency Handling System (Confidential)**  
- Details under process
""")

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write("---")
st.markdown("""
- 👩‍💻 Programming: Intermediate: C, C++, Python, Java, HTML, CSS, JavaScript | Basic: MYSQL, R  
- 📊 Data Visualization: Matplotlib  
- 📚 Frameworks: TensorFlow, PyTorch, scikit-learn
""")

# --- EDUCATION ---
st.write('\n')
st.subheader("EDUCATIONAL QUALIFICATION")
st.write("---")
st.markdown("""
**Bachelor of Technology (B.Tech)**  
- Specialization: Artificial Intelligence & Machine Learning  
- GRAPHIC ERA HILL UNIVERSITY, DEHRADUN  
- Sep 2022 - Jun 2026  
- Grade: 8.27 CGPA
""")

# --- EXPERIENCE --- 
st.write('\n')
st.subheader("Experience")
st.write("---")

st.markdown("""
**Software Developer Intern - TBI** [📄 View Certificate](https://drive.google.com/file/d/1N8sl9BmdMgJnzMbQ-4QjIbxESmMTtTJb/view?usp=sharing) 
  
- GEU · Part-Time  
- Nov 2024 - Feb 2025  
- India · Remote
""")

st.write('\n')

st.markdown("""
**YouTuber - CODING WORLD**  
- YouTube · Part-Time  
- Jun 2023 - Present  
- India · Remote
""")


# --- ACHIEVEMENTS & AWARDS ---
st.write('\n')
st.subheader("ACHIEVEMENTS & AWARDS")
st.write("To download the certificates for verification, please click the embedded links.")
st.write("---")
for title, link in AWARDS.items():
    st.markdown(f"[{title}]({link})")

# --- PROJECTS ---
st.write('\n')
st.subheader("PROJECTS")
st.write("To check it, please click the embedded links below.")
st.write("---")
for title, link in PROJECTS.items():
    if link:
        st.markdown(f"[{title}]({link})")
    else:
        st.markdown(f"**{title}** *(Coming Soon)*")

st.markdown("## 📘 PESE Assignment")

# --- STYLES ---
video_styles = """
<style>
  .card {
    background-color: white;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
    transition: 0.3s;
  }
  .card:hover {
    box-shadow: 0 6px 25px rgba(0, 0, 0, 0.2);
  }
  .video-title {
    font-size: 24px;
    font-weight: bold;
    color: #1f4e79;
    margin-bottom: 10px;
  }
  .review-title {
    font-size: 24px;
    font-weight: bold;
    color: #27ae60;
    margin-bottom: 20px;
  }
  .review-text {
    font-size: 16px;
    color: #333;
    line-height: 1.6;
  }
  .responsive-video {
    position: relative;
    padding-bottom: 56.25%;
    padding-top: 25px;
    height: 0;
  }
  .responsive-video iframe,
  .responsive-video video {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border-radius: 10px;
  }
</style>
"""

# --- VIDEO BLOCK 1: 6 Ring Theory ---
video_block_1 = """
<div class="card">
  <div class="video-title">🎥 Introduction Based on 6 Ring Theory</div>
  <div class="responsive-video">
    <iframe src="https://drive.google.com/file/d/1xAIIXlrfPzqSwgh7SCT7ku5trSRt1N1B/preview" allow="autoplay"></iframe>
  </div>
</div>
"""

# --- VIDEO BLOCK 2: 5 Ring Theory ---
video_block_2 = """
<div class="card">
  <div class="video-title">🎥 Introduction Based on 5 Ring Theory</div>
  <div class="responsive-video">
    <iframe src="https://drive.google.com/file/d/1DSY40zdqZ9Qlntv0cZV4-wTmlJrJYE7b/preview" allow="autoplay"></iframe>
  </div>
</div>
"""

# --- MOVIE REVIEW BLOCK ---
review_block = """
<div class="card">
  <div class="review-title">🎬 Movie Review: <em>The Maze Runner</em></div>
  <div class="review-text">
    <strong>Plot:</strong> The Maze Runner is a gripping sci-fi thriller based on the best-selling novel by James Dashner.
    The movie follows Thomas (Dylan O’Brien), who wakes up in a mysterious, enclosed area called the Glade with no memory of his past.
    He soon discovers that he, along with other young men, is trapped within a giant maze filled with deadly creatures known as Grievers.
    As Thomas begins to question their reality, he teams up with fellow Gladers to find a way out before time runs out.
    <br><br>
    <strong>Review:</strong> The Maze Runner is an exciting sci-fi adventure that delivers non-stop action and suspense.
    While it doesn’t answer all the questions it raises, it keeps audiences hooked and eager for the next installment.
    If you enjoy dystopian thrillers like The Hunger Games, this is definitely worth watching!
  </div>
</div>
"""

# --- COMBINE AND RENDER ALL HTML BLOCKS ---
combined_html = video_styles + video_block_1 + video_block_2 + review_block
st.components.v1.html(combined_html, height=1700, scrolling=True)

st.markdown(" Lectue 1 ")

st.image("5ring.png", caption="Lecture 1", use_column_width=True)

st.markdown(" Lectue 2 ")

st.image("6ring.png", caption="Lectur 2", use_column_width=True)

st.markdown(" Lectue 3 & 4 ")

st.image("Lec3-4.png", caption="Lectur 2", use_column_width=True)

