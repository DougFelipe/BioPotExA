# my_dash_app/callbacks/callbacks.py

# Importações necessárias
from dash import html, dcc, callback, callback_context, dash_table
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd

# Importações locais
from app import app
from layouts.about import get_about_layout
from layouts.data_analysis import get_dataAnalysis_layout
from utils.data_validator import validate_and_process_input
from utils.data_loader import load_database
from utils.data_processing import merge_input_with_database, merge_with_kegg, count_ko_per_pathway, count_ko_per_sample_for_pathway
from utils.table_utils import create_table_from_dataframe
from utils.plot_processing import plot_pathway_ko_counts, plot_sample_ko_counts

# Callback para controle de conteúdo das abas
@app.callback(
    Output('tabs-content', 'children'),
    [Input('tabs', 'value')]
)
def render_tab_content(tab):
    if tab == 'tab-about':
        return get_about_layout()
    elif tab == 'tab-data-analysis':
        return get_dataAnalysis_layout()
    # Adicionar mais condições elif para outras abas conforme necessário

# Callback para upload e processamento de arquivo
@app.callback(
    [Output('stored-data', 'data'), Output('process-data', 'disabled'), Output('alert-container', 'children')],
    [Input('upload-data', 'contents')],
    [State('upload-data', 'filename')]
)
def handle_upload(contents, filename):
    if contents is None:
        raise PreventUpdate

    df, error = validate_and_process_input(contents, filename)
    if error:
        return None, True, html.Div(error, style={'color': 'red'})

    return df.to_dict('records'), False, html.Div('File uploaded and validated successfully', style={'color': 'green'})

# Callback para atualizar tabela na UI após processamento
@app.callback(
    Output('output-data-upload', 'children'),
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')]
)
def update_table(n_clicks, stored_data):
    if n_clicks is None or n_clicks < 1:
        raise PreventUpdate

    if stored_data is None:
        return html.Div('Nenhum dado para exibir.')

    df = pd.DataFrame(stored_data)
    table = create_table_from_dataframe(df, 'data-upload-table')
    return html.Div(table)

# Callback para mostrar tabelas de dados
@app.callback(
    Output('database-data-table', 'children'),
    [Input('process-data', 'n_clicks')],
    prevent_initial_call=True
)
def update_database_table(n_clicks):
    if n_clicks is None or n_clicks < 1:
        raise PreventUpdate

    df_database = load_database('data/database.xlsx')
    table = create_table_from_dataframe(df_database, 'database-data-table')
    return html.Div(table)

# Callback para processar dados e atualizar tabela de contagem de KO
@app.callback(
    Output('ko-count-table-container', 'children'),
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')]
)
def update_ko_count_table(n_clicks, stored_data):
    if n_clicks is None or n_clicks < 1:
        raise PreventUpdate

    if stored_data is None:
        return html.Div('Nenhum dado para exibir.')

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)
    table = dash_table.DataTable(
        data=merged_df.to_dict('records'),
        columns=[{'name': i, 'id': i} for i in merged_df.columns],
        page_size=10,
        style_table={'overflowX': 'auto'}
    )

    return html.Div(table, id='ko-count-table-container')

# Callback para alternar visibilidade de análises adicionais
@app.callback(
    Output('additional-analysis-container', 'style'),
    [Input('process-data', 'n_clicks')]
)
def toggle_additional_analysis_visibility(n_clicks):
    if n_clicks and n_clicks > 0:
        return {'display': 'block'}
    else:
        raise PreventUpdate

# Callback para atualizar tabela com dados mesclados
@app.callback(
    Output('output-merge-table', 'children'),
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')]
)
def update_merged_table(n_clicks, stored_data):
    if n_clicks is None or n_clicks < 1 or not stored_data:
        return None

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_with_kegg(input_df)

    if merged_df.empty:
        return 'Não foram encontradas correspondências com os dados do KEGG.'

    table = create_table_from_dataframe(merged_df, 'output-merge-table')

    return html.Div(table)

# Callback para alternar visibilidade dos gráficos
@app.callback(
    Output('output-graphs', 'style'),
    Input('tabs', 'value')
)
def toggle_graph_visibility(tab):
    if tab == 'tab-data-analysis':
        return {'display': 'block'}


@app.callback(
    [Output('view-results', 'style'), Output('process-data', 'style'), Output('page-state', 'data')],
    [Input('process-data', 'n_clicks')],
    [State('upload-data', 'contents'), State('page-state', 'data')]
)
def process_and_show_view_button(n_clicks, contents, current_state):
    if n_clicks > 0 and contents and current_state == 'initial':
        # Processar os dados aqui
        # data = process_ko_data(contents)
        return {'display': 'inline-block'}, {'display': 'none'}, 'processed'
    return {'display': 'none'}, {'display': 'inline-block'}, current_state

@app.callback(
    [Output('initial-content', 'style'), Output('results-content', 'style')],
    [Input('view-results', 'n_clicks'), State('page-state', 'data')]
)
def display_results(n_clicks, current_state):
    if n_clicks > 0 and current_state == 'processed':
        return {'display': 'none'}, {'display': 'block'}
    return {'display': 'block'}, {'display': 'none'}