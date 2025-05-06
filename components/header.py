"""
header.py
---------
This script defines the header component for a Dash web application. The header includes:
- A main title linking to the "About" page.
- A set of navigation links for different sections of the application.

The header uses HTML components from Dash to structure the left-aligned title and the right-aligned navigation links.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html  # Dash HTML components for creating UI structure

# ----------------------------------------
# Function: Header
# ----------------------------------------

def Header():
    """
    Creates the header component for the web application.

    The header contains:
    - A left-aligned main title ("BioRemPP") linking to the "About" page.
    - Right-aligned navigation links to various sections such as Help, Expected Results, Regulatory Agencies, and more.

    Returns:
    - dash.html.Header: A Dash HTML Header component containing the title and navigation links.
    """
    return html.Header(
        className='main-header',  # CSS class for styling the main header container
        children=[
            # Left-aligned section: Application title
            html.Div(
                className='header-left',  # CSS class for styling the left section
                children=[
                    html.A(
                        'BioRemPP',  # Application name/title
                        href='/about',  # Link to the "About" page
                        className='main-title'  # CSS class for styling the title
                    )
                ]
            ),
            # Right-aligned section: Navigation links
            html.Div(
                className='header-right',  # CSS class for styling the right section
                children=[
                    html.A('Documentation', href='/documentation', className='header-link'),  # Link to Expected Results page
                    html.A("Help", href="/help", className="header-link"),  # Link to Help page
                    html.A('Regulatory Agencies', href='/regulatory', className='header-link'),  # Link to Regulatory Agencies page
                    html.A('Bioremediation', href='/bioremediation', className='header-link'),  # Link to Bioremediation page
                    html.A("Publications", href="/publications", className="header-link"),
                    # html.A('Changelog', href='/changelog', className='header-link'),  # (Commented out) Link to Changelog page
                    html.A('Contact', href='/contact', className='header-link'),  # Link to Contact page
                ]
            )
        ]
    )
