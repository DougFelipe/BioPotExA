from dash import html

def get_regulatory_agencies_layout():
    """
    Constructs the layout for the Regulatory Agencies page.

    Returns:
        A `html.Div` containing the Regulatory Agencies page layout.
    """
    return html.Div(
        className="regulatory-agencies-page",
        children=[
            # Page Title
            html.H1("Regulatory Agencies and Environmental Directives", className="regulatory-title"),
            
            # Introduction Section
            html.P(
                "BioRemPP provides a comprehensive database that includes compounds identified as priority environmental pollutants. "
                "These compounds are recognized by global regulatory agencies due to their environmental and human health impacts",
                className="regulatory-intro"
            ),
            
            # Section: Overview of Priority Pollutants
            html.Div(
                className="regulatory-section",
                children=[
                    html.H2("Priority Environmental Pollutants", className="regulatory-section-title"),
                    html.P(
                        "Priority pollutants are compounds that pose significant risks to environmental and human health. "
                        "These substances often include organic compounds, heavy metals, pesticides, and industrial chemicals. "
                        "They are targeted for monitoring and remediation efforts due to their persistence, toxicity, and bioaccumulation potential",
                        className="regulatory-text"
                    ),
                    html.P(
                        "By focusing on these compounds, BioRemPP aims to support global initiatives for environmental sustainability "
                        "and the development of innovative bioremediation strategies",
                        className="regulatory-text"
                    ),
                ]
            ),

            # Section: Regulatory Agencies
            html.Div(
                className="regulatory-section",
                children=[
                    html.H2("Key Environmental Regulatory Agencies", className="regulatory-section-title"),
                    
                    html.Div(
                        className="regulatory-agency",
                        children=[
                            html.H3("Agency for Toxic Substances and Disease Registry (ATSDR, USA)", className="regulatory-agency-title"),
                            html.P(
                                "The ATSDR identifies hazardous substances and assesses their health effects. Its priority substance list "
                                "guides environmental cleanup and regulatory actions in the USA",
                                className="regulatory-text"
                            ),
                        ]
                    ),
                    
                    html.Div(
                        className="regulatory-agency",
                        children=[
                            html.H3("National Environmental Council (CONAMA, Brazil)", className="regulatory-agency-title"),
                            html.P(
                                "CONAMA establishes guidelines for pollution control, water quality, and the regulation of hazardous substances in Brazil. "
                                "It prioritizes pollutants based on their environmental impact and risks to public health",
                                className="regulatory-text"
                            ),
                        ]
                    ),
                    
                    html.Div(
                        className="regulatory-agency",
                        children=[
                            html.H3("Environmental Protection Agency (EPA, USA)", className="regulatory-agency-title"),
                            html.P(
                                "The EPA regulates pollutants through programs like the National Priority List and CERCLA (Superfund), focusing on "
                                "mitigating environmental contamination and promoting sustainability",
                                className="regulatory-text"
                            ),
                        ]
                    ),
                    
                    html.Div(
                        className="regulatory-agency",
                        children=[
                            html.H3("European Parliament (EP)", className="regulatory-agency-title"),
                            html.P(
                                "The EP enforces directives like the REACH regulation and the Water Framework Directive, which aim to protect "
                                "the environment and human health by monitoring and regulating pollutants across Europe",
                                className="regulatory-text"
                            ),
                        ]
                    ),
                    
                    html.Div(
                        className="regulatory-agency",
                        children=[
                            html.H3("International Agency for Research on Cancer (IARC)", className="regulatory-agency-title"),
                            html.P(
                                "The IARC classifies compounds based on their carcinogenic potential (Groups 1, 2A, and 2B). "
                                "This classification informs regulatory actions and prioritization for monitoring",
                                className="regulatory-text"
                            ),
                        ]
                    ),
                    
                    html.Div(
                        className="regulatory-agency",
                        children=[
                            html.H3("Canadian Environmental Protection Act (CEPA) - Priority Substances Lists (PSL1 and PSL2)", className="regulatory-agency-title"),
                            html.P(
                                "The CEPA prioritizes substances based on their toxicity, persistence, and bioaccumulation. "
                                "PSL1 and PSL2 guide environmental management actions in Canada",
                                className="regulatory-text"
                            ),
                        ]
                    ),
                    
                    html.Div(
                        className="regulatory-agency",
                        children=[
                            html.H3("Water Framework Directive (WFD)", className="regulatory-agency-title"),
                            html.P(
                                "The WFD aims to achieve good water quality in Europe by targeting priority pollutants in surface and groundwater. "
                                "It provides a framework for monitoring and remediation efforts",
                                className="regulatory-text"
                            ),
                        ]
                    ),
                ]
            ),
            
            # Section: Collaboration and Future Directions
            html.Div(
                className="regulatory-section",
                children=[
                    html.H2("Collaboration and Future Directions", className="regulatory-section-title"),
                    html.P(
                        "BioRemPP aligns its database and tools with the standards set by these regulatory agencies. "
                        "By leveraging global frameworks and bioremediation strategies, it aims to contribute to cleaner environments "
                        "and enhanced public health",
                        className="regulatory-text"
                    ),
                ]
            ),
        ]
    )
