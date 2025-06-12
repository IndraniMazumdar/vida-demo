import streamlit as st
from PIL import Image
import time

st.set_page_config(page_title="Vida Demo", layout="wide")

st.title("Vida – AI Intake Simulation")
st.markdown("_An emotional intelligence assistant for mental health triage._")
st.markdown("---")

# Intake Section
st.header("🧍‍♀️ Patient Check-in")

col1, col2 = st.columns([1, 2])
with col1:
    st.image("static/avatar.png", width=220)
    st.markdown("👋 *Hi, I’m Vida. How have you been feeling lately?*")

with col2:
    user_input = st.text_area("Patient Response:")

# Adaptive Follow-up
follow_up = ""
if user_input:
    lowered = user_input.lower()
    if "anxious" in lowered or "anxiety" in lowered:
        follow_up = "Can you describe what triggers your anxiety lately?"
    elif "tired" in lowered or "fatigue" in lowered or "sleep" in lowered:
        follow_up = "How has your sleep been recently?"
    elif "unfocused" in lowered or "concentration" in lowered or "attention" in lowered:
        follow_up = "Have you been struggling with attention at work or school?"
    else:
        follow_up = "Thank you for sharing. Can you tell me more about how your days have been lately?"

    # Display follow-up in a soft card
    st.markdown(
        f"""
        <div style='padding: 15px; background-color: #f0f2f6; border-radius: 10px; margin-top: 10px;'>
            <b>Follow-up Question:</b><br>{follow_up}
        </div>
        """,
        unsafe_allow_html=True
    )

# Divider
st.markdown("---")

# Analysis Section
st.header("AI-Detected Emotional Insights")

if st.button("Run Emotional Analysis"):
    with st.spinner("Analyzing patient input..."):
        time.sleep(2)
    st.success("Analysis complete.")

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

    with st.expander("📋 View Editable Clinician Summary"):
        st.text_area("Generated Report:", 
            """
Patient presents with signs of mild anxiety and fatigue.
Non-verbal cues: low vocal energy, averted gaze, and slow speech rate.
Reports sleep disturbances and concentration difficulties.
Risk level: Low to Moderate. Recommend follow-up and further screening.
""", height=180)

    st.button("Export Summary (Coming Soon)")



