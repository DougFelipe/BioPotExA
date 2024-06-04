# my_dash_app/layouts/about.py

# Importações
from dash import html
from components.about_features_list import create_about_features_list, about_features_list

# -------------------------------
# Layout da Página "About"
# -------------------------------

def get_about_layout():
    """
    Define e retorna o layout para a aba "About".

    Este layout inclui uma introdução ao tema da biorremediação e uma descrição
    do BioPExA.
    """
    return html.Div([
        # Descrição do BioPExA
        html.Div(
            [
                html.Div(
                    [
                        html.H3('BioPExA', className='about-biopexa-title'),
                        html.H3('Biorremediation Potential Explorer & Analyzer BioPExA', className='about-biopexa-subtitle'),
                        html.P([
                            "Aimed at identifying the biotechnological potential for bioremediation, the Bioremediation Potential Explorer & Analyzer (BioPExA) was developed to enable the analysis of functional genome annotation data of bacteria, fungi, and plants, allowing the characterization of organisms with potential for pollutant degradation and providing a user interface and interactive data analysis.",
                            html.Br(),html.Br(),
                            "The BioPExA database integrates data on priority pollutants for bioremediation reported by regulatory agencies, PubChem and KEGG databases.",
                            html.Br(),html.Br(),
                            "Seeking to contribute to sustainable development goals, BioPExA emerges as an innovation in this field by automating the genomic analysis process used in identifying genes, enzymes, metabolic pathways, and biological processes with biotechnological potential to mitigate the environmental impacts associated with these pollutants."
                        ], className='about-content'),
                        # Container de Imagens
                        html.Div(
                            [
                                html.Img(src='/assets/images/SDG06.png', className='about-image'),
                                html.Img(src='/assets/images/SDG13.png', className='about-image'),
                                html.Img(src='/assets/images/SDG14.png', className='about-image'),
                                html.Img(src='/assets/images/SDG15.png', className='about-image')
                            ],
                            className='about-image-container'
                        )
                    ],
                    className='about-text-container'
                ),
                create_about_features_list(about_features_list)
            ],
            className='about-content-container'
        )
    ], className='about-container')
