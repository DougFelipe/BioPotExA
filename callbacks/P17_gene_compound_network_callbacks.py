# callbacks/P17_gene_compound_network_callbacks.py
from dash import callback, Output, Input, State
from app import app
from utils.data_processing import prepare_gene_compound_network_data
from utils.plot_processing import generate_gene_compound_network

@app.callback(
    Output("gene-compound-network-graph", "figure"),
    Input("stored-data", "data")
)
def update_gene_compound_network(stored_data):
    if not stored_data:
        # Retorna uma figura vazia com mensagem
        return go.Figure(
            layout=go.Layout(
                title="No data available to display the network.",
                xaxis=dict(visible=False),
                yaxis=dict(visible=False)
            )
        )

    # Processar os dados
    network_data = prepare_gene_compound_network_data(stored_data)
    if network_data.empty:
        # Retorna uma figura vazia com mensagem
        return go.Figure(
            layout=go.Layout(
                title="No interactions found between genes and compounds.",
                xaxis=dict(visible=False),
                yaxis=dict(visible=False)
            )
        )

    # Gerar o gráfico de rede
    return generate_gene_compound_network(network_data)
