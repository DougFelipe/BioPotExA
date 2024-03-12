# my_dash_app/callbacks/callbacks.py
# Importações necessárias
from dash import html, dcc, callback, callback_context, dash_table,Dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd

# Importações locais
from app import app
from layouts.about import get_about_layout
from layouts.data_analysis import get_dataAnalysis_layout
from utils.data_validator import validate_and_process_input
from utils.data_loader import load_database
from utils.data_processing import merge_input_with_database, process_ko_data, merge_with_kegg, process_ko_data_violin,count_ko_per_pathway
from utils.table_utils import create_table_from_dataframe
from utils.plot_processing import plot_ko_count,create_violin_plot,plot_pathway_ko_counts

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

    return df.to_dict('records'), False, html.Div('Arquivo carregado e validado com sucesso.', style={'color': 'green'})

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

# Callback para o gráfico de barras de contagem de KO
@app.callback(
    Output('ko-count-bar-chart', 'figure'),
    [Input('ko-count-range-slider', 'value')],  # Atualizado para o RangeSlider
    [State('stored-data', 'data')]
)
def update_ko_count_chart(range_slider_values, stored_data):
    if not stored_data:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)
    ko_count_df = process_ko_data(merged_df)

    # Filtrar os dados baseado no intervalo do RangeSlider
    min_value, max_value = range_slider_values
    filtered_ko_count_df = ko_count_df[(ko_count_df['ko_count'] >= min_value) & (ko_count_df['ko_count'] <= max_value)]

    # Gerar o gráfico com os dados filtrados
    fig = plot_ko_count(filtered_ko_count_df)

    return fig


# Callback para atualizar os valores do RangeSlider baseado nos dados carregados
@app.callback(
    [Output('ko-count-range-slider', 'max'),
     Output('ko-count-range-slider', 'value'),
     Output('ko-count-range-slider', 'marks')],
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')]
)
def update_range_slider_values(n_clicks, stored_data):
    if n_clicks < 1 or not stored_data:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)
    ko_count_df = process_ko_data(merged_df)
    max_ko_count = ko_count_df['ko_count'].max()
    marks = {i: str(i) for i in range(0, max_ko_count + 1, max(1, max_ko_count // 10))}

    return max_ko_count, [0, max_ko_count], marks


## Callback para gráfico de violino e boxplot

# Callback para atualizar o gráfico de violino e boxplot com base na seleção do dropdown
@app.callback(
    Output('ko-violin-boxplot-chart', 'figure'),
    [Input('process-data', 'n_clicks'), Input('sample-dropdown', 'value')],
    [State('stored-data', 'data')]
)
def update_ko_violin_boxplot_chart(n_clicks, selected_samples, stored_data):
    if n_clicks < 1 or not stored_data:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)

    # Se nenhuma amostra for selecionada, use todas as amostras
    if not selected_samples:
        selected_samples = input_df['sample'].unique()

    filtered_df = merged_df[merged_df['sample'].isin(selected_samples)]
    ko_count_per_sample = process_ko_data_violin(filtered_df)
    fig = create_violin_plot(ko_count_per_sample)
    return fig

# Callback para atualizar as opções do dropdown baseado nos dados carregados
@app.callback(
    Output('sample-dropdown', 'options'),
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')]
)
def update_dropdown_options(n_clicks, stored_data):
    if n_clicks < 1 or not stored_data:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)
    # Supondo que 'sample' é a coluna que contém os nomes das amostras
    sample_options = [{'label': sample, 'value': sample} for sample in input_df['sample'].unique()]
    return sample_options


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
 

# ----------------------------------------
# Callbacks para análise das vias
# ----------------------------------------

# Callback para inicializar o dropdown e o gráfico de barras após o processamento dos dados
@app.callback(
    [Output('pathway-sample-dropdown', 'options'),
     Output('pathway-sample-dropdown', 'value')],
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')]
)
def initialize_dropdown_and_chart(n_clicks, stored_data):
    if n_clicks < 1 or not stored_data:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_with_kegg(input_df)
    pathway_count_df = count_ko_per_pathway(merged_df)

    samples = sorted(pathway_count_df['sample'].unique())
    default_sample = samples[0]

    dropdown_options = [{'label': sample, 'value': sample} for sample in samples]

    return dropdown_options, default_sample

# Callback exclusivo para atualizar o gráfico de barras com base na seleção do dropdown
@app.callback(
    Output('pathway-ko-bar-chart', 'figure'),
    [Input('pathway-sample-dropdown', 'value')],
    [State('stored-data', 'data')]
)
def update_bar_chart(selected_sample, stored_data):
    if not stored_data or not selected_sample:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_with_kegg(input_df)
    pathway_count_df = count_ko_per_pathway(merged_df)
    
    fig = plot_pathway_ko_counts(pathway_count_df, selected_sample)

    return fig
