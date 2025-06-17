"""
utils.core
==========

The ``utils.core`` subpackage provides the core utility functions for the BioRemPP
application, including modules for data loading, validation, merging with external
databases, type optimization, and user feedback.

This subpackage is designed to support high-throughput preprocessing and analysis
of biological and chemical data, enabling seamless integration with reference
databases such as KEGG, HADEG, and ToxCSM, as well as user-uploaded transcriptomic
or metagenomic datasets.

Available Modules
-----------------
data_loader : module
    Functions to load datasets (CSV, Excel) into pandas DataFrames.
data_processing : module
    Functions to merge user input with KEGG, HADEG, ToxCSM, and BioRemPP reference databases.
data_validator : module
    Validates and parses uploaded `.txt` files, including base64 decoding and structure checks.
feedback_alerts : module
    Creates reusable Bootstrap alerts for displaying user feedback in the frontend.
optimize_dtypes : module
    Utilities for memory-efficient optimization of categorical and numerical data types.
table_utils : module
    Functions to convert DataFrames into interactive AG Grid tables for Dash dashboards.
upload_handlers : module
    Handles file upload events, validation logic, and example data retrieval.

Public Objects
--------------
The following functions and objects are re-exported at the package level
for convenience and are accessible as ``utils.core.<function>``.

- load_database
- merge_input_with_database
- merge_with_kegg
- merge_input_with_database_hadegDB
- merge_with_toxcsm
- validate_and_process_input
- decode_content_if_base64
- process_content_lines
- create_alert
- optimize_dtypes
- optimize_kegg_dtypes
- optimize_hadeg_dtypes
- optimize_toxcsm_dtypes
- create_table_from_dataframe
- validate_upload_size
- load_example_data
- process_uploaded_file
- handle_upload_or_example
- validate_upload_comprehensive
- validate_biopotex_format
"""


# -------------------------------
# Public imports
# -------------------------------

# data_loader.py
from .data_loader import load_database

# data_processing.py
from .data_processing import (
    merge_input_with_database,
    merge_with_kegg,
    merge_input_with_database_hadegDB,
    merge_with_toxcsm
)

# data_validator.py
from .data_validator import (
    validate_and_process_input,
    decode_content_if_base64,
    process_content_lines
)

# feedback_alerts.py
from .feedback_alerts import create_alert

# optimize_dtypes.py
from .optimize_dtypes import (
    optimize_dtypes,
    optimize_kegg_dtypes,
    optimize_hadeg_dtypes,
    optimize_toxcsm_dtypes
)

# table_utils.py
from .table_utils import create_table_from_dataframe

# upload_handlers.py
from .upload_handlers import (
    validate_upload_size,
    load_example_data,
    process_uploaded_file,
    handle_upload_or_example,
    validate_upload_comprehensive,
    validate_biopotex_format
)

# -------------------------------
# Variáveis de conveniência
# -------------------------------

__all__ = [
    # data_loader
    "load_database",

    # data_processing
    "merge_input_with_database",
    "merge_with_kegg",
    "merge_input_with_database_hadegDB",
    "merge_with_toxcsm",

    # data_validator
    "validate_and_process_input",
    "decode_content_if_base64",
    "process_content_lines",

    # feedback_alerts
    "create_alert",

    # optimize_dtypes
    "optimize_dtypes",
    "optimize_kegg_dtypes",
    "optimize_hadeg_dtypes",
    "optimize_toxcsm_dtypes",

    # table_utils
    "create_table_from_dataframe",

    # upload_handlers
    "validate_upload_size",
    "load_example_data",
    "process_uploaded_file",
    "handle_upload_or_example",
    "validate_upload_comprehensive",
    "validate_biopotex_format"
]
