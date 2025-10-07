import cv2
import os

def preprocess_face(path: str) -> str:
    # Simple preprocessing (resize + crop center)
    image = cv2.imread(path)
    h, w = image.shape[:2]
    crop_size = min(h, w)
    x = (w - crop_size) // 2
    y = (h - crop_size) // 2
    cropped = image[y:y+crop_size, x:x+crop_size]
    resized = cv2.resize(cropped, (512, 512))

    output_path = path.replace("input", "temp_preprocessed")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cv2.imwrite(output_path, resized)

    return output_path
