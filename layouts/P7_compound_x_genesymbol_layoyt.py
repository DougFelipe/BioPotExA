"""
P7_compound_x_genesymbol_layout.py
-----------------------------------
This script defines the layout for a scatter plot visualizing the relationship between genes and compounds. 
It includes dropdown filters for selecting specific compounds and genes and an initial message displayed 
until the filters are applied.

The layout is designed to dynamically update based on user selections.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html, dcc  # Dash HTML and core components for layout creation

# ----------------------------------------
# Function: get_gene_compound_scatter_layout
# ----------------------------------------

def get_gene_compound_scatter_layout():
    """
    Constructs the layout for the scatter plot showing the relationship between genes and compounds.

    The layout includes:
    - Dropdown filters for selecting compound names and gene symbols.
    - A container for the scatter plot or an initial message if no filters are applied.

    Returns:
    - dash.html.Div: A Dash HTML Div containing the filters and the graph display area.
    """
    return html.Div(
        [
            # Filters Section
            html.Div(
                [
                    # Dropdown for filtering by compound name
                    html.Div('Filter by Compound Name', className='menu-text'),
                    dcc.Dropdown(
                        id='p7-compound-dropdown',
                        multi=True,  # Allows multiple selections
                        placeholder='Select Compound(s)'  # Placeholder text for the dropdown
                    ),
                    # Dropdown for filtering by gene symbol
                    html.Div('Filter by Gene Symbol', className='menu-text'),
                    dcc.Dropdown(
                        id='p7-gene-dropdown',
                        multi=True,  # Allows multiple selections
                        placeholder='Select Gene(s)'  # Placeholder text for the dropdown
                    ),
                ],
                className='navigation-menu'  # CSS class for styling the filters section
            ),
            # Graph Container
            html.Div(
                id='p7-gene-compound-scatter-container',  # Container for the scatter plot or initial message
                className='graph-container',  # CSS class for styling the graph container
                style={'height': 'auto', 'overflowY': 'auto'},  # Dynamic height and vertical overflow handling
                children=html.P(  # Initial message displayed before any filters are applied
                    "Select compound or gene to view results",
                    style={
                        'textAlign': 'center',  # Centers the text
                        'color': 'gray',  # Gray color for the text
                        'fontSize': '16px'  # Font size for the message
                    }
                )
            )
        ],
        className='graph-card'  # CSS class for the overall card layout
    )
