"""
plot_processing.py
------------------
This script contains functions for creating various plots using Plotly

"""

# ----------------------------------------
# Imports
# ----------------------------------------

# Standard Library Imports
import base64
import io
import math

# Third-Party Libraries
import pandas as pd  # Data manipulation
import matplotlib.pyplot as plt  # Visualization with Matplotlib
from matplotlib import use as set_matplotlib_backend  # Backend configuration for Matplotlib
from scipy.cluster.hierarchy import dendrogram  # For hierarchical clustering
import networkx as nx  # For creating and visualizing networks

# Plotly for Interactive Visualizations
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Dash for Web Components and Interactivity
from dash import html, dcc, Input, Output, State

# UpSetPlot for specialized visualizations
from upsetplot import from_memberships, plot

# Project-Specific Utilities
from utils.data_processing import prepare_upsetplot_data, merge_input_with_database

# Matplotlib Backend Configuration
set_matplotlib_backend('Agg')  # Set the backend to 'Agg' for non-interactive rendering

# -------------------------------
# Function: plot_ko_count
# -------------------------------

def plot_ko_count(ko_count_df):
    """
    Creates a bar chart showing the count of unique KOs (genes) per sample.

    Parameters:
    - ko_count_df (pd.DataFrame): A DataFrame containing the KO counts per sample. 
                                  Expected columns: 'sample', 'ko_count'.

    Returns:
    - plotly.graph_objects.Figure: A Plotly bar chart object with KO counts.
    """
    # Create the bar chart and display the KO counts as text on the bars.
    fig = px.bar(
        ko_count_df, 
        x='sample', 
        y='ko_count', 
        text='ko_count',  # Display KO counts as text labels.
        template="simple_white"  # Use the "simple_white" template for clean styling.
    )
    
    # Update trace properties: text position and bar color.
    fig.update_traces(
        textposition='auto',  # Automatically position the text above or inside bars.
        marker=dict(color='steelblue')  # Set the bar color to 'steelblue'.
    )
    
    # Update layout with titles, axis properties, and text formatting.
    fig.update_layout(
        title="Gene Count by Sample",
        xaxis_title='Sample',
        yaxis_title='Unique Gene Count',
        xaxis={'categoryorder': 'total descending'},  # Order categories based on descending values.
        xaxis_tickangle=45,  # Rotate x-axis labels for better readability.
        uniformtext_minsize=10,  # Ensure a minimum font size for text labels.
        uniformtext_mode='hide'  # Hide text labels that don't fit in the bars.
    )
    
    # Return the final figure.
    return fig

# -------------------------------
# Function: create_violin_plot
# -------------------------------

def create_violin_plot(ko_count_per_sample):
    """
    Creates a violin plot with a boxplot overlay to visualize the distribution of unique KO counts per sample.

    Parameters:
    - ko_count_per_sample (pd.DataFrame): A DataFrame containing the KO counts per sample. 
                                          Expected column: 'ko_count'.

    Returns:
    - plotly.graph_objects.Figure: A Plotly violin plot object.
    """
    # Create the violin plot with box overlay and display all points.
    fig = px.violin(
        ko_count_per_sample,
        y='ko_count',
        box=True,  # Add a boxplot overlay.
        points='all',  # Display all points on the plot.
        hover_name='sample',  # Show sample name on hover.
        hover_data={'sample': False, 'ko_count': True},  # Include 'ko_count' and hide 'sample' hover data.
        template="simple_white"  # Use a clean template.
    )

    # Update trace properties: marker size, opacity, and jitter for better visualization.
    fig.update_traces(
        marker=dict(size=5, opacity=1),  # Set point size and opacity.
        line=dict(width=1),  # Set line width.
        jitter=0.3,  # Add jitter to points for better separation.
        pointpos=0  # Center points within the violin.
    )

    # Update the layout with axis titles and styling.
    fig.update_layout(
        yaxis_title='Unique Gene Count',
        showlegend=False,  # Hide the legend.
        template='plotly_white',  # Use a clean white template.
        xaxis_title=''  # Remove the x-axis title.
    )

    # Return the final figure.
    return fig

