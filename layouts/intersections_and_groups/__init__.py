"""
layouts.intersections_and_groups
===============================

This subpackage provides layout components for the intersections and groups analyses
in the BioRemPP application. It includes layouts for clustering dendrograms, UpSet intersection plots,
and scatter plots of sample grouping by compound class.

Included Modules
----------------
- clustering_dendrogram_layout: Layout for the sample clustering dendrogram view.
- intersection_analysis_layout: Layout for the UpSet intersection analysis plot.
- sample_grouping_by_compound_class_pattern_layout: Layout for visualizing sample grouping patterns by compound class.

Exports
-------
- get_sample_clustering_layout (from clustering_dendrogram_layout)
- get_sample_upset_layout (from intersection_analysis_layout)
- get_sample_groups_layout (from sample_grouping_by_compound_class_pattern_layout)
"""

# clustering_dendrogram_layout.py
from .clustering_dendrogram_layout import get_sample_clustering_layout

# intersection_analysis_layout.py
from .intersection_analysis_layout import get_sample_upset_layout

# sample_grouping_by_compound_class_pattern_layout.py
from .sample_grouping_by_compound_class_pattern_layout import get_sample_groups_layout

__all__ = [
    "get_sample_clustering_layout",
    "get_sample_upset_layout",
    "get_sample_groups_layout",
]
