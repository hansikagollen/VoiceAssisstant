import streamlit as st
import speech_recognition as sr
from voice import speak_telugu

st.set_page_config(page_title="Telugu Scheme Assistant")

st.title("🏛️ Telugu Voice-Based Government Scheme Agent")

audio_bytes = st.audio_input("🎤 Tap and speak Telugu")

if audio_bytes is not None:
    # 🔊 PLAY BACK WHAT USER SPOKE
    st.audio(audio_bytes, format="audio/wav")

    # Save audio to file
    with open("input.wav", "wb") as f:
        f.write(audio_bytes.getvalue())

    # Speech to text
    r = sr.Recognizer()
    with sr.AudioFile("input.wav") as source:
        audio_data = r.record(source)

    try:
        text = r.recognize_google(audio_data, language="te-IN")
        st.success(f"📝 You said: {text}")

        reply = f"మీ సమాచారం అందింది: {text}"
        st.info(reply)

        speak_telugu(reply)

    except sr.UnknownValueError:
        st.error("❌ Telugu speech not recognized. Please try again.")
