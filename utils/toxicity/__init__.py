"""
utils.toxicity
==============

The `utils.toxicity` subpackage provides functions for processing toxicity
prediction data and visualizing it as faceted heatmaps within the BioRemPP application.

Modules
-------
toxicity_prediction_heatmap_plot : module
    Contains `plot_heatmap_faceted` for rendering toxicity prediction heatmaps, faceted by category.
toxicity_prediction_heatmap_processing : module
    Contains `process_heatmap_data` to transform raw toxicity prediction columns into a long-format DataFrame.

Public Objects
--------------
The following functions are re-exported at the package level:

- plot_heatmap_faceted
- process_heatmap_data
"""

from .toxicity_prediction_heatmap_plot import plot_heatmap_faceted
from .toxicity_prediction_heatmap_processing import process_heatmap_data

__all__ = [
    "plot_heatmap_faceted",
    "process_heatmap_data"
]
