import pytest
from app import create_app, db
from app.models.product import Product
from app.models.user import User
from app.services.price_service import PriceService


@pytest.fixture
def app():
    application = create_app('testing')
    with application.app_context():
        db.create_all()
        yield application
        db.drop_all()


def test_update_price(app):
    with app.app_context():
        user = User(username='testowner', role='owner')
        user.set_password('pass')
        product = Product(barcode='11112222', name='Priced Item', current_price=2.00)
        db.session.add_all([user, product])
        db.session.commit()

        updated = PriceService.update_price(product.id, 3.50, user.id)
        assert updated.current_price == 3.50

        history = PriceService.get_history_records(product_id=product.id)
        assert len(history) == 1
        assert history[0].old_price == 2.00
        assert history[0].new_price == 3.50
