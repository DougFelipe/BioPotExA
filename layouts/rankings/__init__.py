"""
layouts.rankings
================

This subpackage provides Bootstrap-based Dash layouts for ranking visualizations within the BioRemPP application.

Included modules:
-----------------
- ranking_compounds_by_gene_interaction_layout: Layout for ranking compounds by associated gene count.
- ranking_compounds_by_sample_interaction_layout: Layout for ranking compounds by associated sample count.
- ranking_samples_by_compound_interaction_layout: Layout for ranking samples by number of unique compounds.

Each layout is designed to facilitate interactive data exploration using standardized dropdowns, sliders, and placeholders.
"""

# -------------------------------
# Public Imports
# -------------------------------

from .ranking_compounds_by_gene_interaction_layout import get_rank_compounds_gene_layout
from .ranking_compounds_by_sample_interaction_layout import get_rank_compounds_layout as get_rank_compounds_by_sample_layout
from .ranking_samples_by_compound_interaction_layout import get_rank_compounds_layout as get_rank_samples_by_compound_layout

# -------------------------------
# Convenience Variables
# -------------------------------

__all__ = [
    "get_rank_compounds_gene_layout",
    "get_rank_compounds_by_sample_layout",
    "get_rank_samples_by_compound_layout",
]
