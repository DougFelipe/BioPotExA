"""
feedback_alerts.py
------------------
Generates standardized feedback alerts for the user interface.

Functions:
- create_alert: Creates a bootstrap alert.
"""

import dash_bootstrap_components as dbc
from dash import html



def create_alert(message, color='success', dismissable=True, duration=4000):
    """
    Creates a formatted alert for user feedback.

    Parameters:
    - message (str or list): Text or list of dash components to display.
    - color (str): Color theme of the alert ('success', 'danger', etc.).
    - dismissable (bool): Whether the alert can be manually closed.
    - duration (int): Duration in milliseconds before auto-closing.

    Returns:
    - dbc.Alert: Dash bootstrap component alert.
    """
    return dbc.Alert(
        message,
        color=color,
        is_open=True,
        dismissable=dismissable,
        duration=duration
    )
