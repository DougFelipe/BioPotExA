"""
callbacks package
=================

The `callbacks` package orchestrates all user-driven logic in the BioPotExA platform, managing application state, interactive data processing, and dynamic updates to all analytical visualizations.

Unlike explicit layout functions (see `layouts`), callbacks are registered globally as *side-effects* upon import: **importing this package ensures all Dash callbacks are registered to the main application instance**.

This package is modularized into several subpackages, each targeting a distinct scope of the application's functionality. All core Dash callback functions and event handlers are defined here, enabling a maintainable and scalable structure for scientific web applications.

Submodules Overview
-------------------
- core:
    Foundational callbacks for primary data ingestion, table rendering, and registering advanced analysis suggestion routines.
- dashboard:
    Manages top-level UI feedback such as offcanvas toggling, progress feedback, visibility of analytical sections, and EDA report generation.
- entity_interactions:
    Handles callbacks for visualizing gene-compound/sample-compound interactions and compound class-based scatter plots.
- gene_pathway_analysis:
    Contains callbacks for generating and updating gene/pathway-related analyses, including KOs, gene distributions, and pathway-specific metrics.
- heatmaps:
    Specialized callbacks for constructing and updating all major heatmap visualizations (sample-reference, gene-sample, pathway-compound).
- intersections_and_groups:
    Responsible for group-based explorations, intersection analyses, and hierarchical clustering/dendrogram visualizations.
- rankings:
    Manages ranking visualizations for compounds, genes, and samples, often based on selected compound classes.
- results_overview:
    Renders the main results tables for all integrated databases (BioRemPP, HADEG, TOXCSM), supporting on-demand data visualization.
- toxicity:
    Callbacks for toxicity-related analytics, including toxicity prediction heatmaps and risk profile updates.

Usage
-----
Simply import the package once when initializing your Dash app:

    import callbacks  # All callbacks registered automatically

**Do not import callback functions individually.** Importing this package guarantees that all Dash events and outputs are properly registered to the application.

Public API
----------
The package exposes, via explicit import, only the primary callback registration helper `register_analysis_suggestions_callbacks`, which must be called explicitly at app initialization to enable dynamic analytical guidance features. All other callbacks are registered automatically on module import.

Refer to each submodule for details on callback signatures and logic.
"""

from importlib import import_module

_submodules = [
    # core
    'callbacks.core.callbacks',
    'callbacks.core.download_tables',
    'callbacks.core.merge_feedback_callbacks',
    # dashboard
    'callbacks.dashboard.analysis_suggestions_callbacks',
    'callbacks.dashboard.display_tables',
    'callbacks.dashboard.eda_report_callbacks',
    'callbacks.dashboard.progress_callbacks',
    'callbacks.dashboard.toggle_visibility',
    # entity_interactions
    'callbacks.entity_interactions.enzyme_activity_by_sample_callbacks',
    'callbacks.entity_interactions.gene_compound_interaction_callbacks',
    'callbacks.entity_interactions.gene_compound_interaction_network_callbacks',
    'callbacks.entity_interactions.sample_compound_interaction_callbacks',
    'callbacks.entity_interactions.sample_gene_associations_callbacks',
    # gene_pathway_analysis
    'callbacks.gene_pathway_analysis.distribution_of_ko_in_pathways_callbacks',
    'callbacks.gene_pathway_analysis.gene_counts_across_samples_callbacks',
    'callbacks.gene_pathway_analysis.gene_distribution_among_samples_callbacks',
    # heatmaps
    'callbacks.heatmaps.gene_sample_heatmap_callbacks',
    'callbacks.heatmaps.pathway_compound_interaction_callbacks',
    'callbacks.heatmaps.sample_reference_agency_heatmap_callbacks',
    # intersections_and_groups
    'callbacks.intersections_and_groups.clustering_dendrogram_callbacks',
    'callbacks.intersections_and_groups.intersection_analysis_callbacks',
    'callbacks.intersections_and_groups.sample_grouping_by_compound_class_pattern_callbacks',
    # rankings
    'callbacks.rankings.ranking_compounds_by_gene_interaction_callbacks',
    'callbacks.rankings.ranking_compounds_by_sample_interaction_callbacks',
    'callbacks.rankings.ranking_samples_by_compound_interaction_callbacks',
    # results_overview
    'callbacks.results_overview.biorempp_results_table_callbacks',
    'callbacks.results_overview.hadeg_results_table_callbacks',
    'callbacks.results_overview.toxcsm_results_table_callbacks',
    # toxicity
    'callbacks.toxicity.toxicity_prediction_heatmap_callbacks',
]

for _mod_path in _submodules:
    import_module(_mod_path)

# ---------------------------------------------------------------------------
# Public re‑exports
# ---------------------------------------------------------------------------
from callbacks.dashboard.analysis_suggestions_callbacks import (
    register_analysis_suggestions_callbacks,
)

__all__ = [
    'register_analysis_suggestions_callbacks',
]

# Clean‑up internal names
del import_module, _mod_path, _submodules
