# BioRemPP Project

## Overview

BioRemPP is an interactive Dash Plotly application designed to analyze and explore functional genomic data related to bioremediation potential. By leveraging KEGG Orthology (KO) identifiers, the platform enables the investigation of metabolic pathways, identification of key genes, microbial consortia design, clustering analyses, and other detailed data examinations. Researchers can interactively visualize and manipulate their datasets through dynamic graphs, adjustable tables, and a variety of integrated visualization modules.

The application’s modular and extensible architecture supports the continuous integration of new data analysis techniques and custom visualizations, ensuring that BioRemPP can evolve alongside advances in bioremediation research. With responsive design and a rich set of features, BioRemPP facilitates an efficient, user-friendly workflow for environmental and biotech researchers focusing on pollutant degradation and sustainability.

## Key Features

- **Data Upload and Processing**: Easily upload your datasets (formatted as specified) for immediate analysis.
- **Interactive Visualizations**: Explore data through interactive graphs, heatmaps, scatter plots, bar charts, dendrograms, and more.
- **Metabolic Pathway Analysis**: Investigate KO-based pathways, identify key enzymes, and understand microbial capabilities for bioremediation.
- **Gene and Compound Associations**: Examine relationships between compounds, genes, and samples to pinpoint critical interactions.
- **Clustering and Intersection Analyses**: Perform sample clustering, examine intersections of orthologous genes across samples (UpSet plots), and analyze enzyme activity profiles.
- **Database Integration**: Seamlessly integrate with KEGG, HADEG, and TOXCSM databases to enrich your data, providing regulatory insights and toxicity predictions.
- **Modular Architecture**: Extend and customize the platform to include new visualization modules, data processing methods, and analysis techniques.
- **Continuous Expansion**: The platform is prepared to incorporate ongoing developments and integrate new functionalities as bioremediation research progresses.

## Project Structure

```plaintext
├── .gitignore
├── .vscode
│   └── extensions.json
├── README.md
├── app.py
├── assets
│   ├── biorempp_sample_data.txt
│   ├── exemple1.jpg
│   ├── images
│   │   ├── CHEBI_LOGO.png
│   │   ├── HADEG_LOGO.png
│   │   ├── KEGG_LOGO.gif
│   │   ├── NCBI_LOGO.png
│   │   ├── PUBCHEM_LOGO.png
│   │   └── TOXCSM_LOGO.png
│   ├── scroll.js
│   └── style.css
├── callbacks
│   ├── P1_COUNT_KO_callbacks.py
│   ├── P2_KO_20PATHWAY_callbacks.py
│   ├── P3_compounds_callbacks.py
│   ├── P4_rank_compounds_callbacks.py
│   ├── P5_rank_compounds_callbacks.py
│   ├── P6_rank_compounds_callbacks.py
│   ├── P7_compound_x_genesymbol_callbacks.py
│   ├── P8_sample_x_genesymbol_callbacks.py
│   ├── P9_sample_x_referenceAG_callbacks.py
│   ├── P10_sample_grouping_profile_callbacks.py
│   ├── P11_gene_sample__heatmap_callbacks.py
│   ├── P12_compaund_pathway_callbacks.py
│   ├── P13_gene_sample_scatter_callbacks.py
│   ├── P14_sample_enzyme_activity_callbacks.py
│   ├── P15_sample_clustering_callbacks.py
│   ├── P16_sample_upset_callbacks.py
│   ├── P17_gene_compound_network_callbacks.py
│   ├── T1_biorempp_callbacks.py
│   ├── T2_hadeg_callbacks.py
│   ├── T3_toxcsm_callbacks.py
│   ├── callbacks.py
│   └── p18_heatmap_faceted_callbacks.py
├── components
│   ├── alerts.py
│   ├── bioremediation.py
│   ├── download_button.py
│   ├── features.py
│   ├── footer.py
│   ├── header.py
│   ├── navbar.py
│   ├── regulatory_agencies.py
│   ├── step_guide.py
│   └── tooltip_sample.py
├── index.py
├── layouts
│   ├── P1_KO_COUNT.py
│   ├── P2_KO_20PATHWAY.py
│   ├── P3_compounds_layout.py
│   ├── P4_rank_compounds_layout.py
│   ├── P5_rank_compounds_layout.py
│   ├── P6_rank_compounds_layout.py
│   ├── P7_compound_x_genesymbol_layoyt.py
│   ├── P8_sample_x_genesymbol_layout.py
│   ├── P9_sample_x_referenceAG_layout.py
│   ├── P10_sample_grouping_profile_layout.py
│   ├── P11_gene_sample__heatmap_layout.py
│   ├── P12_compaund_pathway_layout.py
│   ├── P13_gene_sample_scatter_layout.py
│   ├── P14_sample_enzyme_activity_layout.py
│   ├── P15_sample_clustering_layout.py
│   ├── P16_sample_upset_layout.py
│   ├── P17_gene_compound_network_layout.py
│   ├── p18_heatmap_faceted_layout.py
│   ├── T1_biorempp.py
│   ├── T2_hadeg.py
│   ├── T3_toxcsm.py
│   ├── about.py
│   ├── data_analysis.py
│   ├── help.py
│   ├── results.py
│   └── __init__.py
├── requirements.txt
└── utils
    ├── components.py
    ├── data_loader.py
    ├── data_processing.py
    ├── data_validator.py
    ├── filters.py
    ├── plot_processing.py
    └── table_utils.py
```

