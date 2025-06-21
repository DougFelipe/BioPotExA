"""
P17_gene_compound_network_callbacks.py
--------------------------------------
Callback para atualização da visualização da Rede Gene-Compound na aplicação Dash.
"""

from dash import callback, Output, Input
from app import app

# Importa apenas a função de interface do módulo de plot
from utils.entity_interactions.gene_compound_interaction_network_plot import generate_gene_compound_network

import plotly.graph_objects as go
import pandas as pd

@app.callback(
    Output("gene-compound-network-graph", "figure"),
    Input("biorempp-merged-data", "data")
)
def update_gene_compound_network(biorempp_data):
    """
    Atualiza o gráfico de rede Gene-Compound com base nos dados processados.

    Parâmetros
    ----------
    biorempp_data : list[dict]
        Dados processados e armazenados no store do BioRemPP.

    Retorna
    -------
    go.Figure
        Figura Plotly com a rede, ou figura vazia com mensagem.
    """
    if not biorempp_data:
        return go.Figure(
            layout=go.Layout(
                title="No data available to display the network",
                xaxis=dict(visible=False),
                yaxis=dict(visible=False)
            )
        )

    # Monta DataFrame e garante colunas obrigatórias
    merged_df = pd.DataFrame(biorempp_data)
    if not {'genesymbol', 'compoundname'}.issubset(merged_df.columns):
        return go.Figure(
            layout=go.Layout(
                title="Required columns ('genesymbol', 'compoundname') not found in the data",
                xaxis=dict(visible=False),
                yaxis=dict(visible=False)
            )
        )

    network_data = merged_df[['genesymbol', 'compoundname']].dropna().drop_duplicates()
    if network_data.empty:
        return go.Figure(
            layout=go.Layout(
                title="No interactions found between genes and compounds",
                xaxis=dict(visible=False),
                yaxis=dict(visible=False)
            )
        )

    # Chama função de interface do plot (modularizada)
    return generate_gene_compound_network(network_data)
