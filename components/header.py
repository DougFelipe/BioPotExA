"""
header.py
---------
This script defines the header component for a Dash web application. The header includes:
- A main title linking to the "About" page.
- A set of navigation links for different sections of the application.

The header uses HTML components from Dash to structure the left-aligned title and the right-aligned navigation links.
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
            html.Span("BioRemPP", style={"color": "#14532d", "fontWeight": "bold", "fontSize": "26px"}),
            html.Div("Bioremediation Potential Profile", style={
                "fontSize": "14px",
                "color": "#e0e0e0",  # tom suave para contraste sobre fundo verde
                "marginTop": "-2px",
                "fontStyle": "italic"
            })
        ]),
        brand_href="/about",
        color="success",
        dark=True,
        children=[
            dbc.NavItem(dbc.NavLink("Documentation", href="/documentation", style={"color": "#fff"})),
            dbc.NavItem(dbc.NavLink("Help", href="/help", style={"color": "#fff"})),
            dbc.NavItem(dbc.NavLink("Regulatory Agencies", href="/regulatory", style={"color": "#fff"})),
            dbc.NavItem(dbc.NavLink("Publications", href="/publications", style={"color": "#fff"})),
            dbc.NavItem(dbc.NavLink("Contact", href="/contact", style={"color": "#fff"})),
        ],
        style={
            "borderTopLeftRadius": "1rem",
            "borderTopRightRadius": "1rem",
            "marginBottom": "20px",
            "boxShadow": "0 4px 12px rgba(0, 0, 0, 0.3)"
        }
    )
