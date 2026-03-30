# 🧠 AI Product Identifier for Visually Impaired


## 👨‍🎓 Student Details
- **Name:** Pradeep Nain
- **GitHub:** https://github.com/Flanker745
- **Branch:** CSE (AI/ML)  
- **Year:** 1st Year  
- **University:** VIT Bhopal University  

---

## 📌 Overview

This project is a **real-time object detection system** designed to assist visually impaired individuals by identifying objects through a camera and announcing their names using speech.

The system uses Artificial Intelligence and Machine Learning techniques to detect everyday objects and provide audio feedback without any user interaction.

---

## 🎯 Features

* 📷 Real-time object detection using webcam
* 🔲 Bounding boxes around detected objects
* 🔊 Automatic voice output (no user input required)
* ⚡ Optimized for CPU (works without GPU)
* 🧠 Uses pre-trained AI model
* 🧱 Object-Oriented Programming (OOP) structure

---

## 🧠 Technologies Used

* Python
* YOLOv8
* OpenCV
* pyttsx3

---

## 📂 Project Structure

```
blind_product_ai/
│
├── main.py          # Main application
├── detector.py      # Object detection logic
├── speaker.py       # Text-to-speech module
├── requirements.txt # Dependencies
├── yolov8n.pt
├── .gitignore
├── README.md

```

---

## ⚙️ Installation

### 1. Clone repository

```
git clone https://github.com/Flanker745/blind_product_ai.git
cd blind_product_ai
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```
### 3. ⚙️ PyTorch Installation (CPU Users)

```
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

---

### 3. Install system dependency (Linux only)

```
sudo apt install espeak espeak-ng
```

---

## ▶️ How to Run

```
python main.py
```

---

## 🧪 Output

* Opens webcam
* Detects object
* Draws bounding box
* Speaks:

> "I detected a bottle"

---

## 🧠 How It Works

1. Camera captures live video
2. YOLOv8 model detects objects
3. Detected object name is extracted
4. pyttsx3 converts text → speech
5. Output is spoken to user

---

## ⚡ Performance Optimization

* Frame skipping to reduce CPU load
* Frame resizing (640x480)
* Limited detections per frame
* Speech cooldown to avoid repetition

---

## 📊 Dataset

The model uses a **pre-trained COCO dataset**, which includes 80+ common object categories such as:

* bottle
* cup
* laptop
* mobile phone

No custom dataset training is required.

---

## 🚧 Challenges Faced

* Lag on CPU systems
* Repeated speech output
* Window not closing properly
* Speech engine dependency (Linux)

---

## 👨‍💻 Author

* Pradeep Nain

---

## ⭐ Conclusion

This project demonstrates how AI can be used to solve real-world problems and improve accessibility for visually impaired individuals using computer vision and speech technologies.
