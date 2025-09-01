from detector import PlateDetector
from ocr import PlateOCR
from verification import validate_tr_plate
import cv2

#İLK BAŞTA ÇALIŞMIYODU HATA VERİYODU BENDE DEBUG İÇİN AYIRDIM HER KISMI

# Detector ve OCR objelerini oluştur
detector = PlateDetector()
ocr = PlateOCR()

# Test edilecek görseli yükle
image_path = "sample_images/sample1.jpg"
image = cv2.imread(image_path)
if image is None:
    print("Görsel bulunamadı:", image_path)
    exit()

# Plaka tespiti
plates = detector.detect_plate(image)
print("Bulunan plaka sayısı:", len(plates))

if len(plates) == 0:
    print("Plaka tespit edilemedi.")
else:
    # Her plaka crop’u için OCR ve doğrulama
    for idx, plate_crop in enumerate(plates):
        print(f"\n--- Plaka {idx+1} ---")
        
        # OCR ile metni oku
        text = ocr.read_plate(plate_crop)
        print("OCR sonucu:", text)

        # TR plaka formatına uygunsa ekrana yaz
        if text and validate_tr_plate(text):
            print("Plaka bulundu:", text)
        else:
            print("TR formatına uymuyor veya okunamadı")
