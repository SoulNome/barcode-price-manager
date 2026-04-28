"""Alias for database/init_db.py — run from project root."""
import subprocess, sys
subprocess.run([sys.executable, 'database/init_db.py'], check=True)
