# Utils Directory Documentation

## Overview

This document provides an overview and details of the `utils` directory in the **BioRemPP** project. Each file is briefly described with a focus on its purpose and general components.

## Navigation

- [Utils Directory Documentation](#utils-directory-documentation)
  - [Overview](#overview)
  - [Navigation](#navigation)
    - [components.py](#componentspy)
    - [data\_loader.py](#data_loaderpy)
    - [data\_processing.py](#data_processingpy)
    - [data\_validator.py](#data_validatorpy)
    - [filters.py](#filterspy)
    - [plot\_processing.py](#plot_processingpy)
    - [table\_utils.py](#table_utilspy)

---

### components.py

Contains reusable **Dash UI components** for creating consistent visual elements in the application.  
- Includes a `create_card` function to generate styled HTML cards with titles and descriptions.  
- Utilizes Dash's `html` and `dcc` modules for layout design.

---

### data_loader.py

Handles **data loading** operations, primarily focusing on importing datasets from Excel files.  
- Contains utilities to read and return data as pandas DataFrames.  
- Ensures efficient integration with the broader data processing workflows.

---

### data_processing.py

Offers **data manipulation and transformation utilities** to support various analysis workflows in the application.  
- Includes data merging functionalities with external databases such as KEGG, HADEG, and ToxCSM.  
- Provides mechanisms to aggregate and process gene, sample, and pathway data for analytical visualizations.  
- Supports complex transformations like hierarchical clustering and heatmap generation.

---

### data_validator.py

Responsible for **input validation** and pre-processing of uploaded files.  
- Validates file formats and decodes base64-encoded content.  
- Extracts key-value pairs for further processing and ensures compliance with expected data structures.

---

### filters.py

Defines reusable **filtering components** for the UI.  
- Implements a `create_range_slider` function, allowing users to dynamically adjust value ranges for data filtering.  
- Supports customization of slider attributes, such as minimum/maximum values and visual markers.

---

### plot_processing.py

Focuses on **visualization creation and customization** using Plotly.  
- Supports bar charts, scatter plots, violin plots, and heatmaps.  
- Contains specialized utilities for visualizing data relationships, such as compound-sample interactions and pathway clustering.  
- Includes helper functions for integrating UpSet plots and network diagrams.

---

### table_utils.py

Facilitates the **creation of interactive data tables** using Dash AG Grid.  
- Provides a utility to render pandas DataFrames as fully interactive tables.  
- Supports features like column hiding, sorting, filtering, and floating filters.  
- Allows dynamic customization to adapt tables to various use cases.

---

This documentation aims to provide a concise yet comprehensive overview of the `utils` module and its components, enabling developers to effectively utilize its functionalities.
```
