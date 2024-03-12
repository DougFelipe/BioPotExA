import pandas as pd
import numpy as np
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# Simulando os dados
data = {
    'Raça': ['Labrador', 'Beagle', 'Bulldog', 'Poodle', 'Golden Retriever',
             'Husky Siberiano', 'Dachshund', 'Boxer', 'Chihuahua', 'Pit Bull',
             'Rottweiler', 'Doberman', 'Shih Tzu', 'Border Collie', 'Cocker Spaniel',
             'Dálmata', 'Pastor Alemão', 'Maltês', 'Pug', 'Yorkshire'],
    'Expectativa de Vida Máxima (Anos)': np.random.randint(10, 16, 20)
}

df = pd.DataFrame(data)

# Criando o aplicativo Dash
app = dash.Dash(__name__)

# Layout da aplicação Dash
app.layout = html.Div([
     html.Div([
                html.H2('Solução 3: Pesquisa de Texto com Sugestões'),
                dcc.Dropdown(
                    id='text-search-dropdown',
                    options=[{'label': raça, 'value': raça} for raça in df['Raça']],
                    multi=True,
                    placeholder="Digite para buscar raças...",
                    style={'width': '100%'}
                ),
                dcc.Graph(id='graph-text-search'),
            ], style={'width': '210mm', 'height': '297mm', 'padding': '10mm', 'boxSizing': 'border-box'})
        ])

# Callback para o gráfico da Pesquisa de Texto com Sugestões
@app.callback(
    Output('graph-text-search', 'figure'),
    [Input('text-search-dropdown', 'value')]
)
def update_graph_text_search(selected_races):
    # Se nenhuma raça for selecionada, mostre o gráfico com todas as raças
    if not selected_races:
        filtered_df = df
    else:
        filtered_df = df[df['Raça'].isin(selected_races)]
    
    fig = px.box(filtered_df, y='Expectativa de Vida Máxima (Anos)', points='all')

    # Atualiza o layout do gráfico
    fig.update_layout(
        xaxis_title='',
        yaxis_title='Expectativa de Vida Máxima (Anos)',
        title_text='Distribuição da Expectativa de Vida Máxima por Raça Selecionada'
    )
    
    # Atualiza os traços para melhorar a visualização dos pontos
    fig.update_traces(marker=dict(size=5, opacity=1), line=dict(width=1))
    
    return fig

# Rodando o servidor
if __name__ == '__main__':
    app.run_server(debug=True)
