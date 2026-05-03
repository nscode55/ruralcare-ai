import streamlit as st
from utils import predict, get_recommendation

st.title("RuralCare AI - Symptom Checker")

st.write("Select your symptoms:")

fever = st.checkbox("Fever")
cough = st.checkbox("Cough")
headache = st.checkbox("Headache")
fatigue = st.checkbox("Fatigue")
nausea = st.checkbox("Nausea")
body_pain = st.checkbox("Body Pain")

if st.button("Check Condition"):
    symptoms = [
        int(fever),
        int(cough),
        int(headache),
        int(fatigue),
        int(nausea),
        int(body_pain)
    ]

    result = predict(symptoms)
    recommendation = get_recommendation(result)

    st.success(f"Possible condition: {result}")
    st.info(f"Advice: {recommendation}")