import streamlit as st
from utils import predict, get_recommendation

# Page config
st.set_page_config(page_title="RuralCare AI", page_icon="🩺", layout="centered")

# Custom CSS (GREEN theme + clean)
st.markdown("""
<style>
/* Background */
.stApp {
    background: linear-gradient(135deg, #e8f5e9, #c8e6c9);
}

/* Title */
.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #1b5e20;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #2e7d32;
    margin-bottom: 25px;
}

/* Button */
.stButton>button {
    background-color: #2e7d32;
    color: white;
    font-size: 18px;
    border-radius: 10px;
    padding: 10px;
    width: 100%;
}

/* Result box */
.result {
    background: #ffffff;
    padding: 20px;
    border-radius: 12px;
    margin-top: 20px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🩺 RuralCare AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Smart Symptom Checker for Rural Healthcare</div>', unsafe_allow_html=True)

st.write("### Select your symptoms")

# Symptom inputs (no box wrapping)
col1, col2 = st.columns(2)

with col1:
    fever = st.checkbox("🤒 Fever")
    cough = st.checkbox("😷 Cough")
    headache = st.checkbox("🤕 Headache")

with col2:
    fatigue = st.checkbox("😴 Fatigue")
    nausea = st.checkbox("🤢 Nausea")
    body_pain = st.checkbox("💪 Body Pain")

st.write("")

# Button
if st.button("🔍 Analyze Symptoms"):
    symptoms = [
        int(fever),
        int(cough),
        int(headache),
        int(fatigue),
        int(nausea),
        int(body_pain)
    ]

    with st.spinner("Analyzing..."):
        result = predict(symptoms)
        recommendation = get_recommendation(result)

    # Severity logic
    if result in ["Covid", "Dengue", "Pneumonia", "Typhoid"]:
        severity = "🔴 High"
    elif result in ["Flu", "Bronchitis"]:
        severity = "🟡 Medium"
    else:
        severity = "🟢 Low"

    # Result display (single clean box)
    st.markdown('<div class="result">', unsafe_allow_html=True)

    st.success(f"🩺 Condition: {result}")
    st.warning(f"⚠️ Severity: {severity}")
    st.info(f"💡 Advice: {recommendation}")

    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("🌍 Built for SDG 3: Good Health & Well-being")
