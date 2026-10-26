from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
from flask_login import login_required, current_user
from app.services.product_service import ProductService
from app.services.api_service import ApiService
from app.utils.decorators import owner_required

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
    return jsonify({'error': 'Product not found', 'barcode': barcode, 'can_create': current_user.is_owner}), 404


@products_bp.route('/create', methods=['GET', 'POST'])
@login_required
@owner_required
def create():
    barcode = request.args.get('barcode', '')
    if request.method == 'POST':
        barcode = request.form.get('barcode', '').strip()
        name = request.form.get('name', '').strip()
        brand = request.form.get('brand', '').strip()
        category = request.form.get('category', '').strip()
        if not barcode or not name:
            flash('Barcode and product name are required.', 'warning')
            return render_template('product_create.html', barcode=barcode)
        product = ProductService.create_manual(barcode=barcode, name=name, brand=brand, category=category)
        if product:
            flash(f'Product "{name}" added successfully.', 'success')
            return redirect(url_for('prices.edit', product_id=product.id))
        flash('A product with that barcode already exists.', 'danger')
    return render_template('product_create.html', barcode=barcode)


@products_bp.route('/delete/<int:product_id>', methods=['POST'])
@login_required
@owner_required
def delete(product_id):
    ProductService.delete_product(product_id)
    flash('Product deleted.', 'success')
    return redirect(url_for('products.dashboard'))
