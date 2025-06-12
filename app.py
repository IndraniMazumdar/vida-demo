import streamlit as st
from PIL import Image

st.set_page_config(page_title="Vida Demo", layout="wide")

st.sidebar.title("👩🏽‍⚕️ Vida – AI Mental Health Assistant")
st.sidebar.markdown("This is a simulated demo of Vida's emotional triage capability for mental health clinicians.")

st.title("🧠 AI Intake Simulation")
st.markdown("Meet **Vida**, your intelligent emotional health assistant. Vida engages patients before the first session to help clinicians start with empathy—not paperwork.")

# Avatar + User Input
col1, col2 = st.columns([1, 2])
with col1:
    st.image("static/avatar.png", width=250)
    st.markdown("👋 *Hi, I’m Vida. How have you been feeling lately?*")

with col2:
    user_input = st.text_area("💬 Patient Response:", 
                              "I’ve been okay I guess. Just a bit tired and not sleeping great. It’s been hard to concentrate.")

# Adaptive Follow-up Logic
follow_up = ""
if user_input:
    lowered = user_input.lower()
    if "anxious" in lowered or "anxiety" in lowered:
        follow_up = "😟 Can you describe what triggers your anxiety lately?"
    elif "tired" in lowered or "fatigue" in lowered or "sleep" in lowered:
        follow_up = "😴 How has your sleep been recently?"
    elif "unfocused" in lowered or "concentration" in lowered or "attention" in lowered:
        follow_up = "🧠 Have you been struggling with attention at work or school?"
    else:
        follow_up = "💬 Thank you for sharing. Can you tell me more about how your days have been lately?"

if follow_up:
    st.markdown(f"**Follow-up Question:** {follow_up}")

# Emotional Analysis Button
if st.button("🧠 Run Emotional Analysis"):
    st.success("Analyzing patient input...")

    st.markdown("---")
    st.subheader("🔍 AI-Detected Emotional Insights")

    col3, col4, col5 = st.columns(3)
    with col3:
        st.metric("😐 Facial Emotion", "Mild Anxiety")
        st.metric("📝 Sentiment", "Neutral → Negative")
    with col4:
        st.metric("🗣️ Tone of Voice", "Flat")
        st.metric("👁️ Gaze", "Averted")
    with col5:
        st.metric("⏱️ Speech Rate", "Slow")
        st.metric("💭 Cognitive Load", "Moderate")

    st.markdown("---")
    st.subheader("📋 Editable Clinician Summary")
    st.text_area("Generated Report:", 
                 """
Patient presents with signs of mild anxiety and fatigue.
Non-verbal cues: low vocal energy, averted gaze, and slow speech rate.
Reports sleep disturbances and concentration difficulties.
Risk level: Low to Moderate. Recommend follow-up and further screening.
""", height=200)

    st.success("✅ Emotional triage summary generated.")


