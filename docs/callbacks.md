# Callbacks Directory Documentation

## Overview

The `callbacks` directory contains the core logic that powers the interactive features of the BioRemPP application. Each file in this directory defines Dash callbacks, which connect user inputs (e.g., dropdown selections, button clicks) with outputs (e.g., graphs, tables, and visualizations). The callbacks are modularly organized by feature, facilitating maintenance and scalability.

### Navigation Menu

- [Callbacks Directory Documentation](#callbacks-directory-documentation)
  - [Overview](#overview)
    - [Navigation Menu](#navigation-menu)
    - [General Callbacks](#general-callbacks)
    - [P1\_COUNT\_KO\_callbacks.py](#p1_count_ko_callbackspy)
    - [P2\_KO\_20PATHWAY\_callbacks.py](#p2_ko_20pathway_callbackspy)
    - [P3\_compounds\_callbacks.py](#p3_compounds_callbackspy)
    - [P4\_rank\_compounds\_callbacks.py](#p4_rank_compounds_callbackspy)
    - [P5\_rank\_compounds\_callbacks.py](#p5_rank_compounds_callbackspy)
    - [P6\_rank\_compounds\_callbacks.py](#p6_rank_compounds_callbackspy)
    - [P7\_compound\_x\_genesymbol\_callbacks.py](#p7_compound_x_genesymbol_callbackspy)
    - [P8\_sample\_x\_genesymbol\_callbacks.py](#p8_sample_x_genesymbol_callbackspy)
    - [P9\_sample\_x\_referenceAG\_callbacks.py](#p9_sample_x_referenceag_callbackspy)
    - [P10\_sample\_grouping\_profile\_callbacks.py](#p10_sample_grouping_profile_callbackspy)
    - [P11\_gene\_sample\_heatmap\_callbacks.py](#p11_gene_sample_heatmap_callbackspy)
    - [P12\_compound\_pathway\_callbacks.py](#p12_compound_pathway_callbackspy)
    - [P13\_gene\_sample\_scatter\_callbacks.py](#p13_gene_sample_scatter_callbackspy)
    - [P14\_sample\_enzyme\_activity\_callbacks.py](#p14_sample_enzyme_activity_callbackspy)
    - [P15\_sample\_clustering\_callbacks.py](#p15_sample_clustering_callbackspy)
    - [P16\_sample\_upset\_callbacks.py](#p16_sample_upset_callbackspy)
    - [P17\_gene\_compound\_network\_callbacks.py](#p17_gene_compound_network_callbackspy)
    - [T1\_biorempp\_callbacks.py](#t1_biorempp_callbackspy)
    - [T2\_hadeg\_callbacks.py](#t2_hadeg_callbackspy)
    - [T3\_toxcsm\_callbacks.py](#t3_toxcsm_callbackspy)
    - [p18\_heatmap\_faceted\_callbacks.py](#p18_heatmap_faceted_callbackspy)

---

### General Callbacks

**File:** `callbacks.py`  
**Description:**  
This file contains global callbacks used throughout the application. Key functionalities include:

- Handling file uploads or loading example datasets.
- Updating visualizations and interactive elements based on the user's actions.
- Managing page transitions and visibility of UI elements like alerts and progress bars.

---

### P1_COUNT_KO_callbacks.py

**Description:**  
Handles the visualization of KO (KEGG Orthology) count data. Features include:

- Bar charts for KO count distributions.
- Range sliders to filter KO counts.
- Integration with dropdown menus for selecting samples.

---

### P2_KO_20PATHWAY_callbacks.py

**Description:**  
Focused on pathway-level KO analyses. Key functionalities include:

- Dropdowns for selecting pathways and samples.
- Visualizations of KO distributions across pathways and samples.

---

### P3_compounds_callbacks.py

**Description:**  
Manages the display of compound-related data. Features include:

- Scatter plots of compound classes.
- Dropdowns for selecting compound classes to filter data.

---

### P4_rank_compounds_callbacks.py

**Description:**  
Enables ranking analysis of samples based on compound counts. Key features:

- Scatter plots for ranking compounds across samples.
- Dynamic range sliders for adjusting the ranking criteria.

---

### P5_rank_compounds_callbacks.py

**Description:**  
Focuses on ranking individual compounds within classes. Key functionalities:

- Dropdowns for selecting compound classes.
- Bar charts to rank compounds by importance within selected classes.

---

### P6_rank_compounds_callbacks.py

**Description:**  
Analyzes gene rankings within compound classes. Key features:

- Dropdowns to select compound classes.
- Bar charts for gene rankings within the selected class.

---

### P7_compound_x_genesymbol_callbacks.py

**Description:**  
Explores the relationships between compounds and gene symbols. Features include:

- Dropdowns for filtering by compound names or gene symbols.
- Scatter plots visualizing these relationships.

---

### P8_sample_x_genesymbol_callbacks.py

**Description:**  
Analyzes gene expression across samples. Key functionalities:

- Dropdowns for selecting specific samples and gene symbols.
- Scatter plots for visualizing gene expression trends.

---

### P9_sample_x_referenceAG_callbacks.py

**Description:**  
Generates heatmaps comparing samples against reference data. Features include:

- Heatmaps for visualizing similarities or differences between samples and references.

---

### P10_sample_grouping_profile_callbacks.py

**Description:**  
Groups samples based on compound classifications. Key functionalities:

- Dropdowns for selecting compound classes.
- Graphs showing sample grouping profiles.

---

### P11_gene_sample_heatmap_callbacks.py

**Description:**  
Creates heatmaps for gene expression across samples. Features include:

- Dropdowns for filtering by pathways or compound classes.
- Heatmaps displaying gene-sample interactions.

---

### P12_compound_pathway_callbacks.py

**Description:**  
Visualizes compound-pathway relationships. Key functionalities:

- Dropdowns for selecting samples and pathways.
- Heatmaps of pathway activities for selected samples.

---

### P13_gene_sample_scatter_callbacks.py

**Description:**  
Generates scatter plots for gene expression levels across samples. Features include:

- Dropdowns for pathway selection.
- Scatter plots for analyzing gene-sample relationships.

---

### P14_sample_enzyme_activity_callbacks.py

**Description:**  
Analyzes enzyme activities within samples. Key functionalities:

- Dropdowns for selecting specific samples.
- Bar charts displaying enzyme activity counts.

---

### P15_sample_clustering_callbacks.py

**Description:**  
Performs clustering analysis on samples. Features include:

- Dropdowns for selecting clustering methods and distance metrics.
- Dendrogram visualizations of clustered samples.

---

### P16_sample_upset_callbacks.py

**Description:**  
Creates UpSet plots to analyze intersections of gene sets across samples. Features include:

- Dropdowns for selecting sample subsets.
- Visualizations of gene set intersections.

---

### P17_gene_compound_network_callbacks.py

**Description:**  
Generates networks of gene-compound interactions. Key functionalities:

- Network graphs visualizing relationships between genes and compounds.
- Integration with KEGG and other databases for enriched insights.

---

### T1_biorempp_callbacks.py

**Description:**  
Processes and visualizes results for bioremediation potential. Features include:

- Tables summarizing bioremediation capabilities.
- Integration with KEGG data.

---

### T2_hadeg_callbacks.py

**Description:**  
Processes data specific to the HADEG database. Key functionalities:

- Tables summarizing HADEG database results.
- Filtering and visualization of HADEG-specific insights.

---

### T3_toxcsm_callbacks.py

**Description:**  
Handles toxicity analysis using ToxCSM data. Features include:

- Tables for toxicity predictions.
- Integration with ToxCSM for enhanced data processing.

---

### p18_heatmap_faceted_callbacks.py

**Description:**  
Creates faceted heatmaps for toxicity data. Key functionalities:

- Data merging and processing for faceted heatmaps.
- Visualizations to compare toxicity levels across multiple dimensions.
