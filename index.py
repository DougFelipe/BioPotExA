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
# Dash imports
from dash import Dash, dcc, html, Input, Output

# Components (importados diretamente do pacote)
from components import (
    Header,
    navbar,
    hadeg_alert,
    toxcsm_alert,
    analysis_suggestions_offcanvas,
    analytical_highlight_component,
    NeonDivider,
    get_sample_data_button,
    create_range_slider
)

# Páginas específicas
from components.pages.documentation import get_features_layout
from components.pages.bioremediation import get_bioremediation_layout
from components.pages.regulatory_agencies import get_regulatory_agencies_layout
from components.pages.contact import get_contact_page
from components.pages.publications import get_publications_layout
from components.pages.about import get_about_layout
from components.pages.data_analysis import get_dataAnalysis_page
from components.pages.results import get_results_layout
from components.pages.help import get_help_layout

# Import all callbacks (automatic registration by side effect)
import callbacks

# Explicit registration for suggestion system
from callbacks.dashboard.analysis_suggestions_callbacks import register_analysis_suggestions_callbacks



# Import the application instance
from app import app, server
register_analysis_suggestions_callbacks(app)
# ----------------------------------------
# Main Layout Configuration
# ----------------------------------------

# Define the main application layout with support for page navigation
app.layout = html.Div(  
    className='main-content',  
    children=[  
        dcc.Location(id='url', refresh=False),  
        Header(),  
        html.Div(id='page-content'),  
        dcc.Store(id='stored-data'),  
        dcc.Store(id='merge-status'),  
        # NOVOS STORES ESPECÍFICOS POR BANCO  
        dcc.Store(id='biorempp-merged-data', data=None),  
        dcc.Store(id='kegg-merged-data', data=None),   
        dcc.Store(id='hadeg-merged-data', data=None),  
        dcc.Store(id='toxcsm-merged-data', data=None),  
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

    try:
        if pathname == '/data-analysis':
            layout = get_dataAnalysis_page()
        elif pathname == '/results':
            layout = get_results_layout()
        elif pathname == '/help':
            layout = get_help_layout()
        elif pathname == '/documentation':
            layout = get_features_layout()
       # elif pathname == '/bioremediation':
        #    layout = get_bioremediation_layout()
        elif pathname == '/regulatory':
            layout = get_regulatory_agencies_layout()
        elif pathname == '/contact':
            layout = get_contact_page()
        elif pathname == '/publications':
            layout = get_publications_layout()
        else:
            layout = get_about_layout()

        logging.info(f"[INFO] Layout carregado: {layout.__class__.__name__}")
        return layout

    except Exception as e:
        logging.exception("Erro ao renderizar a página:")
        return html.Div([
            html.H3("Erro ao carregar a página"),
            html.P("Ocorreu um problema ao tentar exibir o conteúdo solicitado."),
            html.Pre(str(e))
        ])

    return layout

# ----------------------------------------
# Server Initialization
# ----------------------------------------

if __name__ == '__main__':
    print("Starting BioRemPP App...")  # <-- Debug print
    app.run_server(debug=True)  # Development
