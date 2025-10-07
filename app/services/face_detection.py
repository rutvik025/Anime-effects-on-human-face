import cv2
import mediapipe as mp

def detect_face(path: str) -> bool:
    image = cv2.imread(path)
    if image is None:
        return False

    mp_face = mp.solutions.face_detection.FaceDetection()
    results = mp_face.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    return results.detections is not None and len(results.detections) > 0
