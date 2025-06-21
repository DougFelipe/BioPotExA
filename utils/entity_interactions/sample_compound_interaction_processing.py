"""

----------------------
Funções utilitárias para manipulação e filtragem de dados de classes de compostos.

"""

import pandas as pd

import pandas as pd

def extract_compound_classes(biorempp_data):
    """
    Extrai as classes de compostos únicas dos dados processados (list[dict] ou DataFrame).

    Parameters
    ----------
    biorempp_data : list[dict] | pd.DataFrame

    Returns
    -------
    list
    """
    # Trate DataFrame e lista separadamente
    if isinstance(biorempp_data, pd.DataFrame):
        if biorempp_data.empty or 'compoundclass' not in biorempp_data.columns:
            return []
        values = biorempp_data['compoundclass'].dropna().unique()
        return sorted(values)
    # Para lista ou None
    if not biorempp_data:
        return []
    df = pd.DataFrame(biorempp_data)
    if 'compoundclass' not in df.columns:
        return []
    values = df['compoundclass'].dropna().unique()
    return sorted(values)


def filter_by_compound_class(biorempp_data, selected_class):
    """
    Filtra os dados pelo valor de classe de composto selecionado.

    Parameters
    ----------
    biorempp_data : list[dict] | pd.DataFrame
    selected_class : str

    Returns
    -------
    pd.DataFrame
    """
    # Trate DataFrame e lista separadamente
    if isinstance(biorempp_data, pd.DataFrame):
        if biorempp_data.empty or not selected_class or 'compoundclass' not in biorempp_data.columns:
            return pd.DataFrame()
        return biorempp_data[biorempp_data['compoundclass'] == selected_class]
    # Para lista ou None
    if not biorempp_data or not selected_class:
        return pd.DataFrame()
    df = pd.DataFrame(biorempp_data)
    if 'compoundclass' not in df.columns:
        return pd.DataFrame()
    return df[df['compoundclass'] == selected_class]
