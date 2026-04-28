"""
Configuration file for Barcode Price Management System
"""
import os
from datetime import timedelta


class Config:
    """Base configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-change-in-production'
    FLASK_ENV = os.environ.get('FLASK_ENV') or 'development'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///price_system.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True

    OPEN_FOOD_FACTS_API = 'https://world.openfoodfacts.org/api/v0/product/'

    MAX_PRODUCTS = 2000
    PRICE_HISTORY_RETENTION_DAYS = 730  # 2 years
    API_TIMEOUT = 5  # seconds

    CACHE_ENABLED = True
    CACHE_DURATION = 3600  # 1 hour


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
