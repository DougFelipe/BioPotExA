"""
app.py
------
This script initializes the main Dash application instance. It sets up the application with:
- An external Bootstrap theme for consistent and responsive styling.
- Additional configurations to handle advanced Dash features like callbacks and custom scripts.

The application instance (`app`) is the central object used throughout the project to define layouts, callbacks, and other app-level settings.
"""

# ----------------------------------------
# Imports
# ----------------------------------------
from dash import Dash  # Core Dash class for creating the application
import dash_bootstrap_components as dbc  # Bootstrap components for enhanced UI styling
import logging

# ----------------------------------------
# Logging Configuration (Global)
# ----------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# ----------------------------------------
# Dash Application Instance
# ----------------------------------------
app = Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.MINTY,
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css",
        "https://www.w3schools.com/w3css/4/w3.css"
    ],
    suppress_callback_exceptions=True,
    external_scripts=["/assets/scroll.js"],
    title="BioRemPP"
)

# ----------------------------------------
# Application Server Configuration
# ----------------------------------------
server = app.server  # <-- WSGI entrypoint for Gunicorn/WSGI servers
