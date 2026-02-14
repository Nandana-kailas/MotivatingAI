import streamlit as st
import cv2
import numpy as np
from fer import FER
import os
import random

st.title("🎭 Emotion-Based Malayalam Dialogue Bot")

detector = FER(mtcnn=True)

uploaded_file = st.file_uploader("Upload your image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:

    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)

    result = detector.detect_emotions(img)

    if result:
        emotions = result[0]["emotions"]

        happy = emotions["happy"]
        sad = emotions["sad"]
        neutral = emotions["neutral"]
        surprise = emotions["surprise"]

        if happy > 0.6:
            final_emotion = "happy"
        elif surprise > 0.5:
            final_emotion = "surprise"
        elif sad > 0.4 or neutral > 0.5:
            final_emotion = "sad"
        else:
            final_emotion = "lazy"

        st.image(img, channels="BGR")
        st.success(f"Detected Emotion: {final_emotion.upper()}")

        # Play audio
        folder = f"audio/{final_emotion}"
        if os.path.exists(folder):
            files = [f for f in os.listdir(folder) if f.endswith((".mp3", ".wav"))]
            if files:
                audio_file = random.choice(files)
                audio_path = os.path.join(folder, audio_file)

                with open(audio_path, "rb") as f:
                    audio_bytes = f.read()

                st.audio(audio_bytes)

    else:
        st.warning("No face detected")