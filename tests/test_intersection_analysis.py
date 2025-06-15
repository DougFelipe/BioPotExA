import pytest
import pandas as pd

from utils.intersections_and_groups.intersection_analysis_processing import (
    prepare_upsetplot_data,
)
from utils.data_validator import validate_and_process_input


# --------- Helpers para simular conteúdo base64 ----------

def get_base64_txt_content(text):
    import base64
    return 'data:text/plain;base64,' + base64.b64encode(text.encode('utf-8')).decode('utf-8')


# --------- Casos de Teste ---------

def test_prepare_upsetplot_data_valid_from_txt_input():
    """
    Verifica se a função prepara corretamente os dados a partir do conteúdo `.txt` simulado.
    """
    raw_text = """>Sample1
K00001
K00002
>Sample2
K00002
K00003
"""
    contents = get_base64_txt_content(raw_text)
    df, error = validate_and_process_input(contents, "input.txt")

    assert error is None
    assert isinstance(df, pd.DataFrame)
    assert set(df.columns) == {"sample", "ko"}
    
    selected = ["Sample1", "Sample2"]
    result = prepare_upsetplot_data(df, selected)

    # 4 combinações únicas
    assert result.shape[0] == 4
    assert not result.duplicated().any()


def test_prepare_upsetplot_data_empty_selection():
    """
    Verifica se o retorno está correto com uma lista vazia de amostras.
    """
    raw_text = """>S1
K001
K002
"""
    contents = get_base64_txt_content(raw_text)
    df, _ = validate_and_process_input(contents, "data.txt")

    selected = []  # Nenhuma amostra selecionada
    result = prepare_upsetplot_data(df, selected)

    assert result.empty


def test_prepare_upsetplot_data_missing_columns():
    """
    Verifica se erro é levantado quando colunas obrigatórias estão ausentes.
    """
    invalid_df = pd.DataFrame({"x": [1, 2], "y": [3, 4]})
    with pytest.raises(ValueError, match="Missing required column"):
        prepare_upsetplot_data(invalid_df, ["S1"])


def test_prepare_upsetplot_data_invalid_types():
    """
    Verifica se tipos errados de entrada são tratados corretamente.
    """
    with pytest.raises(ValueError, match="Expected merged_data to be a pandas DataFrame."):
        prepare_upsetplot_data("not_a_dataframe", ["S1"])

    with pytest.raises(ValueError, match="Expected selected_samples to be a list."):
        prepare_upsetplot_data(pd.DataFrame({"sample": [], "ko": []}), "S1")
