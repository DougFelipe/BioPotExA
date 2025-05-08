"""
header.py
---------
This script defines the header component for a Dash web application. The header includes:
- A main title linking to the "About" page.
- A set of navigation links for different sections of the ape the left-aligned title and the right-aligned navigation links.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html  # Dash HTML components for creating UI structure
import dash_bootstrap_components as dbc

# ----------------------------------------
# Function: Header
# ----------------------------------------

def Header():
    return dbc.NavbarSimple(
        brand=html.Div([
            html.Span("BioRemPP", style={
                "color": "#14532d",
                "fontWeight": "bold",
                "fontSize": "26px"
            }),
            html.Div("Bioremediation Potential Profile", style={
                "fontSize": "14px",
                "color": "#348e4c",  # verde médio para contraste sutil
                "marginTop": "-2px",
                "fontStyle": "italic"
            })
        ]),
        brand_href="/about",
        dark=False,  # ⚠️ Não usar dark=True em fundo transparente para evitar texto branco automático
        color=None,
        children=[
            dbc.NavItem(dbc.NavLink("Documentation", href="/documentation", style={"color": "#348e4c", "fontWeight": "500"})),
            dbc.NavItem(dbc.NavLink("Help", href="/help", style={"color": "#348e4c", "fontWeight": "500"})),
            dbc.NavItem(dbc.NavLink("Regulatory Agencies", href="/regulatory", style={"color": "#348e4c", "fontWeight": "500"})),
            dbc.NavItem(dbc.NavLink("Publications", href="/publications", style={"color": "#348e4c", "fontWeight": "500"})),
            dbc.NavItem(dbc.NavLink("Contact", href="/contact", style={"color": "#348e4c", "fontWeight": "500"})),
        ],
        style={
            "backgroundColor": "transparent",
            "borderTopLeftRadius": "0rem",
            "borderTopRightRadius": "0rem",
            "marginBottom": "20px",
            "boxShadow": "none"
        }
    )
