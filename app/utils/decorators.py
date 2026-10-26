from functools import wraps
from flask import jsonify, redirect, url_for, flash, request
from flask_login import current_user


def owner_required(f):
    """Restrict endpoint to users with 'owner' role."""
    @wraps(f)
    def decorated(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_owner:
            if request.is_json or request.method == 'POST':
                return jsonify({'error': 'Owner access required'}), 403
            flash('Owner access required.', 'danger')
            return redirect(url_for('products.dashboard'))
        return f(*args, **kwargs)
    return decorated
