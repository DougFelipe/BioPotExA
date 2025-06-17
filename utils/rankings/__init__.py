"""
utils.rankings
==============

The `utils.rankings` subpackage provides routines for computing and visualizing rankings
of compounds and samples based on their biological interactions. Each pair of modules
handles both data processing to calculate counts and Plotly-based plotting functions to
render bar charts of the results.

Modules
-------
ranking_compounds_by_gene_interaction_plot : module
    - plot_compound_gene_ranking: Bar chart of compounds ranked by number of unique genes.
ranking_compounds_by_gene_interaction_processing : module
    - process_compound_gene_ranking: Computes unique gene counts per compound.
ranking_compounds_by_sample_interaction_plot : module
    - plot_compound_ranking: Bar chart of compounds ranked by number of unique samples.
ranking_compounds_by_sample_interaction_processing : module
    - process_compound_ranking: Computes unique sample counts per compound.
ranking_samples_by_compound_interaction_plot : module
    - plot_sample_ranking: Bar chart of samples ranked by number of unique compounds.
ranking_samples_by_compound_interaction_processing : module
    - process_sample_ranking: Computes unique compound counts per sample.

Public Objects
--------------

The following functions are re-exported at the package level:

- plot_compound_gene_ranking
- process_compound_gene_ranking
- plot_compound_ranking
- process_compound_ranking
- plot_sample_ranking
- process_sample_ranking
"""

from .ranking_compounds_by_gene_interaction_plot import plot_compound_gene_ranking
from .ranking_compounds_by_gene_interaction_processing import process_compound_gene_ranking
from .ranking_compounds_by_sample_interaction_plot import plot_compound_ranking
from .ranking_compounds_by_sample_interaction_processing import process_compound_ranking
from .ranking_samples_by_compound_interaction_plot import plot_sample_ranking
from .ranking_samples_by_compound_interaction_processing import process_sample_ranking

__all__ = [
    "plot_compound_gene_ranking",
    "process_compound_gene_ranking",
    "plot_compound_ranking",
    "process_compound_ranking",
    "plot_sample_ranking",
    "process_sample_ranking"
]
