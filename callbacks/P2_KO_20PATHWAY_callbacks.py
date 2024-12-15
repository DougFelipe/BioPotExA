# my_dash_app/callbacks/P2_KO_20PATHWAY_callbacks.py

# Necessary imports
from dash import callback, html, dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd

# Local imports
from app import app
from utils.data_processing import merge_with_kegg, count_ko_per_pathway, count_ko_per_sample_for_pathway
from utils.plot_processing import plot_pathway_ko_counts, plot_sample_ko_counts


# Callback to initialize the sample dropdown
@app.callback(
    [Output('pathway-sample-dropdown', 'options'),
     Output('pathway-sample-dropdown', 'value')],
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')]
)
def initialize_pathway_sample_dropdown(n_clicks, stored_data):
    if not stored_data or n_clicks < 1:
        raise PreventUpdate

    # Prepare data
    input_df = pd.DataFrame(stored_data)
    merged_df = merge_with_kegg(input_df)
    samples = sorted(merged_df['sample'].unique())

    dropdown_options = [{'label': sample, 'value': sample} for sample in samples]

    return dropdown_options, None  # No default value selected


# Callback to update the KO chart per sample
@app.callback(
    Output('pathway-ko-chart-container', 'children'),
    [Input('pathway-sample-dropdown', 'value')],
    [State('stored-data', 'data')]
)
def update_pathway_ko_chart(selected_sample, stored_data):
    if not stored_data:
        return html.P(
            "No chart available. Please select a sample.",
            id="no-pathway-ko-chart-message",
            style={"textAlign": "center", "color": "gray"}
        )

    if not selected_sample:
        return html.P(
            "No sample selected. Please choose a sample.",
            id="no-pathway-ko-chart-message",
            style={"textAlign": "center", "color": "gray"}
        )

    # Prepare data
    input_df = pd.DataFrame(stored_data)
    merged_df = merge_with_kegg(input_df)

    if merged_df.empty:
        return html.P(
            "The processed data is empty. Please check the input data.",
            id="empty-data-message",
            style={"textAlign": "center", "color": "gray"}
        )

    pathway_count_df = count_ko_per_pathway(merged_df)

    if pathway_count_df.empty or selected_sample not in pathway_count_df['sample'].unique():
        return html.P(
            f"No data available for sample '{selected_sample}'.",
            id="no-data-for-sample-message",
            style={"textAlign": "center", "color": "gray"}
        )

    # Generate chart
    fig = plot_pathway_ko_counts(pathway_count_df, selected_sample)

    return dcc.Graph(figure=fig, style={"width": "100%", "margin-top": "20px"})


# Callback to initialize the pathway dropdown
@app.callback(
    [Output('via-dropdown', 'options'),
     Output('via-dropdown', 'value')],
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')]
)
def initialize_via_dropdown(n_clicks, stored_data):
    if not stored_data or n_clicks < 1:
        raise PreventUpdate

    # Prepare data
    input_df = pd.DataFrame(stored_data)
    merged_df = merge_with_kegg(input_df)
    pathways = sorted(merged_df['pathname'].unique())

    dropdown_options = [{'label': pathway, 'value': pathway} for pathway in pathways]

    return dropdown_options, None  # No default value selected


# Callback to update the KO chart per sample for a selected pathway
@app.callback(
    Output('via-ko-chart-container', 'children'),
    [Input('via-dropdown', 'value')],
    [State('stored-data', 'data')]
)
def update_via_ko_chart(selected_via, stored_data):
    if not stored_data:
        return html.P(
            "No chart available. Please select a pathway.",
            id="no-via-ko-chart-message",
            style={"textAlign": "center", "color": "gray"}
        )

    if not selected_via:
        return html.P(
            "No pathway selected. Please choose a pathway.",
            id="no-via-ko-chart-message",
            style={"textAlign": "center", "color": "gray"}
        )

    # Prepare data
    input_df = pd.DataFrame(stored_data)
    merged_df = merge_with_kegg(input_df)

    if merged_df.empty:
        return html.P(
            "The processed data is empty. Please check the input data.",
            id="empty-data-message",
            style={"textAlign": "center", "color": "gray"}
        )

    sample_count_df = count_ko_per_sample_for_pathway(merged_df, selected_via)

    if sample_count_df.empty:
        return html.P(
            f"No data available for pathway '{selected_via}'.",
            id="no-data-for-pathway-message",
            style={"textAlign": "center", "color": "gray"}
        )

    # Generate chart
    fig = plot_sample_ko_counts(sample_count_df, selected_via)

    return dcc.Graph(figure=fig, style={"width": "100%", "margin-top": "20px"})
