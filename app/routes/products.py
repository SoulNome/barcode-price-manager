from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from app.services.product_service import ProductService
from app.services.api_service import ApiService

products_bp = Blueprint('products', __name__)


@products_bp.route('/dashboard')
@login_required
def dashboard():
    products = ProductService.get_all_products()
    return render_template('dashboard.html', products=products, user=current_user)


@products_bp.route('/lookup', methods=['GET', 'POST'])
@login_required
def lookup():
    return render_template('price_lookup.html', user=current_user)


@products_bp.route('/scan', methods=['POST'])
@login_required
def scan():
    barcode = request.json.get('barcode', '').strip()
    if not barcode:
        return jsonify({'error': 'Barcode is required'}), 400

    product = ProductService.get_or_fetch_product(barcode)
    if product:
        return jsonify(product.to_dict()), 200
    return jsonify({'error': 'Product not found'}), 404
