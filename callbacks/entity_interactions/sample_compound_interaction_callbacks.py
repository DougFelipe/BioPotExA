"""
P3_compounds_callbacks.py
-------------------------
Callbacks Dash para interação com classes de compostos. As funções de processamento foram movidas para o módulo utilitário.

"""

from dash import callback, html, dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from app import app

# Import utilitários de processamento
from utils.entity_interactions.sample_compound_interaction_processing import (
    extract_compound_classes,
    filter_by_compound_class
)
from utils.entity_interactions.sample_compound_interaction_plot import plot_compound_scatter

# -------------------- Callback: Dropdown --------------------

@app.callback(
    [Output('compound-class-dropdown', 'options'),
     Output('compound-class-dropdown', 'value')],
    Input('biorempp-merged-data', 'data')
)
def initialize_compound_class_dropdown(biorempp_data):
    """
    Inicializa o dropdown usando função utilitária de extração.
    """
    classes = extract_compound_classes(biorempp_data)
    options = [{'label': cls, 'value': cls} for cls in classes]
    return options, None

# -------------------- Callback: Gráfico --------------------

@app.callback(
    Output('compound-scatter-container', 'children'),
    Input('compound-class-dropdown', 'value'),
    State('biorempp-merged-data', 'data')
)
def update_compound_scatter_plot(selected_class, biorempp_data):
    """
    Atualiza o gráfico chamando a função de filtragem e o plot utilitário.
    """
    filtered_df = filter_by_compound_class(biorempp_data, selected_class)
    if filtered_df.empty:
        return html.P(
            "No graph available. Please select a compound class",
            style={"textAlign": "center", "color": "gray", "fontSize": "16px", "marginTop": "20px"}
        )
    fig = plot_compound_scatter(filtered_df)
    return dcc.Graph(figure=fig, style={"height": "100%"})
