from app import db
from app.models.product import Product
from app.models.price_history import PriceHistory
from datetime import datetime


class PriceService:

    @staticmethod
    def update_price(product_id: int, new_price: float, user_id: int, notes: str = '') -> Product | None:
        product = Product.query.get(product_id)
        if not product:
            return None

        record = PriceHistory(
            product_id=product_id,
            user_id=user_id,
            old_price=product.current_price,
            new_price=new_price,
            notes=notes,
        )
        product.current_price = new_price
        product.updated_at = datetime.utcnow()

        db.session.add(record)
        db.session.commit()
        return product

    @staticmethod
    def get_history(page: int = 1, per_page: int = 25):
        return PriceHistory.query.order_by(PriceHistory.changed_at.desc()).paginate(
            page=page, per_page=per_page, error_out=False
        )

    @staticmethod
    def get_history_records(limit: int = 50, product_id: int = None):
        query = PriceHistory.query.order_by(PriceHistory.changed_at.desc())
        if product_id:
            query = query.filter_by(product_id=product_id)
        return query.limit(limit).all()

    @staticmethod
    def get_summary() -> dict:
        total_products = Product.query.count()
        total_changes = PriceHistory.query.count()
        priced = Product.query.filter(Product.current_price.isnot(None)).count()
        recent = (
            PriceHistory.query
            .order_by(PriceHistory.changed_at.desc())
            .limit(10)
            .all()
        )
        return {
            'total_products': total_products,
            'total_price_changes': total_changes,
            'products_with_price': priced,
            'products_without_price': total_products - priced,
            'recent_changes': [r.to_dict() for r in recent],
        }
