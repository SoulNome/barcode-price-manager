"""
Backup the SQLite database with a timestamp.
Usage: python scripts/backup_db.py
"""
import shutil
import os
from datetime import datetime

DB_PATH = 'instance/price_system.db'
BACKUP_DIR = 'backups'

os.makedirs(BACKUP_DIR, exist_ok=True)
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
dest = os.path.join(BACKUP_DIR, f'price_system_{timestamp}.db')

if os.path.exists(DB_PATH):
    shutil.copy2(DB_PATH, dest)
    print(f'Backup saved: {dest}')
else:
    print(f'Database not found at {DB_PATH}')
