# Importações necessárias
from dash import html
from layouts.data_analysis import get_dataAnalysis_layout  # Importa o layout da página Data Analysis

# -------------------------------
# Layout da Página "About"
# -------------------------------

def get_about_layout():
    """
    Define e retorna o layout para a aba "About".

    Este layout inclui uma introdução ao tema da biorremediação e uma descrição
    do BioRemPP.
    """
    return html.Div([
        # Descrição do BioRemPP
        html.Div(
            [
                html.Div(
                    [
                        html.H3('BioRemPP', className='about-BioRemPP-title'),  # Título principal
                        html.H3('Biorremediation Potential Profile', className='about-BioRemPP-subtitle'),  # Subtítulo
                        html.Hr(className="my-2"),  # Linha horizontal para separação
                        html.P([
                            "Aimed at identifying the biotechnological potential for bioremediation, the Biorremediation Potential Profile (BioRemPP) was developed to enable the analysis of functional genome annotation data of bacteria, fungi, and plants, allowing the characterization of organisms with potential for pollutant degradation and providing a user interface and interactive data analysis",
                            html.Br(), html.Br(),
                            "The BioRemPP database integrates data on priority pollutants for bioremediation reported by regulatory agencies, PubChem and KEGG databases",
                            html.Br(), html.Br(),
                            "Seeking to contribute to sustainable development goals, BioRemPP emerges as an innovation in this field by automating the genomic analysis process used in identifying genes, enzymes, metabolic pathways, and biological processes with biotechnological potential to mitigate the environmental impacts associated with these pollutants"
                        ], className='about-content'),
                        
                        # **Adiciona o conteúdo de Data Analysis aqui**
                        html.Div(
                            get_dataAnalysis_layout(),
                            className='data-analysis-content'
                        ),

                        # Texto de "Integration of Databases"
                        html.H4("Integration of Databases", className='integration-title'),
                        
                        # Container de Imagens
                        html.Div(
                            [
                                html.Img(src='/assets/images/CHEBI_LOGO.png', className='about-image'),  
                                html.Img(src='/assets/images/PUBCHEM_LOGO.png', className='about-image'),  
                                html.Img(src='/assets/images/NCBI_LOGO.png', className='about-image'),  
                                html.Img(src='/assets/images/KEGG_LOGO.gif', className='about-image'),  
                                html.Img(src='/assets/images/HADEG_LOGO.png', className='about-image'), 
                                html.Img(src='/assets/images/TOXCSM_LOGO.png', className='about-image'),  
                            ],
                            className='about-image-container'
                        )
                    ],
                    className='about-text-container'
                ),
            ],
            className='about-content-container'
        )
    ], className='about-container')
