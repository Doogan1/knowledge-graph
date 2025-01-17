from flask import Flask
from pathlib import Path

app = Flask(__name__)

# Ensure the app instance folder exists
Path(app.instance_path).mkdir(parents=True, exist_ok=True)

from app import routes  # Import routes after app is created to avoid circular imports