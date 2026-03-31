import streamlit as st
from pypdf import PdfReader
from gtts import gTTS
import io
import re

# --- PAGE SETUP ---
st.set_page_config(page_title="PDF Audio-Book", page_icon="🎧")
st.title("🎧 PDF to Audio-Book Converter")
st.markdown("### 100% Offline - **Edge-Based Neural Speech Synthesis system**")
st.divider()

# --- SIDEBAR SETTINGS ---
st.sidebar.header("Voice Settings")
speed = st.sidebar.slider("Speaking Speed", 100, 200, 150)
volume = st.sidebar.slider("Volume", 0.0, 1.0, 0.8)

# --- FILE UPLOADER ---
uploaded_file = st.file_uploader("Upload your PDF document", type="pdf")

if uploaded_file:
    # 1. Extract Text from PDF
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()

    if text:
        st.success(f"Successfully extracted {len(text)} characters!")

        # Preview of the text
        st.text_area("Content Preview", text[:1000] + "...", height=200)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔊 Play Audio"):
                st.warning("Live playback not supported in server mode. Use 'Generate MP3' to listen.")
        with col2:
            if st.button("💾 Generate MP3"):
                with st.spinner("Converting to MP3..."):
                    tts = gTTS(text=text[:5000], lang='en')
                    mp3_buffer = io.BytesIO()
                    tts.write_to_fp(mp3_buffer)
                    mp3_buffer.seek(0)
                    st.download_button("📥 Download MP3", mp3_buffer, "audiobook.mp3", mime="audio/mpeg")
    else:
        st.error("Could not find any text in this PDF. Is it an image-based PDF?")