# -------------------------------
# Function: plot_pathway_ko_counts
# -------------------------------

def plot_pathway_ko_counts(pathway_count_df, selected_sample):
    """
    Creates a bar chart showing the count of unique KOs for each pathway in a selected sample.

    Parameters:
    - pathway_count_df (pd.DataFrame): A DataFrame containing KO counts grouped by pathways and samples.
                                       Expected columns: 'sample', 'pathname', 'unique_ko_count'.
    - selected_sample (str): The sample name to filter the data.

    Returns:
    - plotly.graph_objects.Figure: A Plotly bar chart object showing KO counts per pathway.
    """
    # Filter the DataFrame to include only the data for the selected sample.
    filtered_df = pathway_count_df[pathway_count_df['sample'] == selected_sample]

    # Sort the filtered data by KO count in descending order.
    filtered_df = filtered_df.sort_values('unique_ko_count', ascending=False)

    # Create the bar chart with KO counts displayed as text.
    fig = px.bar(
        filtered_df,
        x='pathname',  # Pathway names on the x-axis.
        y='unique_ko_count',  # KO counts on the y-axis.
        title=f'Unique Gene Count to {selected_sample}',  # Dynamic title with the selected sample name.
        text='unique_ko_count',  # Display KO counts as text on the bars.
        template="simple_white"  # Use the "simple_white" template for clean styling.
    )

    # Update the layout with axis titles and sorting options.
    fig.update_layout(
        xaxis_title='Pathway',  # Label for the x-axis.
        yaxis_title='Unique Gene Count',  # Label for the y-axis.
        xaxis={'categoryorder': 'total descending'}  # Order pathways by descending KO count.
    )

    # Return the final figure.
    return fig

# -------------------------------
# Function: plot_sample_ko_counts
# -------------------------------

def plot_sample_ko_counts(sample_count_df, selected_pathway):
    """
    Creates a bar chart showing the count of unique KOs for a selected metabolic pathway across samples.

    Parameters:
    - sample_count_df (pd.DataFrame): A DataFrame containing KO counts per sample for the selected pathway.
                                      Expected columns: 'sample', 'unique_ko_count'.
    - selected_pathway (str): The name of the selected metabolic pathway.

    Returns:
    - plotly.graph_objects.Figure: A Plotly bar chart object visualizing KO counts.
    """
    # Validate input data
    if sample_count_df.empty:
        raise ValueError("The sample count DataFrame is empty.")
    
    if 'sample' not in sample_count_df.columns or 'unique_ko_count' not in sample_count_df.columns:
        raise ValueError("The DataFrame must contain 'sample' and 'unique_ko_count' columns.")
    
    if sample_count_df['sample'].isnull().any() or sample_count_df['unique_ko_count'].isnull().any():
        raise ValueError("Null values detected in 'sample' or 'unique_ko_count' columns.")
    
    # Create the bar chart
    fig = px.bar(
        sample_count_df,
        x='sample',
        y='unique_ko_count',
        title=f'Unique Gene Count for Pathway: {selected_pathway}',
        text='unique_ko_count',  # Display KO counts on bars
        template="simple_white"
    )
    
    # Update chart layout
    fig.update_layout(
        xaxis_title='Sample',
        yaxis_title='Unique Gene Count',
        xaxis={'categoryorder': 'total descending'},  # Order samples by descending KO count
        xaxis_tickangle=45  # Rotate x-axis labels
    )
    
    return fig

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
# Function: plot_sample_ranking
# -------------------------------

