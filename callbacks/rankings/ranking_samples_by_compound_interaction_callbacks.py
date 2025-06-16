"""
P4_rank_compounds_callbacks.py
------------------------------
This script defines the Dash callbacks for the "Rank Compounds" feature of the web application. 
It dynamically updates:
- A scatter plot displaying the ranking of samples by compound interaction.
- The range slider used to filter the ranking based on the number of compounds.

The script integrates data processing and plotting utilities to process user inputs and update the UI accordingly.

Functions:
- `update_sample_ranking_plot`: Updates the ranking plot based on range slider values.
- `update_range_slider_values`: Dynamically updates the range slider's maximum value, initial range, and tick marks.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import callback  # Dash callback decorator
from dash.dependencies import Input, Output, State  # Dash callback dependencies
from dash.exceptions import PreventUpdate  # Prevent callback execution under specific conditions
import pandas as pd  # Data manipulation

from app import app  # Main Dash application instance
from utils.core.data_processing import merge_input_with_database  # Utility function to merge input data with the database
from utils.rankings.ranking_samples_by_compound_interaction_processing import process_sample_ranking  # Function to process sample ranking
from utils.rankings.ranking_samples_by_compound_interaction_plot import plot_sample_ranking  # Function to plot sample ranking

# ----------------------------------------
# Callback: Update Sample Ranking Plot
# ----------------------------------------

@app.callback(  
    Output('rank-compounds-scatter-plot', 'figure'),  # Updates the scatter plot figure  
    [Input('compound-count-range-slider', 'value')],  # Listens for range slider value changes  
    [State('biorempp-merged-data', 'data')]  # MUDANÇA: usar store específico  
)  
def update_sample_ranking_plot(range_slider_values, biorempp_data):  
    """  
    Updates the scatter plot showing the ranking of samples by the number of compounds using pre-processed data.  
  
    Parameters:  
    - range_slider_values (list): The current minimum and maximum values of the range slider.  
    - biorempp_data (list of dict): Pre-processed data from BioRemPP store.  
  
    Returns:  
    - plotly.graph_objects.Figure: The updated scatter plot.  
    """  
    if not biorempp_data:  
        raise PreventUpdate  # Stops the callback if no processed data is available  
  
    # Convert stored processed data into a DataFrame (dados já processados)  
    merged_df = pd.DataFrame(biorempp_data)  
    sample_ranking_df = process_sample_ranking(merged_df)  # Processes the sample ranking data  
  
    # Filter the data based on the range slider values  
    min_value, max_value = range_slider_values  
    filtered_df = sample_ranking_df[  
        (sample_ranking_df['num_compounds'] >= min_value) &  
        (sample_ranking_df['num_compounds'] <= max_value)  
    ]  
  
    # Generate the plot with the filtered data  
    fig = plot_sample_ranking(filtered_df)  
    return fig
# ----------------------------------------
# Callback: Update Range Slider Values
# ----------------------------------------

@app.callback(  
    [  
        Output('compound-count-range-slider', 'max'),  # Updates the maximum value of the range slider  
        Output('compound-count-range-slider', 'value'),  # Updates the initial range of the slider  
        Output('compound-count-range-slider', 'marks')  # Updates the tick marks of the slider  
    ],  
    [Input('biorempp-merged-data', 'data')]  # MUDANÇA: usar store específico  
)  
def update_range_slider_values(biorempp_data):  
    """  
    Dynamically updates the range slider values using pre-processed data.  
  
    Parameters:  
    - biorempp_data (list of dict): Pre-processed data from BioRemPP store.  
  
    Returns:  
    - int: The maximum value for the range slider.  
    - list: The initial range [0, max_value].  
    - dict: Tick marks for the range slider.  
    """  
    if not biorempp_data:  
        raise PreventUpdate  # Stops the callback if no processed data is available  
  
    # Convert stored processed data into a DataFrame (dados já processados)  
    merged_df = pd.DataFrame(biorempp_data)  
    sample_ranking_df = process_sample_ranking(merged_df)  # Processes the sample ranking data  
  
    # Define the maximum value for the range slider  
    max_value = sample_ranking_df['num_compounds'].max()  
  
    # Define the initial range and marks for the range slider  
    marks = {i: str(i) for i in range(0, max_value + 1, max(1, max_value // 10))}  # Evenly spaced marks  
    return max_value, [0, max_value], marks
