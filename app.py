import streamlit as st
import numpy as np
import tensorflow as tf
import mne
import tempfile

# Load model
model = tf.keras.models.load_model("eeg_model.h5")

st.title("EEG Seizure Detection System")

uploaded_file = st.file_uploader("Upload EEG (.edf file)")

def preprocess_eeg(file):
    raw = mne.io.read_raw_edf(file, preload=True)
    data = raw.get_data()

    # Normalize
    data = (data - np.mean(data)) / np.std(data)

    # Adjust based on model input
    data = data[:, :5000]

    data = data.reshape(1, data.shape[0], data.shape[1], 1)

    return data

if uploaded_file is not None:
    st.write("Processing...")

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        path = tmp.name

    try:
        eeg = preprocess_eeg(path)

        pred = model.predict(eeg)
        confidence = float(pred[0][0])

        if confidence > 0.5:
            st.error("⚠️ Seizure Detected")
        else:
            st.success("✅ No Seizure Detected")

        st.write(f"Confidence: {confidence:.2f}")

    except Exception as e:
        st.error(f"Error: {e}")
