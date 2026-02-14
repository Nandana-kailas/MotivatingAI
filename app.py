import cv2
import os
import random
import time
import pygame
from fer import FER

# ---------------- AUDIO SETUP ----------------
pygame.mixer.init()
pygame.mixer.music.set_volume(1.0)

AUDIO_BASE = "audio"
ANALYSIS_TIME = 3  # seconds

detector = FER(mtcnn=True)

def play_audio(emotion):
    folder = os.path.join(AUDIO_BASE, emotion)

    if not os.path.exists(folder):
        print("❌ Folder not found!")
        return

    files = [f for f in os.listdir(folder) if f.endswith((".mp3", ".wav"))]
    if not files:
        print("❌ No audio files!")
        return

    file = random.choice(files)
    path = os.path.join(folder, file)

    print("Playing:", path)
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.5)

    print("✅ Audio finished")


# ---------------- CAMERA ----------------
cap = cv2.VideoCapture(0)

print("Emotion Bot Running... Press Q to quit")

while True:

    sad_scores = []
    happy_scores = []
    neutral_scores = []
    face_detected_frames = 0

    start_time = time.time()

    print("\n🎥 Show your emotion...")

    while time.time() - start_time < ANALYSIS_TIME:
        ret, frame = cap.read()
        if not ret:
            break

        result = detector.detect_emotions(frame)

        if result:
            emotions = result[0]["emotions"]

            sad_scores.append(emotions["sad"])
            happy_scores.append(emotions["happy"])
            neutral_scores.append(emotions["neutral"])
            face_detected_frames += 1

        cv2.putText(frame, "Analyzing...",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 255),
                    2)

        cv2.imshow("Emotion Bot", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            cap.release()
            cv2.destroyAllWindows()
            pygame.mixer.quit()
            exit()

    # ---------------- NO FACE = LAZY ----------------
    if face_detected_frames < 5:
        final_emotion = "lazy"
        print("📱 No proper face detected → LAZY")

    else:
        avg_sad = sum(sad_scores) / len(sad_scores)
        avg_happy = sum(happy_scores) / len(happy_scores)
        avg_neutral = sum(neutral_scores) / len(neutral_scores)

        print(f"Sad: {avg_sad:.2f} | Happy: {avg_happy:.2f} | Neutral: {avg_neutral:.2f}")

        # ---------------- NEW LOGIC ----------------
        # HAPPY must be clearly dominant
        if avg_happy > 0.6 and avg_happy > avg_sad and avg_happy > avg_neutral:
            final_emotion = "happy"

        # SAD includes both SAD and NEUTRAL
        elif (avg_sad > 0.4) or (avg_neutral > 0.5):
            final_emotion = "sad"

        else:
            final_emotion = "lazy"

    print("🔥 Final Emotion:", final_emotion.upper())

    # ---------------- DISPLAY RESULT ----------------
    ret, frame = cap.read()
    cv2.rectangle(frame, (0, 0), (frame.shape[1], 80), (0, 0, 0), -1)

    cv2.putText(frame,
                f"Detected: {final_emotion.upper()}",
                (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2)

    cv2.imshow("Emotion Bot", frame)
    cv2.waitKey(2000)

    play_audio(final_emotion)

    print("🔁 Ready for next emotion...")

cap.release()
cv2.destroyAllWindows()
pygame.mixer.quit()