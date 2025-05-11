# components/badge_analytical.py

from dash import html
import dash_bootstrap_components as dbc

def analytical_highlight():
    return dbc.Badge(
        "Analytical Highlight",
        color="success",
        className="mx-auto mb-2 d-block",
        pill=True,
        style={"width": "fit-content"}  # Ocupa apenas o espaço do texto
    )
