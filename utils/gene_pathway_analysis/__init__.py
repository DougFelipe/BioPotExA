"""
utils.gene_pathway_analysis
===========================

The `utils.gene_pathway_analysis` subpackage provides functions for processing and
visualizing KEGG Orthology (KO) data in the context of metabolic pathways and samples.
It includes modules for counting and ranking KOs across pathways and samples,
as well as generating bar charts and scatter plots.

Modules
-------
distribution_of_ko_in_pathways_plot : module
    - plot_pathway_ko_counts
    - plot_sample_ko_counts
distribution_of_ko_in_pathways_processing : module
    - validate_columns
    - count_ko_per_pathway
    - count_ko_per_sample_for_pathway
gene_counts_across_samples_plot : module
    - plot_ko_count
    - create_violin_plot
gene_counts_across_samples_processing : module
    - validate_ko_dataframe
    - process_ko_data
    - process_ko_data_violin
gene_distribution_among_samples_plot : module
    - plot_sample_ko_scatter
gene_distribution_among_samples_processing : module
    - get_ko_per_sample_for_pathway

Public Objects
--------------
The following functions are exported at the package level for convenience:

- plot_pathway_ko_counts
- plot_sample_ko_counts
- validate_columns
- count_ko_per_pathway
- count_ko_per_sample_for_pathway
- plot_ko_count
- create_violin_plot
- validate_ko_dataframe
- process_ko_data
- process_ko_data_violin
- plot_sample_ko_scatter
- get_ko_per_sample_for_pathway
"""

from .distribution_of_ko_in_pathways_plot import (
    plot_pathway_ko_counts,
    plot_sample_ko_counts
)
from .distribution_of_ko_in_pathways_processing import (
    validate_columns,
    count_ko_per_pathway,
    count_ko_per_sample_for_pathway
)
from .gene_counts_across_samples_plot import (
    plot_ko_count,
    create_violin_plot
)
from .gene_counts_across_samples_processing import (
    validate_ko_dataframe,
    process_ko_data,
    process_ko_data_violin
)
from .gene_distribution_among_samples_plot import plot_sample_ko_scatter
from .gene_distribution_among_samples_processing import get_ko_per_sample_for_pathway

__all__ = [
    "plot_pathway_ko_counts",
    "plot_sample_ko_counts",
    "validate_columns",
    "count_ko_per_pathway",
    "count_ko_per_sample_for_pathway",
    "plot_ko_count",
    "create_violin_plot",
    "validate_ko_dataframe",
    "process_ko_data",
    "process_ko_data_violin",
    "plot_sample_ko_scatter",
    "get_ko_per_sample_for_pathway"
]
