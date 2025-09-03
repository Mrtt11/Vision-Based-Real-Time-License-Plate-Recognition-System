# 📸 Turkish License Plate Detection & Recognition

Bu proje, YOLOv8 tabanlı **plaka tespit sistemi** ve Tesseract OCR tabanlı **plaka okuma sistemi** içerir.  
Amaç: Görüntü veya video akışı üzerinde plakaları tespit etmek, plakayı kırpıp OCR ile yazıya dökmek.  

---

## 🚀 Özellikler
- YOLOv8 ile eğitilmiş plaka tespit modeli (`best.pt`)
- Plaka tespit edildikten sonra otomatik crop işlemi
- Pytesseract ile plakanın metin olarak okunması
- CPU üzerinde çalıştırılabilir (GPU desteği opsiyonel)
- Çıktılar `runs/` klasörüne kaydedilir

---

## 📂 Klasör Yapısı
Vision-Based.../
│── plate-detection-system/
│ ├── detect.py # Ana çalışma dosyası
│── weights
│ │── best.pt # Kendi eğittiğim model
│── test_images/ # Test için örnek görseller
│── requirements.txt
│── README.md


## 🔧 Kurulum
1. Depoyu klonla veya indir:
   ```bash
   git clone https://github.com/kullanici/project.git
   cd project

Sanal ortam oluştur:

python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate # Linux/Mac

Bağımlılıkları kur:

pip install -r requirements.txt

📊 Örnek Çıktı

Girdi: Araç resmi

YOLO → Plaka kutusu bulur

Crop → Plaka kesilir

OCR → 34 AB 123

Çıktı ekranda ve runs/outputs/ klasörüne kaydedilir.