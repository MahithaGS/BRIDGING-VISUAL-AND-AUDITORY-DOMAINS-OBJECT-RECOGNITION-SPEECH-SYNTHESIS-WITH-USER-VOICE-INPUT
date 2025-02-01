from gtts import gTTS
import os
import time

# Function for real-time TTS (text-to-speech)
def speak(text):
    speech = gTTS(text=text, lang='en', slow=False)
    file_name = "temp_output.mp3"
    speech.save(file_name)
    os.system(f"start {file_name}")  # For Windows
    time.sleep(1)
    os.remove(file_name)

