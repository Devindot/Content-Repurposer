import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Import your custom modules
from utils.content_fetcher import fetch_content_from_url
from modules.ai_repurposer import generate_blog_post, generate_twitter_thread, generate_linkedin_post

# --- Page Configuration ---
st.set_page_config(
    page_title="Content Repurposing Engine",
    page_icon="♻️",
    layout="wide"
)

# --- Custom CSS for Final UI ---
css = """
<style>
    /* --- Font Import --- */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&family=Inter:wght@400;500&display=swap');

    /* --- General Styles & Dynamic Background --- */
    body {
        font-family: 'Inter', 'Microsoft Sans Serif', system-ui, sans-serif;
    }
    [data-testid="stAppViewContainer"] {
        background-color: #0c0c0f;
        background-image:
            radial-gradient(at 20% 15%, hsla(211, 80%, 30%, 0.3) 0px, transparent 50%),
            radial-gradient(at 80% 25%, hsla(289, 70%, 25%, 0.25) 0px, transparent 50%),
            radial-gradient(at 25% 85%, hsla(320, 75%, 35%, 0.3) 0px, transparent 50%),
            radial-gradient(at 75% 90%, hsla(200, 85%, 30%, 0.35) 0px, transparent 50%);
        color: #e0e0e0;
    }

    /* --- Typography and Hierarchy --- */
    .title {
        font-family: 'Poppins', sans-serif;
        font-size: 3.8rem;
        font-weight: 700;
        text-align: center;
        color: #ffffff;
        text-shadow: 0 0 15px rgba(255, 255, 255, 0.2);
        letter-spacing: -1px;
        padding-top: 2rem;
    }
    .subtitle {
        text-align: center;
        color: #a0a0a0;
        font-size: 1.1rem;
        margin-bottom: 2.5rem;
    }
    
    /* --- Glass Box Styling --- */
    .glass-container {
        background: rgba(30, 30, 40, 0.4);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 2rem; 
    }
    .glass-box-text {
        text-align: center;
        color: #d1d5db;
        font-size: 1.2rem;
        font-family: 'Poppins', sans-serif;
    }
    
    /* --- Input Bar & Button Styling --- */
    [data-testid="stTextInput"] input {
        background-color: #2c2c2c;
        border: 1px solid #4a4a4a;
        border-radius: 15px;
        padding: 1rem 1.25rem;
        font-size: 1.1rem;
        transition: all 0.2s;
    }
    /* MODIFICATION #1: Restored the focus (hover gradient) effect */
    [data-testid="stTextInput"] input:focus {
        border-color: #00aaff;
        box-shadow: 0 0 0 3px rgba(0, 170, 255, 0.3);
    }
    .stButton>button {
        border: none;
        border-radius: 15px;
        color: #ffffff;
        background: #00aaff;
        transition: all 0.2s ease-in-out;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
    }
    .stButton>button:hover {
        filter: brightness(1.2);
    }

    /* --- Sidebar Navigation & Output Tabs --- */
    [data-testid="stSidebar"] { background-color: rgba(12, 12, 15, 0.8); }
    .stTabs [aria-selected="true"] { border-bottom: 2px solid #00aaff; color: #00aaff; }
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# --- Session State Initialization ---
if 'source_content' not in st.session_state:
    st.session_state.source_content = ""

# --- Main Page Layout ---
st.markdown('<h1 class="title">Content Repurposing Engine ♻️</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">By Devin Thakur</p>', unsafe_allow_html=True)

# --- Central Column for Content Alignment ---
col1, col2, col3 = st.columns([1, 2.5, 1])
with col2:
    st.html(
        """
        <div class="glass-container">
            <p class="glass-box-text">Transform your content into Blog Posts, Twitter Threads, or LinkedIn Posts</p>
        </div>
        """
    )
    
    url_input = st.text_input("URL", label_visibility="collapsed", placeholder="Paste your content URL here...")

    # --- MODIFICATION #2: Reverted to the reliable st.columns method for centering ---
    b_col1, b_col2, b_col3 = st.columns([2, 1, 2])
    with b_col2:
        submit_button = st.button("Fetch")
    
    if submit_button:
        if url_input:
            with st.spinner("Fetching and analyzing..."):
                content = fetch_content_from_url(url_input)
                if content.startswith("Error:"):
                    st.session_state.source_content = ""
                    st.error(content)
                else:
                    st.session_state.source_content = content
        else:
            st.warning("Please enter a URL.")

# --- Content Generation Section ---
if st.session_state.source_content:
    st.markdown("---")
    st.info("Content fetched successfully! Choose a format below to generate.")
    
    tab1, tab2, tab3 = st.tabs(["✍️ Blog Post", "🐦 Twitter Thread", "💼 LinkedIn Post"])

    with tab1:
        if st.button("Generate Blog Post"):
            with st.spinner("AI is writing your blog post..."):
                blog_post = generate_blog_post(st.session_state.source_content)
                st.markdown("### Generated Blog Post")
                st.markdown(blog_post)
                with st.expander("View and Copy Raw Markdown"):
                    st.code(blog_post, language='markdown')

    with tab2:
        if st.button("Generate Twitter Thread"):
            with st.spinner("AI is crafting your Twitter thread..."):
                twitter_thread = generate_twitter_thread(st.session_state.source_content)
                st.markdown("### Generated Twitter Thread")
                st.markdown(twitter_thread)
                with st.expander("View and Copy Raw Text"):
                    st.code(twitter_thread)

    with tab3:
        if st.button("Generate LinkedIn Post"):
            with st.spinner("AI is creating your LinkedIn post..."):
                linkedin_post = generate_linkedin_post(st.session_state.source_content)
                st.markdown("### Generated LinkedIn Post")
                st.markdown(linkedin_post)
                with st.expander("View and Copy Raw Text"):
                    st.code(linkedin_post)