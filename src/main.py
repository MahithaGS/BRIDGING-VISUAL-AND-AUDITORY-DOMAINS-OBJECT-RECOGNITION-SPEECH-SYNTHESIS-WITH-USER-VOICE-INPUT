from object_detection import detect_objects
from speech_synthesis import speak
from voice_input import listen_for_commands
import cv2

# Initialize YOLO model (YOLO-based object detection)
cap = cv2.VideoCapture(0)

# Main function to assist blind people
def assist_blind_people():
    while True:
        print("Listening for commands...")

        command = listen_for_commands()

        if command.lower() == "describe scene":
            ret, frame = cap.read()
            if not ret:
                speak("Sorry, I could not capture the image.")
                continue
            detections = detect_objects(frame)
            description = "I see: "
            if detections:
                for detection in detections:
                    description += f"{detection['class_name']} "
            else:
                description += "nothing."
            speak(description)
        elif command.lower() == "exit":
            speak("Exiting the application.")
            break
        else:
            speak("Unknown command. Please say 'describe scene' or 'exit'.")

    cap.release()

# Run the assist function
if __name__ == "__main__":
    assist_blind_people()

