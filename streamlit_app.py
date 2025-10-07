import streamlit as st
from PIL import Image
import os
import tempfile

from app.services.validation import validate_image
from app.services.face_detection import detect_face
from app.services.preprocessing import preprocess_face
from app.services.background import remove_background
from app.services.avatar_model import generate_avatar
from app.services.postprocess import finalize_avatar


# Page config
st.set_page_config(page_title="Avatar Generator", layout="wide")

st.title("🎭 AI Avatar Generator")
st.write("Upload a human photo and generate a cartoon-style avatar.")

# Upload section
uploaded_file = st.file_uploader("Upload Image (JPEG/PNG)", type=["jpg", "jpeg", "png"])

# Avatar style selection
style = st.selectbox("Choose Avatar Style", ["Hayao", "Shinkai", "Paprika", "Hosoda"])

if uploaded_file is not None:
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
        temp_file.write(uploaded_file.read())
        input_path = temp_file.name

    # Display original uploaded image
    st.image(Image.open(input_path), caption="Uploaded Image", width=400)

    if st.button("Generate Avatar"):
        with st.spinner("Processing..."):
            # Step 1: Validate resolution
            if not validate_image(input_path):
                st.error("❌ Invalid image. Please upload a clear, high-resolution face image.")

            # Step 2: Face detection
            elif not detect_face(input_path):
                st.warning("⚠️ No human face detected. Please upload a photo containing a clear, front-facing human face.")

            # Step 3: Hosoda unavailable
            elif style == "Hosoda":
                st.error("⚠️ Hosoda style is not available yet. Please select Hayao, Shinkai, or Paprika.")

            else:
                try:
                    # Step 4: Preprocess
                    preprocessed_path = preprocess_face(input_path)

                    # Step 5: Background Removal
                    bg_removed_path = remove_background(preprocessed_path)

                    # Step 6: Avatar Generation
                    avatar_path = generate_avatar(bg_removed_path, style=style)

                    # Step 7: Postprocess
                    output_path = finalize_avatar(avatar_path, "app/static/output")

                    # Display results side by side
                    col1, col2 = st.columns(2)
                    with col1:
                        st.image(Image.open(input_path), caption="Original", width=400)
                    with col2:
                        st.image(Image.open(output_path), caption=f"Avatar ({style} Style)", width=400)


                    st.success("✅ Avatar generated successfully!")
                    st.download_button(
                        "Download Avatar",
                        data=open(output_path, "rb").read(),
                        file_name=f"avatar_{style.lower()}.png",
                        mime="image/png"
                    )
                except FileNotFoundError as e:
                    st.error(f"❌ Model not found: {e}")
                except Exception as e:
                    st.error(f"⚠️ An error occurred during avatar generation: {e}")
