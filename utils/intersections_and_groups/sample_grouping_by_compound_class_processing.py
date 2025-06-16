import logging
import pandas as pd
from typing import List

# Configure o logger do módulo
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def group_by_class(compoundclass_choice: str, tabela: pd.DataFrame) -> pd.DataFrame:
    """  
    Groups samples by their compound profiles using hash-based set comparison for O(n) complexity.  
    """  
    required_cols = {'compoundclass', 'sample', 'compoundname'}  
    if not required_cols.issubset(tabela.columns):  
        missing = required_cols - set(tabela.columns)  
        raise ValueError(f"Missing required columns in input DataFrame: {missing}")  
  
    logger.info("Filtering data by compound class: '%s'", compoundclass_choice)  
    dados_selecionados = tabela[tabela['compoundclass'] == compoundclass_choice]  
  
    if dados_selecionados.empty:  
        raise ValueError(f"No data found for compound class: {compoundclass_choice}")  
  
    # Usar hash de conjuntos para agrupamento O(n)  
    compound_profile_to_group = {}  # hash do perfil -> índice do grupo  
    grupos = []  
      
    for sample in dados_selecionados['sample'].unique():  
        compostos = frozenset(dados_selecionados.loc[  
            dados_selecionados['sample'] == sample, 'compoundname'  
        ].unique())  
          
        if compostos:  
            # Usar hash do frozenset como chave  
            profile_hash = hash(compostos)  
              
            if profile_hash in compound_profile_to_group:  
                # Grupo já existe, adicionar amostra  
                group_idx = compound_profile_to_group[profile_hash]  
                grupos[group_idx]['samples'].append(sample)  
            else:  
                # Criar novo grupo  
                new_group = {'compostos': list(compostos), 'samples': [sample]}  
                grupos.append(new_group)  
                compound_profile_to_group[profile_hash] = len(grupos) - 1  
  
    logger.info("Identified %d distinct groups for class '%s'", len(grupos), compoundclass_choice)  
  
    # Resto da função permanece igual  
    tabela_grupos = tabela.copy()  
    tabela_grupos['grupo'] = None  
  
    for i, grupo in enumerate(grupos):  
        label = f"{compoundclass_choice} - Group {i + 1}"  
        tabela_grupos.loc[  
            (tabela_grupos['sample'].isin(grupo['samples'])) &  
            (tabela_grupos['compoundname'].isin(grupo['compostos'])),  
            'grupo'  
        ] = label  
  
    resultado = tabela_grupos[tabela_grupos['compoundclass'] == compoundclass_choice]  
    return resultado


def minimize_groups(df: pd.DataFrame) -> List[str]:
    """
    Reduces the number of groups required to cover all compounds with minimal redundancy.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing 'grupo' and 'compoundname' columns.

    Returns
    -------
    list of str
        List of selected group labels that together cover all compounds.

    Raises
    ------
    ValueError
        If required columns are missing or the input DataFrame is empty.
    """
    required_cols = {'grupo', 'compoundname'}
    if not required_cols.issubset(df.columns):
        missing = required_cols - set(df.columns)
        raise ValueError(f"Missing required columns in input DataFrame: {missing}")

    if df.empty:
        raise ValueError("Input DataFrame is empty.")

    logger.info("Minimizing groups to cover all compounds")

    group_compounds = (
        df.groupby('grupo')['compoundname']
        .apply(lambda x: list(set(x)))
        .reset_index()
    )

    all_compounds = set(df['compoundname'].unique())
    selected_groups = []

    while all_compounds:
        max_cover = 0
        best_group = None

        for _, row in group_compounds.iterrows():
            group = row['grupo']
            compounds = set(row['compoundname'])
            coverage = len(all_compounds & compounds)

            if coverage > max_cover:
                max_cover = coverage
                best_group = group

        if best_group is None:
            raise ValueError("Failed to find a group covering remaining compounds.")

        selected_groups.append(best_group)
        covered = set(
            group_compounds.loc[group_compounds['grupo'] == best_group, 'compoundname'].values[0]
        )
        all_compounds -= covered
        group_compounds = group_compounds[group_compounds['grupo'] != best_group]

        logger.debug("Selected group '%s', %d compounds remaining", best_group, len(all_compounds))

    logger.info("Total selected groups: %d", len(selected_groups))
    return selected_groups
