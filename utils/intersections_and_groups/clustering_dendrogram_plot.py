import base64
import io
# Força backend não-GUI para evitar erro de thread
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram
from dash import html


def plot_dendrogram(clustering_matrix, sample_labels, distance_metric, method):
    """
    Creates a dendrogram to visualize hierarchical clustering using sample labels.

    Parameters
    ----------
    clustering_matrix : np.ndarray
        Linkage matrix resulting from a hierarchical clustering method.
    sample_labels : list
        List of sample names to use as x-axis labels.
    distance_metric : str
        The distance metric used for clustering (e.g., 'euclidean', 'cityblock').
    method : str
        The linkage method used for clustering (e.g., 'average', 'single').

    Returns
    -------
    dash.html.Img
        A Dash HTML image component containing the rendered dendrogram in base64.
    """
    try:
        plt.figure(figsize=(10, 6))
        dendrogram(clustering_matrix, labels=sample_labels)

        # Dynamic title
        plt.title(f'Sample Clustering Dendrogram\nDistance: {distance_metric.capitalize()}, Method: {method.capitalize()}')
        plt.xlabel('Samples')
        plt.ylabel('Distance')

        # Improve label readability
        plt.xticks(rotation=-45, ha='left')

        # Encode plot as base64
        buf = io.BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight')
        buf.seek(0)
        encoded_image = base64.b64encode(buf.read()).decode('utf-8')
        buf.close()
        plt.close()

        return html.Img(src=f'data:image/png;base64,{encoded_image}', style={"width": "100%"})

    except Exception as e:
        return html.Div([
            html.P("⚠️ Failed to generate dendrogram."),
            html.Pre(str(e), style={"color": "red", "whiteSpace": "pre-wrap"})
        ])
