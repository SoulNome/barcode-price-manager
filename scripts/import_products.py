"""
Bulk-import products from a CSV file.
CSV format: barcode,name,brand,category,price
Usage: python scripts/import_products.py products.csv
"""
import sys
import os
import csv

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app, db
from app.models.product import Product

app = create_app('development')

csv_file = sys.argv[1] if len(sys.argv) > 1 else 'products.csv'

with app.app_context():
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        added = 0
        for row in reader:
            barcode = row.get('barcode', '').strip()
            if not barcode or Product.query.filter_by(barcode=barcode).first():
                continue
            product = Product(
                barcode=barcode,
                name=row.get('name', 'Unknown'),
                brand=row.get('brand', ''),
                category=row.get('category', ''),
                current_price=float(row['price']) if row.get('price') else None,
            )
            db.session.add(product)
            added += 1
        db.session.commit()
        print(f'Imported {added} products.')
