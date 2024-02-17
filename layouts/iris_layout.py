# my_dash_app/layouts/iris.py
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Simulando um dataset semelhante ao Iris
# Este dataset será substituído pelo seu dataset real
df = pd.DataFrame({
    'SepalLength': [5.1, 4.9, 4.7, 4.6, 5.0],
    'SepalWidth': [3.5, 3.0, 3.2, 3.1, 3.6],
    'PetalLength': [1.4, 1.4, 1.3, 1.5, 1.4],
    'PetalWidth': [0.2, 0.2, 0.2, 0.2, 0.2],
    'Species': ['setosa', 'setosa', 'setosa', 'setosa', 'setosa']
})

# Criando o gráfico de barras com Plotly Express
fig = px.bar(df, x='Species', y='SepalLength', title='Sepal Length by Species')

# Definindo o layout da página
def get_iris_layout():
    return html.Div([
        dcc.Graph(
            id='iris-bar-chart',
            figure=fig
        ),
        html.Table(
            # Cabeçalho da tabela
            [html.Tr([html.Th(col) for col in df.columns])] +
            # Corpo da tabela
            [html.Tr([
                html.Td(df.iloc[i][col]) for col in df.columns
            ]) for i in range(min(len(df), 5))],
            style={'padding': '20px'}
        )
    ], className='tabs-content')