### Directory Descriptions

**assets**: Static files including custom JavaScript, CSS, and images.

**callbacks**: Contains all Dash callbacks organized by feature. Each file corresponds to a specific functionality or dataset visualization, ensuring modular and maintainable code.

**components**: Reusable Dash components (e.g., headers, footers, navigation bars, alerts, tooltips) that provide UI building blocks.

**layouts**: Defines the layouts and structures of various pages and analytical sections (e.g., KO counts, pathways, compound-scatter views, clustering dendrograms, and advanced toxicity heatmaps).

**utils**: Utility scripts and helpers for data loading, validation, processing, filtering, plotting, and table generation.

**index.py**: Defines the main layout and integrates callbacks, serving as the central point of the application.

**app.py**: The core entry point for running the Dash application, initializing the server, and configuring settings.

**requirements.txt**: Lists the Python dependencies and packages required to run BioRemPP.

**README.md**: This documentation, providing an overview, usage instructions, and details about the project’s structure and features.

## Data Flow Diagram

```plaintext
[User Input Data]
       |
       v
[Data Validation & Processing] 
       |
       v
[Integrated Databases (KEGG, HADEG, TOXCSM)]
       |
       v
[Dash Callbacks & Processing Logic] 
       |
       v
[Layouts & Visual Components] 
       |
       v
[Interactive Dash Application]
```

## Usage Instructions

1. **Install Dependencies**:  
   Ensure you have Python 3.x and run:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:  
   Start the Dash server:
   ```bash
   python app.py
   ```
   Access the application at `http://127.0.0.1:8050`.

3. **Upload Data & Analysis**:
   - Upload your dataset (in the specified format) via the provided UI.
   - Click “Submit” to process the data.
   - Once processing completes, navigate through interactive charts, heatmaps, and tables.
   - Explore gene distributions, compound rankings, clustering analyses, and toxicity predictions.

## Contributing

Contributions are welcome! Please see `CONTRIBUTING.md` for guidance on how to propose enhancements, report issues, or submit pull requests.

## License

This project is currently under an "All Rights Reserved" license. For more details, see `LICENSE`.

## Contact

For support or inquiries, please contact us via [email](mailto:dougbiomed@gmail.com).

We hope BioRemPP enhances your research experience, facilitating deeper insights into bioremediation potential and guiding data-driven decisions towards sustainable environmental solutions.

 tag upload-and-processing-refactor-ongoing -m "Start of upload and processing refactor ongoing."
