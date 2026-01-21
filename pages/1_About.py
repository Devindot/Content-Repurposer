import streamlit as st

st.set_page_config(page_title="About", page_icon="🧑‍💻", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    body { font-family: 'Inter', sans-serif; }
    [data-testid="stAppViewContainer"] { background: #1e1e1e; color: #e0e0e0; }
    .st-emotion-cache-1y4p8pa { padding-top: 3rem; }
    h1, h2, h3 { color: #ffffff; }
    [data-testid="stSidebar"] { background-color: #1a1a1a; }
    
    /* Style for the hyperlinks */
    a:link, a:visited {
        color: #00aaff;
        text-decoration: none;
    }
    a:hover, a:active {
        color: #0077b3;
        text-decoration: underline;
    }
</style>
""", unsafe_allow_html=True)

st.title("About the Project & Creator")
st.markdown("---")

col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.image("assets/profile-pic.png")

with col2:
    st.header("Devin Thakur")
    st.subheader("B.Tech Information Technology Student | VIT, Vellore")
    st.markdown("""
    This project was built by Devin Thakur, a B.Tech Information Technology student at the Vellore Institute of Technology (VIT). 
    Driven by a passion for AI and building practical software solutions, this tool was created to explore and demonstrate 
    the capabilities of modern Large Language Models.
    """)
    
    # MODIFICATION: Your personal links have been added here
    st.markdown("""
    **Connect with me:**
    - **[GitHub](https://github.com/Devindot)**
    - **[LinkedIn](https://www.linkedin.com/in/devinthakur3009)**
    """)

st.markdown("---")
st.header("About the Project")
st.markdown("""
This **Content Repurposing Engine** is an AI-powered application designed to streamline the content creation workflow. 
It leverages Large Language Models (LLMs) to automatically transform a single source of content—like a YouTube video 
or a blog post—into various formats suitable for different platforms.
""")
st.markdown("""
**Key Features & Tech Stack:**
- **Frontend:** Streamlit
- **AI/Backend:** Python, LangChain
- **LLM:** Google Gemini Pro
- **Content Scraping:** BeautifulSoup, YouTube Transcript API
""")