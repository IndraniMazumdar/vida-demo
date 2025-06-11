import streamlit as st
from PIL import Image

st.set_page_config(page_title="Vida Demo", layout="wide")

st.sidebar.title("👩🏽‍⚕️ Vida – AI Mental Health Assistant")
st.sidebar.markdown("Simulated emotional intake demo.")

st.title("🎥 AI Intake Simulation")
st.markdown("Meet Vida, your AI assistant. Patients engage in a brief check-in before meeting their clinician.")

# Avatar + Simulated Input
col1, col2 = st.columns([1, 2])
with col1:
    st.image("static/avatar.png", width=250)
    st.markdown("👋 *Hi, I’m Vida. How have you been feeling lately?*")

with col2:
    st.text_area("🎤 Simulated Patient Response (Transcript):", 
                 "I’ve been okay I guess. Just a bit tired and not sleeping great. It’s been hard to concentrate.")

# Simulated "Run Analysis"
if st.button("🧠 Run Emotional Analysis"):
    st.success("Analyzing input...")

    st.markdown("---")
    st.subheader("🔍 AI Insights")

    col3, col4, col5 = st.columns(3)
    with col3:
        st.metric("Facial Emotion", "Mild Anxiety")
        st.metric("Sentiment", "Neutral → Negative")
    with col4:
        st.metric("Tone of Voice", "Flat")
        st.metric("Gaze", "Averted")
    with col5:
        st.metric("Speech Rate", "Slow")
        st.metric("Cognitive Load", "Moderate")

    st.markdown("---")
    st.subheader("📋 Clinician Summary")
    st.text_area("Editable Report:", 
                 """
Patient shows mild anxiety and fatigue.
Low vocal energy and disengaged gaze.
Reports sleep issues and concentration difficulty.
Risk: Low to Moderate. Recommend follow-up.
""", height=200)

    st.success("✅ Summary ready for clinician.")

