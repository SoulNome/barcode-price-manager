from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user
from app.utils.decorators import owner_required

reports_bp = Blueprint('reports', __name__)


@reports_bp.route('/')
@login_required
@owner_required
def index():
    return render_template('reports.html', user=current_user)


@reports_bp.route('/summary')
@login_required
@owner_required
def summary():
    from app.services.price_service import PriceService
    data = PriceService.get_summary()
    return jsonify(data)
