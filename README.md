🎭 Emotion Bot – Face Emotion Based Audio Player

An AI-powered real-time emotion detection system that analyzes facial expressions using a webcam and plays emotion-mapped audio responses.

This project uses computer vision and deep learning to detect Happy, Sad, or Lazy emotions and plays corresponding audio clips.

🚀 Features

🎥 Real-time face detection using webcam

🧠 Emotion recognition using deep learning

🔊 Automatic audio playback based on detected emotion

📊 3-second emotion averaging for stable detection

💤 Detects "Lazy" when no proper face is detected

🛠️ Tech Stack

Python 3.10+

OpenCV – Webcam capture & display

FER – Facial emotion recognition

MTCNN – Face detection backend

Pygame – Audio playback

NumPy

📂 Project Structure
Emotion-Bot/
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
git clone https://github.com/your-username/emotion-bot.git
cd emotion-bot

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv


Activate:

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt


If you don’t have requirements.txt, install manually:

pip install opencv-python fer mtcnn pygame numpy

▶️ How It Works

Webcam captures live video.

Face is detected using MTCNN.

Emotions are analyzed using FER.

Scores are averaged over 3 seconds.

Final emotion is classified:

Happy → If dominant (> 0.6 confidence)

Sad → Includes Sad + High Neutral

Lazy → No face detected or low emotion confidence

Corresponding audio is played from audio/<emotion>/.

🎮 Run the Project
python emotion_bot.py


Press Q to quit.

📌 Emotion Logic
Happy → avg_happy > 0.6 and dominant
Sad → avg_sad > 0.4 OR avg_neutral > 0.5
Lazy → No face or weak emotion

🔮 Future Improvements

Add more emotions (Angry, Surprise, Fear)

Add GUI interface

Deploy as a desktop application

Add Malayalam movie dialogue database 🎬

Improve accuracy using custom-trained model

📷 Example Output
Sad: 0.12 | Happy: 0.78 | Neutral: 0.10
🔥 Final Emotion: HAPPY
Playing: audio/happy/dialogue1.mp3

👩‍💻 Authors

Nandana Kailas
KTU Student | AI & Computer Vision Enthusiast

Sharon Elsa Binu
Project Contributor | Development & Testing Support

📄 License

This project is open-source and available under the MIT License.
