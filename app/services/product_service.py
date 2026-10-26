from app import db
from app.models.product import Product
from app.services.api_service import ApiService
from app.services.cache_service import CacheService


class ProductService:

    @staticmethod
    def get_all_products():
        return Product.query.order_by(Product.name).all()

    @staticmethod
    def get_product_by_id(product_id: int) -> Product | None:
        return Product.query.get(product_id)

    @staticmethod
    def get_product_by_barcode(barcode: str) -> Product | None:
        return Product.query.filter_by(barcode=barcode).first()

    @staticmethod
    def get_or_fetch_product(barcode: str) -> Product | None:
        # Check DB first
        product = ProductService.get_product_by_barcode(barcode)
        if product:
            return product

        # Check cache
        cached = CacheService.get(f'product:{barcode}')
        if cached:
            return cached

        # Hit external API
        data = ApiService.fetch_product(barcode)
        if not data:
            return None

        product = Product(
            barcode=data['barcode'],
            name=data['name'],
            brand=data.get('brand', ''),
            category=data.get('category', ''),
            image_url=data.get('image_url', ''),
            api_data=data.get('api_data', ''),
        )
        db.session.add(product)
        db.session.commit()
        CacheService.set(f'product:{barcode}', product)
        return product

    @staticmethod
    def create_manual(barcode: str, name: str, brand: str = '', category: str = '') -> Product | None:
        if ProductService.get_product_by_barcode(barcode):
            return None
        product = Product(barcode=barcode, name=name, brand=brand, category=category)
        db.session.add(product)
        db.session.commit()
        return product

    @staticmethod
    def delete_product(product_id: int) -> bool:
        product = Product.query.get(product_id)
        if not product:
            return False
        db.session.delete(product)
        db.session.commit()
        CacheService.delete(f'product:{product.barcode}')
        return True
