"""
step_guide.py
-------------
This script defines components for a step-by-step guide in a Dash web application. 
It dynamically generates cards for each step of a process, including step numbers, titles, 
and descriptions, which can be displayed in the user interface.

The guide helps users understand the workflow, such as uploading data, submitting it for analysis, 
and viewing results.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html  # Dash HTML components for creating the UI structure

# ----------------------------------------
# Step Guide Configuration
# ----------------------------------------

# List of steps for the guide
step_guide_list = [
    {"step_number": "Step 1", "title": "Upload", "description": "Upload your data files in the specified format for analysis"},
    {"step_number": "Step 2", "title": "Submit", "description": "Submit your data for processing and validation"},
    {"step_number": "Step 3", "title": "View Results", "description": "View the analysis results and download reports"}
]

# ----------------------------------------
# Function: create_step_card
# ----------------------------------------

def create_step_card(step_number, title, description):
    """
    Creates a single step card component displaying a step number, title, and description.

    Parameters:
    - step_number (str): The number or label of the step (e.g., "Step 1").
    - title (str): The title of the step (e.g., "Upload").
    - description (str): A short description of the step (e.g., "Upload your data files...").

    Returns:
    - dash.html.Div: A Dash HTML Div component representing the step card.
    """
    return html.Div(
        className='step-card',  # Custom CSS class for styling the step card
        children=[
            html.Div(
                className='box',  # Outer container with a box layout
                children=[
                    html.Div(
                        className='content',  # Inner content container
                        children=[
                            # Step number displayed prominently
                            html.H2(step_number, className='step-number'),
                            html.Div(
                                className='step-info',  # Container for title and description
                                children=[
                                    # Step title
                                    html.H3(title),
                                    # Step description
                                    html.P(description)
                                ]
                            )
                        ]
                    )
                ]
            )
        ]
    )

# ----------------------------------------
# Function: create_step_guide
# ----------------------------------------

def create_step_guide():
    """
    Creates a container with multiple step cards generated dynamically from the step guide list.

    Iterates through the `step_guide_list` and creates a card for each step using the `create_step_card` function.

    Returns:
    - dash.html.Div: A Dash HTML Div component containing all step cards.
    """
    return html.Div(
        className='step-cards-container',  # Custom CSS class for the container holding all cards
        children=[
            # Generate a step card for each step in the guide list
            create_step_card(step['step_number'], step['title'], step['description']) 
            for step in step_guide_list
        ]
    )
