"""
layouts.toxicity
================

This subpackage provides layout components for displaying toxicity prediction heatmaps
with faceted visualizations in the BioRemPP Dash web application.

Included modules:
-----------------
- toxicity_prediction_heatmap_layout: Layout for rendering the faceted toxicity prediction heatmap.
"""

# -------------------------------
# Public Imports (Exposed on package import)
# -------------------------------

# toxicity_prediction_heatmap_layout.py
from .toxicity_prediction_heatmap_layout import get_toxicity_heatmap_layout

# -------------------------------
# Convenience Variables
# -------------------------------

__all__ = [
    # toxicity_prediction_heatmap_layout
    "get_toxicity_heatmap_layout"
]
