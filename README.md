🎭 MOTIVATING AI
👥 Team Name: GEMS



👩‍💻 Team Members

Nandana Kailas – Saintgits College of Engineering

Sharon Elsa Binu – Saintgits College of Engineering

🔗 Hosted Project Link:
https://github.com/Nandana-kailas/MotivatingAI

📌 Project Description

Motivating AI is an AI-powered real-time emotion detection system that analyzes facial expressions using a webcam and automatically plays emotion-mapped Malayalam movie dialogues 🎬.

The system uses Computer Vision and Deep Learning to detect user emotions and respond with humorous or motivational dialogue audio to improve mood and reduce stress.

❗ Problem Statement

In modern office environments, employees often experience high levels of stress, work pressure, and mental fatigue due to tight deadlines, multitasking, and continuous screen exposure.

Although organizations implement stress-management strategies, there is a lack of real-time, emotion-aware systems that can instantly respond to an individual's emotional state during work hours.

💡 Proposed Solution

To address this gap, we developed a lightweight AI-based application that:

Detects facial emotions in real-time using a webcam

Classifies emotional states such as Happy, Sad, or Lazy

Plays appropriate Malayalam movie dialogues to lighten the mood

This project provides quick emotional relief using minimal computational resources while creating a positive and interactive workplace experience.

🚀 Features

🎥 Real-time webcam face detection

🧠 Emotion recognition using Deep Learning

🔊 Automatic audio playback based on detected emotion

📊 3-second emotion averaging for stable detection

💤 Detects "Lazy" when no face is properly detected

💻 Lightweight desktop execution

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
├── app.py
├── requirements.txt
└── README.md

⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/Nandana-kailas/MotivatingAI.git

cd MotivatingAI

2️⃣ Create Virtual Environment (Recommended)

python -m venv venv


Activate (Windows):

venv\Scripts\activate

3️⃣ Install Dependencies

pip install -r requirements.txt


If requirements.txt is missing:

pip install opencv-python fer mtcnn pygame numpy

▶️ Run the Project

python app.py


Press Q to quit the application.

🧠 How It Works

Webcam captures live video feed

Face is detected using MTCNN

Emotions are analyzed using FER

Emotion scores are averaged over 3 seconds

Final emotion is classified

Emotion Classification Logic
Emotion	Condition
Happy	avg_happy > 0.6
Sad	avg_sad > 0.4 OR avg_neutral > 0.5
Lazy	No face detected

After classification, a corresponding Malayalam movie dialogue is played from the audio/ folder.

📷 Example Output
Sad: 0.12 | Happy: 0.78 | Neutral: 0.10  
🔥 Final Emotion: HAPPY  
🔊 Playing: audio/happy/dialogue1.mp3


Demo Output & Results

Screenshot1:   https://github.com/Nandana-kailas/MotivatingAI/blob/main/Screenshot%202026-02-15%20093715.png

Screenshot2:   https://github.com/Nandana-kailas/MotivatingAI/blob/main/Screenshot%202026-02-15%20093728.png

Screenshot3:   https://github.com/Nandana-kailas/MotivatingAI/blob/main/Screenshot%202026-02-15%20093753.png

Screenshot4:   https://github.com/Nandana-kailas/MotivatingAI/blob/main/Screenshot%202026-02-15%20093815.png

🔮 Future Improvements

Add more emotions (Angry, Disgust, Surprise)

Improve detection accuracy

Add graphical user interface (GUI)

Expand Malayalam movie dialogue database 🎬

Convert into desktop executable (.exe)



👩‍💻 Team Contributions

🔹 Sharon Elsa Binu

Core emotion detection logic

Audio integration

Deployment setup

Debugging and testing

🔹 Nandana Kailas

Audio selection and mapping

GitHub management

Documentation preparation

📄 License

This project is open-source and available under the MIT License.
