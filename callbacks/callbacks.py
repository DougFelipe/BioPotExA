# my_dash_app/callbacks/callbacks.py
from dash import html, dcc, dash_table, callback, callback_context
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from dash_table import DataTable

from app import app
import base64
import pandas as pd
import plotly.express as px
import io


from layouts.about import get_about_layout
from layouts.data_analysis import get_dataAnalysis_layout

from utils.data_validator import validate_and_process_input
from utils.data_loader import load_database
from utils.data_processing import merge_input_with_database, process_ko_data


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

#### CALLBACKS PARA MOSTRAR AS TABELAS
# Adicione este callback após os outros callbacks
@app.callback(
    Output('database-data-table', 'children'),
    [Input('process-data', 'n_clicks')],
    prevent_initial_call=True  # Isso evita que o callback seja chamado na inicialização
)
def update_database_table(n_clicks):
    if n_clicks is None or n_clicks < 1:
        raise PreventUpdate

    # Carregue os dados do arquivo Excel
    df_database = load_database('data/database.xlsx')

    # Crie uma tabela Dash DataTable com os dados do Excel
    table = dash_table.DataTable(
        data=df_database.to_dict('records'),
        columns=[{'name': col, 'id': col} for col in df_database.columns],
        page_size=10,
        style_table={'overflowX': 'auto'}
    )

    return html.Div(table)



# Callback para processar os dados e atualizar a tabela na interface do usuário
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

    # Converter os dados armazenados de volta para um DataFrame
    input_df = pd.DataFrame(stored_data)

    # Chama a função para fazer o merge dos dados do input com os dados do database
    merged_df = merge_input_with_database(input_df)

    # Crie e retorne a tabela Dash DataTable com os dados unidos
    table = dash_table.DataTable(
        data=merged_df.to_dict('records'),
        columns=[{'name': i, 'id': i} for i in merged_df.columns],
        page_size=10,
        style_table={'overflowX': 'auto'}
    )

    return html.Div(table, id='ko-count-table-container')


###CALLBACK DO GRÁFICO P1
# Supondo que este seja o callback onde você quer mostrar a tabela e o gráfico
@app.callback(
    Output('ko-count-output', 'children'),  # ID do container no layout
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')]
)
def update_ko_count_output(n_clicks, stored_data):
    if n_clicks < 1 or not stored_data:
        raise PreventUpdate

    # Converter os dados armazenados de volta para um DataFrame
    input_df = pd.DataFrame(stored_data)
    
    # Supondo que você tenha carregado o DataFrame do database em algum lugar
    database_df = 'data/database.xlsx'

    # Merge dos dados de input com o banco de dados
    merged_df = merge_input_with_database(input_df, database_df)

    # Calcula a contagem de 'ko' únicos para cada 'sample'
    ko_counts = process_ko_data(merged_df)

    # Gerar a tabela de dados unidos
    merged_table = DataTable(
        data=merged_df.to_dict('records'),
        columns=[{'name': i, 'id': i} for i in merged_df.columns],
        page_size=10,
        style_table={'overflowX': 'auto'}
    )

    # Gerar o gráfico de barras com a contagem de 'ko'
    fig = px.bar(ko_counts, x='sample', y='ko_count', title="Contagem de KO por Sample")

    # Retornar a tabela e o gráfico para a interface do usuário
    return html.Div([
       dcc.Graph(figure=fig),
       html.Div(merged_table, style={'padding': '20px'})
    ])







####PROVAVELMENTE DISABLE
# Callback para alternar a visibilidade dos gráficos
@app.callback(
    Output('output-graphs', 'style'),
    Input('tabs', 'value')
)
def toggle_graph_visibility(tab):
    if tab == 'tab-data-analysis':
        return {'display': 'block'}  # Mostra os gráficos quando a aba Data Analysis é selecionada
 


