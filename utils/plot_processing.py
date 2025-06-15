"""
plot_processing.py
------------------
This script contains functions for creating various plots using Plotly

"""

# ----------------------------------------
# Imports
# ----------------------------------------

# Standard Library Imports
import math

# Third-Party Libraries
import pandas as pd  # Data manipulation
from matplotlib import use as set_matplotlib_backend  # Backend configuration for Matplotlib
import networkx as nx  # For creating and visualizing networks

# Plotly for Interactive Visualizations
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Dash for Web Components and Interactivity
from dash import dcc, Input, Output, State

# UpSetPlot for specialized visualizations
from upsetplot import from_memberships, plot



# Matplotlib Backend Configuration
set_matplotlib_backend('Agg')  # Set the backend to 'Agg' for non-interactive rendering
