"""
about.py
--------
This script defines the layout for the "About" page of the Dash web application. 
The "About" page provides an introduction to the Bioremediation Potential Profile (BioRemPP), 
including its purpose, features, and integration with external databases.

The page includes:
- A title and subtitle describing BioRemPP.
- An explanation of the tool's biotechnological potential in bioremediation.
- Visual representation of integrated databases.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html  # Dash HTML components for UI structure
from layouts.data_analysis import get_dataAnalysis_layout  # Import the Data Analysis page layout

# ----------------------------------------
# Function: get_about_layout
# ----------------------------------------

def get_about_layout():
    """
    Defines and returns the layout for the "About" tab.

    The layout includes:
    - A description of BioRemPP's purpose and functionality.
    - Content imported from the Data Analysis layout.
    - A section highlighting the integration of various databases.
    - Logos of the integrated databases.

    Additionally, it now displays an image (graphical_abstract.png) above the "How to Cite" section.

    Returns:
    - dash.html.Div: The "About" page layout as a Dash HTML Div component.
    """
    return html.Div(
        [
            # BioRemPP Description Section
            html.Div(
                [
                    html.Div(
                        [
                            # Main Title
                            #html.H3('BioRemPP', className='about-BioRemPP-title'),
                            # Subtitle
                            html.H3('Bioremediation Potential Profile', className='about-BioRemPP-subtitle'),
                            # Horizontal line for separation
                            html.Hr(className="my-2"),
                            # Description of BioRemPP
                            html.P(
                                [
                                    (
                                        "Aimed at identifying the biotechnological potential for bioremediation, the Bioremediation Potential Profile (BioRemPP) was developed to enable the analysis of functional genome annotation data of bacteria, fungi, and plants, allowing the characterization of organisms with potential for pollutant degradation and providing a user interface and interactive data analysis"
                                    ),
                                    html.Br(), html.Br(),
                                    (
                                        "BioRemPP emerges as an innovative data analysis tool in the field of bioremediation by automating the genomic analysis process used in identifying genes, enzymes, metabolic pathways, and biological processes with biotechnological potential to mitigate the environmental impacts associated with these pollutants"
                                    )
                                ],
                                className='about-content'
                            ),



                            # Include content from Data Analysis layout
                            html.Div(
                                get_dataAnalysis_layout(),  # Content dynamically imported from Data Analysis
                                className='data-analysis-content'
                            ),
                        ],
                        className='about-text-container'  # CSS class for the main text container
                    ),
                ],
                className='about-content-container'  # CSS class for the content container
            )
        ],
        className='about-container'  # CSS class for the overall "About" page container
    )