def plot_sample_ranking(sample_ranking_df):
    """
    Creates a bar chart to visualize the ranking of samples based on the number of unique compounds.

    Parameters:
    - sample_ranking_df (pd.DataFrame): A DataFrame containing sample rankings by unique compounds.
                                        Expected columns: 'sample', 'num_compounds'.

    Returns:
    - plotly.graph_objects.Figure: A Plotly bar chart object visualizing sample rankings.
    """
    # Sort the DataFrame by the number of compounds in descending order
    sample_ranking_df = sample_ranking_df.sort_values(by='num_compounds', ascending=False)

    # Create the bar chart
    fig = px.bar(
        sample_ranking_df,
        x='sample',
        y='num_compounds',
        text='num_compounds',  # Display the number of compounds on the bars
        template='simple_white'
    )
    
    # Update chart layout
    fig.update_traces(
        textposition='auto',
        marker=dict(color='steelblue')  # Set bar color
    )
    fig.update_layout(
        title='Ranking of Samples by Compound Interaction',
        xaxis_title='Sample',
        yaxis_title='Number of Compounds',
        xaxis=dict(
            categoryorder='total descending',
            tickangle=45  # Rotate x-axis labels
        ),
        uniformtext_minsize=10,
        uniformtext_mode='hide'
    )
    
    return fig




# -------------------------------
# Function: plot_compound_ranking (P5_rank_compounds)
# -------------------------------

def plot_compound_ranking(compound_ranking_df):
    """
    Creates a bar chart to visualize the ranking of compounds based on the number of unique samples associated.

    Parameters:
    - compound_ranking_df (pd.DataFrame): A DataFrame containing compounds and the count of unique samples.
                                          Expected columns: 'compoundname', 'num_samples'.

    Returns:
    - plotly.graph_objects.Figure: A Plotly bar chart object showing the compound rankings.
    """
    # Sort the DataFrame by the number of samples in descending order
    compound_ranking_df = compound_ranking_df.sort_values(by='num_samples', ascending=False)

    # Create the bar chart with text labels displaying the sample counts
    fig = px.bar(
        compound_ranking_df,
        x='compoundname',
        y='num_samples',
        text='num_samples',  # Display sample counts on the bars
        title='Ranking of Compounds by Sample Interaction',
        template='simple_white'
    )

    # Update trace and layout for better visualization
    fig.update_traces(
        textposition='auto',  # Automatically position the text labels
        marker=dict(color='steelblue')  # Set the bar color
    )
    fig.update_layout(
        xaxis_title='Compound',
        yaxis_title='Number of Samples',
        xaxis=dict(
            categoryorder='total descending',  # Order compounds by descending sample count
            tickangle=45  # Rotate x-axis labels for readability
        ),
        uniformtext_minsize=10,  # Ensure a minimum text size
        uniformtext_mode='hide'  # Hide text labels that do not fit
    )

    return fig

# -------------------------------
# Function: plot_compound_gene_ranking (P6_rank_genes)
# -------------------------------

