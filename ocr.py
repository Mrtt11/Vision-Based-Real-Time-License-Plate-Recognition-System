# ocr.py
import easyocr

class PlateOCR:
    def __init__(self):
        self.reader = easyocr.Reader(['tr', 'en'])

    def read_plate(self, plate_img):
        results = self.reader.readtext(plate_img)
        if results:
            # çıktıları önce buluyoruz sonra birleştiriyoruz (çünkü yazdığım kodlarda ya en başını ya en sonunu buluyordu sadece)
            parts = [res[1] for res in results]
            text = "".join(parts)
            return text.replace(" ", "").upper()
        return None
