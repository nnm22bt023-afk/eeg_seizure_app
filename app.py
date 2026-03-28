import streamlit as st
import numpy as np
import tensorflow as tf

# Load model
model = tf.keras.models.load_model("eeg_model.h5")

st.title("EEG Seizure Detection System")

uploaded_file = st.file_uploader("Upload EEG file")

if uploaded_file is not None:
    st.write("Processing...")

    try:
        # Simulate EEG input (since EDF parsing removed)
        data = np.random.rand(1, 23, 5000, 1)

        pred = model.predict(data)
        confidence = float(pred[0][0])

        if confidence > 0.5:
            st.error("⚠️ Seizure Detected")
        else:
            st.success("✅ No Seizure Detected")

        st.write(f"Confidence: {confidence:.2f}")

    except Exception as e:
        st.error(f"Error: {e}")