def plot_compound_gene_ranking(compound_gene_ranking_df):
    """
    Creates a bar chart to visualize the ranking of compounds based on the number of unique genes associated.

    Parameters:
    - compound_gene_ranking_df (pd.DataFrame): A DataFrame containing compounds and the count of unique genes.
                                               Expected columns: 'compoundname', 'num_genes'.

    Returns:
    - plotly.graph_objects.Figure: A Plotly bar chart object showing the compound rankings.
    """
    # Sort the DataFrame by the number of genes in descending order
    compound_gene_ranking_df = compound_gene_ranking_df.sort_values(by='num_genes', ascending=False)

    # Create the bar chart with text labels displaying the gene counts
    fig = px.bar(
        compound_gene_ranking_df,
        x='compoundname',
        y='num_genes',
        text='num_genes',  # Display gene counts on the bars
        title='Ranking of Compounds by Gene Interaction',
        template='simple_white'
    )

    # Update trace and layout for better visualization
    fig.update_traces(
        textposition='auto',  # Automatically position the text labels
        marker=dict(color='steelblue')  # Set the bar color
    )
    fig.update_layout(
        xaxis_title='Compound',
        yaxis_title='Number of Genes',
        xaxis=dict(
            categoryorder='total descending',  # Order compounds by descending gene count
            tickangle=45  # Rotate x-axis labels for readability
        ),
        uniformtext_minsize=10,  # Ensure a minimum text size
        uniformtext_mode='hide'  # Hide text labels that do not fit
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

# -------------------------------
# Function: plot_sample_gene_scatter (P8_gene_sample_association)
# -------------------------------

def plot_sample_gene_scatter(df):
    """
    Creates a scatter plot to visualize the relationship between samples and genes. 
    Dynamically adjusts chart dimensions to ensure all axis labels are visible and prioritizes 
    the most frequent samples.

    Parameters:
    - df (pd.DataFrame): A filtered DataFrame containing gene and sample associations.
                         Expected columns: 'sample', 'genesymbol'.

    Returns:
    - plotly.graph_objects.Figure: A Plotly scatter plot object.
    """
    # Base dimensions for the chart
    base_height = 400  # Default chart height
    extra_height_per_label_y = 25  # Additional height for each excess label on the y-axis
    base_width = 800  # Default chart width
    extra_width_per_label_x = 10  # Additional width for each excess label on the x-axis

    # Calculate the total height based on unique samples
    num_labels_y = df['sample'].nunique()
    label_limit_y = 1  # Minimum threshold for height adjustment
    height = base_height + (num_labels_y - label_limit_y) * extra_height_per_label_y if num_labels_y > label_limit_y else base_height

    # Calculate the total width based on unique genes
    num_labels_x = df['genesymbol'].nunique()
    label_limit_x = 10  # Minimum threshold for width adjustment
    width = base_width + (num_labels_x - label_limit_x) * extra_width_per_label_x if num_labels_x > label_limit_x else base_width

    # Order samples by frequency of occurrence
    sample_order = df['sample'].value_counts().index.tolist()

    # Create the scatter plot
    fig = px.scatter(
        df,
        x='genesymbol',
        y='sample',
        title='Scatter Plot of Genes vs Samples',
        template='simple_white',
        category_orders={'sample': sample_order}  # Prioritize the most frequent samples
    )

    # Update chart layout
    fig.update_layout(
        height=height,
        width=width,
        yaxis=dict(
            tickmode='array',
            tickvals=df['sample'].unique(),
            ticktext=df['sample'].unique(),
            automargin=True,
            tickfont=dict(size=10)  # Adjust font size for readability
        ),
        xaxis=dict(
            tickangle=45,  # Rotate x-axis labels
            tickmode='array',
            tickvals=df['genesymbol'].unique(),
            ticktext=df['genesymbol'].unique(),
            automargin=True,
            tickfont=dict(size=10)
        ),
        xaxis_title='Gene Symbol',
        yaxis_title='Sample',
        margin=dict(l=200, b=100)  # Add margins for long labels
    )

    return fig

# -------------------------------
# Function: plot_sample_reference_heatmap (P9_sample_reference_heatmap)
# -------------------------------

def plot_sample_reference_heatmap(df):
    """
    Creates a heatmap to visualize the count of 'compoundname' for each combination of samples and reference AG.

    Parameters:
    - df (pd.DataFrame): A pivoted DataFrame containing counts of compounds for combinations 
                         of 'sample' and 'referenceAG'. The index should represent 'referenceAG' 
                         and columns should represent 'sample'.

    Returns:
    - plotly.graph_objects.Figure: A Plotly heatmap object.
    """
    # Base dimensions for the heatmap
    base_height = 400
    base_width = 400
    extra_height_per_label = 20  # Additional height per label on the y-axis
    extra_width_per_label = 20   # Additional width per label on the x-axis

    # Calculate dynamic chart dimensions based on the number of labels
    num_labels_x = len(df.columns)  # Number of labels on the x-axis
    num_labels_y = len(df.index)    # Number of labels on the y-axis
    height = base_height + (num_labels_y * extra_height_per_label)
    width = base_width + (num_labels_x * extra_width_per_label)

    # Create the heatmap
    fig = px.imshow(
        df,
        labels=dict(x="Sample", y="Reference AG", color="Compound Count"),
        x=df.columns,
        y=df.index,
        color_continuous_scale="Viridis",
        title="Heatmap of Samples vs Reference AG"
    )

    # Update chart layout to ensure visibility of all labels
    fig.update_layout(
        xaxis=dict(
            title=dict(text="Sample", standoff=50),  # Add spacing for x-axis title
            tickangle=45,
            tickfont=dict(size=10),
            automargin=True
        ),
        yaxis=dict(
            title=dict(text="Reference AG", standoff=50),  # Add spacing for y-axis title
            tickfont=dict(size=10),
            automargin=True
        ),
        margin=dict(l=200, b=200)  # Adjust margins for long labels
    )

    return fig

# -------------------------------
# Function: plot_sample_groups (P10_group_by_class)
# -------------------------------

def plot_sample_groups(df):
    """
    Creates a scatter plot with subplots to visualize sample groups based on compound interactions.

    Parameters:
    - df (pd.DataFrame): A DataFrame containing sample groups. Expected columns include 'sample', 
                         'compoundname', and 'grupo' (group identifier).

    Returns:
    - plotly.graph_objects.Figure: A Plotly figure with subplots for each group.
    """
    # Extract unique groups from the DataFrame
    unique_groups = df['grupo'].unique()

    # Create subplots for each group
    fig = make_subplots(
        rows=1,
        cols=len(unique_groups),
        shared_yaxes=True,  # Share the y-axis across subplots
        subplot_titles=unique_groups,
        horizontal_spacing=0.1
    )

    # Add scatter plots for each group
    for i, group in enumerate(unique_groups):
        group_df = df[df['grupo'] == group]
        group_df = group_df.dropna(subset=['sample', 'compoundname'])  # Drop rows with missing values

        fig.add_trace(
            go.Scatter(
                x=group_df['sample'],
                y=group_df['compoundname'],
                mode='markers',
                name=group,
                showlegend=False
            ),
            row=1,
            col=i+1
        )

    # Update the layout for the entire figure
    fig.update_layout(
        title_text='Sample Groups by Compound Interaction',
        template='simple_white',
        showlegend=False,
        height=600,
        width=300 * len(unique_groups),  # Dynamically adjust width based on group count
    )

    # Configure axes
    fig.update_yaxes(
        tickangle=0,
        tickfont=dict(size=10)
    )

    for i in range(1, len(unique_groups) + 1):
        fig.update_xaxes(row=1, col=i, tickangle=45, title_text=None)

    return fig


# ----------------------------------------
# Function: plot_sample_gene_heatmap (P11)
# ----------------------------------------

def plot_sample_gene_heatmap(grouped_df):
    """
    Creates a heatmap to visualize the relationship between genes and samples with KO counts.
    Handles empty cells by replacing them with a default value to ensure consistent visuals.

    Parameters:
    - grouped_df (pd.DataFrame): A DataFrame grouped by 'Gene' and 'sample', containing the KO count. 
                                 Expected columns: 'Gene', 'sample', 'ko_count'.

    Returns:
    - plotly.graph_objects.Figure: A Plotly heatmap object.
    """
    # Pivot the DataFrame to create a matrix with 'Gene' as rows and 'sample' as columns
    pivot_df = grouped_df.pivot(index='Gene', columns='sample', values='ko_count')

    # Replace NaN values with 0 to handle empty cells
    pivot_df = pivot_df.fillna(0)

    # Create the heatmap
    fig = px.imshow(
        pivot_df,
        color_continuous_scale='Oranges',  # Use an orange color scale
        labels=dict(x="Sample", y="Gene", color="KO Count"),
        title="Heatmap of Ortholog Counts by Sample",
        zmin=0,  # Set minimum value for the color scale
        zmax=pivot_df.max().max()  # Set maximum value for the color scale
    )

    # Update layout for better visualization
    fig.update_layout(
        xaxis=dict(
            title='Sample',
            tickangle=45,  # Rotate x-axis labels
            automargin=True
        ),
        yaxis=dict(
            title='Gene',
            automargin=True
        ),
        coloraxis_colorbar=dict(
            title="KO Count",
            tickvals=list(range(int(grouped_df['ko_count'].min()), int(grouped_df['ko_count'].max()) + 1)),
            ticktext=list(range(int(grouped_df['ko_count'].min()), int(grouped_df['ko_count'].max()) + 1))
        ),
        plot_bgcolor='white',  # Set background color to white
        paper_bgcolor='white'  # Set layout background color to white
    )

    # Remove grid lines for a cleaner look
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)

    return fig

