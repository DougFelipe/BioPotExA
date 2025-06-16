"""
P6_rank_compounds_callbacks.py
------------------------------
This script defines the callbacks for handling the ranking of compounds by gene interaction in a Dash web application.

Key functionalities:
- Populate the dropdown with compound classes based on the processed data.
- Generate a bar plot visualizing the ranking of compounds by the number of unique genes interacting with them.

The callbacks handle user interactions, such as processing data after a button click and dynamically updating the plot based on the selected compound class.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import callback, html, dcc  # Dash components for callbacks and layout
from dash.dependencies import Input, Output, State  # Input, Output, and State for callback interactivity
from dash.exceptions import PreventUpdate  # Exception to prevent unnecessary updates
import pandas as pd  # Data manipulation with pandas

from app import app  # Application instance
from utils.core.data_processing import merge_input_with_database  # Function to merge input data with the database
from utils.rankings.ranking_compounds_by_gene_interaction_processing import process_compound_gene_ranking  # Function to process compound gene ranking
from utils.rankings.ranking_compounds_by_gene_interaction_plot import plot_compound_gene_ranking  # Function to plot compound gene ranking

# ----------------------------------------
# Callback: Initialize Dropdown for Compound Classes
# ----------------------------------------

@app.callback(  
    [Output('p6-compound-class-dropdown', 'options'),  
     Output('p6-compound-class-dropdown', 'value')],  
    [Input('biorempp-merged-data', 'data')]  # USAR STORE ESPECÍFICO  
)  
def initialize_compound_class_dropdown(biorempp_data):  
    """  
    Inicializa dropdown usando dados já processados do store BioRemPP  
    """  
    if not biorempp_data:  
        return [], None  
      
    # Dados já estão processados - não precisa fazer merge novamente  
    merged_df = pd.DataFrame(biorempp_data)  
    compound_classes = sorted(merged_df['compoundclass'].unique())  
    dropdown_options = [{'label': cls, 'value': cls} for cls in compound_classes]  
    return dropdown_options, None  

# ----------------------------------------
# Callback: Update Ranking Plot
# ----------------------------------------

@app.callback(  
    Output('p6-compound-ranking-container', 'children'),  
    [Input('p6-compound-class-dropdown', 'value')],  
    [State('biorempp-merged-data', 'data')]  # USAR STORE ESPECÍFICO  
)  
def update_compound_gene_ranking_plot(selected_class, biorempp_data):  
    """  
    Atualiza gráfico usando dados já processados do store BioRemPP  
    """  
    if not selected_class or not biorempp_data:  
        return html.P("No data available. Please select a compound class")  
      
    # Dados já estão processados - não precisa fazer merge novamente  
    merged_df = pd.DataFrame(biorempp_data)  
    filtered_df = merged_df[merged_df['compoundclass'] == selected_class]  
      
    if filtered_df.empty:  
        return html.P("No data available for the selected compound class")  
      
    compound_gene_ranking_df = process_compound_gene_ranking(filtered_df)  
    fig = plot_compound_gene_ranking(compound_gene_ranking_df)  
    return dcc.Graph(figure=fig, id="p6-rank-compounds-bar-plot")
