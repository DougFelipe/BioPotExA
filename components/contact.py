from dash import html

def get_contact_page():
    """
    Returns the layout for the Contact page.
    """
    return html.Div(
        className="contact-page",
        children=[
            # Section: Title
            html.H1("Contact", className="contact-title"),

            # Section: Profile Picture and Titles
            html.Div(
                className="profile-section",
                children=[
                    html.Img(
                        src="./assets/developer.jpeg",
                        alt="Developer Picture",
                        className="profile-picture"
                    ),
                    html.Div(
                        className="text-section",
                        children=[
                            html.H3("Douglas Felipe", className="developer-name"),
                            html.H5("Biomedical Scientist, MSc. in Bioinformatics", className="academic-title"),
                            html.H4("BioRemPP Developer", className="developer-title"),
                        ]
                    ),
                ]
            ),

            # Section: Description
            html.Div(
                className="description-section",
                children=[
                    html.P(
                        "Currently, I am a PhD student in Bioinformatics at "
                        "UFRN, focusing on developing biotechnological solutions using microbiology to mitigate environmental pollution through bioremediation. "
                        "My expertise combines molecular biology, microbiology, bioinformatics, and software engineering",
                        className="developer-description"
                    ),
                    html.P(
                        "As a Software Engineering student, I specialize in Data Science, Artificial Intelligence, and "
                        "Computational Intelligence, applying these skills to develop integrated software solutions that automate data science and machine learning workflows",
                        className="developer-description"
                    ),
                ]
            ),

            # Section: Contact Methods
            html.Div(
                className="contact-methods",
                children=[
                    html.H4("Get in Touch", className="contact-header"),
                    html.P(
                        "Feel free to reach out via email for collaboration or inquiries:",
                        className="contact-text"
                    ),
                    html.A("biorempp@gmail.com", href="mailto:biorempp@gmail.com", className="contact-email"),
                ]
            ),

            # Section: Social Media Icons
            html.Div(
                className="social-media",
                children=[
                    html.A(
                        html.I(className="w3-xlarge w3-hover-opacity fa fa-github"),
                        href="https://github.com/your-profile",
                        target="_blank",
                        className="social-icon"
                    ),
                    html.A(
                        html.I(className="w3-xlarge w3-hover-opacity fa fa-linkedin"),
                        href="https://linkedin.com/in/your-profile",
                        target="_blank",
                        className="social-icon"
                    ),
                    html.A(
                        html.I(className="w3-xlarge w3-hover-opacity fa fa-instagram"),
                        href="https://instagram.com/your-profile",
                        target="_blank",
                        className="social-icon"
                    ),
                    html.A(
                        html.I(className="w3-xlarge w3-hover-opacity fa fa-envelope"),
                        href="mailto:biorempp@gmail.com",
                        target="_blank",
                        className="social-icon"
                    ),
                ]
            ),
        ]
    )
