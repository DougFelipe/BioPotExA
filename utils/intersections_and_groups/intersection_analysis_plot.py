import base64
import io
import logging
import matplotlib.pyplot as plt
import pandas as pd
from upsetplot import from_memberships, plot

from utils.intersections_and_groups.intersection_analysis_processing import (
    prepare_upsetplot_data,
)
from utils.data_processing import merge_input_with_database

# Configure logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def render_upsetplot(stored_data: dict, selected_samples: list) -> str:
    """
    Renders an UpSet Plot based on selected samples and their associated KOs 
    after merging with the reference database.

    Parameters
    ----------
    stored_data : dict
        Dictionary-formatted input data, typically obtained via Dash callbacks.
    selected_samples : list
        List of selected sample names to include in the plot.

    Returns
    -------
    str
        Base64-encoded PNG image of the generated UpSet Plot.

    Raises
    ------
    ValueError
        If fewer than two samples are selected, or if required fields are missing.
    """

    if not isinstance(selected_samples, list) or len(selected_samples) < 2:
        raise ValueError("At least two samples must be selected.")

    logger.info("Converting stored data to DataFrame...")
    input_df = pd.DataFrame(stored_data)

    logger.info("Merging input data with reference database...")
    merged_data = merge_input_with_database(input_df)

    logger.info("Preparing data for UpSet plot...")
    filtered_df = prepare_upsetplot_data(merged_data, selected_samples)

    logger.info("Generating KO to sample memberships...")
    memberships = (
        filtered_df.groupby("ko")["sample"]
        .apply(lambda x: list(set(x)))
    )

    if memberships.empty:
        raise ValueError("No valid KO/sample memberships found.")

    upset_df = from_memberships(memberships)
    upset_data = upset_df.groupby(upset_df.index).sum()

    # Attempt to generate MultiIndex
    try:
        index_element = upset_data.index[0]
        num_levels = len(index_element) if isinstance(index_element, tuple) else 1
        index_names = selected_samples[:num_levels]
        upset_data.index = pd.MultiIndex.from_tuples(
            upset_data.index, names=index_names
        )
    except Exception as e:
        logger.error("Failed to create MultiIndex for UpSet data.")
        raise ValueError("Data structure is incompatible with UpSetPlot.") from e

    # Plotting
    logger.info("Rendering UpSet plot...")
    plt.figure(figsize=(10, 6))
    plot(upset_data, orientation="horizontal")

    buffer = io.BytesIO()
    plt.savefig(buffer, format="png", bbox_inches="tight")
    plt.close()
    buffer.seek(0)

    image_data = base64.b64encode(buffer.read()).decode("utf-8")
    return f"data:image/png;base64,{image_data}"
