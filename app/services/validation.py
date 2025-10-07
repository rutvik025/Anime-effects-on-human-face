import cv2

def validate_image(path: str, min_resolution=(200, 200)) -> bool:
    image = cv2.imread(path)
    if image is None:
        return False
    
    h, w = image.shape[:2]
    if h < min_resolution[0] or w < min_resolution[1]:
        return False
    return True
