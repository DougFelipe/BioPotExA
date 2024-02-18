# my_dash_app/callbacks/callbacks.py
from dash import html, dcc, dash_table, callback, callback_context
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from app import app
import base64
import pandas as pd
import plotly.express as px
import io


from layouts.about import get_about_layout
from layouts.data_analysis import get_dataAnalysis_layout

from utils.data_validator import validate_and_process_input

@app.callback(
    Output('tabs-content', 'children'),
    [Input('tabs', 'value')]
)
def render_tab_content(tab):
    if tab == 'tab-about':
        return get_about_layout()
    elif tab == 'tab-data-analysis':
        return get_dataAnalysis_layout()
    # Adicione mais condições elif para outras abas conforme necessário.



# Callback para o upload e processamento do arquivo
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

    # O DataFrame é convertido para um dicionário para armazenamento em dcc.Store
    return df.to_dict('records'), False, html.Div('Arquivo carregado e validado com sucesso.', style={'color': 'green'})

# Callback para atualizar a tabela na interface do usuário após o processamento
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

    # Converter os dados armazenados de volta para um DataFrame
    df = pd.DataFrame(stored_data)
    return dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[{'name': i, 'id': i} for i in df.columns],
        page_size=10,  # Número de linhas a serem exibidas por página
        style_table={'overflowX': 'auto'}
    )












####PROVAVELMENTE DISABLE
# Callback para alternar a visibilidade dos gráficos
@app.callback(
    Output('output-graphs', 'style'),
    Input('tabs', 'value')
)
def toggle_graph_visibility(tab):
    if tab == 'tab-data-analysis':
        return {'display': 'block'}  # Mostra os gráficos quando a aba Data Analysis é selecionada
 


