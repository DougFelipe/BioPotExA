"""
components.ui
=============

Submódulo de componentes de interface gráfica (UI) reutilizáveis para o projeto BioPotExA.

Cada módulo define um componente específico da interface do usuário, como alertas, botões, barras de navegação etc.
Todos os componentes listados abaixo são expostos diretamente ao importar `components.ui`.

Componentes Disponíveis:
- hadeg_alert, toxcsm_alert (alerts)
- analysis_suggestions_offcanvas (analysis_suggestions)
- analytical_highlight_component (analytical_highlight)
- NeonDivider (divider)
- get_sample_data_button (download_button)
- create_range_slider (filters)
- Header (header)
- navbar (navbar)
- StepGuide (step_guide)
- TooltipSample (tooltip_sample)
"""

from .alerts import hadeg_alert, toxcsm_alert
from .analysis_suggestions import analysis_suggestions_offcanvas
from .analytical_highlight import analytical_highlight_component
from .divider import NeonDivider
from .download_button import get_sample_data_button
from .filters import create_range_slider
from .header import Header
from .navbar import navbar
from .step_guide import create_step_guide
from .tooltip_sample import input_format_tooltip

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
