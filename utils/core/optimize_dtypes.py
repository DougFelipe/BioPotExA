import pandas as pd
#     - selected_genes (list[str]): List of genes selected by the user.
import logging

logging.basicConfig(level=logging.INFO)

def optimize_dtypes(df: pd.DataFrame) -> pd.DataFrame:  
    """  
    Otimiza tipos de dados convertendo colunas repetitivas para categorical.  
      
    Parameters  
    ----------  
    df : pd.DataFrame  
        DataFrame a ser otimizado  
          
    Returns  
    -------  
    pd.DataFrame  
        DataFrame com tipos otimizados para melhor performance de memória  
    """  
    categorical_columns = [  
        'ko', 'genesymbol', 'genename', 'cpd', 'compoundclass',   
        'referenceAG', 'compoundname', 'enzyme_activity', 'sample'  
    ]  
      
    for col in categorical_columns:  
        if col in df.columns:  
            df[col] = df[col].astype("category")  
      
    return df


def optimize_kegg_dtypes(df: pd.DataFrame) -> pd.DataFrame:  
    """  
    Otimiza tipos de dados para DataFrames KEGG convertendo colunas repetitivas para categorical.  
      
    Parameters  
    ----------  
    df : pd.DataFrame  
        DataFrame KEGG a ser otimizado  
          
    Returns  
    -------  
    pd.DataFrame  
        DataFrame com tipos otimizados para melhor performance de memória  
    """  
    # Colunas específicas do KEGG que se beneficiam de categorical  
    kegg_categorical_columns = [  
        'ko',           # KEGG Orthology identifiers (repetitivos)  
        'pathname',     # Pathway names (limitado conjunto de valores)  
        'genesymbol',   # Gene symbols (repetitivos)  
        'sample'        # Sample names (se presente no input)  
    ]  
      
    for col in kegg_categorical_columns:  
        if col in df.columns:  
            df[col] = df[col].astype("category")  
      
    return df


def optimize_hadeg_dtypes(df: pd.DataFrame) -> pd.DataFrame:  
    """  
    Otimiza tipos de dados para DataFrames HADEG convertendo colunas repetitivas para categorical.  
      
    Parameters  
    ----------  
    df : pd.DataFrame  
        DataFrame HADEG a ser otimizado  
          
    Returns  
    -------  
    pd.DataFrame  
        DataFrame com tipos otimizados para melhor performance de memória  
    """  
    # Colunas específicas do HADEG que se beneficiam de categorical  
    hadeg_categorical_columns = [  
        'Gene',             # Gene names (repetitivos como alkB, ahpC)  
        'ko',               # KEGG Orthology identifiers (repetitivos)  
        'Pathway',          # Pathway names (limitado conjunto de valores)  
        'compound_pathway', # Compound pathway types (Alkanes, Alkenes, etc.)  
        'sample'            # Sample names (se presente no input)  
    ]  
      
    for col in hadeg_categorical_columns:  
        if col in df.columns:  
            df[col] = df[col].astype("category")  
      
    return df


def optimize_toxcsm_dtypes(df: pd.DataFrame) -> pd.DataFrame:  
    """  
    Otimiza tipos de dados para DataFrames ToxCSM convertendo colunas repetitivas para categorical.  
      
    Parameters  
    ----------  
    df : pd.DataFrame  
        DataFrame ToxCSM a ser otimizado  
          
    Returns  
    -------  
    pd.DataFrame  
        DataFrame com tipos otimizados para melhor performance de memória  
    """  
    # Colunas específicas do ToxCSM que se beneficiam de categorical  
    toxcsm_categorical_columns = [  
        'SMILES',           # Estruturas químicas (podem ser repetitivas)  
        'cpd',              # Compound identifiers (chave de merge)  
        'ChEBI',            # ChEBI identifiers  
        'compoundname',     # Compound names (repetitivos)  
        'sample'            # Sample names (se presente no input)  
    ]  
      
    # Otimizar colunas categóricas básicas  
    for col in toxcsm_categorical_columns:  
        if col in df.columns:  
            df[col] = df[col].astype("category")  
      
    # Otimizar todas as colunas de labels (que têm valores repetitivos como "High Safety", "Low Toxicity")  
    label_columns = [col for col in df.columns if col.startswith('label_')]  
    for col in label_columns:  
        if col in df.columns:  
            df[col] = df[col].astype("category")  
      
    # Otimizar colunas de valores numéricos para float32 (reduz uso de memória)  
    value_columns = [col for col in df.columns if col.startswith('value_')]  
    for col in value_columns:  
        if col in df.columns:  
            df[col] = pd.to_numeric(df[col], errors='coerce').astype('float32')  
      
    return df
