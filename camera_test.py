import cv2
from deepface import DeepFace

cap = cv2.VideoCapture(0)

print("Camera Test Running... Press Q to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera not working")
        break

    try:
        result = DeepFace.analyze(
            frame,
            actions=["emotion"],
            enforce_detection=False
        )

        detected = result[0]["dominant_emotion"]

        cv2.putText(
            frame,
            f"Raw Emotion: {detected}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        print("Detected:", detected)

    except Exception as e:
        print("Error:", e)

    cv2.imshow("Camera Test", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
