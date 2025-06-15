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



# -------------------------------
# Function: plot_compound_scatter
# -------------------------------

def plot_compound_scatter(df):
    """
    Creates a scatter plot to visualize the relationship between samples and compounds,
    with dynamically adjusted layout based on data size.

    Parameters:
    - df (pd.DataFrame): A filtered DataFrame containing columns 'sample', 'compoundname', and 'compoundclass'.

    Returns:
    - plotly.graph_objects.Figure: A Plotly scatter plot object.
    """
    if df.empty:
        raise ValueError("The DataFrame is empty. No data to display.")
    
    # Base layout parameters
    base_height = 400
    base_width = 800
    extra_width_per_label = 10
    label_limit_x = 20

    # Calculate dynamic chart dimensions
    num_labels_x = df['sample'].nunique()
    width = base_width + (num_labels_x - label_limit_x) * extra_width_per_label if num_labels_x > label_limit_x else base_width

    extra_height_per_label = 15
    num_labels_y = df['compoundname'].nunique()
    height = base_height + (num_labels_y - 1) * extra_height_per_label if num_labels_y > 1 else base_height

    # Dynamic tick spacing for x-axis
    tick_spacing_x = max(1, num_labels_x // 20)

    # Create the scatter plot
    fig = px.scatter(
        df,
        x='sample',
        y='compoundname',
        title='Scatter Plot of Samples vs Compounds',
        template='simple_white'
    )
    
    # Update chart layout
    fig.update_layout(
        height=height,
        width=width,
        yaxis=dict(
            categoryorder='total ascending',
            title='Compoundname',
            tickmode='array',
            tickvals=df['compoundname'].unique(),
            ticktext=df['compoundname'].unique(),
            automargin=True,
            tickfont=dict(size=10)
        ),
        xaxis=dict(
            title='Sample',
            tickangle=45,
            tickmode='linear',
            tickvals=df['sample'].unique()[::tick_spacing_x],
            ticktext=df['sample'].unique()[::tick_spacing_x],
            automargin=True
        ),
        margin=dict(l=200, b=150)
    )
    
    return fig





# -------------------------------
# Function: plot_gene_compound_scatter (P7_gene_compound_association)
# -------------------------------

def plot_gene_compound_scatter(df):
    """
    Creates a scatter plot to visualize the relationship between genes and compounds. 
    Adjusts layout dynamically to ensure visibility of all axis labels and prioritizes the most frequent compounds.

    Parameters:
    - df (pd.DataFrame): A filtered DataFrame containing gene and compound associations.
                         Expected columns: 'genesymbol', 'compoundname'.

    Returns:
    - plotly.graph_objects.Figure: A Plotly scatter plot object.
    """
    # Define base dimensions and adjustments for dynamic layout
    base_height = 400  # Default chart height
    extra_height_per_label_y = 25  # Extra height per unique y-axis label
    base_width = 800  # Default chart width
    extra_width_per_label_x = 10  # Extra width per unique x-axis label

    # Calculate dynamic height based on the number of unique compounds
    num_labels_y = df['compoundname'].nunique()
    label_limit_y = 1  # Minimum threshold to add extra height
    height = base_height + (num_labels_y - label_limit_y) * extra_height_per_label_y if num_labels_y > label_limit_y else base_height

    # Calculate dynamic width based on the number of unique genes
    num_labels_x = df['genesymbol'].nunique()
    label_limit_x = 10  # Minimum threshold to add extra width
    width = base_width + (num_labels_x - label_limit_x) * extra_width_per_label_x if num_labels_x > label_limit_x else base_width

    # Order compounds by frequency for better visualization
    compound_order = df['compoundname'].value_counts().index.tolist()

    # Create the scatter plot
    fig = px.scatter(
        df,
        x='genesymbol',
        y='compoundname',
        title='Scatter Plot of Genes vs Compounds',
        template='simple_white',
        category_orders={'compoundname': compound_order}  # Set compound order for the y-axis
    )

    # Update chart layout to adjust margins, axis labels, and font size
    fig.update_layout(
        height=height,
        width=width,
        yaxis=dict(
            categoryorder='total ascending',
            tickmode='array',
            tickvals=df['compoundname'].unique(),
            ticktext=df['compoundname'].unique(),
            automargin=True,
            tickfont=dict(size=10)
        ),
        xaxis=dict(
            title='Gene Symbol',
            tickangle=45,
            tickmode='array',
            tickvals=df['genesymbol'].unique(),
            ticktext=df['genesymbol'].unique(),
            automargin=True,
            tickfont=dict(size=10)
        ),
        yaxis_title='Compound Name',
        margin=dict(l=200, b=100)  # Adjust margins for long labels
    )

    return fig
