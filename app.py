import streamlit as st
from PIL import Image
from streamlit_webrtc import webrtc_streamer
import time

st.set_page_config(page_title="Vida Advanced Demo", layout="wide")
st.title("🧠 VIDA: Multimodal Agentic AI Intake")
st.markdown("_An emotional intelligence assistant for mental health triage._")
st.markdown("---")

# Sidebar
st.sidebar.header("Select Mode")
mode = st.sidebar.radio("Mode", ["Live Demo", "Agent Logs", "Clinician Summary"])

if mode == "Live Demo":
    st.header("🎥 Live Video Capture")
    st.markdown("Recording and analyzing facial emotion and gaze...")
    webrtc_streamer(key="video")

    st.header("🎙️ Voice Recording (coming soon)")
    st.markdown("Record and transcribe patient voice input")

    st.header("💬 Text Prompt")
    user_input = st.text_input("Patient response:", "")
    if user_input:
        st.write(f"Transcribed Text: {user_input}")
        # Here you'd run your NLP Agent

elif mode == "Agent Logs":
    st.header("🧠 Agent Outputs (Simulated)")
    st.json({
        "Emotion Agent": {"emotion": "Sad", "confidence": 0.76},
        "Speech Agent": {"tone": "Flat", "speech_rate": "Slow"},
        "Gaze Agent": {"gaze_direction": "Downcast", "blinks_per_min": 12},
        "NLP Agent": {"sentiment": "Negative", "keywords": ["anxiety", "tired"]}
    })

elif mode == "Clinician Summary":
    st.header("📋 Final Editable Summary")
    st.text_area("Summary:", "Patient displays signs of low mood with flat affect and downcast gaze.", height=200)
    st.button("Submit Summary")




