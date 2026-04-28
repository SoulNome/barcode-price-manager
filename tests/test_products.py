import pytest
from app import create_app, db
from app.models.product import Product


@pytest.fixture
def app():
    application = create_app('testing')
    with application.app_context():
        db.create_all()
        yield application
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


def test_product_creation(app):
    with app.app_context():
        product = Product(barcode='12345678', name='Test Product', current_price=1.99)
        db.session.add(product)
        db.session.commit()
        fetched = Product.query.filter_by(barcode='12345678').first()
        assert fetched is not None
        assert fetched.name == 'Test Product'
        assert fetched.current_price == 1.99


def test_product_to_dict(app):
    with app.app_context():
        product = Product(barcode='99887766', name='Dict Product')
        db.session.add(product)
        db.session.commit()
        d = product.to_dict()
        assert d['barcode'] == '99887766'
        assert d['name'] == 'Dict Product'
