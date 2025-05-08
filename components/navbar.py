"""
navbar.py
---------
This script defines the navigation bar for a Dash web application using Dash HTML components and 
Dash Bootstrap Components (DBC). The navigation bar organizes links into collapsible card sections 
for clear and structured navigation through the application.

The navbar includes:
- A title and subtitle.
- Seven sections, each containing relevant navigation links as `dbc.Card` components.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html  # Dash HTML components for building UI
import dash_bootstrap_components as dbc  # Bootstrap components for styling and cards

# ----------------------------------------
# Navbar Component
# ----------------------------------------

# Main navigation bar containing all sections and links
navbar = html.Div(
    [
        # Application Title
        html.A(
            "Homepage",  # Main application title
            href="/",  # Link to the homepage
            className="navbar-title"  # CSS class for styling the title
        ),
        
        # Subtitle and Navigation Menu Container
        html.Div(
            [
                # Subtitle for the navigation bar
                html.P(
                    "Navigation Menu",
                    className="navbar-subtitle"  # CSS class for styling the subtitle
                ),

                # Container for navigation links organized into cards
                html.Div(
                    [
                        # Section 1: Data Tables and Database Integration
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5("Data Tables and Database Integration", className="card-title"),  # Section title
                                    html.A("BioRemPP Results Table", href="#main-results-table", className="nav-link"),  # Link 1
                                    html.A("HADEG Results Table", href="#hadeg-results-table", className="nav-link"),  # Link 2
                                    html.A("ToxCSM Results Table", href="#toxcsm-results-table", className="nav-link"),  # Link 3
                                ]
                            ),
                            className="nav-card"  # CSS class for styling the card
                        ),

                        # Section 2: Gene and Metabolic Pathway Analysis
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5("Gene and Metabolic Pathway Analysis", className="card-title"),
                                    html.A("Gene Counts Across Samples", href="#gene-count-chart", className="nav-link"),
                                    html.A("Gene Distribution Among Samples", href="#violin-boxplot", className="nav-link"),
                                    html.A("Distribution of KO in Pathways", href="#pathway-ko-bar-chart", className="nav-link"),
                                    html.A("Pathway Activity per Sample", href="#sample-ko-pathway-chart", className="nav-link"),
                                    html.A("Scatter Plot of KOs by Sample", href="#sample-ko-scatter", className="nav-link"),
                                ]
                            ),
                            className="nav-card"
                        ),

                        # Section 3: Interactions Between Entities
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5("Interactions Between Entities", className="card-title"),
                                    html.A("Sample-Compound Interaction", href="#compound-scatter-chart", className="nav-link"),
                                    html.A("Gene-Compound Interaction", href="#gene-compound-scatter-chart", className="nav-link"),
                                    html.A("Sample-Gene Associations", href="#sample-gene-scatter-chart", className="nav-link"),
                                    html.A("Enzyme Activity by Sample", href="#sample-enzyme-activity", className="nav-link"),
                                    html.A("Gene-Compound Network", href="#gene-compound-network", className="nav-link"),
                                ]
                            ),
                            className="nav-card"
                        ),

                        # Section 4: Ranking and Prioritization
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5("Ranking and Prioritization", className="card-title"),
                                    html.A("Ranking of Samples by Compound Interaction", href="#sample-rank-compounds-chart", className="nav-link"),
                                    html.A("Ranking of Compounds by Sample Interaction", href="#compound-rank-chart", className="nav-link"),
                                    html.A("Ranking of Compounds by Gene Interaction", href="#compound-rank-gene-chart", className="nav-link"),
                                ]
                            ),
                            className="nav-card"
                        ),

                        # Section 5: Patterns and Interactions with Heatmaps
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5("Patterns and Interactions with Heatmaps", className="card-title"),
                                    html.A("Sample-Reference Agency Heatmap", href="#sample-reference-heatmap", className="nav-link"),
                                    html.A("Gene-Sample Heatmap", href="#gene-sample-heatmap", className="nav-link"),
                                    html.A("Pathway-Compound Interaction Map", href="#pathway-heatmap", className="nav-link"),
                                ]
                            ),
                            className="nav-card"
                        ),

                        # Section 6: Intersection and Group Exploration
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5("Intersection and Group Exploration", className="card-title"),
                                    html.A("Sample Grouping by Compound Class Pattern", href="#sample-groups-chart", className="nav-link"),
                                    html.A("Intersection Analysis", href="#sample-upset-plot", className="nav-link"),
                                    html.A("Clustering Dendrogram", href="#sample-clustering-dendrogram", className="nav-link"),
                                ]
                            ),
                            className="nav-card"
                        ),

                        # Section 7: Toxicity Predictions
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5("Toxicity Predictions", className="card-title"),
                                    html.A("Comprehensive Toxicity Prediction Heatmap", href="#toxicity-heatmap-faceted", className="nav-link"),
                                ]
                            ),
                            className="nav-card"
                        ),
                    ],
                    className="nav-links"  # CSS class for the overall container of all cards
                ),
            ],
            className="navbar-menu-container"  # CSS class for the menu container
        ),
    ],
    className="navbar-container"  # CSS class for the overall navbar container
)
