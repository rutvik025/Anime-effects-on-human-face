import cv2
import os

def finalize_avatar(path: str, output_dir: str) -> str:
    # Ensure output folder exists
    os.makedirs(output_dir, exist_ok=True)

    image = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    final_path = os.path.join(output_dir, "avatar.png")
    cv2.imwrite(final_path, image)
    return final_path
