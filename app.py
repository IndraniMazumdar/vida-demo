import streamlit as st
from PIL import Image
import time

st.set_page_config(page_title="Vida Demo", layout="wide")

st.title("🧠 Vida – AI Intake Simulation")
st.markdown("_An emotional intelligence assistant for mental health triage._")
st.markdown("---")

# Patient Selector
st.sidebar.header("📋 Choose a Sample Patient")
selected_patient = st.sidebar.selectbox("Select Patient:", ["Patient A", "Patient B", "Patient C"])

# Define sample profiles
if selected_patient == "Patient A":
    avatar_path = "static/avatar.png"
    response = "Just been tired, not sleeping well."
    follow_up = "😴 How has your sleep been recently?"
    emotion = "Low Energy"
    sentiment = "Flat"
    gaze = "Downcast"
    summary = """
Patient appears fatigued with minimal vocal variation and downward gaze.
Reports sleep disturbances. No immediate emotional spikes.
Risk level: Low. Recommend monitoring and routine check-in.
"""

elif selected_patient == "Patient B":
    avatar_path = "static/avatar.png"
    response = "I’ve been anxious lately and on edge."
    follow_up = "😟 Can you describe what triggers your anxiety lately?"
    emotion = "Mild Anxiety"
    sentiment = "Negative"
    gaze = "Darting"
    summary = """
Patient shows signs of mild anxiety and restlessness.
Rapid eye movement and elevated vocal tension observed.
Risk level: Moderate. Recommend further screening.
"""

elif selected_patient == "Patient C":
    avatar_path = "static/avatar.png"
    response = "I can’t focus on anything at work or home."
    follow_up = "🧠 Have you been struggling with attention at work or school?"
    emotion = "Distracted"
    sentiment = "Flat"
    gaze = "Unfocused"
    summary = """
Patient reports cognitive distraction and trouble concentrating.
Non-verbal indicators show disengaged posture and low vocal clarity.
Risk level: Low to Moderate. Recommend cognitive screening.
"""

# Intake Layout
st.header("🧍‍♀️ Patient Check-in")

col1, col2 = st.columns([1, 2])
with col1:
    st.image(avatar_path, width=220)
    st.markdown("👋 *Hi, I’m Vida. How have you been feeling lately?*")

with col2:
    st.markdown("### 💬 Patient Response")
    st.markdown(f"🗣️ _{response}_")

# Follow-up display
st.markdown(
    f"""
    <div style='padding: 15px; background-color: #f0f2f6; border-radius: 10px; margin-top: 10px;'>
        <b>Follow-up Question:</b><br>{follow_up}
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")
st.header("🔍 AI-Detected Emotional Insights")

if st.button("🧠 Run Emotional Analysis"):
    with st.spinner("Analyzing patient input..."):
        time.sleep(2)
    st.success("Analysis complete.")

    col3, col4, col5 = st.columns(3)
    with col3:
        st.metric("😐 Facial Emotion", emotion)
        st.metric("📝 Sentiment", sentiment)
    with col4:
        st.metric("🗣️ Tone of Voice", "Flat")
        st.metric("👁️ Gaze", gaze)
    with col5:
        st.metric("⏱️ Speech Rate", "Slow")
        st.metric("💭 Cognitive Load", "Moderate")

# Summary Section
st.markdown("---")
st.header("📋 Editable Clinician Summary")

with st.expander("📝 View Generated Summary"):
    st.text_area("Generated Report:", summary.strip(), height=180)

st.button("📤 Export Summary (Coming Soon)")



