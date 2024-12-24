"""
P1_COUNT_KO_callbacks.py
------------------------
This script defines callback functions for updating various components of a Dash web application related to KO (Keystone Organism) count analysis.

The callbacks dynamically update:
- A bar chart displaying KO counts.
- RangeSlider values based on loaded data.
- A violin plot representing KO distributions.
- Dropdown options for selecting samples.

Functions:
- `update_ko_count_chart`: Updates the KO count bar chart based on RangeSlider values.
- `update_range_slider_values`: Adjusts RangeSlider properties dynamically based on data.
- `update_ko_violin_boxplot_chart`: Updates the violin and boxplot chart based on sample selection.
- `update_dropdown_options`: Updates the dropdown menu options for sample selection.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

# Necessary imports
from dash import callback, dash_table, html  # Dash core components
from dash.dependencies import Input, Output, State  # Dependencies for callbacks
from dash.exceptions import PreventUpdate  # Prevents unnecessary updates
import pandas as pd  # Data manipulation

# Local imports
from app import app  # Dash application instance
from utils.data_processing import merge_input_with_database, process_ko_data, process_ko_data_violin
from utils.plot_processing import plot_ko_count, create_violin_plot

# ----------------------------------------
# Callback: Update KO Count Bar Chart
# ----------------------------------------

@app.callback(
    Output('ko-count-bar-chart', 'figure'),
    [Input('ko-count-range-slider', 'value')],
    [State('stored-data', 'data')]
)
def update_ko_count_chart(range_slider_values, stored_data):
    """
    Updates the KO count bar chart based on the selected RangeSlider values.

    Parameters:
    - range_slider_values (list): The minimum and maximum values from the RangeSlider.
    - stored_data (list): Data stored in the Dash Store component.

    Returns:
    - plotly.graph_objects.Figure: The updated bar chart.
    """
    if not stored_data:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)  # Convert stored data to DataFrame
    merged_df = merge_input_with_database(input_df)  # Merge input data with the database
    ko_count_df = process_ko_data(merged_df)  # Process KO data

    # Filter KO counts based on RangeSlider values
    min_value, max_value = range_slider_values
    filtered_ko_count_df = ko_count_df[(ko_count_df['ko_count'] >= min_value) & (ko_count_df['ko_count'] <= max_value)]

    fig = plot_ko_count(filtered_ko_count_df)  # Generate bar chart
    return fig

# ----------------------------------------
# Callback: Update RangeSlider Values
# ----------------------------------------

@app.callback(
    [Output('ko-count-range-slider', 'max'),
     Output('ko-count-range-slider', 'value'),
     Output('ko-count-range-slider', 'marks')],
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')]
)
def update_range_slider_values(n_clicks, stored_data):
    """
    Dynamically updates the RangeSlider's maximum value, default range, and tick marks.

    Parameters:
    - n_clicks (int): Number of times the "process data" button is clicked.
    - stored_data (list): Data stored in the Dash Store component.

    Returns:
    - int: Maximum KO count.
    - list: Default RangeSlider values ([min, max]).
    - dict: Marks for the RangeSlider.
    """
    if n_clicks < 1 or not stored_data:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)  # Convert stored data to DataFrame
    merged_df = merge_input_with_database(input_df)  # Merge input data with the database
    ko_count_df = process_ko_data(merged_df)  # Process KO data

    max_ko_count = ko_count_df['ko_count'].max()  # Determine max KO count
    marks = {i: str(i) for i in range(0, max_ko_count + 1, max(1, max_ko_count // 10))}  # Generate tick marks

    return max_ko_count, [0, max_ko_count], marks

# ----------------------------------------
# Callback: Update Violin Plot
# ----------------------------------------

@app.callback(
    Output('ko-violin-boxplot-chart', 'figure'),
    [Input('process-data', 'n_clicks'), Input('sample-dropdown', 'value')],
    [State('stored-data', 'data')]
)
def update_ko_violin_boxplot_chart(n_clicks, selected_samples, stored_data):
    """
    Updates the violin and boxplot chart based on the selected samples from the dropdown.

    Parameters:
    - n_clicks (int): Number of times the "process data" button is clicked.
    - selected_samples (list): List of selected samples from the dropdown.
    - stored_data (list): Data stored in the Dash Store component.

    Returns:
    - plotly.graph_objects.Figure: The updated violin plot.
    """
    if n_clicks < 1 or not stored_data:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)  # Convert stored data to DataFrame
    merged_df = merge_input_with_database(input_df)  # Merge input data with the database

    # Use all samples if none are selected
    if not selected_samples:
        selected_samples = input_df['sample'].unique()

    # Filter data based on selected samples
    filtered_df = merged_df[merged_df['sample'].isin(selected_samples)]
    ko_count_per_sample = process_ko_data_violin(filtered_df)  # Process KO data for violin plot
    fig = create_violin_plot(ko_count_per_sample)  # Generate violin plot
    return fig

# ----------------------------------------
# Callback: Update Dropdown Options
# ----------------------------------------

@app.callback(
    Output('sample-dropdown', 'options'),
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')]
)
def update_dropdown_options(n_clicks, stored_data):
    """
    Updates the sample dropdown menu options based on the loaded data.

    Parameters:
    - n_clicks (int): Number of times the "process data" button is clicked.
    - stored_data (list): Data stored in the Dash Store component.

    Returns:
    - list: List of options for the dropdown menu, each as a dictionary with `label` and `value`.
    """
    if n_clicks < 1 or not stored_data:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)  # Convert stored data to DataFrame
    sample_options = [{'label': sample, 'value': sample} for sample in input_df['sample'].unique()]  # Generate dropdown options
    return sample_options
