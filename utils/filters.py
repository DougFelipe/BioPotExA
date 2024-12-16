"""
filters.py
----------
This script provides utility functions for creating filter components in Dash applications, 
including a function to generate a configurable RangeSlider.
"""

# -------------------------------
# Imports
# -------------------------------

# Import Dash Core Components (dcc) to create interactive UI elements.
from dash import dcc

# -------------------------------
# Function: create_range_slider
# -------------------------------

def create_range_slider(slider_id: str) -> dcc.RangeSlider:
    """
    Creates and returns a Dash RangeSlider component with initial configurations.

    Parameters:
    - slider_id (str): The unique ID for the RangeSlider component.

    Returns:
    - dcc.RangeSlider: A Dash RangeSlider component with initial settings.
    """

    # Create and configure the RangeSlider component.
    # This component allows users to select a range of values interactively.
    return dcc.RangeSlider(
        id=slider_id,  # Assign the specified ID to the slider for callback referencing.
        min=0,  # Initial minimum value of the slider.
        max=10,  # Initial maximum value of the slider. This value will be adjusted dynamically.
        value=[0, 10],  # Initial selected range, spanning the entire slider range. Adjustable dynamically.
        marks={i: str(i) for i in range(11)},  # Initial tick marks, labeled from 0 to 10.
        className='range-slider'  # Add a CSS class for styling purposes.
    )
