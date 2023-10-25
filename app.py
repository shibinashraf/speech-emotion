import streamlit as st
import requests

# API endpoint and API key
API_URL = "https://api-inference.huggingface.co/models/ehcalabres/wav2vec2-lg-xlsr-en-speech-emotion-recognition"
API_KEY = "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"

st.title("Speech Emotion Recognition")

# Upload audio file
audio_file = st.file_uploader("Upload an audio file", type=["wav"])

if audio_file:
    # Read the uploaded audio file
    audio_data = audio_file.read()

    # Make an API request
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.post(API_URL, headers=headers, data=audio_data)

    if response.status_code == 200:
        results = response.json()
        
        # The result is a list, and you might want to access the first item (assuming there is only one)
        if results:
            emotion = results[0]["label"]
            st.success(f"Detected Emotion: {emotion}")
        else:
            st.error("No emotion detected in the provided audio file.")
    else:
        st.error("Error: Unable to recognize emotion from the provided audio file.")
