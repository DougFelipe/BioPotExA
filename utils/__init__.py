"""
utils
=====

The `utils` package aggregates a suite of utility subpackages and modules
used throughout the BioRemPP application. It provides core data handling,
entity interaction analysis, gene–pathway workflows, heatmap generation,
intersection and grouping analyses, ranking routines, and toxicity
visualizations, as well as centralized logging configuration.

Subpackages
-----------
- core
    Essential data loading, validation, processing, type optimization,
    table utilities, and upload handling functions.
- entity_interactions
    Functions to analyze and plot gene–compound, enzyme, and sample
    interactions (both processing and plotting).
- gene_pathway_analysis
    Routines for counting and plotting KEGG Orthology (KO) distributions
    across pathways and samples.
- heatmaps
    Heatmap-specific data processing and plot generation modules.
- intersections_and_groups
    Hierarchical clustering, UpSet intersection analysis, and group-based
    plotting tools.
- rankings
    Modules for computing and visualizing rankings of compounds and samples
    based on interaction counts.
- toxicity
    Processing and faceted heatmap plotting for toxicity prediction results.

Modules
-------
- logger_config
    Configures and initializes application-wide logging settings.

Public API
----------
Import subpackages and modules directly from `utils`::

    from utils import core, entity_interactions, gene_pathway_analysis
    from utils import heatmaps, intersections_and_groups, rankings, toxicity
    from utils.logger_config import setup_logger

"""
# Expose subpackages
from . import core
from . import entity_interactions
from . import gene_pathway_analysis
from . import heatmaps
from . import intersections_and_groups
from . import rankings
from . import toxicity

# Expose logger configuration
from .logger_config import setup_logger

__all__ = [
    'core',
    'entity_interactions',
    'gene_pathway_analysis',
    'heatmaps',
    'intersections_and_groups',
    'rankings',
    'toxicity',
    'setup_logger'
]
