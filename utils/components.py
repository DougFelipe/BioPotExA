"""
components.py
-------------
This script provides reusable UI components for a Dash application. 
It includes a utility function to create HTML cards with a title and description.
"""

# -------------------------------
# Imports
# -------------------------------

# Import Dash HTML and Core Components for building UI elements.
from dash import html, dcc

# -------------------------------
# Function: create_card
# -------------------------------

def create_card(title: str, content: str) -> html.Div:
    """
    Creates and returns an HTML card component with a title and a description.

    Parameters:
    - title (str): The title to be displayed on the card.
    - content (str): The description or content to be displayed on the card.

    Returns:
    - html.Div: A Dash HTML component representing the card, styled with CSS classes.
    """
    return html.Div(
        children=[
            # Title of the card, styled with a custom CSS class.
            html.H3(title, className='analysis-title'),

            # Description or content of the card, styled with a custom CSS class.
            html.P(content, className='analysis-description')
        ],
        # Main container for the card, styled with a custom CSS class.
        className='analysis-card'
    )
