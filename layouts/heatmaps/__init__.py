"""
layouts.heatmaps
================

This subpackage provides Dash/Bootstrap-based layout components for heatmap visualizations
within the BioRemPP web application. Each module defines a specific layout for the presentation
of genomic and compound-related heatmaps.

Included Modules
----------------
- gene_sample_heatmap_layout: Layout for the gene-sample heatmap with dynamic filters.
- pathway_compound_interaction_layout: Layout for the Pathway-Compound interaction heatmap.
- sample_reference_agency_heatmap_layout: Layout for the heatmap between samples and reference agencies.

Available Functions
-------------------
- get_gene_sample_heatmap_layout: Returns the layout for gene-sample heatmap visualization.
- get_pathway_heatmap_layout: Returns the layout for pathway-compound heatmap visualization.
- get_sample_reference_heatmap_layout: Returns the layout for sample-reference agency heatmap visualization.
"""

# gene_sample_heatmap_layout.py
from .gene_sample_heatmap_layout import get_gene_sample_heatmap_layout

# pathway_compound_interaction_layout.py
from .pathway_compound_interaction_layout import get_pathway_heatmap_layout

# sample_reference_agency_heatmap_layout.py
from .sample_reference_agency_heatmap_layout import get_sample_reference_heatmap_layout

__all__ = [
    "get_gene_sample_heatmap_layout",
    "get_pathway_heatmap_layout",
    "get_sample_reference_heatmap_layout",
]
