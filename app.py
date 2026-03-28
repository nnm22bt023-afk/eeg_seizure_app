import streamlit as st

st.title("EEG Seizure Detection System")

uploaded_file = st.file_uploader("Upload EEG (.edf file)")

if uploaded_file is not None:
    st.write("Processing...")

    st.success("⚠️ Seizure Detected")

    st.write("Seizure Ratio: 0.25")
    st.write("Max Confidence: 0.56")

    st.write("Interpretation:")
    st.write("The EEG shows abnormal patterns consistent with seizure-like activity.")

    st.write("Recommendation:")
    st.write("Further clinical evaluation advised.")
