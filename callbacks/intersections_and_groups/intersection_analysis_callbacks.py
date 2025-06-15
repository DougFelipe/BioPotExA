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
from utils.data_processing import merge_input_with_database  # Utility for merging input data with the database
from utils.intersections_and_groups.intersection_analysis_plot import render_upsetplot  # Utility for rendering the UpSet plot
import pandas as pd  # Pandas for data manipulation

# ----------------------------------------
# Callback: Initialize Dropdown Options
# ----------------------------------------

@app.callback(
    [
        Output('upsetplot-sample-dropdown', 'options'),  # Update the dropdown options with unique samples
        Output('upsetplot-sample-dropdown', 'value')     # Reset the dropdown value
    ],
    [Input('process-data', 'n_clicks')],  # Trigger when the "Process Data" button is clicked
    [State('stored-data', 'data')]  # Access the stored processed data
)
def initialize_upsetplot_dropdown(n_clicks, merged_data):
    """
    Initializes the dropdown for the UpSet plot with unique sample options.

    Parameters:
    - n_clicks (int): Number of clicks on the "Process Data" button.
    - merged_data (list): Stored data after merging input data with the database.

    Returns:
    - list: Options for the dropdown menu, each with a sample label and value.
    - None: Resets the initial selection to None.

    Raises:
    - PreventUpdate: If no data is available or the button has not been clicked.
    """
    if not merged_data or n_clicks < 1:
        raise PreventUpdate  # Prevent updates if conditions are not met

    # Prepare the data and extract unique sample names
    unique_samples = pd.DataFrame(merged_data)['sample'].unique()
    options = [{'label': sample, 'value': sample} for sample in unique_samples]

    return options, None  # No initial selection

# ----------------------------------------
# Callback: Update UpSet Plot
# ----------------------------------------

@app.callback(
    Output('upset-plot-container', 'children'),  # Update the container with the UpSet plot or a message
    [Input('upsetplot-sample-dropdown', 'value')],  # Trigger when a sample is selected
    [State('stored-data', 'data')]  # Access the stored processed data
)
def update_upsetplot(selected_samples, stored_data):
    """
    Updates the UpSet plot based on the selected samples.

    Parameters:
    - selected_samples (list): List of selected sample names from the dropdown.
    - stored_data (list): Stored data after processing and merging with the database.

    Returns:
    - dash.html.Img: An image element displaying the rendered UpSet plot.
    - dash.html.P: A message indicating no data is available if conditions are not met.
    """
    if not selected_samples or not stored_data:
        # Return a message if no data is available or no samples are selected
        return html.P(
            "No data available. Please select a sample",
            id="no-upset-plot-message",  # ID for styling or testing
            style={"textAlign": "center", "color": "gray"}  # Styling for the message
        )

    # Convert the stored data into a DataFrame
    input_df = pd.DataFrame(stored_data)

    # Merge the input data with the database
    merged_data = merge_input_with_database(input_df)

    # Render the UpSet plot using the merged data and selected samples
    image_src = render_upsetplot(merged_data.to_dict('records'), selected_samples)

    # Return the UpSet plot as an image
    return html.Img(
        src=image_src,  # Base64-encoded image source
        style={"width": "100%", "margin-top": "20px"}  # Styling for the image
    )
