import streamlit as st

st.set_page_config(page_title="Home - Language Translator", page_icon="🌐")

st.title("🌐 Welcome to the Language Translator App")
st.subheader("Translate text and hear it spoken — in 100+ languages!")

st.markdown("""
## 🧠 Problem Statement
In our increasingly globalized world, **language barriers** often limit access to information, communication, and opportunities. Whether you're traveling, studying abroad, or communicating with someone across the globe, not knowing a language can become a real challenge.

## ✅ What This App Solves
This simple but powerful app allows users to:
- Instantly **translate any text** to over 100 languages.
- **Listen to the translated audio** for proper pronunciation.
- Choose both the **source** and **target** languages manually or use auto-detection.

## 🚀 Features
- User-friendly interface built using **Streamlit**
- Powered by **Google Translate** API and **gTTS (Google Text-to-Speech)**
- Multi-language support for both input and output
- Audio preview and **downloadable voice output**
- Fast, efficient, and lightweight!

## 💼 Use Cases
- Students trying to learn new languages
- Travelers visiting foreign countries
- Customer support or online services requiring multi-language communication
- Personal accessibility for reading foreign content

---
### 👉 Start translating from the sidebar!
""")
