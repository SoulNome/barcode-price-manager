from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app(config_name='default'):
    app = Flask(__name__, template_folder='templates', static_folder='../static')
    app.config.from_object(config[config_name])

    db.init_app(app)
    login_manager.init_app(app)

    from app.routes.products import products_bp
    from app.routes.prices import prices_bp
    from app.routes.history import history_bp
    from app.routes.reports import reports_bp
    from app.auth import auth_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(products_bp, url_prefix='/products')
    app.register_blueprint(prices_bp, url_prefix='/prices')
    app.register_blueprint(history_bp, url_prefix='/history')
    app.register_blueprint(reports_bp, url_prefix='/reports')

    return app
