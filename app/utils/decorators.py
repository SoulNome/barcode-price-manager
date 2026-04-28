from functools import wraps
from flask import jsonify
from flask_login import current_user


def owner_required(f):
    """Restrict endpoint to users with 'owner' role."""
    @wraps(f)
    def decorated(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_owner:
            return jsonify({'error': 'Owner access required'}), 403
        return f(*args, **kwargs)
    return decorated
