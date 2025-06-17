"""
P16_sample_upset_callbacks.py
-----------------------------
This script defines callbacks for generating and updating an UpSet plot in a Dash web application.
The UpSet plot visualizes the intersection of samples and their associated KOs.

Callbacks:
1. `initialize_upsetplot_dropdown`: Initializes the dropdown with unique sample options based on the processed data.
2. `update_upsetplot`: Updates the UpSet plot based on the selected samples and merged data.

Dependencies:
- Dash for interactivity.
- Pandas for data manipulation.
- Custom utilities for merging input data and rendering the UpSet plot.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import callback, html  # Dash core components and HTML components
from dash.dependencies import Input, Output, State  # Input, Output, and State for callback functionality
from dash.exceptions import PreventUpdate  # Exception to prevent unnecessary updates

from app import app  # Application instance

# Custom utilities
from utils.intersections_and_groups.intersection_analysis_plot import render_upsetplot  # Function to render UpSet plot

import pandas as pd  # Pandas for data manipulation

# ----------------------------------------
# Callback: Initialize Dropdown Options
# ----------------------------------------

@app.callback(  
    [  
        Output('upsetplot-sample-dropdown', 'options'),  # Update the dropdown options with unique samples  
        Output('upsetplot-sample-dropdown', 'value')     # Reset the dropdown value  
    ],  
    [Input('biorempp-merged-data', 'data')]  # MUDANÇA: usar store específico  
)  
def initialize_upsetplot_dropdown(biorempp_data):  
    """  
    Initializes the dropdown for the UpSet plot with unique sample options using pre-processed data.  
  
    Parameters:  
    - biorempp_data (list of dict): Pre-processed data from BioRemPP store.  
  
    Returns:  
    - list: Options for the dropdown menu, each with a sample label and value.  
    - None: Resets the initial selection to None.  
    """  
    if not biorempp_data:  
        return [], None  # Return empty options if no processed data is available  
  
    # Convert stored processed data into a DataFrame (dados já processados)  
    merged_df = pd.DataFrame(biorempp_data)  
    unique_samples = merged_df['sample'].unique()  
    options = [{'label': sample, 'value': sample} for sample in unique_samples]  
  
    return options, None  # No initial selection

# ----------------------------------------
# Callback: Update UpSet Plot
# ----------------------------------------

@app.callback(  
    Output('upset-plot-container', 'children'),  # Update the container with the UpSet plot or a message  
    [Input('upsetplot-sample-dropdown', 'value')],  # Trigger when a sample is selected  
    [State('biorempp-merged-data', 'data')]  # MUDANÇA: usar store específico  
)  
def update_upsetplot(selected_samples, biorempp_data):  
    """  
    Updates the UpSet plot based on the selected samples using pre-processed data.  
  
    Parameters:  
    - selected_samples (list): List of selected sample names from the dropdown.  
    - biorempp_data (list of dict): Pre-processed data from BioRemPP store.  
  
    Returns:  
    - dash.html.Img: An image element displaying the rendered UpSet plot.  
    - dash.html.P: A message indicating no data is available if conditions are not met.  
    """  
    if not selected_samples or not biorempp_data:  
        # Return a message if no data is available or no samples are selected  
        return html.P(  
            "No data available. Please select a sample",  
            id="no-upset-plot-message",  # ID for styling or testing  
            style={"textAlign": "center", "color": "gray"}  # Styling for the message  
        )  
  
    # Convert stored processed data into a DataFrame (dados já processados)  
    merged_df = pd.DataFrame(biorempp_data)  
  
    # Render the UpSet plot using the processed data and selected samples  
    image_src = render_upsetplot(merged_df.to_dict('records'), selected_samples)  
  
    # Return the UpSet plot as an image  
    return html.Img(  
        src=image_src,  # Base64-encoded image source  
        style={"width": "100%", "margin-top": "20px"}  # Styling for the image  
    )
