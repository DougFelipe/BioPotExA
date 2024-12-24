"""
P8_sample_x_genesymbol_layout.py
---------------------------------
This script defines the layout for a scatter plot that visualizes the relationship 
between samples and genes. It includes interactive filters for selecting specific 
samples and genes to refine the visualization.

The layout consists of:
- Dropdown menus for filtering by sample and gene.
- A container for displaying the scatter plot or a placeholder message when no selection is made.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html, dcc  # Dash HTML and DCC components for UI construction

# ----------------------------------------
# Function: get_sample_gene_scatter_layout
# ----------------------------------------

def get_sample_gene_scatter_layout():
    """
    Constructs the layout for the scatter plot visualizing the relationship 
    between samples and genes, including filters for both.

    Returns:
    - html.Div: A Dash HTML Div containing dropdown menus for filtering and 
      a container for the scatter plot or placeholder text.
    """
    return html.Div([
        # Section for dropdown menus
        html.Div([
            # Sample filter dropdown
            html.Div('Filter by Sample', className='menu-text'),  # Label for sample dropdown
            dcc.Dropdown(
                id='p8-sample-dropdown',  # ID for the sample dropdown
                multi=True,  # Allows multiple selections
                placeholder='Select samples'  # Placeholder text
            ),

            # Gene filter dropdown
            html.Div('Filter by Gene', className='menu-text', style={'margin-top': '20px'}),  # Label for gene dropdown
            dcc.Dropdown(
                id='p8-gene-dropdown',  # ID for the gene dropdown
                multi=True,  # Allows multiple selections
                placeholder='Select genes'  # Placeholder text
            )
        ], className='navigation-menu'),  # CSS class for styling the filter section

        # Container for the scatter plot or placeholder message
        html.Div(
            id='p8-sample-gene-scatter-container',  # ID for the scatter plot container
            children=html.P(
                "Select sample or gene to view results",  # Placeholder message
                style={'textAlign': 'center', 'color': 'gray', 'fontSize': '16px'}  # Styling for the placeholder text
            ),
            className='graph-container',  # CSS class for styling the container
            style={'height': 'auto', 'overflowY': 'auto'}  # Ensures auto height and scrollable content
        )
    ], className='graph-card')  # CSS class for styling the main card container
