"""
layouts
=======

The `layouts` package aggregates subpackages and modules that provide all the visual components (layouts)
for the main pages and sections of the BioRemPP application. Each subpackage corresponds to a thematic area
of the user interface and organizes Dash/Bootstrap layouts for different stages of data analysis.

Available Subpackages
---------------------
- results_overview
    Layouts for summary tables of the main result databases (BioRemPP, HADEG, ToxCSM).
- gene_pathway_analysis
    Layouts for analytical visualizations of genes, orthologs (KO), and metabolic pathways.
- entity_interactions
    Layouts for interactive exploration of enzymes, genes, compounds, and samples.
- rankings
    Layouts for ranking visualizations of compounds, genes, and samples by interaction counts.
- intersections_and_groups
    Layouts for intersection analysis (UpSet plots), hierarchical clustering, and group pattern visualization.
- heatmaps
    Layouts for heatmap visualizations of genomic, chemical, and reference data.
- toxicity
    Layouts for visualization of toxicity prediction results.

Public API
----------
The most relevant layouts from each subpackage are re-exported here, enabling direct imports::

    from layouts import get_gene_sample_heatmap_layout, get_sample_upset_layout

Exposed Layout Functions
------------------------
- Results tables: get_biorempp_results_table_layout, get_hadeg_results_table_layout, get_toxcsm_results_table_layout
- Gene and pathway analyses: get_pathway_ko_bar_chart_layout, get_sample_ko_pathway_bar_chart_layout, get_ko_count_bar_chart_layout, get_ko_violin_boxplot_layout, get_sample_ko_scatter_layout
- Entity interactions: get_sample_enzyme_activity_layout, get_gene_compound_scatter_layout, get_gene_compound_network_layout, get_compound_scatter_layout, get_sample_gene_scatter_layout
- Rankings: get_rank_compounds_gene_layout, get_rank_compounds_by_sample_layout, get_rank_samples_by_compound_layout
- Intersections and grouping: get_sample_clustering_layout, get_sample_upset_layout, get_sample_groups_layout
- Heatmaps: get_gene_sample_heatmap_layout, get_pathway_heatmap_layout, get_sample_reference_heatmap_layout
- Toxicity: get_toxicity_heatmap_layout

Refer to the subpackage documentation for details on each layout function.
"""

# ----------------------------------------------------------------------
# Results-overview layouts
# ----------------------------------------------------------------------
from .results_overview import (
    get_biorempp_results_table_layout,
    get_hadeg_results_table_layout,
    get_toxcsm_results_table_layout,
)

# ----------------------------------------------------------------------
# Gene & pathway-analysis layouts
# ----------------------------------------------------------------------
from .gene_pathway_analysis import (
    get_pathway_ko_bar_chart_layout,
    get_sample_ko_pathway_bar_chart_layout,
    get_ko_count_bar_chart_layout,
    get_ko_violin_boxplot_layout,
    get_sample_ko_scatter_layout,
)

# ----------------------------------------------------------------------
# Entity-interaction layouts
# ----------------------------------------------------------------------
from .entity_interactions import (
    get_sample_enzyme_activity_layout,
    get_gene_compound_scatter_layout,
    get_gene_compound_network_layout,
    get_compound_scatter_layout,
    get_sample_gene_scatter_layout,
)

# ----------------------------------------------------------------------
# Ranking layouts
# ----------------------------------------------------------------------
from .rankings import (
    get_rank_compounds_gene_layout,
    get_rank_compounds_by_sample_layout,
    get_rank_samples_by_compound_layout,
)

# ----------------------------------------------------------------------
# Intersections & grouping layouts
# ----------------------------------------------------------------------
from .intersections_and_groups import (
    get_sample_clustering_layout,
    get_sample_upset_layout,
    get_sample_groups_layout,
)

# ----------------------------------------------------------------------
# Heat-map layouts
# ----------------------------------------------------------------------
from .heatmaps import (
    get_gene_sample_heatmap_layout,
    get_pathway_heatmap_layout,
    get_sample_reference_heatmap_layout,
)

# ----------------------------------------------------------------------
# Toxicity layouts
# ----------------------------------------------------------------------
from .toxicity import get_toxicity_heatmap_layout

# ----------------------------------------------------------------------
# Public interface
# ----------------------------------------------------------------------
__all__ = [
    # results_overview
    "get_biorempp_results_table_layout",
    "get_hadeg_results_table_layout",
    "get_toxcsm_results_table_layout",
    # gene_pathway_analysis
    "get_pathway_ko_bar_chart_layout",
    "get_sample_ko_pathway_bar_chart_layout",
    "get_ko_count_bar_chart_layout",
    "get_ko_violin_boxplot_layout",
    "get_sample_ko_scatter_layout",
    # entity_interactions
    "get_sample_enzyme_activity_layout",
    "get_gene_compound_scatter_layout",
    "get_gene_compound_network_layout",
    "get_compound_scatter_layout",
    "get_sample_gene_scatter_layout",
    # rankings
    "get_rank_compounds_gene_layout",
    "get_rank_compounds_by_sample_layout",
    "get_rank_samples_by_compound_layout",
    # intersections_and_groups
    "get_sample_clustering_layout",
    "get_sample_upset_layout",
    "get_sample_groups_layout",
    # heatmaps
    "get_gene_sample_heatmap_layout",
    "get_pathway_heatmap_layout",
    "get_sample_reference_heatmap_layout",
    # toxicity
    "get_toxicity_heatmap_layout",
]
