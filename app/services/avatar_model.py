import os
import numpy as np
import onnxruntime as ort
from PIL import Image
import cv2

# === Pre/Post Processing Helpers ===
def preprocess_img_for_onnx(img_path: str, size: int = 512) -> np.ndarray:
    img = Image.open(img_path).convert("RGB")
    img = img.resize((size, size))
    arr = np.array(img).astype("float32") / 127.5 - 1.0   # scale to [-1,1]
    arr = np.expand_dims(arr, axis=0)  # shape: [1, H, W, 3]
    return arr

def postprocess_output(onnx_output) -> Image.Image:
    out = onnx_output[0][0]  # shape: [H, W, 3]
    out = (out + 1) / 2      # [-1,1] -> [0,1]
    out = np.clip(out, 0, 1)
    out = (out * 255).astype("uint8")
    return Image.fromarray(out)

# === Avatar Generation Function using ONNX ===
def generate_avatar(path: str, style: str = "Hayao") -> str:
    # Map style to ONNX model file
    style_to_model = {
        "Hayao": "app/models/AnimeGANv2_Hayao.onnx",
        "Shinkai": "app/models/AnimeGANv2_Shinkai.onnx",
        "Paprika": "app/models/AnimeGANv2_Paprika.onnx",
    }

    model_path = style_to_model.get(style)
    if model_path is None or not os.path.exists(model_path):
        raise FileNotFoundError(f"ONNX model not found for style '{style}': {model_path}")

    # Preprocess
    input_tensor = preprocess_img_for_onnx(path)

    # Load model
    session = ort.InferenceSession(model_path, providers=["CPUExecutionProvider"])
    input_name = session.get_inputs()[0].name
    output_name = session.get_outputs()[0].name

    # Run inference
    onnx_out = session.run([output_name], {input_name: input_tensor})

    # Postprocess
    output_img = postprocess_output(onnx_out)

    # Save output
    output_path = path.replace("temp_bg_removed", "temp_avatar").replace(".jpg", ".png")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    output_img.save(output_path)

    return output_path
