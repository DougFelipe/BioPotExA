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
                "Bioremediation is a sustainable technology that uses biological organisms, such as bacteria, fungi, or plants, to remediate and restore polluted environments. "
                "This page explores its applications, benefits, and other critical aspects, emphasizing how it aids in reducing contamination and promoting environmental health.",
                className="features-intro"
            ),

            # Applications Section
            html.Div(
                className="features-section",
                children=[
                    html.H2("Applications of Bioremediation", className="features-section-title"),
                    html.P(
                        "Bioremediation is applied across various fields to address contamination issues. Key areas of application include:",
                        className="features-text"
                    ),
                    html.Ul(
                        className="features-list",
                        children=[
                            html.Li("Oil spill cleanup in marine environments and soil."),
                            html.Li("Treatment of industrial effluents and chemical pollutants."),
                            html.Li("Remediation of heavy metals in contaminated water or soil."),
                            html.Li("Degradation of pesticides and agricultural runoffs."),
                            html.Li("Restoration of ecosystems affected by mining activities."),
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
                        "Bioremediation offers numerous advantages over conventional remediation methods, including:",
                        className="features-text"
                    ),
                    html.Ul(
                        className="features-list",
                        children=[
                            html.Li("Cost-effectiveness compared to chemical or mechanical methods."),
                            html.Li("Environmentally friendly as it leverages natural processes."),
                            html.Li("Ability to target specific pollutants with precision."),
                            html.Li("Minimal ecological disruption during remediation."),
                            html.Li("Scalability to address small-scale or large-scale contamination."),
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
                        "The success of bioremediation relies on the use of specific biological organisms with unique metabolic capabilities, such as:",
                        className="features-text"
                    ),
                    html.Ul(
                        className="features-list",
                        children=[
                            html.Li("Bacteria: Known for their ability to degrade hydrocarbons, pesticides, and industrial chemicals."),
                            html.Li("Fungi: Effective in breaking down complex organic pollutants like dyes and synthetic chemicals."),
                            html.Li("Plants: Used in phytoremediation to absorb or stabilize heavy metals and toxins."),
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
                        "While bioremediation shows immense promise, challenges remain, including optimizing conditions for microbial activity, handling large-scale contamination, and ensuring long-term ecological balance. "
                        "Future research is focused on enhancing microbial efficiency, developing robust monitoring systems, and exploring genetic engineering to improve pollutant degradation capabilities.",
                        className="features-text"
                    ),
                ]
            ),

            # Additional Resources Section
            html.Div(
                className="features-section",
                children=[
                    html.H2("Additional Resources", className="features-section-title"),
                    html.P(
                        "To learn more about bioremediation, visit these external resources or explore the references section of this application.",
                        className="features-text"
                    ),
                    html.A("Learn More About Bioremediation", href="https://en.wikipedia.org/wiki/Bioremediation", className="features-link"),
                ]
            ),
        ]
    )
