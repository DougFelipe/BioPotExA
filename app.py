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

# ----------------------------------------
# Dash Application Instance
# ----------------------------------------

# Create the main Dash application instance
app = Dash(
    __name__,  # Defines the name of the module for internal app reference
    external_stylesheets=[dbc.themes.MINTY],  # Applies the Minty theme from Bootstrap for consistent styling
    suppress_callback_exceptions=True,  # Allows the use of callbacks for components not immediately in the layout
    external_scripts=["/assets/scroll.js"]  # Includes a custom JavaScript file for scroll functionality
)
