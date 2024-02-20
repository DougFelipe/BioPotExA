# Importações
from dash import html

# -------------------------------
# Definições de Listas e Itens
# -------------------------------

# Lista de características para análise de dados
features_list_1 = [
    "Análise da contabilização do total de genes associados a compostos prioritários",
    "Análise da distribuição do total de genes associados a compostos prioritários",
    "Análise de genes em vias de metabolismo e degradação de xenobióticos no KEGG",
    "Análise do perfil de degradação das amostras por classe de compostos",
    "Análise da relação entre genes e compostos"
]

# -------------------------------
# Criação de Componentes
# -------------------------------

# Função para criar cards de lista
def create_list_card(title, features):
    """
    Cria e retorna um card HTML com um título e uma lista de características.

    :param title: Título do card.
    :param features: Lista de características a serem incluídas no card.
    :return: Um componente HTML Div representando o card.
    """
    return html.Div(
        [
            html.H4(title, className='list-title'),
            html.Ul([html.Li(feature) for feature in features], className='list-group')
        ],
        className='list-card'
    )

# -------------------------------
# Layout da Página "About"
# -------------------------------

def get_about_layout():
    """
    Define e retorna o layout para a aba "About".

    Este layout inclui uma introdução ao tema da biorremediação, uma descrição
    do BioPExA e uma lista de características de análise de dados.
    """
    return html.Div([
        html.H3('About Biorremediation', className='about-title'),
        # Conteúdo introdutório sobre biorremediação
        html.P([
            "Environmental pollutants encompass a variety of chemicals that pose significant risks to ecosystems and human health, regulated by environmental agencies worldwide. Physicochemical treatment methods are costly and often inefficient, necessitating the development of more efficient and environmentally friendly methods. Bioremediation is the process of using living organisms to degrade or remove environmental contaminants through their natural metabolic processes ",
            html.A("(Iwamoto and Nasu, 2001)", href="https://www.sciencedirect.com/science/article/abs/pii/S1389172301801900", target="_blank"), ". It relies on the ability of certain microorganisms, such as bacteria, fungi, and plants, to convert organic substrates into sources of carbon and energy ",
            html.A("(Megharaj et al., 2011)", href="https://pubmed.ncbi.nlm.nih.gov/21722961/", target="_blank"), ". Bioremediation has emerged as an important sustainable technology for the decontamination of environments polluted by toxic substances ",
            html.A("(Tyagi et al., 2011)", href="https://pubmed.ncbi.nlm.nih.gov/20680666/", target="_blank"), ". It offers advantages as a low-cost, efficient, and environmentally safe option compared to physicochemical methods ",
            html.A("(Das and Chandran, 2011)", href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3042690/", target="_blank"), ". Studies demonstrate the potential of bioremediation in degrading a wide variety of contaminants, such as petroleum, pesticides, chlorinated solvents, among others. Therefore, research in bioremediation is essential to understand and apply biological processes capable of sustainably mitigating environmental damage."
        ], className='about-content'),
        # Descrição do BioPExA
        html.H3('BioPExA', className='about-biopexa-title'),
        html.P([
            "Aimed at identifying the biotechnological potential for bioremediation, the Bioremediation Potential Explorer & Analyzer (BioPExA) was developed to enable the analysis of functional genome annotation data of bacteria, fungi, and plants, allowing the characterization of organisms with potential for pollutant degradation and provinding and user interface and interactive data analysis. The BioPExA database integrates data on priority pollutants for bioremediation reported by regulatory agencies, PubChem and KEGG databases. Seeking to contribute to sustainable development goals, BioPExA emerges as an innovation in this field by automating the genomic analysis process used in identifying genes, enzymes, metabolic pathways, and biological processes with biotechnological potential to mitigate the environmental impacts associated with these pollutants."
        ], className='about-content'),
        # Card com a lista de características de análise de dados
        html.Div(
            [
                create_list_card("Data Analysis Features", features_list_1)
            ],
            className='list-container'
        )
    ], className='about-container')
