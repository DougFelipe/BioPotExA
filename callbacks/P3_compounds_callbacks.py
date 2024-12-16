from dash import callback, html, dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd
from app import app
from utils.data_processing import merge_input_with_database
from utils.plot_processing import plot_compound_scatter

# Callback para inicializar o dropdown
@app.callback(
    [Output('compound-class-dropdown', 'options'),
     Output('compound-class-dropdown', 'value')],
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')]
)
def initialize_compound_class_dropdown(n_clicks, stored_data):
    if not stored_data or n_clicks < 1:
        raise PreventUpdate

    # Processar os dados
    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)
    compound_classes = sorted(merged_df['compoundclass'].unique())

    # Configurar as opções do dropdown e limpar o valor padrão
    dropdown_options = [{'label': cls, 'value': cls} for cls in compound_classes]
    return dropdown_options, None  # Nenhum valor selecionado inicialmente


# Callback para atualizar o gráfico de dispersão ou exibir mensagem padrão
@app.callback(
    Output('compound-scatter-container', 'children'),
    [Input('compound-class-dropdown', 'value')],
    [State('stored-data', 'data')]
)
def update_compound_scatter_plot(selected_class, stored_data):
    # Caso nenhuma classe ou dados estejam disponíveis, exibir mensagem padrão
    if not stored_data or not selected_class:
        return html.P(
            "No graph available. Please select a compound class",
            style={"textAlign": "center", "color": "gray", "fontSize": "16px", "marginTop": "20px"}
        )

    # Processar os dados e renderizar o gráfico
    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)
    filtered_df = merged_df[merged_df['compoundclass'] == selected_class]

    # Gerar o gráfico
    fig = plot_compound_scatter(filtered_df)

    return dcc.Graph(figure=fig, style={"height": "100%"})
