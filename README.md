# Barcode-Based Price Management System

A web-based system for grocery store price management with automatic product lookup via barcode scanning.

## Features
- **Automatic Product Lookup**: Scan barcode → retrieves product name from Open Food Facts API
- **Real-time Price Management**: Update prices instantly with complete audit trail
- **Role-Based Access**: Owner (full access) and Employee (read-only)
- **Price History**: Complete record of all price changes (who, what, when)
- **Offline Capability**: Works offline using local cache after first scan
- **Reports & Analytics**: Price change reports and analytics

## Stack
- **Backend**: Python 3.9+ / Flask
- **Database**: SQLite (local)
- **Frontend**: HTML5 / CSS3 / Bootstrap / JavaScript
- **API**: Open Food Facts (free)
- **Hardware**: Raspberry Pi 4 (4GB RAM), USB Barcode Scanner, HDMI Monitor

## Quick Start

```bash
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Initialize database
python database/init_db.py

# 4. Run
python run.py
```

App available at: `http://localhost:5000`

## Default Credentials
| Field    | Value    |
|----------|----------|
| Username | admin    |
| Password | admin123 |
| Role     | Owner    |

## Workflow
1. Scan barcode → system fetches product name & current price
2. Owner presses `*` to enter edit mode, types new price, presses `ENTER`
3. Price saved with full audit record (user, timestamp, old/new value)

## Project Structure
```
barcode-price-manager/
├── app/           # Flask application (routes, models, services)
├── static/        # CSS, JS, images
├── database/      # SQLite setup & schema
├── tests/         # Unit tests
├── docs/          # Documentation
├── scripts/       # Utility scripts
└── raspberry_pi/  # Pi-specific config
```

## Deployment
See `docs/INSTALLATION_GUIDE.md` for Raspberry Pi setup.

## Testing
```bash
pytest
pytest --cov=app tests/
```
