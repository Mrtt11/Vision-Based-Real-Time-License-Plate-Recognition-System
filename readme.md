# 📸 Turkish License Plate Detection & Recognition  

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python)](https://www.python.org/)  
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Detection-orange.svg?logo=ultralytics)](https://github.com/ultralytics/ultralytics)  
[![OCR](https://img.shields.io/badge/OCR-Tesseract-green.svg?logo=google)](https://github.com/tesseract-ocr/tesseract)  

YOLOv8 tabanlı **plaka tespit sistemi** ve Tesseract OCR tabanlı **plaka okuma sistemi**.  
Görüntü veya video akışı üzerinden araç plakaları tespit edilir, plaka bölgesi kırpılır ve OCR ile metne dönüştürülür.  

---

## 🚀 Özellikler
- 🔍 **Plaka Tespiti** – YOLOv8 ile eğitilmiş özel model (`best.pt`)  
- ✂️ **Otomatik Crop** – Tespit edilen plaka bölgesi otomatik kırpılır  
- 📝 **Plaka Okuma** – Pytesseract OCR ile metin çıkarılır  
- 💻 **Donanım Desteği** – CPU üzerinde çalışabilir, GPU opsiyonel  
- 📂 **Çıktı Yönetimi** – Sonuçlar `runs/outputs/` klasörüne kaydedilir  

---

## 📂 Proje Yapısı
```bash
Vision-Based.../
│── plate-detection-system/
│   ├── detect.py          # Ana çalışma dosyası
│── weights/
│   ├── best.pt            # Eğitilmiş YOLOv8 modeli
│── test_images/           # Test için örnek görseller
│── requirements.txt
│── README.md
```

🔧 Kurulum

Depoyu klonla:

git clone https://github.com/kullanici/project.git
cd project


Sanal ortam oluştur ve etkinleştir:

python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate # Linux/Mac


Bağımlılıkları yükle:

pip install -r requirements.txt

▶️ Kullanım
Görsel üzerinde plaka tespiti:
python detect.py --source test_images/car1.jpg

Video üzerinde plaka tespiti:
python detect.py --source test_videos/test.mp4

📊 Örnek Çıktı

Girdi: Araç resmi

➡️ YOLOv8 → Plaka kutusu bulunur
➡️ Crop → Plaka kesilir
➡️ OCR → 34 AB 123

✅ Çıktı ekranda görüntülenir ve runs/outputs/ klasörüne kaydedilir.

🏋️‍♂️ Model Eğitimi

Bu model, Kaggle’daki
Turkish License Plate Dataset

verisinin ilk 1500 görseli ile eğitilmiştir.

📌 Gereksinimler

Python 3.10+

PyTorch

Ultralytics YOLOv8

Pytesseract

OpenCV

📜 Lisans

Bu proje eğitim amaçlı geliştirilmiştir.