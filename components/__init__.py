"""
components
==========

Reusable UI components for the BioRemPP Dash application, built using Dash and Dash Bootstrap Components (DBC).

Modules and Functions:

- alerts.py:
    - hadeg_alert()
    - toxcsm_alert()

- analysis_suggestions_offcanvas.py:
    - analysis_suggestions_offcanvas(offcanvas_id, is_open)

- analytical_highlight.py:
    - analytical_highlight()

- divider.py:
    - NeonDivider(className, style)

- download_button.py:
    - get_sample_data_button()

- filters.py:
    - create_range_slider(slider_id)

- header.py:
    - Header()

- navbar.py:
    - navbar
"""

# Alerts
from .alerts import hadeg_alert, toxcsm_alert

# Offcanvas Component
from .analysis_suggestions_offcanvas import analysis_suggestions_offcanvas

# Analytical Highlight Badge
from .analytical_highlight import analytical_highlight

# Neon Divider
from .divider import NeonDivider

# Download Button
from .download_button import get_sample_data_button

# Filters
from .filters import create_range_slider

# Header Component
from .header import Header

# Navbar Component
from .navbar import navbar

__all__ = [
    "hadeg_alert",
    "toxcsm_alert",
    "analysis_suggestions_offcanvas",
    "analytical_highlight",
    "NeonDivider",
    "get_sample_data_button",
    "create_range_slider",
    "Header",
    "navbar"
]
