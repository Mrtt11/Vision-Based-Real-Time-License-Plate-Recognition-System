# detector.py
from ultralytics import YOLO
import cv2

class PlateDetector:
    def __init__(self, weights_path="weights/best.pt"):
        self.model = YOLO(weights_path)

    def detect_plate(self, image):
        results = self.model(image) 
        plates = []

        for r in results:
            for box in r.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                margin = 10
                plate_crop = image[
                    max(0, y1 - margin):y2 + margin,
                    max(0, x1 - margin):x2 + margin
                ]
                plates.append(plate_crop)

        return plates
