from rembg import remove
import cv2
import numpy as np
import os

def remove_background(path: str) -> str:
    image = cv2.imread(path)
    output = remove(image)

    output_path = path.replace("temp_preprocessed", "temp_bg_removed")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cv2.imwrite(output_path, output)

    return output_path
