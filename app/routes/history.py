from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from app.services.price_service import PriceService

history_bp = Blueprint('history', __name__)


@history_bp.route('/')
@login_required
def index():
    page = request.args.get('page', 1, type=int)
    per_page = 25
    history = PriceService.get_history(page=page, per_page=per_page)
    return render_template('history.html', history=history, user=current_user)


@history_bp.route('/api')
@login_required
def api_history():
    limit = request.args.get('limit', 50, type=int)
    product_id = request.args.get('product_id', type=int)
    records = PriceService.get_history_records(limit=limit, product_id=product_id)
    return jsonify([r.to_dict() for r in records])