# ----------------------------------------
# Function: plot_pathway_heatmap (P12)
# ----------------------------------------

def plot_pathway_heatmap(df, selected_sample):
    """
    Creates a heatmap to visualize the relationship between pathways and compound pathways with KO counts.
    The heatmaps are displayed as horizontal facets with fixed spacing.

    Parameters:
    - df (pd.DataFrame): A DataFrame grouped by 'Pathway', 'compound_pathway', and 'sample', containing KO counts.
                         Expected columns: 'Pathway', 'compound_pathway', 'sample', 'ko_count'.
    - selected_sample (str): The selected sample to filter the data.

    Returns:
    - plotly.graph_objects.Figure: A Plotly heatmap object with facets for each compound pathway.
    """
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go

    # Filter the DataFrame for the selected sample
    df = df[df['sample'] == selected_sample]

    # Get unique compound pathways
    compound_pathways = df['compound_pathway'].unique()
    n_cols = len(compound_pathways)  # Number of facets based on unique pathways

    # Configure total width with fixed spacing of 100px between facets
    subplot_width = 100  # Standard width for each facet
    spacing = 500  # Fixed space between facets
    total_width = n_cols * subplot_width + (n_cols - 1) * spacing

    # Create subplots with one row and multiple columns
    fig = make_subplots(
        rows=1, cols=n_cols,
        shared_yaxes=False,  # Independent y-axes for each facet
        horizontal_spacing=spacing / total_width  # Convert fixed spacing to a proportional value
    )

    # Add heatmap for each compound pathway
    for i, compound_pathway in enumerate(compound_pathways, start=1):
        # Filter DataFrame for the current pathway
        df_filtered = df[df['compound_pathway'] == compound_pathway]

        # Create the heatmap matrix
        heatmap_data = df_filtered.pivot_table(
            index='Pathway', columns='compound_pathway', values='ko_count', aggfunc='sum', fill_value=0
        )

        # Remove empty rows and columns
        heatmap_data = heatmap_data.loc[(heatmap_data != 0).any(axis=1), (heatmap_data != 0).any(axis=0)]

        # Only add the heatmap if data exists
        if not heatmap_data.empty:
            heatmap = go.Heatmap(
                z=heatmap_data.values,
                x=heatmap_data.columns,
                y=heatmap_data.index,
                colorscale='Oranges',
                showscale=True,  # Display the color bar
                colorbar=dict(
                    title=dict(
                        text='KO Count',
                        side='right'
                    ),
                    x=(subplot_width * (i - 1) + (i - 1) * spacing + subplot_width) / total_width,  # Position horizontally
                    xanchor='left',
                    y=0.5,
                    yanchor='middle',
                    lenmode='fraction',
                    len=0.6  # Set color bar height
                )
            )
            fig.add_trace(heatmap, row=1, col=i)

        # Update the x-axis for the current column
        fig.update_xaxes(
            automargin=True,
            row=1, col=i
        )

    # Update global layout
    fig.update_layout(
        height=600,  # Fixed total height
        width=total_width,  # Total width based on the number of facets and spacing
        title=f'Heatmap of Pathway vs Compound Pathway for Sample {selected_sample}',  # Global title
        yaxis_title='Pathway',  # Global y-axis title
        template='simple_white',
        showlegend=False  # Remove redundant legends
    )

    # Remove facet titles
    for annotation in fig['layout']['annotations']:
        annotation['text'] = ''

    return fig


