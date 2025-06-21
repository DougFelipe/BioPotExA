# utils/p7_gene_compound_utils.py
import pandas as pd

def extract_dropdown_options_from_data(data, field):
    """Extrai opções de dropdown (ordenadas) de um campo específico de uma lista de dicionários."""
    if not data or field not in data[0]:
        return []
    values = sorted(pd.DataFrame(data)[field].dropna().unique())
    return [{'label': v, 'value': v} for v in values]

def filter_gene_compound_df(data, selected_compounds=None, selected_genes=None):
    """Filtra o DataFrame conforme genes e/ou compostos selecionados."""
    df = pd.DataFrame(data)
    if selected_compounds:
        df = df[df['compoundname'].isin(selected_compounds)]
    if selected_genes:
        df = df[df['genesymbol'].isin(selected_genes)]
    return df
