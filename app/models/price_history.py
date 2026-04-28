from app import db
from datetime import datetime


class PriceHistory(db.Model):
    __tablename__ = 'price_history'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    old_price = db.Column(db.Float, nullable=True)
    new_price = db.Column(db.Float, nullable=False)
    changed_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    notes = db.Column(db.String(255), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'product_name': self.product.name if self.product else None,
            'barcode': self.product.barcode if self.product else None,
            'user': self.changed_by.username if self.changed_by else None,
            'old_price': self.old_price,
            'new_price': self.new_price,
            'changed_at': self.changed_at.isoformat(),
            'notes': self.notes,
        }

    def __repr__(self):
        return f'<PriceHistory product={self.product_id} {self.old_price}->{self.new_price}>'