# ----------------------------------------
# Function: plot_sample_ko_scatter (P13)
# ----------------------------------------

def plot_sample_ko_scatter(scatter_data, selected_pathway):
    """
    Creates a scatter plot to display the KOs (KEGG Orthology) associated with each sample for a selected pathway.

    Parameters:
    - scatter_data (pd.DataFrame): A DataFrame containing 'sample' and 'genesymbol'.
    - selected_pathway (str): The selected metabolic pathway (used in the plot title).

    Returns:
    - plotly.graph_objects.Figure: A Plotly scatter plot object.
    """
    # Define base dimensions for the chart
    base_height = 400
    base_width = 800
    extra_width_per_label = 10  # Extra width per additional x-axis label
    label_limit_x = 20  # Maximum number of labels on the x-axis before adjusting width

    # Calculate the number of unique labels on the x-axis (samples)
    num_labels_x = scatter_data['sample'].nunique()

    # Dynamically adjust chart width based on the number of x-axis labels
    width = base_width + (num_labels_x - label_limit_x) * extra_width_per_label if num_labels_x > label_limit_x else base_width

    # Dynamically adjust chart height based on the number of y-axis labels (genesymbol)
    extra_height_per_label = 15
    num_labels_y = scatter_data['genesymbol'].nunique()
    label_limit_y = 1
    height = base_height + (num_labels_y - label_limit_y) * extra_height_per_label if num_labels_y > label_limit_y else base_height

    # Dynamic tick spacing for the x-axis
    tick_spacing_x = max(1, num_labels_x // 20)  # Limit to displaying 20 labels on the x-axis

    # Create the scatter plot
    fig = px.scatter(
        scatter_data,
        x='sample',
        y='genesymbol',
        title=f'Scatter Plot of KOs by Sample for Pathway: {selected_pathway}',
        template='simple_white'
    )

    # Update chart layout
    fig.update_layout(
        height=height,
        width=width,
        yaxis=dict(
            categoryorder='total ascending',
            title='Genesymbol',
            tickmode='array',
            tickvals=scatter_data['genesymbol'].unique(),
            ticktext=scatter_data['genesymbol'].unique(),
            automargin=True,
            tickfont=dict(size=10),
        ),
        xaxis=dict(
            title='Sample',
            tickangle=45,  # Rotate x-axis labels
            tickmode='linear',
            tickvals=scatter_data['sample'].unique()[::tick_spacing_x],
            ticktext=scatter_data['sample'].unique()[::tick_spacing_x],
            automargin=True,
        ),
        margin=dict(l=200, b=150)  # Margins for long labels
    )

    return fig

# ----------------------------------------
# Function: plot_enzyme_activity_counts
# ----------------------------------------

def plot_enzyme_activity_counts(enzyme_count_df, sample):
    """
    Creates a bar chart to display the unique enzyme activities for a selected sample.

    Parameters:
    - enzyme_count_df (pd.DataFrame): A DataFrame containing enzyme activities and their unique KO counts.
                                      Expected columns: 'enzyme_activity', 'unique_ko_count'.
    - sample (str): The name of the selected sample.

    Returns:
    - plotly.graph_objects.Figure: A Plotly bar chart object.
    """
    if enzyme_count_df.empty:
        raise ValueError("The enzyme activity count DataFrame is empty.")

    # Create the bar chart
    fig = px.bar(
        enzyme_count_df,
        x='enzyme_activity',
        y='unique_ko_count',
        title=f'Unique Enzyme Activities for {sample}',
        text='unique_ko_count',  # Display unique KO counts on the bars
        template="simple_white"
    )

    # Update chart layout
    fig.update_layout(
        xaxis_title='Enzyme Activity',
        yaxis_title='Unique Gene Count',
        xaxis_tickangle=45  # Rotate x-axis labels
    )

    return fig

# ----------------------------------------
# Function: plot_dendrogram (P15)
# ----------------------------------------

def plot_dendrogram(clustering_matrix, sample_labels, distance_metric, method):
    """
    Creates a dendrogram to visualize hierarchical clustering, using sample names as x-axis labels.

    Parameters:
    - clustering_matrix: The clustering matrix generated by a hierarchical clustering function.
    - sample_labels (list): A list of sample names to use as x-axis labels.
    - distance_metric (str): The distance metric used for clustering.
    - method (str): The clustering method used (e.g., 'average', 'single').

    Returns:
    - dash.html.Img: An HTML image object containing the dendrogram as a PNG.
    """

    # Create the dendrogram as a Matplotlib figure
    plt.figure(figsize=(10, 6))
    dendrogram(clustering_matrix, labels=sample_labels)

    # Add a dynamic title
    plt.title(f'Sample Clustering Dendrogram\nDistance: {distance_metric.capitalize()}, Method: {method.capitalize()}')
    plt.xlabel('Samples')
    plt.ylabel('Distance')

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=-45, ha='left')

    # Convert the Matplotlib figure to a base64-encoded PNG
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    encoded_image = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()

    # Close the figure to avoid Matplotlib conflicts
    plt.close()

    # Return the image as an HTML component for Dash
    return html.Img(src=f'data:image/png;base64,{encoded_image}', style={"width": "100%"})


