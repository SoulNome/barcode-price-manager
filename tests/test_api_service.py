import pytest
from unittest.mock import patch, MagicMock
from app import create_app


@pytest.fixture
def app():
    application = create_app('testing')
    with application.app_context():
        yield application


def test_fetch_product_success(app):
    from app.services.api_service import ApiService

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        'status': 1,
        'product': {
            'product_name': 'Mock Chips',
            'brands': 'MockBrand',
            'categories': 'Snacks, Chips',
            'image_front_url': '',
        }
    }

    with app.app_context():
        with patch('requests.get', return_value=mock_response):
            result = ApiService.fetch_product('12345678901')
            assert result is not None
            assert result['name'] == 'Mock Chips'
            assert result['brand'] == 'MockBrand'


def test_fetch_product_not_found(app):
    from app.services.api_service import ApiService

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'status': 0}

    with app.app_context():
        with patch('requests.get', return_value=mock_response):
            result = ApiService.fetch_product('00000000000')
            assert result is None
