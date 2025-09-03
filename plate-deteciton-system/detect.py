from ultralytics import YOLO
import cv2
import easyocr

# 1. Eğittiğin YOLO modelini yükle
model = YOLO("runs_plates/yolov8n-plates/weights/best.pt")

# 2. OCR motoru başlat
reader = easyocr.Reader(['en', 'tr'])

# 3. Test için görüntü dosyası (buraya kamerayı da bağlayabilirsin)
img_path = "test_images/sample2.jpg"
image = cv2.imread(img_path)

# 4. YOLO ile tahmin
results = model.predict(source=image)

for result in results:
    boxes = result.boxes.xyxy.cpu().numpy()  # x1, y1, x2, y2 formatında
    for box in boxes:
        x1, y1, x2, y2 = map(int, box)
        
        # 5. Plakayı kes (crop)
        plate_crop = image[y1:y2, x1:x2]

        # 6. OCR uygula
        ocr_result = reader.readtext(plate_crop)

        print("📌 Plaka bulundu!")
        for (_, text, prob) in ocr_result:
            print(f" → Tahmin: {text} (güven: {prob:.2f})")

        # 7. İstersen ekranda da göster
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(image, text, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

cv2.imwrite("output.jpg", image)