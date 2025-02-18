"""
about.py
--------
This script defines the layout for the "About" page of the Dash web application. 
The "About" page provides an introduction to the Bioremediation Potential Profile (BioRemPP), 
including its purpose, features, and integration with external databases.

Additionally, it now contains the data upload and submission components (previously in data_analysis.py), 
placed above the "How to Cite" section.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html, dcc  # Dash HTML components
from dash import html  # For UI structure
import dash_bootstrap_components as dbc
from layouts.data_analysis import get_dataAnalysis_layout  # Import the Data Analysis layout (minus upload/submit)
from components.tooltip_sample import input_format_tooltip
from components.download_button import get_sample_data_button
from dash.dependencies import Input, Output, State


# ----------------------------------------
# Function: get_about_layout
# ----------------------------------------

def get_about_layout():
    """
    Defines and returns the layout for the "About" tab.

    The layout includes:
    - A description of BioRemPP's purpose and functionality.
    - The data upload and submission components (previously in data_analysis.py),
      now placed above the "How to Cite" section.
    - Content imported from the Data Analysis layout (minus the upload/submit components).
    - A section highlighting the integration of various databases.
    - Logos of the integrated databases.
    - An image (graphical_abstract.png) above the "How to Cite" section.

    Returns:
    - dash.html.Div: The "About" page layout as a Dash HTML Div component.
    """
    return html.Div(
        className='about-container',  # Overall container class
        children=[
            # BioRemPP Description Section
            html.Div(
                className='about-content-container',
                children=[
                    html.Div(
                        className='about-text-container',
                        children=[
                            # Title & Intro
                            html.H3('Bioremediation Potential Profile', className='about-BioRemPP-subtitle'),
                            html.Hr(className="my-2"),
                            html.P(
                                [
                                    (
                                        "Aimed at identifying the biotechnological potential for bioremediation, the "
                                        "Bioremediation Potential Profile (BioRemPP) was developed to enable the analysis "
                                        "of functional genome annotation data of bacteria, fungi, and plants, allowing "
                                        "the characterization of organisms with potential for pollutant degradation and "
                                        "providing a user interface and interactive data analysis"
                                    ),
                                    html.Br(), html.Br(),
                                    (
                                        "BioRemPP emerges as an innovative data analysis tool in the field of bioremediation "
                                        "by automating the genomic analysis process used in identifying genes, enzymes, "
                                        "metabolic pathways, and biological processes with biotechnological potential to "
                                        "mitigate the environmental impacts associated with these pollutants"
                                    )
                                ],
                                className='about-content'
                            ),

                            # Graphical Abstract Image
                            html.Img(
                                src='/assets/images/graphical_abstract.png',
                                alt='Graphical Abstract',
                                className='graphical-abstract-image'
                            ),

                            # ========== [UPLOAD & SUBMIT COMPONENTS MOVED HERE] ==========
                            # Title "Upload and Analyze Your Data"
                            html.Div(
                                [
                                    html.H2('Upload and Analyze Your Data', className='how-to-use'),
                                    html.Hr(className="my-2"),
                                ],
                                className='title-container'
                            ),

                            html.Div(
                                id='upload-process-card',
                                className='upload-process-card-style',
                                children=[
                                    # Brief explanatory text
                                    html.Div(
                                        className='upload-explanatory-text',
                                        children=[
                                            html.P(
                                                "Submit your file or click the button to load the example dataset",
                                                className='step-explanation'
                                            )
                                        ]
                                    ),
                                    # Container to align the buttons
                                    html.Div(
                                        className='upload-buttons-container',
                                        children=[
                                            dcc.Upload(
                                                id='upload-data',
                                                children=html.Div(['Drag and Drop or ', html.A('Select a File')]),
                                                className='upload-button-style'
                                            ),
                                            html.Span('Or', className='upload-or-text'),
                                            html.Button(
                                                'Click to Automatically Upload Exemple Data',
                                                id='see-example-data',
                                                n_clicks=0,
                                                className='process-sample-button-style'
                                            )
                                        ]
                                    ),
                                    html.Div(
                                        id='alert-container',
                                        className='alert-container'
                                    ),
                                    html.Div(
                                        html.Hr(className="my-2")
                                    ),
                                    html.Div(
                                        className='button-progress-container',
                                        children=[
                                            html.Button(
                                                'Submit',
                                                id='process-data',
                                                n_clicks=0,
                                                className='process-button-style'
                                            ),
                                            html.Button(
                                                'View Results',
                                                id='view-results',
                                                n_clicks=0,
                                                className='view-results-style',
                                                style={'display': 'none'}  # Initially hidden
                                            ),
                                            # Progress bar
                                            html.Div(
                                                id="progress-container",
                                                children=[
                                                    dcc.Interval(
                                                        id="progress-interval",
                                                        n_intervals=0,
                                                        interval=1000,  # 1 second
                                                        disabled=True
                                                    ),
                                                    dbc.Progress(
                                                        id="progress-bar",
                                                        value=0,
                                                        striped=True,
                                                        animated=True,
                                                    )
                                                ],
                                                style={"display": "none"}
                                            ),
                                        ]
                                    ),
                                ]
                            ),
                            # ========== [END OF MOVED COMPONENTS] ==========

                            # "How to Cite" Section
                            html.Div(
                                [
                                    html.H2('How to Cite', className='how-to-use'),
                                    html.Hr(className="my-2"),
                                ],
                                className='title-container'
                            ),
                            html.Div(
                                id='citation-disclaimer-card',
                                className='upload-process-card-style',
                                children=[
                                    html.Div(
                                        className='citation-disclaimer-container',
                                        children=[
                                            html.P([
                                                html.Strong("The BioRemPP server is free and open to all users, and there is no login requirement")
                                            ], className='citation-info-text'),
                                            html.P([
                                                html.Strong("Your citation is really important to us. Please cite this paper if you publish or present results using BioRemPP analysis")
                                            ], className='citation-request-text'),
                                            html.Blockquote(
                                                """
                                                'Placeholder for Citation'
                                                """,
                                                className='citation-text'
                                            )
                                        ]
                                    )
                                ]
                            ),

                            # Data Analysis Layout (minus the upload components)
                            html.Div(
                                get_dataAnalysis_layout(),
                                className='data-analysis-content'
                            ),

                            # Integration of Databases
                            html.H4(
                                "Integration of Databases",
                                className='integration-title'
                            ),
                            html.Div(
                                className='about-image-container',
                                children=[
                                    html.Img(
                                        src='/assets/images/CHEBI_LOGO.png',
                                        className='about-image'
                                    ),
                                    html.Img(
                                        src='/assets/images/PUBCHEM_LOGO.png',
                                        className='about-image'
                                    ),
                                    html.Img(
                                        src='/assets/images/NCBI_LOGO.png',
                                        className='about-image'
                                    ),
                                    html.Img(
                                        src='/assets/images/KEGG_LOGO.gif',
                                        className='about-image'
                                    ),
                                    html.Img(
                                        src='/assets/images/HADEG_LOGO.png',
                                        className='about-image'
                                    ),
                                    html.Img(
                                        src='/assets/images/TOXCSM_LOGO.png',
                                        className='about-image'
                                    ),
                                ]
                            )
                        ]
                    )
                ]
            )
        ]
    )
