"""
P1_COUNT_KO_callbacks.py
------------------------
This script defines callback functions for updating various components of a Dash web application related to KO (KEGG Orthologs) count analysis.

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

# Dash core components
from dash import callback, dash_table, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

# Base libraries
import pandas as pd

# App instance
from app import app

# Core processing
from utils.core.data_processing import merge_input_with_database

# Gene Pathway Analysis – Data processing
from utils.gene_pathway_analysis.gene_counts_across_samples_processing import (
    process_ko_data,
    process_ko_data_violin,
)

# Gene Pathway Analysis – Plotting
from utils.gene_pathway_analysis.gene_counts_across_samples_plot import (
    plot_ko_count,
    create_violin_plot,
)


# ----------------------------------------
# Callback: Update KO Count Bar Chart
# ----------------------------------------

@app.callback(  
    Output('ko-count-bar-chart', 'figure'),  
    [Input('ko-count-range-slider', 'value')],  
    [State('biorempp-merged-data', 'data')]  # MUDANÇA: usar store específico  
)  
def update_ko_count_chart(range_slider_values, biorempp_data):  
    """  
    Updates the KO count bar chart based on the selected RangeSlider values using pre-processed data.  
  
    Parameters:  
    - range_slider_values (list): The minimum and maximum values from the RangeSlider.  
    - biorempp_data (list of dict): Pre-processed data from BioRemPP store.  
  
    Returns:  
    - plotly.graph_objects.Figure: The updated bar chart.  
    """  
    if not biorempp_data:  
        raise PreventUpdate  
  
    # Convert stored processed data into a DataFrame (dados já processados)  
    merged_df = pd.DataFrame(biorempp_data)  
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
    [Input('biorempp-merged-data', 'data')]  # MUDANÇA: usar store específico  
)  
def update_range_slider_values(biorempp_data):  
    """  
    Dynamically updates the RangeSlider's maximum value, default range, and tick marks using pre-processed data.  
  
    Parameters:  
    - biorempp_data (list of dict): Pre-processed data from BioRemPP store.  
  
    Returns:  
    - int: Maximum KO count.  
    - list: Default RangeSlider values ([min, max]).  
    - dict: Marks for the RangeSlider.  
    """  
    if not biorempp_data:  
        raise PreventUpdate  
  
    # Convert stored processed data into a DataFrame (dados já processados)  
    merged_df = pd.DataFrame(biorempp_data)  
    ko_count_df = process_ko_data(merged_df)  # Process KO data  
  
    max_ko_count = ko_count_df['ko_count'].max()  # Determine max KO count  
    marks = {i: str(i) for i in range(0, max_ko_count + 1, max(1, max_ko_count // 10))}  # Generate tick marks  
  
    return max_ko_count, [0, max_ko_count], marks

# ----------------------------------------
# Callback: Update Violin Plot
# ----------------------------------------


@callback(
    Output('ko-violin-boxplot-chart', 'figure'),
    Input('process-data', 'n_clicks'),
    State('stored-data', 'data')
)
def update_ko_violin_boxplot_chart(n_clicks, stored_data):
    """
    Updates the KO violin and boxplot chart using all available samples.

    Parameters
    ----------
    n_clicks : int
        Number of clicks on the "process data" button.
    stored_data : list
        List of dictionaries representing input data stored in Dash Store.

    Returns
    -------
    plotly.graph_objects.Figure
        The violin and boxplot figure of KO distributions.
    
    Raises
    ------
    PreventUpdate
        If data has not been processed or is missing.
    """
    if n_clicks < 1 or not stored_data:
        raise PreventUpdate

    # Load and merge data
    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)

    # Use all available samples
    filtered_df = merged_df.copy()
    ko_count_per_sample = process_ko_data_violin(filtered_df)

    # Generate and return plot
    fig = create_violin_plot(ko_count_per_sample)
    return fig
