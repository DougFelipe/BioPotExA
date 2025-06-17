"""
utils.entity_interactions
=========================

This subpackage provides all visual and analytical functions related to the interaction
between biological entities, such as genes, compounds, enzymes, and samples.

It includes data processing routines for filtering and summarizing merged datasets, as well
as Plotly-based functions for generating interactive visualizations such as scatter plots,
bar charts, and network graphs that illustrate key relationships across entities.

Available Modules
-----------------
enzyme_activity_by_sample_plot : module
    Generates bar plots summarizing enzyme activity per sample.
enzyme_activity_by_sample_processing : module
    Calculates the count of unique KO entries per enzyme for a specific sample.
gene_compound_interaction_network_plot : module
    Builds an interactive network graph of gene-compound associations.
gene_compound_interaction_network_processing : module
    Prepares input data for graph visualization by cleaning and merging relationships.
gene_compound_interaction_plot : module
    Generates a scatter plot showing associations between genes and compounds.
sample_compound_interaction_plot : module
    Creates scatter plots of sample-compound relationships, colored by compound class.
sample_gene_associations_plot : module
    Produces scatter plots linking samples to expressed gene symbols.
processing_gene_sample_compound.md : document
    Markdown documentation explaining internal logic for association processing.

Public Objects
--------------
These functions are re-exported for convenience and can be imported directly from
``utils.entity_interactions``.

- plot_enzyme_activity_counts
- count_unique_enzyme_activities
- generate_gene_compound_network
- prepare_gene_compound_network_data
- plot_gene_compound_scatter
- plot_compound_scatter
- plot_sample_gene_scatter
"""

# -------------------------------
# Public Imports (exposed at package level)
# -------------------------------

from .enzyme_activity_by_sample_plot import plot_enzyme_activity_counts
from .enzyme_activity_by_sample_processing import count_unique_enzyme_activities
from .gene_compound_interaction_network_plot import generate_gene_compound_network
from .gene_compound_interaction_network_processing import prepare_gene_compound_network_data
from .gene_compound_interaction_plot import plot_gene_compound_scatter
from .sample_compound_interaction_plot import plot_compound_scatter
from .sample_gene_associations_plot import plot_sample_gene_scatter

__all__ = [
    "plot_enzyme_activity_counts",
    "count_unique_enzyme_activities",
    "generate_gene_compound_network",
    "prepare_gene_compound_network_data",
    "plot_gene_compound_scatter",
    "plot_compound_scatter",
    "plot_sample_gene_scatter"
]
