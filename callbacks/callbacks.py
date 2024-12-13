# my_dash_app/callbacks/callbacks.py
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, callback, callback_context, dash_table
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd

from app import app
from layouts.about import get_about_layout
from layouts.data_analysis import get_dataAnalysis_layout
from layouts.results import get_results_layout  # Certifique-se de importar o layout de resultados
from utils.data_validator import validate_and_process_input
from utils.data_loader import load_database
from utils.data_processing import merge_input_with_database, merge_with_kegg, count_ko_per_pathway, count_ko_per_sample_for_pathway
from utils.table_utils import create_table_from_dataframe
from utils.plot_processing import plot_pathway_ko_counts, plot_sample_ko_counts
from utils.data_processing import merge_input_with_database_hadegDB, merge_with_toxcsm



@callback(
    [
        Output('stored-data', 'data'),
        Output('process-data', 'disabled'),
        Output('alert-container', 'children'),
        Output('page-state', 'data', allow_duplicate=True)
    ],
    [
        Input('upload-data', 'contents'),
        Input('see-example-data', 'n_clicks')
    ],
    [State('upload-data', 'filename')],
    prevent_initial_call=True
)
def handle_upload_or_example(contents, n_clicks_example, filename):
    ctx = dash.callback_context

    if not ctx.triggered:
        raise PreventUpdate

    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if triggered_id == 'see-example-data':
        try:
            example_data_path = 'data/sample_data.txt'
            with open(example_data_path, 'r') as file:
                example_contents = file.read()

            df, error = validate_and_process_input(example_contents, 'sample_data.txt')
            if error:
                return None, True, dbc.Alert(
                    f'Error processing example dataset: {error}', 
                    color='danger', 
                    is_open=True, 
                    duration=4000
                ), 'initial'

            return (
                df.to_dict('records'), 
                False, 
                dbc.Alert(
                    'Example dataset loaded successfully', 
                    color='success', 
                    is_open=True, 
                    duration=4000
                ), 
                'loaded'
            )
        except Exception as e:
            return None, True, dbc.Alert(
                f'Error loading example dataset: {str(e)}', 
                color='danger', 
                is_open=True, 
                duration=4000
            ), 'initial'

    if triggered_id == 'upload-data':
        if contents:
            df, error = validate_and_process_input(contents, filename)
            if error:
                return None, True, dbc.Alert(
                    error, 
                    color='danger', 
                    is_open=True, 
                    duration=4000
                ), 'initial'

            return (
                df.to_dict('records'),
                False, 
                dbc.Alert(
                    'File uploaded and validated successfully', 
                    color='success', 
                    is_open=True, 
                    duration=4000
                ), 
                'loaded'
            )

    raise PreventUpdate


@app.callback(
    Output('output-data-upload', 'children'),
    Input('stored-data', 'data')  # Atualiza com qualquer modificação no stored-data
)
def update_table(stored_data):
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

@app.callback(
    Output('output-merge-table', 'children'),
    [Input('view-results', 'n_clicks')],
    [State('stored-data', 'data')]
)
def update_merged_table(n_clicks, stored_data):
    if n_clicks is None or n_clicks < 1 or not stored_data:
        return None

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)

    if merged_df.empty:
        return 'No matches found with KEGG data.'

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


@callback(
    [
        Output('progress-bar', 'value'),  # Atualiza o progresso
        Output('progress-bar', 'label'),  # Atualiza o rótulo
        Output('progress-interval', 'disabled'),  # Habilita ou desabilita o intervalo
        Output('progress-container', 'style')  # Controla a exibição da barra
    ],
    [
        Input('upload-data', 'contents'),
        Input('see-example-data', 'n_clicks'),
        Input('process-data', 'n_clicks'),
        Input('progress-interval', 'n_intervals')
    ],
    prevent_initial_call=True
)
def handle_progress(contents, n_clicks_example, n_clicks_submit, n_intervals):
    ctx = dash.callback_context
    triggered_id = ctx.triggered_id

    # Caso o usuário faça upload ou carregue o exemplo
    if triggered_id in ['upload-data', 'see-example-data']:
        return 0, "", True, {"display": "block", "textAlign": "center"}  # Mostra a barra, mas não inicia o progresso

    # Caso o botão "Click to Submit" seja clicado
    if triggered_id == 'process-data':
        return 0, "", False, {"display": "block", "textAlign": "center"}  # Reseta e inicia o progresso

    # Caso os intervalos estejam atualizando a barra
    if triggered_id == 'progress-interval':
        progress = min(n_intervals * 10, 100)  # Incrementa 10% por segundo
        if progress == 100:
            return progress, "Processing Complete!", True, {"display": "block", "textAlign": "center"}  # Finaliza
        return progress, f"{progress}%", False, {"display": "block", "textAlign": "center"}  # Continua o progresso

    raise PreventUpdate

@app.callback(
    [Output('initial-content', 'style'), 
     Output('results-content', 'style')],
    [Input('view-results', 'n_clicks'), 
     State('page-state', 'data')],
    prevent_initial_call=True
)
def display_results(n_clicks, current_state):
    if n_clicks > 0 and current_state == 'processed':
        return {'display': 'none'}, {'display': 'block'}
    return {'display': 'block'}, {'display': 'none'}

@callback(
    [
        Output('view-results', 'style'),  # Controle de visibilidade do botão "View Results"
        Output('process-data', 'style'),  # Controle de visibilidade do botão "Click to Submit"
        Output('page-state', 'data')
    ],
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data'), State('page-state', 'data')],
    prevent_initial_call=True
)
def process_and_toggle_elements(n_clicks, stored_data, current_state):
    if n_clicks > 0 and stored_data and current_state == 'loaded':
        return (
            {'display': 'inline-block'},  # Mostra "View Results"
            {'display': 'none'},  # Oculta "Click to Submit"
            'processed'  # Atualiza o estado para "processed"
        )
    return (
        {'display': 'none'},  # Oculta "View Results"
        {'display': 'inline-block'},  # Mostra "Click to Submit"
        current_state
    )



@app.callback(
    Output('output-merge-hadeg-table', 'children'),
    Input('stored-data', 'data')  # Dispara ao atualizar o stored-data
)
def update_merged_hadeg_table(stored_data):
    if not stored_data:
        return None

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database_hadegDB(input_df)

    if merged_df.empty:
        return 'No matches found with the hadegDB database.'

    table = create_table_from_dataframe(merged_df, 'output-merge-hadeg-table')
    return html.Div(table)


@app.callback(
    Output('output-merge-toxcsm-table', 'children'),
    Input('stored-data', 'data')  # Dispara ao atualizar o stored-data
)
def update_merged_toxcsm_table(stored_data):
    if not stored_data:
        return None

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)

    if merged_df.empty:
        return 'No matches found with the database.'

    final_merged_df = merge_with_toxcsm(merged_df)

    if final_merged_df.empty:
        return 'No matches found with the ToxCSM database.'

    hidden_columns = ['ko', 'compoundclass']
    table = create_table_from_dataframe(final_merged_df, 'output-merge-toxcsm-table', hidden_columns=hidden_columns)

    return html.Div(table)



