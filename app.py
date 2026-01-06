import os
import streamlit as st
from dotenv import load_dotenv
from tensorlake.applications import run_local_application

# IMPORTANT: import the Tensorlake application + input model
from podcast_agent import podcast_agent, CrawlInput

load_dotenv()

# -------------------------
# PAGE CONFIG
# -------------------------

st.set_page_config(
    page_title="Article to Podcast Generator",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------------
# CUSTOM CSS (ORIGINAL + FIXES ONLY)
# -------------------------

st.markdown(
    """
<style>

/* -------- BASE THEME -------- */
.stApp {
    background-color: #0E1117;
    color: #FFFFFF;
}

section[data-testid="stSidebar"] {
    background-color: #161B22;
    border-right: 1px solid #30363D;
}

/* -------- CARDS -------- */
.feature-card {
    background-color: #1A1C23;
    padding: 24px;
    border-radius: 12px;
    border: 1px solid #333;
    min-height: 250px;
    margin-bottom: 20px;
}

.banner {
    background: linear-gradient(90deg, #1E1E2F 0%, #2D2D44 100%);
    padding: 30px;
    border-radius: 12px;
    border-left: 5px solid #6C5CE7;
    margin-bottom: 30px;
}

/* -------- BUTTON FIX -------- */
.stButton > button {
    background: linear-gradient(135deg, #6C5CE7, #8E7BFF) !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.6rem 1.3rem !important;
    font-weight: 600 !important;
    box-shadow: 0 4px 12px rgba(108,92,231,0.35);
}

.stButton > button:hover {
    background: linear-gradient(135deg, #5A4BD8, #7B6BFF) !important;
    transform: translateY(-1px);
}

/* -------- DOWNLOAD BUTTON -------- */
.stDownloadButton > button {
    background: #00C896 !important;
    color: #0E1117 !important;
    font-weight: 600 !important;
    border-radius: 10px !important;
}

/* -------- INPUTS -------- */
.stTextInput input {
    background-color: #0E1117 !important;
    color: #FFFFFF !important;
    border: 1px solid #30363D !important;
    border-radius: 8px !important;
}

/* -------- SLIDER -------- */
.stSlider > div {
    color: #6C5CE7 !important;
}

/* -------- AUDIO -------- */
audio {
    width: 100%;
    border-radius: 12px;
}

/* -------- EXPANDER -------- */
.streamlit-expanderHeader {
    color: #FFFFFF !important;
}

/* -------- IMAGE FIX -------- */
img {
    max-width: 100%;
    height: auto;
}

</style>
""",
    unsafe_allow_html=True,
)

# -------------------------
# SIDEBAR
# -------------------------

with st.sidebar:
    st.image(
        "https://mintcdn.com/tensorlake-35e9e726/fVE8-oNRlpqs-U2A/logo/TL-Dark.svg",
        use_container_width=True,
    )

    st.subheader("🔑 API Configuration")

    if "gemini_api_key" not in st.session_state:
        st.session_state.gemini_api_key = os.getenv("GEMINI_API_KEY") or ""
    if "elevenlabs_api_key" not in st.session_state:
        st.session_state.elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY") or ""

    gemini_key = st.text_input(
        "Gemini API Key",
        value=st.session_state.gemini_api_key,
        type="password",
    )

    eleven_key = st.text_input(
        "ElevenLabs API Key",
        value=st.session_state.elevenlabs_api_key,
        type="password",
    )

    if st.button("💾 Save API Keys"):
        st.session_state.gemini_api_key = gemini_key
        st.session_state.elevenlabs_api_key = eleven_key
        st.success("API Keys Saved!")

    max_depth = st.slider("Crawl Depth", 0, 3, 1)

    st.markdown("---")
    st.subheader("🎯 Key Capabilities")
    st.markdown(
        """
    - **Tensorlake Orchestration**: Full agent pipeline  
    - **JS-aware Crawling**: PyDoll + Chromium  
    - **AI Summarization**: Gemini  
    - **Voice Synthesis**: ElevenLabs  
    """
    )

    st.markdown("---")
    st.markdown("Developed with ❤️ using Tensorlake")

# -------------------------
# MAIN HEADER
# -------------------------

st.markdown(
    """
<div class="banner">
    <h3>✨ Transform Articles into Podcasts</h3>
    <p>One-click crawling, summarization, and voice generation powered by Tensorlake.</p>
</div>
""",
    unsafe_allow_html=True,
)

# -------------------------
# FEATURE CARDS
# -------------------------

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
<div class="feature-card">
    <h3>🔍 Extraction Mode</h3>
    <ul>
        <li>Depth-first crawling</li>
        <li>JS-rendered pages</li>
        <li>Clean text extraction</li>
    </ul>
</div>
""",
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
<div class="feature-card">
    <h3>🎙️ Generation Mode</h3>
    <ul>
        <li>Podcast-style summarization</li>
        <li>Natural voice synthesis</li>
        <li>Instant MP3 output</li>
    </ul>
</div>
""",
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)

# -------------------------
# INPUT SECTION
# -------------------------

article_url = st.text_input(
    "Enter the article URL:",
    placeholder="https://www.koreaherald.com/article/10648326",
)

# -------------------------
# GENERATE BUTTON
# -------------------------

if st.button("🚀 Generate Podcast Audio"):
    if not article_url:
        st.error("❌ Please provide an article URL.")
    elif not st.session_state.gemini_api_key or not st.session_state.elevenlabs_api_key:
        st.error("❌ Please configure API keys in the sidebar.")
    else:
        with st.status("🎬 Running Tensorlake pipeline...", expanded=True) as status:
            try:
                input_data = CrawlInput(
                    url=article_url,
                    max_depth=max_depth,
                    max_links=1,
                )

                request = run_local_application(podcast_agent, input_data)
                audio_file = request.output()
                audio_bytes = audio_file.content

                status.update(
                    label="✅ Podcast generated successfully!",
                    state="complete",
                )

                st.markdown("---")
                st.success("🎉 Your podcast is ready!")

                col_a, col_b = st.columns([2, 1])

                with col_a:
                    st.subheader("🎧 Podcast Audio")
                    st.audio(audio_bytes, format="audio/mp3")

                with col_b:
                    st.subheader("📥 Download")
                    st.download_button(
                        "Download MP3",
                        data=audio_bytes,
                        file_name="podcast_audio.mp3",
                        mime="audio/mpeg",
                        type="primary",
                    )

            except Exception as e:
                status.update(label="❌ Pipeline failed", state="error")
                st.error(str(e))
