# Layouts Directory Documentation

## Overview

The `layouts` directory contains the page and component layouts for the **BioRemPP** application. Each file in this directory corresponds to a specific section or visualization within the application. These layouts define how data is presented to users, including graphs, tables, and interactive elements.

### Navigation

- [Layouts Directory Documentation](#layouts-directory-documentation)
  - [Overview](#overview)
    - [Navigation](#navigation)
  - [Layout Files](#layout-files)
    - [P1\_KO\_COUNT.py](#p1_ko_countpy)
    - [P2\_KO\_20PATHWAY.py](#p2_ko_20pathwaypy)
    - [P3\_compounds\_layout.py](#p3_compounds_layoutpy)
    - [P4\_rank\_compounds\_layout.py](#p4_rank_compounds_layoutpy)
    - [P5\_rank\_compounds\_layout.py](#p5_rank_compounds_layoutpy)
    - [P6\_rank\_compounds\_layout.py](#p6_rank_compounds_layoutpy)
    - [P7\_compound\_x\_genesymbol\_layoyt.py](#p7_compound_x_genesymbol_layoytpy)
    - [P8\_sample\_x\_genesymbol\_layout.py](#p8_sample_x_genesymbol_layoutpy)
    - [P9\_sample\_x\_referenceAG\_layout.py](#p9_sample_x_referenceag_layoutpy)
    - [P10\_sample\_grouping\_profile\_layout.py](#p10_sample_grouping_profile_layoutpy)
    - [P11\_gene\_sample\_\_heatmap\_layout.py](#p11_gene_sample__heatmap_layoutpy)
    - [P12\_compaund\_pathway\_layout.py](#p12_compaund_pathway_layoutpy)
    - [P13\_gene\_sample\_scatter\_layout.py](#p13_gene_sample_scatter_layoutpy)
    - [P14\_sample\_enzyme\_activity\_layout.py](#p14_sample_enzyme_activity_layoutpy)
    - [P15\_sample\_clustering\_layout.py](#p15_sample_clustering_layoutpy)
    - [P16\_sample\_upset\_layout.py](#p16_sample_upset_layoutpy)
    - [P17\_gene\_compound\_network\_layout.py](#p17_gene_compound_network_layoutpy)
    - [T1\_biorempp.py](#t1_biorempppy)
    - [T2\_hadeg.py](#t2_hadegpy)
    - [T3\_toxcsm.py](#t3_toxcsmpy)
    - [about.py](#aboutpy)
    - [data\_analysis.py](#data_analysispy)
    - [help.py](#helppy)
    - [p18\_heatmap\_faceted\_layout.py](#p18_heatmap_faceted_layoutpy)
    - [results.py](#resultspy)

---

## Layout Files

### P1_KO_COUNT.py

Defines layouts for visualizing **KO counts** in samples. Includes bar charts and violin/box plots with filters for ranges and sample selection.

### P2_KO_20PATHWAY.py

Contains layouts for KO pathway analysis, including bar charts for KO distribution in pathways and sample-specific pathway activity.

### P3_compounds_layout.py

Provides the layout for a scatter plot showing **compound interactions**. Includes dropdown filters for compound classes.

### P4_rank_compounds_layout.py

Contains a layout for ranking samples by **compound interaction count**. Features a range slider for compound count filtering.

### P5_rank_compounds_layout.py

Defines the layout for ranking **compounds** based on their interaction with samples. Includes a dropdown for compound class selection.

### P6_rank_compounds_layout.py

Focuses on ranking **compounds by gene interaction**. Adds dropdown filters for compound classes.

### P7_compound_x_genesymbol_layoyt.py

Provides a scatter plot layout for visualizing interactions between **genes and compounds**. Includes dropdowns for gene and compound selection.

### P8_sample_x_genesymbol_layout.py

Defines a scatter plot layout for relationships between **samples and genes**. Includes dropdowns for sample and gene filters.

### P9_sample_x_referenceAG_layout.py

Contains a heatmap layout to explore **sample associations with reference agencies**.

### P10_sample_grouping_profile_layout.py

Provides a layout for **sample grouping** based on compound classes, including scatter plots and dropdown filters.

### P11_gene_sample__heatmap_layout.py

Defines a heatmap layout for **gene-sample relationships**, with dropdown filters for pathways and compound pathways.

### P12_compaund_pathway_layout.py

Contains a heatmap layout for exploring **pathways and compound pathways**. Includes a dropdown for sample selection.

### P13_gene_sample_scatter_layout.py

Focuses on scatter plots of **genes across samples for a specific pathway**, including dropdown filters for pathways.

### P14_sample_enzyme_activity_layout.py

Defines a layout for bar charts showing **enzyme activity counts by sample**. Includes sample filters.

### P15_sample_clustering_layout.py

Contains the layout for hierarchical **sample clustering** using dendrograms. Includes dropdowns for clustering methods and distance metrics.

### P16_sample_upset_layout.py

Provides the layout for **UpSet plots**, visualizing intersections of orthologous genes across samples.

### P17_gene_compound_network_layout.py

Defines a layout for network graphs that illustrate **gene-compound interactions**.

### T1_biorempp.py

Creates the layout for displaying the **BioRemPP Results Table**, with a button to render the table.

### T2_hadeg.py

Defines the layout for the **HADEG Results Table**, featuring buttons to view the data.

### T3_toxcsm.py

Provides the layout for the **ToxCSM Results Table**, including interactive buttons for table rendering.

### about.py

Defines the "About" page layout, presenting an overview of **BioRemPP** and its integration with external databases.

### data_analysis.py

Contains layouts and components for the **Data Analysis page**, including steps for data upload, processing, and visualization.

### help.py

Provides the layout for the **Help and Support page**, including detailed instructions and examples for using the application.

### p18_heatmap_faceted_layout.py

Defines the layout for a **toxicity heatmap** with faceted views, showcasing toxicity predictions across various analysis categories.

### results.py

Consolidates layouts for **results visualization**, including charts, tables, and network graphs for pathways, compounds, and samples.

--- 
