# my_dash_app/callbacks/callbacks.py
from dash import html, dcc, dash_table, callback
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from app import app
import base64
import pandas as pd
import plotly.express as px
import io


from layouts.about import get_about_layout
from layouts.data_analysis import get_dataAnalysis_layout

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_tab_content(tab):
    if tab == 'tab-about':
        return get_about_layout()
    elif tab == 'tab-data-analysis':
        return get_dataAnalysis_layout()
    # Você pode adicionar mais condições elif para outras abas aqui.


@app.callback(
    Output('process-data', 'disabled'),
    Output('alert-container', 'children'),
    Input('upload-data', 'contents'),
    prevent_initial_call=True
)
def update_upload_status(contents):
    if contents is not None:
        # Habilita o botão de processamento e exibe o alerta de sucesso
        return False, html.Div('Arquivo carregado com sucesso!', style={'color': 'green'})
    return True, None

@app.callback(
    Output('output-data-upload', 'children'),
    Input('process-data', 'n_clicks'),
    State('upload-data', 'contents'),
    prevent_initial_call=True
)
def process_file(n_clicks, contents):
    if n_clicks > 0 and contents:
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        content = decoded.decode('utf-8')
        lines = content.split('\n')

        # Supondo que cada linha do seu arquivo txt é uma string que você quer contar
        strings_df = pd.DataFrame({'String': lines})
        string_counts = strings_df['String'].value_counts().reset_index()
        string_counts.columns = ['String', 'Frequência']

        # Criando um gráfico de barras com a frequência das strings
        fig = px.bar(string_counts.head(10), x='String', y='Frequência', title='Top 10 Strings Frequentes')

        # Criando uma tabela com as 5 primeiras linhas do arquivo
        table = dash_table.DataTable(
            data=strings_df.head(5).to_dict('records'),
            columns=[{'name': 'String', 'id': 'String'}],
            style_table={'height': '150px', 'overflowY': 'auto'}
        )

        return html.Div([
            dcc.Graph(figure=fig),
            html.H5('5 Primeiras Linhas do Arquivo:'),
            table
        ])
    return None


# Este callback processa o arquivo carregado e armazena os dados
@callback(
    Output('stored-data', 'data'),
    Input('upload-data', 'contents'),
    prevent_initial_call=True
)
def process_and_store_data(contents):
    if not contents:
        raise PreventUpdate

    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
    
    # Armazene os dados em um formato que possa ser usado para criar gráficos
    return df.to_dict('records')

# Este callback atualiza os gráficos com base nos dados armazenados
@callback(
    Output('output-graphs', 'children'),
    Input('stored-data', 'data'),
    prevent_initial_call=True
)
def update_graphs(stored_data):
    if not stored_data:
        raise PreventUpdate

    df = pd.DataFrame(stored_data)
    graphs = []

    # Suponha que temos várias colunas para as quais queremos gráficos
    for column in df.columns:
        if df[column].dtype in ['float64', 'int64']:  # Apenas para colunas numéricas
            fig = px.bar(df, x='Nome_da_Coluna_Categoria', y=column)
            graphs.append(dcc.Graph(figure=fig))

    return graphs


# Callback para alternar a visibilidade dos gráficos
@app.callback(
    Output('output-graphs', 'style'),
    Input('tabs', 'value')
)
def toggle_graph_visibility(tab):
    if tab == 'tab-data-analysis':
        return {'display': 'block'}  # Mostra os gráficos quando a aba Data Analysis é selecionada
 