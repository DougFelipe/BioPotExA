# CONDEUDO DA PÁGINA ABOUT

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
                            "Aimed at identifying the biotechnological potential for bioremediation, the Bioremediation Potential Explorer & Analyzer (BioPExA) was developed to enable the analysis of functional genome annotation data of bacteria, fungi, and plants, allowing the characterization of organisms with potential for pollutant degradation and providing a user interface and interactive data analysis. The BioPExA database integrates data on priority pollutants for bioremediation reported by regulatory agencies, PubChem and KEGG databases. Seeking to contribute to sustainable development goals, BioPExA emerges as an innovation in this field by automating the genomic analysis process used in identifying genes, enzymes, metabolic pathways, and biological processes with biotechnological potential to mitigate the environmental impacts associated with these pollutants."
                        ], className='about-content'),



                            html.P(
                            'Nossa plataforma de análise de dados é projetada para pesquisadores e profissionais que '
                            'precisam avaliar o potencial de biorremediação de genomas e metagenomas. Com uma interface '
                            'intuitiva e recursos avançados, a ferramenta facilita a anotação funcional e a identificação de '
                            'genes-chave envolvidos na degradação de poluentes e outras funções ecológicas relevantes.',
                            className='about-content'
                        ),
                        html.P(
                            'Para começar, faça o upload dos seus dados no formato especificado, utilizando a função de arrastar e soltar '
                            'ou selecionando o arquivo manualmente. Após a análise, você pode facilmente '
                            'exportar os dados para uso em publicações, apresentações ou para análises subsequentes em outras plataformas.',
                            className='about-content'
                        ),



                        # my_dash_app/layouts/results.py

from dash import html
import dash_bootstrap_components as dbc
from layouts.P1_KO_COUNT import get_ko_count_bar_chart_layout, get_ko_violin_boxplot_layout
from layouts.P2_KO_20PATHWAY import get_pathway_ko_bar_chart_layout, get_sample_ko_pathway_bar_chart_layout

def get_results_layout():
    return html.Div([
        html.H2('Data Analysis Results', className='results-title'),
        html.Hr(className="my-2"),
        html.H4('Results from your submitted data', className='results-subtitle'),
        dbc.Accordion(
            [
                dbc.AccordionItem(
                    html.Div(id='output-merge-table'),  # Contêiner para a tabela mesclada
                    title="Results Table"
                ),
                dbc.AccordionItem(
                    get_ko_count_bar_chart_layout(),
                    title="Gene count associated with priority compounds",
                ),
                dbc.AccordionItem(
                    get_ko_violin_boxplot_layout(),
                    title="Distribution of genes associated with priority compounds"
                ),
                dbc.AccordionItem(
                    get_pathway_ko_bar_chart_layout(),
                    title="KEGG Xenobiotics Biodegradation and Metabolism (Grouped by Sample)"
                ),
                dbc.AccordionItem(
                    get_sample_ko_pathway_bar_chart_layout(),
                    title="KEGG Xenobiotics Biodegradation and Metabolism (Grouped by Pathway)"
                ),
                dbc.AccordionItem(
                    html.Div("Rank of associated genes with priority compounds "),  # Rank of associated genes with priority compounds
                    title="Rank of associated genes with priority compounds"
                ),
                dbc.AccordionItem(
                    html.Div("Rank of organisms with priority compounds degradation potential"),  # Rank of organisms with priority compounds degradation potential
                    title="Rank of organisms with priority compounds degradation potential"
                ),
                dbc.AccordionItem(
                    html.Div("Rank of priority compounds degradation potential"),  # Rank of priority compounds degradation potential
                    title="Rank of priority compounds degradation potential"
                ),
                dbc.AccordionItem(
                    html.Div("Genes present in samples"),  # 
                    title="Genes present in samples"
                ),
                dbc.AccordionItem(
                    html.Div("Relashinship between compounds and samples"),  # Relashinship between compounds and samples
                    title="Relashinship between compounds and samples   "
                ),
            ],
            start_collapsed=True,
            always_open=True,
        )
    ])
