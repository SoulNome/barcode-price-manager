from flask import Blueprint, request, jsonify, render_template
from flask_login import login_required, current_user
from app.utils.decorators import owner_required
from app.services.price_service import PriceService

prices_bp = Blueprint('prices', __name__)


@prices_bp.route('/edit/<int:product_id>', methods=['GET'])
@login_required
@owner_required
def edit(product_id):
    from app.services.product_service import ProductService
    product = ProductService.get_product_by_id(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    return render_template('price_edit.html', product=product, user=current_user)


@prices_bp.route('/update', methods=['POST'])
@login_required
@owner_required
def update():
    data = request.json
    product_id = data.get('product_id')
    new_price = data.get('new_price')

    if not product_id or new_price is None:
        return jsonify({'error': 'product_id and new_price are required'}), 400

    result = PriceService.update_price(product_id, float(new_price), current_user.id)
    if result:
        return jsonify({'success': True, 'product': result.to_dict()}), 200
    return jsonify({'error': 'Failed to update price'}), 500
