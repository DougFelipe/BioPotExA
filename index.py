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
from components.pages.documentation import get_features_layout  
from components.pages.bioremediation import get_bioremediation_layout  
from components.pages.regulatory_agencies import get_regulatory_agencies_layout  
from components.pages.contact import get_contact_page
from components.pages.publications import get_publications_layout


# Import layout functions for different pages
from components.pages.about import get_about_layout  
from components.pages.data_analysis import get_dataAnalysis_page  
from components.pages.results import get_results_layout  
from components.pages.help import get_help_layout  


# Import callbacks for application interactivity
import callbacks.core.callbacks
import callbacks.core.merge_feedback_callbacks
import callbacks.results_overview.biorempp_results_table_callbacks
import callbacks.results_overview.hadeg_results_table_callbacks
import callbacks.results_overview.toxcsm_results_table_callbacks
import callbacks.gene_pathway_analysis.P1_COUNT_KO_callbacks
import callbacks.gene_pathway_analysis.P2_KO_20PATHWAY_callbacks
import callbacks.entity_interactions.sample_compound_interaction_callbacks
import callbacks.rankings.P4_rank_compounds_callbacks
import callbacks.rankings.P5_rank_compounds_callbacks
import callbacks.rankings.P6_rank_compounds_callbacks
import callbacks.entity_interactions.gene_compound_interaction_callbacks
import callbacks.entity_interactions.sample_gene_associations_callbacks
import callbacks.heatmaps.P9_sample_x_referenceAG_callbacks
import callbacks.intersections_and_groups.P10_sample_grouping_profile_callbacks
import callbacks.heatmaps.P11_gene_sample__heatmap_callbacks
import callbacks.heatmaps.P12_compaund_pathway_callbacks
import callbacks.gene_pathway_analysis.P13_gene_sample_scatter_callbacks
import callbacks.entity_interactions.enzyme_activity_by_sample_callbacks
import callbacks.intersections_and_groups.P15_sample_clustering_callbacks
import callbacks.intersections_and_groups.P16_sample_upset_callbacks
import callbacks.entity_interactions.gene_compound_interaction_network_callbacks
import callbacks.toxicity.p18_heatmap_faceted_callbacks
from callbacks.core.download_tables import download_merged_csv  # Callback for downloading merged data
from callbacks.dashboard.analysis_suggestions_callbacks import register_analysis_suggestions_callbacks
from callbacks.dashboard.eda_report_callbacks import generate_eda_report, toggle_eda_alert


from callbacks.core.callbacks import handle_progress  # Callback for progress handling




# Import the application instance
from app import app
register_analysis_suggestions_callbacks(app)
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
    elif pathname == '/publications':  # Nova rota
        layout = get_publications_layout()
    else:
        layout = get_about_layout()

    logging.info(f"[INFO] Layout retornado: {layout.__class__.__name__}")
    return layout

# ----------------------------------------
# Server Initialization
# ----------------------------------------

if __name__ == '__main__':
    print("Starting BioRemPP App...")  # <-- Debug print
    app.run(debug=False, host="0.0.0.0", port=8050) # Production
    #app.run_server(debug=True)  # Development
