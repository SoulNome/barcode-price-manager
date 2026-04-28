"""
Barcode scanning utilities.
USB barcode scanners act as keyboards — they type the barcode string and press Enter.
This module handles any additional image-based scanning if a camera is used instead.
"""
try:
    from pyzbar.pyzbar import decode
    from PIL import Image
    PYZBAR_AVAILABLE = True
except ImportError:
    PYZBAR_AVAILABLE = False


class BarcodeService:

    @staticmethod
    def decode_image(image_path: str) -> str | None:
        """Decode first barcode found in an image file."""
        if not PYZBAR_AVAILABLE:
            return None
        try:
            img = Image.open(image_path)
            barcodes = decode(img)
            if barcodes:
                return barcodes[0].data.decode('utf-8')
        except Exception:
            pass
        return None

    @staticmethod
    def validate_barcode(barcode: str) -> bool:
        """Basic length/character validation."""
        return barcode.isdigit() and 8 <= len(barcode) <= 14
