import re

def validate_tr_plate(text):
    """
    TR plaka formatı: 34ABC123, 06XY456 vb.
    """
    pattern = r"^[0-9]{2}[A-Z0-9]{1,6}$"
    if re.match(pattern, text):
        return True
    return False
