import requests
import json
from flask import current_app


class ApiService:
    """Fetches product data from Open Food Facts API."""

    @staticmethod
    def fetch_product(barcode: str) -> dict | None:
        base_url = current_app.config.get('OPEN_FOOD_FACTS_API')
        timeout = current_app.config.get('API_TIMEOUT', 5)
        try:
            response = requests.get(f"{base_url}{barcode}.json", timeout=timeout)
            response.raise_for_status()
            data = response.json()
            if data.get('status') == 1:
                return ApiService._parse_product(data['product'], barcode)
        except (requests.RequestException, ValueError):
            pass
        return None

    @staticmethod
    def _parse_product(raw: dict, barcode: str) -> dict:
        return {
            'barcode': barcode,
            'name': raw.get('product_name') or raw.get('product_name_en') or 'Unknown Product',
            'brand': raw.get('brands', ''),
            'category': raw.get('categories', '').split(',')[0].strip(),
            'image_url': raw.get('image_front_url', ''),
            'api_data': json.dumps(raw),
        }
