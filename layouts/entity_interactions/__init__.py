"""
layouts.entity_interactions
==========================

This subpackage provides the Dash/Bootstrap layouts for interactive visualizations of gene, enzyme, sample, and compound associations within the BioRemPP application.

Included Layouts
----------------
- enzyme_activity_by_sample_layout: Layout for enzyme activity bar chart per sample.
- gene_compound_interaction_layout: Layout for gene-compound association scatter plot.
- gene_compound_interaction_network_layout: Layout for gene-compound interaction network graph.
- sample_compound_interaction_layout: Layout for compound scatter plot, filterable by compound class.
- sample_gene_associations_layout: Layout for scatter plot of sample-gene associations.
"""

# -------------------------------
# Public Imports (exposed on import)
# -------------------------------

# enzyme_activity_by_sample_layout.py
from .enzyme_activity_by_sample_layout import get_sample_enzyme_activity_layout

# gene_compound_interaction_layout.py
from .gene_compound_interaction_layout import get_gene_compound_scatter_layout

# gene_compound_interaction_network_layout.py
from .gene_compound_interaction_network_layout import get_gene_compound_network_layout

# sample_compound_interaction_layout.py
from .sample_compound_interaction_layout import get_compound_scatter_layout

# sample_gene_associations_layout.py
from .sample_gene_associations_layout import get_sample_gene_scatter_layout

# -------------------------------
# Convenience Variables
# -------------------------------

__all__ = [
    "get_sample_enzyme_activity_layout",
    "get_gene_compound_scatter_layout",
    "get_gene_compound_network_layout",
    "get_compound_scatter_layout",
    "get_sample_gene_scatter_layout",
]