#P16
# my_dash_app/utils/plot_processing.py
from upsetplot import from_memberships, plot
import matplotlib.pyplot as plt
import pandas as pd
import base64
import io
from sklearn.preprocessing import LabelEncoder


# ----------------------------------------
# Function: render_upsetplot (P16)
# ----------------------------------------

def render_upsetplot(stored_data, selected_samples):
    """
    Renders an UpSet Plot based on selected samples and their associated KOs after merging with the database.

    Parameters:
    - stored_data (dict): Stored data in dictionary format, typically from Dash callbacks.
    - selected_samples (list): List of selected samples to include in the plot.

    Returns:
    - str: Base64-encoded PNG image of the UpSet Plot.
    """
    # Ensure at least two samples are selected
    if len(selected_samples) < 2:
        raise ValueError("At least two samples must be selected to render the UpSet Plot.")

    # Convert stored data to a DataFrame
    input_df = pd.DataFrame(stored_data)

    # Merge input data with the database
    merged_data = merge_input_with_database(input_df)

    # Filter data by selected samples
    filtered_df = merged_data[merged_data['sample'].isin(selected_samples)]

    # Ensure unique KOs for each sample
    filtered_df = filtered_df[['sample', 'ko']].drop_duplicates()

    # Prepare memberships for the UpSet Plot
    memberships = filtered_df.groupby('ko')['sample'].apply(list).apply(lambda x: list(set(x)))

    # Convert memberships to UpSet Plot data format
    upset_data = from_memberships(memberships).groupby(from_memberships(memberships).index).sum()

    # Validate and adjust index dynamically for proper labeling
    try:
        num_levels = len(upset_data.index[0]) if isinstance(upset_data.index[0], tuple) else 1
        index_names = selected_samples[:num_levels]
        new_index = pd.MultiIndex.from_tuples(upset_data.index, names=index_names)
        upset_data.index = new_index
    except Exception as e:
        raise ValueError("Failed to create MultiIndex. Data may be malformed or inconsistent.")

    # Generate the plot
    plt.figure(figsize=(10, 6))
    plot(upset_data, orientation='horizontal')
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight')
    plt.close()
    buffer.seek(0)

    # Encode the plot as a Base64 string
    image_data = base64.b64encode(buffer.read()).decode('utf-8')
    return f"data:image/png;base64,{image_data}"
