"""
utils.heatmaps
===============

The `utils.heatmaps` subpackage provides functions for processing and visualizing data
using heatmaps within the BioRemPP application. Each module handles a specific type of
heatmap generation or data preparation step.

Modules
-------
- gene_sample_heatmap_plot : module
    Creates heatmaps to visualize ortholog counts per gene and sample.
- gene_sample_heatmap_processing : module
    Processes merged input data to compute KO counts grouped by gene and sample.
- pathway_compound_interaction_plot : module
    Generates faceted heatmaps of KO counts by pathway and compound pathway for a sample.
- pathway_compound_interaction_processing : module
    Prepares data by grouping KO counts per pathway, compound pathway, and sample.
- sample_reference_agency_heatmap_plot : module
    Creates heatmaps of compound counts across samples and reference agencies.
- sample_reference_agency_heatmap_processing : module
    Processes merged data into a pivot table for sample-reference agency compound counts.

Public Functions
----------------
The following functions are re-exported at the package level for convenience:

- plot_sample_gene_heatmap
- process_gene_sample_data
- plot_pathway_heatmap
- process_pathway_data
- plot_sample_reference_heatmap
- process_sample_reference_heatmap
"""

# Public Imports
# --------------
from .gene_sample_heatmap_plot import plot_sample_gene_heatmap
from .gene_sample_heatmap_processing import process_gene_sample_data
from .pathway_compound_interaction_plot import plot_pathway_heatmap
from .pathway_compound_interaction_processing import process_pathway_data
from .sample_reference_agency_heatmap_plot import plot_sample_reference_heatmap
from .sample_reference_agency_heatmap_processing import process_sample_reference_heatmap

# Convenience list for import *
__all__ = [
    "plot_sample_gene_heatmap",
    "process_gene_sample_data",
    "plot_pathway_heatmap",
    "process_pathway_data",
    "plot_sample_reference_heatmap",
    "process_sample_reference_heatmap",
]
