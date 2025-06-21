# utils/sample_gene_processing.py

import pandas as pd

def extract_dropdown_options(biorempp_data):
    """
    Extrai as opções dos dropdowns de amostras e genes.
    """
    if not biorempp_data:
        return [], []
    df = pd.DataFrame(biorempp_data)
    sample_options = [{'label': sample, 'value': sample} for sample in sorted(df['sample'].unique())]
    gene_options = [{'label': gene, 'value': gene} for gene in sorted(df['genesymbol'].unique())]
    return sample_options, gene_options

def filter_sample_gene_data(biorempp_data, selected_samples=None, selected_genes=None):
    """
    Filtra os dados processados conforme amostras e genes selecionados.
    """
    if not biorempp_data:
        return pd.DataFrame()  # vazio
    df = pd.DataFrame(biorempp_data)
    if selected_samples:
        df = df[df['sample'].isin(selected_samples)]
    if selected_genes:
        df = df[df['genesymbol'].isin(selected_genes)]
    return df
