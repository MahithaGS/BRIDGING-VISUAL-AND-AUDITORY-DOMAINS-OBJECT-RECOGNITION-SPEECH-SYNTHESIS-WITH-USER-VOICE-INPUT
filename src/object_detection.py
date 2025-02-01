from ultralytics import YOLO

# Initialize YOLO model
model = YOLO("yolov8n.pt")

# Function to detect objects and return descriptions
def detect_objects(frame):
    results = model.predict(source=frame)
    detections = []
    if results:
        boxes = results[0].boxes
        names = results[0].names
        for box in boxes:
            class_name = names[int(box.cls)]
            confidence = box.conf.item()  # Convert tensor to float
            detections.append({
                'class_name': class_name,
                'confidence': confidence
            })
    return detections

