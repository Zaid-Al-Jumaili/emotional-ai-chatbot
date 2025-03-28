import streamlit as st
from emotion_model import detect_emotion
from response_generator import generate_dynamic_response
import time

st.set_page_config(page_title="Gemini Emotion Chatbot", page_icon="🤖", layout="centered")

st.markdown("""
    <div style='text-align: center;'>
        <h1>💬 Emotion-Aware AI Chatbot</h1>
        <p style='font-size: 18px;'>Type how you feel and let the AI talk to you emotionally 💙</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

user_input = st.text_input("Type your message here 👇", "", key="input")

if user_input:
    with st.spinner("Analyzing emotion..."):
        emotion, score = detect_emotion(user_input)

    with st.spinner("AI is thinking..."):
        reply = generate_dynamic_response(user_input, emotion)

    st.markdown(f"<div style='color: gray; font-size: 14px;'>Detected Emotion: <b>{emotion}</b></div>", unsafe_allow_html=True)

    ai_display = st.empty()
    typed = ""
    for char in reply:
        typed += char
        ai_display.markdown(f"<div style='background-color: #f3f3f3; padding: 12px; border-radius: 10px; font-size: 16px;'><b>AI:</b> {typed}</div>", unsafe_allow_html=True)
        time.sleep(0.015)
