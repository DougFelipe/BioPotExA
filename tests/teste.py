import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import numpy as np

# Simulando um DataFrame com 5 categorias e valores aleatórios
np.random.seed(42)
categorias = ['Categoria A', 'Categoria B', 'Categoria C', 'Categoria D', 'Categoria E']
valores = np.random.randint(10, 100, size=len(categorias))
df = pd.DataFrame({'Categoria': categorias, 'Valor': valores})

# Criando o gráfico de barras
fig = px.bar(df, x='Categoria', y='Valor', title="")

# Estilizando o gráfico
fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    margin=dict(l=0, r=0, t=0, b=0)
)

# Inicializando o aplicativo Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Teste de Design", style={'textAlign': 'center'}),
    html.Div([
        html.Div([
            html.H3("Título do Menu", style={'textAlign': 'center'}),
            html.Div([
                html.Div([
                    html.H4("Título Filtro", style={'textAlign': 'center'}),
                    dcc.Dropdown(
                        id='filtro-dropdown',
                        options=[{'label': i, 'value': i} for i in categorias],
                        value=categorias[0],
                    ),
                ], style={'flex': '1', 'paddingRight': '10px'}),
                html.Div([
                    html.H4("Título Filtro", style={'textAlign': 'center'}),
                    dcc.Dropdown(
                        id='filtro-radio',
                        options=[{'label': i, 'value': i} for i in categorias],
                        value=categorias[0],
                    ),
                ], style={'flex': '1', 'paddingLeft': '10px'}),
            ], style={'display': 'flex', 'justifyContent': 'space-between'}),
            html.Div([
                html.H4("Título Filtro", style={'textAlign': 'center'}),
                dcc.Slider(
                    id='filtro-slider',
                    min=0,
                    max=len(categorias)-1,
                    marks={i: categorias[i] for i in range(len(categorias))},
                    value=0,
                ),
            ], style={'paddingTop': '10px'}),
        ], style={
            'backgroundColor': '#9f9f9', 'borderRadius': '15px', 'boxShadow': '0 2px 4px rgba(0,0,0,0.2)', 
            'margin': '0 auto 15px', 'padding': '10px', 'width': '50%'
        }),
        dcc.Graph(
            id='grafico-categorias',
            figure=fig
        ),
    ], style={
        'border': '2px solid #ddd', 'borderRadius': '15px', 'boxShadow': '0 4px 8px rgba(0,0,0,0.2)', 
        'padding': '20px', 'backgroundColor': 'white', 'width': '80%', 'margin': '0 auto', 'paddingTop': '5px'
    }),
], style={'fontFamily': 'Arial', 'padding': '10mm'})

if __name__ == '__main__':
    app.run_server(debug=True)
