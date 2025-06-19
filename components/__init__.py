"""
components
==========

Reusable UI components for the BioRemPP Dash application, built using Dash and Dash Bootstrap Components (DBC).

Este pacote expõe todos os componentes de UI de forma explícita, importando diretamente dos submódulos em `components/ui/`.
"""

# UI Components (importação explícita)
from .ui.alerts import hadeg_alert, toxcsm_alert
from .ui.analysis_suggestions import analysis_suggestions_offcanvas
from .ui.analytical_highlight import analytical_highlight_component
from .ui.divider import NeonDivider
from .ui.download_button import get_sample_data_button
from .ui.filters import create_range_slider
from .ui.header import Header
from .ui.navbar import navbar
from .ui.step_guide import create_step_guide
from .ui.tooltip_sample import input_format_tooltip

__all__ = [
    "hadeg_alert",
    "toxcsm_alert",
    "analysis_suggestions_offcanvas",
    "analytical_highlight_component",
    "NeonDivider",
    "get_sample_data_button",
    "create_range_slider",
    "Header",
    "navbar",
    "create_step_guide",
    "input_format_tooltip"
]
