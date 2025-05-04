"""
index.py
---------
This script initializes the Dash application, defines the main layout, and configures navigation between tabs. 
It serves as the central entry point for the app, integrating various components, callbacks, and layouts.
"""

# ----------------------------------------
# Imports
# ----------------------------------------
import logging
logging.basicConfig(level=logging.INFO)

# Import Dash core components for building the interface
from dash import Dash, dcc, html, Input, Output

# Import custom header component
from components.header import Header
from components.documentation import get_features_layout  
from components.bioremediation import get_bioremediation_layout  
from components.regulatory_agencies import get_regulatory_agencies_layout  
from components.contact import get_contact_page

# Import layout functions for different pages
from layouts.about import get_about_layout  
from layouts.data_analysis import get_dataAnalysis_page  
from layouts.results import get_results_layout  
from layouts.help import get_help_layout  

# Import callbacks for application interactivity
import callbacks.callbacks
import callbacks.core.merge_feedback_callbacks
import callbacks.T1_biorempp_callbacks
import callbacks.T2_hadeg_callbacks
import callbacks.T3_toxcsm_callbacks
import callbacks.P1_COUNT_KO_callbacks
import callbacks.P2_KO_20PATHWAY_callbacks
import callbacks.P3_compounds_callbacks
import callbacks.P4_rank_compounds_callbacks
import callbacks.P5_rank_compounds_callbacks
import callbacks.P6_rank_compounds_callbacks
import callbacks.P7_compound_x_genesymbol_callbacks
import callbacks.P8_sample_x_genesymbol_callbacks
import callbacks.P9_sample_x_referenceAG_callbacks
import callbacks.P10_sample_grouping_profile_callbacks
import callbacks.P11_gene_sample__heatmap_callbacks
import callbacks.P12_compaund_pathway_callbacks
import callbacks.P13_gene_sample_scatter_callbacks
import callbacks.P14_sample_enzyme_activity_callbacks
import callbacks.P15_sample_clustering_callbacks
import callbacks.P16_sample_upset_callbacks
import callbacks.P17_gene_compound_network_callbacks
import callbacks.p18_heatmap_faceted_callbacks
from callbacks.download_tables import download_merged_csv  # Callback for downloading merged data

from callbacks.callbacks import handle_progress  # Callback for progress handling

# Import the application instance
from app import app

# ----------------------------------------
# Main Layout Configuration
# ----------------------------------------

# Define the main application layout with support for page navigation
app.layout = html.Div(
    className='main-content',  # CSS class for the main content container
    children=[
        dcc.Location(id='url', refresh=False),
        Header(),
        html.Div(id='page-content'),
        dcc.Store(id='stored-data'),
        dcc.Store(id='merge-status'),
        html.Div(id='output-graphs', style={'display': 'none'}),
        html.Script("""
    console.log("BioRemPP loaded at: " + window.location.pathname);
""")

    ]
)

@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    logging.info(f"[INFO] Rota acessada: {pathname}")

    if pathname == '/data-analysis':
        layout = get_dataAnalysis_page()
    elif pathname == '/results':
        layout = get_results_layout()
    elif pathname == '/help':
        layout = get_help_layout()
    elif pathname == '/documentation':
        layout = get_features_layout()
    elif pathname == '/bioremediation':
        layout = get_bioremediation_layout()
    elif pathname == '/regulatory':
        layout = get_regulatory_agencies_layout()
    elif pathname == '/contact':
        layout = get_contact_page()
    else:
        layout = get_about_layout()

    logging.info(f"[INFO] Layout retornado: {layout.__class__.__name__}")
    return layout

# ----------------------------------------
# Server Initialization
# ----------------------------------------

if __name__ == '__main__':
    print("Starting BioRemPP App...")  # <-- Debug print
    app.run(debug=False, host="0.0.0.0", port=8050)
    #app.run_server(debug=True)  # Development
