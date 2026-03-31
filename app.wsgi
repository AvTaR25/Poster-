import sys
import logging

# Server errors log karne ke liye
logging.basicConfig(stream=sys.stderr)

# Aapke 'poster' project ka exact server path
PROJECT_DIR = '/var/www/poster'

if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

# app.py se Flask instance ko import karke 'application' naam dena
from app import app as application
