MOTIVATING AI

TEAM NAME: GEMS
TEAM MEMBERS: 1) NANDANA KAILAS- SAINTGITS COLLEGE OF ENGINEERING
              2) SHARON ELSA BINU- SAINTGITS COLLEGE OF ENGINEERING
HOSTED PROJECT LINK: https://github.com/Nandana-kailas/MotivatingAI (GITHUB)  
PROJECT DESCRIPTION:
An AI-powered real-time emotion detection system that analyzes facial expressions using a webcam and plays emotion-mapped Malayalam movie dialogues automatically 🎬
 PROBLEM STATEMENT AND SOLUTION
 In modern office environments, employees often experience high levels of stress, work pressure, and mental fatigue due to tight deadlines, multitasking, and continuous screen exposure. Prolonged stress can negatively impact productivity, emotional well-being, and workplace morale.

Although organizations implement various stress-management strategies, there is a lack of real-time, emotion-aware systems that can instantly respond to an individual’s emotional state during work hours.

To address this gap, we propose a lightweight AI-based web application that uses a webcam to detect employees’ facial emotions in real time. Based on the detected emotion (such as stress, sadness, frustration, or fatigue), the system produces appropriate humorous or well-known motivational movie dialogues to lighten the mood and ease mental pressure.

This project implements a simplified and efficient version of a larger emotion-aware AI concept, focusing on providing quick emotional relief through engaging and relatable dialogue responses. The aim is to create a positive and interactive workplace environment using minimal computational resources.
This project combines Computer Vision + Deep Learning + Audio Playback to create an interactive and entertaining emotion-based response system.

🚀 Features

🎥 Real-time webcam face detection

🧠 Emotion recognition using Deep Learning

🔊 Automatic audio playback based on detected emotion

📊 3-second emotion averaging for stable detection

💤 Detects "Lazy" when no face is properly detected

💻 Lightweight desktop execution (No web framework required)

🛠️ Tech Stack

Python 3.10+

OpenCV – Webcam capture & video processing

FER – Facial emotion recognition

MTCNN – Face detection backend

Pygame – Audio playback

NumPy

📂 Project Structure
MotivatingAI/
│
├── audio/
│   ├── happy/
│   ├── sad/
│   └── lazy/
│
├── emotion_bot.py
├── requirements.txt
└── README.md

⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/Nandana-kailas/MotivatingAI.git
cd MotivatingAI

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv


Activate:
venv\Scripts\activate


3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Run the Project
python app.py

Press Q to quit the application.

🧠 How It Works

Webcam captures live video feed

Face is detected using MTCNN

Emotions are analyzed using FER

Emotion scores are averaged over 3 seconds

Final emotion is classified:

Happy → avg_happy > 0.6

Sad → avg_sad > 0.4 OR avg_neutral > 0.5

Lazy → No face detected or weak emotion
Surprise -> Mouth and eyes wide open
Corresponding Malayalam movie dialogue is played from the audio/ folder

📌 Emotion Logic
Emotion	Condition
Happy	avg_happy > 0.6
Sad	avg_sad > 0.4 OR avg_neutral > 0.5
Lazy	No face detected
📷 Example Output
Sad: 0.12 | Happy: 0.78 | Neutral: 0.10
🔥 Final Emotion: HAPPY
🔊 Playing: audio/happy/dialogue1.mp3

🔮 Future Improvements

Add more emotions (Angry, Disgust)

Add GUI interface

Improve detection accuracy

Add Malayalam movie dialogue database 🎬

Convert into desktop executable (.exe)

👩‍💻 Team Contributions 

Sharon Elsa Binu:

Core emotion detection logic

Audio integration

Deployment setup

Debugging environment issues

Nandana Kailas:

Audio selection and mapping

GitHub management

Documentation preparation

📄 License

This project is open-source under the MIT License.
