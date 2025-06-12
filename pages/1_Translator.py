from deep_translator import GoogleTranslator
from gtts import gTTS
import streamlit as st
from io import BytesIO
import base64

# Set page config
st.set_page_config(page_title="Multilingual Translator", page_icon="🌍")

# Title
st.title("🌍 Multilingual Text Translator with Audio")

# Language dictionary
languages = {
    "Auto Detect": "auto",
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Chinese (Simplified)": "zh-cn",
    "Japanese": "ja",
    "Kannada": "kn",
    "Tamil": "ta",
    "Telugu": "te",
    "Arabic": "ar",
    "Russian": "ru",
    "Korean": "ko",
    "Urdu": "ur",
    "Italian": "it",
    "Portuguese": "pt",
    "Bengali": "bn",
    "Malayalam": "ml",
}

# Layout
col1, col2 = st.columns(2)

with col1:
    src_lang = st.selectbox("Select Source Language", list(languages.keys()), index=0)
with col2:
    tgt_lang = st.selectbox("Select Target Language", list(languages.keys()), index=1)

# Text input
text = st.text_area("Enter text to translate", height=150)

# Translate button
if st.button("🔄 Translate and Generate Audio") and text:
    try:
        src = languages[src_lang]
        tgt = languages[tgt_lang]

        # Translate using deep_translator
        translated_text = GoogleTranslator(source=src, target=tgt).translate(text)
        st.success("✅ Translation successful!")

        st.markdown("**Translated Text:**")
        st.code(translated_text, language='')

        # Generate Audio
        tts = gTTS(text=translated_text, lang=tgt)
        audio_fp = BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)

        # Play Audio
        st.audio(audio_fp, format='audio/mp3')

        # Download Audio
        b64 = base64.b64encode(audio_fp.read()).decode()
        audio_download_link = f'<a href="data:audio/mp3;base64,{b64}" download="translated_audio.mp3">🎧 Download Audio</a>'
        st.markdown(audio_download_link, unsafe_allow_html=True)

    except Exception as e:
        st.error("❌ An error occurred. Please check your input or internet connection.")
        st.exception(e)

elif not text:
    st.info("💡 Please enter text above and click the button to translate.")
