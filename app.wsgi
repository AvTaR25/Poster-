
import sys
import logging

# Error logging ke liye
logging.basicConfig(stream=sys.stderr)

# Apne project folder ka exact server path yahan daalein
# Agar aapka folder /var/www/my_flask_app hai, toh wahi likhein
sys.path.insert(0, '/var/www/aapka_project_folder')

# app.py file se 'app' variable ko import karein aur use 'application' ka naam dein 
# (Apache 'application' naam ka variable hi dhundhta hai)
from app import app as application
