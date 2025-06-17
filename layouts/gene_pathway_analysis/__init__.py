"""
layouts.gene_pathway_analysis
=============================

This subpackage provides structured layouts for gene and pathway analysis visualizations within the BioRemPP application.

Included Modules and Layout Functions
-------------------------------------

- distribution_of_ko_in_pathways_layout
    * get_pathway_ko_bar_chart_layout: Layout for filtering and displaying KO distributions across pathways.
    * get_sample_ko_pathway_bar_chart_layout: Layout for filtering and displaying KO distributions across samples within pathways.

- gene_counts_across_samples_layout
    * get_ko_count_bar_chart_layout: Layout for KO count bar chart with interactive filter.
    * get_ko_violin_boxplot_layout: Layout for KO violin and boxplot chart.

- gene_distribution_among_samples_layout
    * get_sample_ko_scatter_layout: Layout for scatter plot showing KO/sample distribution by pathway.
"""

# -------------------------------
# Public Imports (exposed on import)
# -------------------------------

from .distribution_of_ko_in_pathways_layout import (
    get_pathway_ko_bar_chart_layout,
    get_sample_ko_pathway_bar_chart_layout
)

from .gene_counts_across_samples_layout import (
    get_ko_count_bar_chart_layout,
    get_ko_violin_boxplot_layout
)

from .gene_distribution_among_samples_layout import (
    get_sample_ko_scatter_layout
)

# -------------------------------
# Convenience variable for all imports
# -------------------------------

__all__ = [
    # distribution_of_ko_in_pathways_layout
    "get_pathway_ko_bar_chart_layout",
    "get_sample_ko_pathway_bar_chart_layout",

    # gene_counts_across_samples_layout
    "get_ko_count_bar_chart_layout",
    "get_ko_violin_boxplot_layout",

    # gene_distribution_among_samples_layout
    "get_sample_ko_scatter_layout",
]
