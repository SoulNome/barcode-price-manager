#!/bin/bash
# Raspberry Pi installation script for Barcode Price Manager
set -e

echo "=== Barcode Price Manager - Raspberry Pi Setup ==="

sudo apt-get update -y
sudo apt-get install -y python3 python3-pip python3-venv libzbar0 nginx

cd "$(dirname "$0")/.."

python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

python database/init_db.py

sudo cp raspberry_pi/systemd_service.txt /etc/systemd/system/price-manager.service
sudo systemctl daemon-reload
sudo systemctl enable price-manager
sudo systemctl start price-manager

echo "=== Installation complete ==="
echo "App running at http://localhost:5000"
