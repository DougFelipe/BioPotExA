"""
utils.intersections_and_groups
==============================

The `utils.intersections_and_groups` subpackage provides functions to analyze and visualize
relationships and clusters among samples, genes, compounds, and other biological entities.
It includes modules for hierarchical clustering, intersection (UpSet) analysis, and grouping
by compound class, each with both data processing and plotting capabilities.

Modules
-------
clustering_dendrogram_plot : module
    Generates dendrograms (hierarchical clustering) as Dash HTML images.
clustering_dendrogram_processing : module
    Calculates and caches distance and linkage matrices for sample clustering.
intersection_analysis_plot : module
    Renders UpSet plots to show KO intersections across selected samples.
intersection_analysis_processing : module
    Prepares data (unique sample–KO pairs) for UpSet analysis.
sample_grouping_by_compound_class_plot : module
    Creates scatter subplots of sample groups based on compound interaction profiles.
sample_grouping_by_compound_class_processing : module
    Groups samples by compound class profiles and selects minimal covering groups.

Public Objects
--------------
The following functions are re-exported at the package level:

- plot_dendrogram
- calculate_sample_clustering
- clear_distance_cache
- render_upsetplot
- prepare_upsetplot_data
- plot_sample_groups
- group_by_class
- minimize_groups
"""

from .clustering_dendrogram_plot import plot_dendrogram
from .clustering_dendrogram_processing import (
    calculate_sample_clustering,
    clear_distance_cache
)
from .intersection_analysis_plot import render_upsetplot
from .intersection_analysis_processing import prepare_upsetplot_data
from .sample_grouping_by_compound_class_plot import plot_sample_groups
from .sample_grouping_by_compound_class_processing import (
    group_by_class,
    minimize_groups
)

__all__ = [
    "plot_dendrogram",
    "calculate_sample_clustering",
    "clear_distance_cache",
    "render_upsetplot",
    "prepare_upsetplot_data",
    "plot_sample_groups",
    "group_by_class",
    "minimize_groups"
]
