# components/bioremediation.py
from dash import html

def get_bioremediation_layout():
    """
    Returns the layout of the Bioremediation page.
    """
    return html.Div(
        className="features-page",
        children=[
            # Title Section
            html.H1("Bioremediation", className="features-title"),
            html.P(
                "Bioremediation represents a promising and sustainable approach to mitigating environmental contamination. "
                "Using living organisms like bacteria, fungi, or plants, this method promotes the degradation or neutralization of harmful pollutants, "
                "restoring ecosystems and protecting public health. This page highlights the applications, benefits, challenges, and future opportunities in the field of bioremediation",
                className="features-intro"
            ),

            # Applications Section
            html.Div(
                className="features-section",
                children=[
                    html.H2("Applications of Bioremediation", className="features-section-title"),
                    html.P(
                        "Bioremediation has broad applications across various industries and ecosystems, addressing contamination in soil, water, and air. "
                        "Here are some notable areas where bioremediation is actively employed:",
                        className="features-text"
                    ),
            html.Ul(
                className="features-list",
                children=[
                    html.Li("Oil Spill Cleanup: Removing hydrocarbons from marine and terrestrial environments after oil spills"),
                    html.Li("Industrial Effluent Treatment: Addressing pollutants in wastewater from industries such as textiles, chemicals, and pharmaceuticals"),
                    html.Li("Heavy Metal Remediation: Stabilizing or extracting toxic metals like arsenic, cadmium, and lead from soil and water"),
                    html.Li("Pesticide Degradation: Breaking down harmful agrochemicals that accumulate in agricultural runoff"),
                    html.Li("Ecosystem Restoration: Rehabilitating areas impacted by mining, deforestation, or urbanization"),
                    html.Li("Landfill Leachate Management: Treating contaminated water that seeps from landfills to prevent groundwater pollution"),
                    html.Li("Groundwater Decontamination: Cleaning up contaminated aquifers by using microorganisms to degrade pollutants"),
                    html.Li("Air Pollution Control: Using biofilters and bioreactors to remove volatile organic compounds (VOCs) and odors from industrial emissions"),
                    html.Li("Plastic Biodegradation: Breaking down synthetic plastics and microplastics using enzymes and microorganisms"),
                    html.Li("Radioactive Waste Management: Stabilizing or reducing radioactive contaminants in soil and water through biological means"),
                    html.Li("Pharmaceutical Waste Treatment: Degrading active pharmaceutical compounds in wastewater to prevent ecological harm"),
                    html.Li("Agricultural Waste Management: Managing organic waste like animal manure or crop residues by converting them into biogas or compost"),
                ]
                    )
                ]
            ),

            # Benefits Section
            html.Div(
                className="features-section",
                children=[
                    html.H2("Benefits of Bioremediation", className="features-section-title"),
                    html.P(
                        "Bioremediation offers several advantages over traditional remediation methods, making it a preferred choice in many scenarios. These benefits include:",
                        className="features-text"
                    ),
                    html.Ul(
                        className="features-list",
                        children=[
                            html.Li("Cost-Effectiveness: Often more economical than chemical or mechanical cleanup methods"),
                            html.Li("Environmental Compatibility: Leverages natural processes without introducing additional pollutants"),
                            html.Li("Targeted Pollutant Degradation: Specific organisms can be tailored to degrade particular pollutants"),
                            html.Li("Minimal Ecological Impact: Avoids the large-scale disruption caused by excavation or chemical treatments"),
                            html.Li("Scalability: Effective for both localized contamination and large-scale environmental disasters"),
                            html.Li("Long-Term Sustainability: Promotes natural recovery processes, ensuring ecological balance over time"),
                        ]
                    ),
                ]
            ),

            # Key Organisms Section
            html.Div(
                className="features-section",
                children=[
                    html.H2("Key Organisms in Bioremediation", className="features-section-title"),
                    html.P(
                        "Bioremediation relies on the metabolic capabilities of specific organisms to break down or neutralize pollutants. Each group of organisms brings unique strengths to the process:",
                        className="features-text"
                    ),
                    html.Ul(
                        className="features-list",
                        children=[
                            html.Li("Bacteria: Specialists in degrading hydrocarbons, pesticides, and toxic chemicals. Examples include _Pseudomonas_ and _Bacillus_"),
                            html.Li("Fungi: Effective in breaking down complex pollutants such as dyes, synthetic chemicals, and lignin-based compounds"),
                            html.Li("Plants (Phytoremediation): Capable of absorbing heavy metals and stabilizing toxins in soil and water. Common examples are _Poplar trees_ and _Sunflowers_"),
                            html.Li("Algae: Emerging as a powerful tool for remediating wastewater and capturing carbon emissions"),
                        ]
                    ),
                ]
            ),

            # Challenges and Future Directions Section
            html.Div(
                className="features-section",
                children=[
                    html.H2("Challenges and Future Directions", className="features-section-title"),
                    html.P(
                        "While bioremediation holds immense promise, it is not without challenges. Overcoming these hurdles requires innovative approaches and continuous research. Key challenges include:",
                        className="features-text"
                    ),
                    html.Ul(
                        className="features-list",
                        children=[
                            html.Li("Environmental Variables: Factors such as pH, temperature, and oxygen levels can significantly impact the efficiency of bioremediation"),
                            html.Li("Scaling Up: Laboratory successes often face challenges when applied to large-scale, real-world scenarios"),
                            html.Li("Complex Pollutants: Some contaminants, like heavy metals or mixed waste, are difficult to degrade or neutralize completely"),
                            html.Li("Monitoring and Control: Ensuring the activity of the organisms remains targeted and effective over time"),
                        ]
                    ),
                    html.P(
                        "Future directions in bioremediation aim to address these challenges through advancements such as:",
                        className="features-text"
                    ),
                    html.Ul(
                        className="features-list",
                        children=[
                            html.Li("Genetic Engineering: Developing engineered microbes with enhanced pollutant degradation capabilities"),
                            html.Li("Bioreactor Systems: Creating controlled environments to optimize microbial activity"),
                            html.Li("Omics Technologies: Leveraging genomics, proteomics, and metabolomics to understand and enhance bioremediation processes"),
                            html.Li("Artificial Intelligence: Using AI and machine learning to predict pollutant behavior and optimize remediation strategies"),
                        ]
                    ),
                ]
            ),

            # Additional Insights Section
            html.Div(
                className="features-section",
                children=[
                    html.H2("Why BioRemPP for Bioremediation?", className="features-section-title"),
                    html.P(
                        "BioRemPP complements the field of bioremediation by offering a robust, data-driven platform to analyze genomic potential for pollutant degradation. "
                        "With features for data preprocessing, pathway exploration, and detailed visualizations, the platform bridges the gap between raw genomic data and actionable insights, "
                        "enabling researchers to identify optimal candidates for biotechnological applications in remediation",
                        className="features-text"
                    ),
                ]
            ),
        ]
    )
