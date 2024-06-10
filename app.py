# my_dash_app/app.py
from dash import Dash
import dash_bootstrap_components as dbc


app = Dash(__name__,external_stylesheets=[dbc.themes.MINTY], suppress_callback_exceptions=True)
