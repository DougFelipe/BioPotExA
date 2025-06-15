import pandas as pd
import logging

# Configure o logger para este módulo
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')


def validate_columns(df: pd.DataFrame, required_columns: list):
    """
    Verifica se as colunas obrigatórias estão presentes no DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        O DataFrame a ser validado.
    required_columns : list
        Lista com os nomes das colunas obrigatórias.

    Raises
    ------
    KeyError
        Se qualquer coluna obrigatória estiver ausente no DataFrame.
    """
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        logger.error(f"Colunas ausentes no DataFrame: {missing}")
        raise KeyError(f"Colunas obrigatórias ausentes: {missing}")
    logger.debug(f"Todas as colunas necessárias estão presentes: {required_columns}")


def count_ko_per_pathway(merged_df: pd.DataFrame) -> pd.DataFrame:
    """
    Counts unique KOs for each pathway in each sample.

    Parameters
    ----------
    merged_df : pd.DataFrame
        DataFrame resultante da fusão com os dados KEGG, contendo colunas 'sample', 'pathname' e 'ko'.

    Returns
    -------
    pd.DataFrame
        DataFrame com a contagem de KOs únicos por via metabólica para cada amostra.

    Raises
    ------
    KeyError
        Se colunas obrigatórias estiverem ausentes.
    Exception
        Para qualquer erro inesperado durante o agrupamento.
    """
    try:
        required_columns = ['sample', 'pathname', 'ko']
        validate_columns(merged_df, required_columns)

        logger.info("Calculando o número de KOs únicos por via metabólica e por amostra...")
        pathway_count = (
            merged_df.groupby(['sample', 'pathname'])['ko']
            .nunique()
            .reset_index(name='unique_ko_count')
        )
        logger.info("Contagem concluída com sucesso.")
        return pathway_count

    except KeyError as e:
        logger.exception("Erro de validação de colunas.")
        raise

    except Exception as e:
        logger.exception("Erro inesperado ao calcular KOs por via.")
        raise RuntimeError("Erro ao processar a contagem de KOs por via metabólica.") from e


def count_ko_per_sample_for_pathway(merged_df: pd.DataFrame, selected_pathway: str) -> pd.DataFrame:
    """
    Counts unique KOs for a specific pathway in each sample.

    Parameters
    ----------
    merged_df : pd.DataFrame
        DataFrame contendo dados da fusão com KEGG, com colunas 'sample', 'pathname' e 'ko'.
    selected_pathway : str
        Identificador da via metabólica selecionada para a filtragem.

    Returns
    -------
    pd.DataFrame
        DataFrame com a contagem de KOs únicos por amostra, ordenado de forma decrescente.

    Raises
    ------
    KeyError
        Se colunas obrigatórias estiverem ausentes.
    ValueError
        Se a via metabólica selecionada não estiver presente no DataFrame.
    Exception
        Para qualquer outro erro durante o processamento.
    """
    try:
        required_columns = ['sample', 'pathname', 'ko']
        validate_columns(merged_df, required_columns)

        if selected_pathway not in merged_df['pathname'].unique():
            logger.warning(f"A via metabólica '{selected_pathway}' não foi encontrada no DataFrame.")
            raise ValueError(f"Via metabólica '{selected_pathway}' não encontrada.")

        logger.info(f"Filtrando dados para a via: {selected_pathway}")
        filtered_df = merged_df[merged_df['pathname'] == selected_pathway]

        logger.info("Calculando o número de KOs únicos por amostra...")
        sample_count = (
            filtered_df.groupby('sample')['ko']
            .nunique()
            .reset_index(name='unique_ko_count')
        )

        result = sample_count.sort_values('unique_ko_count', ascending=False)
        logger.info("Contagem por amostra concluída com sucesso.")
        return result

    except (KeyError, ValueError) as e:
        logger.exception("Erro durante o processamento por via metabólica específica.")
        raise

    except Exception as e:
        logger.exception("Erro inesperado ao calcular KOs por amostra para via.")
        raise RuntimeError("Erro ao processar a contagem de KOs por amostra para a via selecionada.") from e
