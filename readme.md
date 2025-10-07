# 🎨 AnimeGANv2 Streamlit App  

Transform your photos into stunning anime-style artwork using **AnimeGANv2** models — all wrapped in a simple and interactive **Streamlit web app**.  

---

## 🚀 Overview  
This project provides an easy-to-use interface for **anime-style image transformation**.  
It leverages **pretrained ONNX models** (Hayao, Paprika, Shinkai) to convert real-world images into stylized anime versions directly in your browser.  

---

## 🧠 Features  
- 🧩 **Multiple Styles** – Supports Hayao, Shinkai, and Paprika model variants.  
- 💻 **Streamlit UI** – Simple, interactive frontend for real-time transformation.  
- ⚡ **ONNX Runtime** – Fast and lightweight inference using optimized models.  
- 🧍 **Face Detection & Preprocessing** – Automatically handles alignment and validation.  
- 🖼️ **High-Quality Outputs** – Generates clean, stylized anime portraits.  

---

## 🗂️ Project Structure  

eeproject/
│
├── streamlit_app.py # Main Streamlit application
├── requirements.txt # Dependencies
├── app/
│ ├── models/ # ONNX pretrained AnimeGANv2 models
│ │ ├── AnimeGANv2_Hayao.onnx
│ │ ├── AnimeGANv2_Paprika.onnx
│ │ └── AnimeGANv2_Shinkai.onnx
│ ├── services/ # Core service modules
│ │ ├── avatar_model.py
│ │ ├── background.py
│ │ ├── face_detection.py
│ │ ├── postprocess.py
│ │ ├── preprocessing.py
│ │ └── validation.py


---

## 🧰 Tech Stack  
- **Python 3.10+**  
- **Streamlit** – for frontend UI  
- **ONNX Runtime** – for model inference  
- **OpenCV, NumPy** – for image processing  
- **Pillow** – for image manipulation  

---

## ⚙️ Installation & Setup  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/rutvik025/Anime-effects-on-human-face.git
cd Anime-effects-on-human-face.


### 2️⃣ Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows use venv\Scripts\activate

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt

### ▶️ Run the Application
```bash
Start the Streamlit app:
streamlit run streamlit_app.py

Then open your browser and navigate to:
👉 http://localhost:8501