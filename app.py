# my_dash_app/app.py

# Importa a classe Dash do pacote dash.
from dash import Dash

# Importa os componentes de bootstrap do pacote dash_bootstrap_components.
import dash_bootstrap_components as dbc


# Cria a instância principal da aplicação Dash, aplicando um tema externo do Bootstrap
# e configurando opções adicionais.
app = Dash(
    __name__,  # Define o nome do módulo da aplicação.
    external_stylesheets=[dbc.themes.MINTY],  # Aplica o tema Minty do Bootstrap.
    suppress_callback_exceptions=True,  # Configuração para suprimir exceções de callbacks.
    external_scripts=["/assets/scroll.js"]  # Inclua o script para scroll
)
