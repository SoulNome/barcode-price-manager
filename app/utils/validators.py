def validate_price(value) -> float | None:
    """Return float price if valid (>= 0), else None."""
    try:
        price = float(value)
        return price if price >= 0 else None
    except (TypeError, ValueError):
        return None


def validate_barcode(barcode: str) -> bool:
    return isinstance(barcode, str) and barcode.isdigit() and 8 <= len(barcode) <= 14
