# app.py (Test-Ready Streamlit UI)

import streamlit as st
from config import settings

st.set_page_config(page_title="AI Content Agent", layout="wide")

st.title("🎥 AI Content Agent (Test Mode)" if settings.TEST_MODE else "🎥 AI Content Agent")

st.markdown("Generate YouTube, TikTok, and Instagram content instantly.")

platform = st.selectbox("Choose Platform", ["YouTube", "TikTok", "Instagram"])
topic = st.text_input("Enter your topic", "How to grow on YouTube in 2025")

if st.button("Generate Content"):
    if settings.TEST_MODE:
        st.success("✅ Test Mode Activated")
        st.markdown("### Title: The YouTube Algorithm Changed Again")
        st.markdown("### Hook: If you're using 2022 tactics on YouTube in 2025… you're invisible.")
        st.markdown("### Script:
1. Intro – The New Game
2. The 3 Growth Levers
3. How Shorts Work
4. AI in Content
5. Call to Action")
        st.markdown("### CTA: Subscribe for weekly growth hacks!")
    else:
        st.warning("🔒 Real mode is not yet configured. Please add your API keys.")