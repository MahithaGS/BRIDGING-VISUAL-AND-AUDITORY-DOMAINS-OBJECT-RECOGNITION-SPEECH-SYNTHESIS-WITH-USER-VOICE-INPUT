# BRIDGING-VISUAL-AND-AUDITORY-DOMAINS-OBJECT-RECOGNITION-SPEECH-SYNTHESIS-WITH-USER-VOICE-INPUT
🔍 Project Overview

This project enhances accessibility for visually impaired users by integrating real-time object recognition and speech synthesis using YOLO V8 and Text-to-Speech (TTS) engines. It enables hands-free interaction through user voice input for seamless navigation.

📌 Features

✔ Real-time object detection using YOLO V8
✔ Speech synthesis to describe detected objects
✔ Voice input for hands-free operation
✔ QR Code Audio Output for accessibility
✔ Pre-trained models for fast inference

🏢 Project Structure

Bridging-Visual-and-Auditory-Domains/
│── README.md                # Project overview, setup instructions, and usage
│── .gitignore               # Files to ignore in version control
│── requirements.txt         # Dependencies (YOLOv8, OpenCV, gTTS, etc.)
│── research_paper/
│   └── Bridging_Visual_and_Auditory_Domains.pdf  
│   └── Bridging_Visual_and_Auditory_Domains.docx  
│── src/                     
│   └── main.py              # Main script to run the model
│   └── object_detection.py   # YOLO-based object detection
│   └── speech_synthesis.py   # Converts text to speech
│   └── voice_input.py        # Handles user voice commands
│── models/                   
│   └── yolov8_model.pth      # YOLO V8 model
│   └── tts_model.pth         # Text-to-Speech model
│── data/                    
│   └── images/               # Test images
│   └── audio/                # Generated audio files
│── results/                  
│   └── output_images/        # Detected objects with bounding boxes
│   └── output_audio/         # Audio descriptions
│── LICENSE                   

🚀 Installation & Setup

Prerequisites

Ensure you have Python 3.8+ installed.

Clone the Repository

git clone https://github.com/MahithaGS/Bridging-Visual-and-Auditory-Domains.git
cd Bridging-Visual-and-Auditory-Domains

Install Dependencies

pip install -r requirements.txt

🏃‍♂️ Running the Project

Run Object Detection & Speech Synthesis

python src/main.py

This will:✔ Initiates on a Voice Command ✔ Capture an image using a camera 📷✔ Detect objects using YOLO V8 🎯✔ Convert detected objects into speech 🎧

📊 Results & Performance

The model successfully detects objects and describes them via speech synthesis.

Accuracy improves with better lighting and higher-resolution images.

🛠 Technologies Used

YOLO V8 - Real-time Object Detection

gTTS (Google Text-to-Speech) - Converts text to voice

SpeechRecognition - Processes user voice input

OpenCV - Image processing

🔮 Future Improvements

Real-time navigation assistance 📍

Integration with smart glasses 🕶

Multi-language support 🌍

📧 Contact

For any questions, reach out to:✉ mahithags.23@example.com📍 GitHub Profile : https://github.com/MahithaGS
