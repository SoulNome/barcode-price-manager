from app import db
from datetime import datetime


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    barcode = db.Column(db.String(50), unique=True, nullable=False, index=True)
    name = db.Column(db.String(200), nullable=False)
    brand = db.Column(db.String(100), nullable=True)
    category = db.Column(db.String(100), nullable=True)
    current_price = db.Column(db.Float, nullable=True)
    image_url = db.Column(db.String(500), nullable=True)
    api_data = db.Column(db.Text, nullable=True)  # JSON from Open Food Facts
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    price_history = db.relationship('PriceHistory', backref='product', lazy='dynamic',
                                    order_by='PriceHistory.changed_at.desc()')

    def to_dict(self):
        return {
            'id': self.id,
            'barcode': self.barcode,
            'name': self.name,
            'brand': self.brand,
            'category': self.category,
            'current_price': self.current_price,
            'image_url': self.image_url,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }

    def __repr__(self):
        return f'<Product {self.barcode}: {self.name}>'
