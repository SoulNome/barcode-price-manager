"""
Run once to initialize database and create the default owner account.
Usage: python database/init_db.py
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app, db
from app.models.user import User

app = create_app('development')

with app.app_context():
    db.create_all()
    print('Tables created.')

    if not User.query.filter_by(username='admin').first():
        owner = User(username='admin', role='owner')
        owner.set_password('admin123')
        db.session.add(owner)
        db.session.commit()
        print('Default admin user created (username: admin / password: admin123).')
    else:
        print('Admin user already exists.')

    print('Database initialized successfully.')
