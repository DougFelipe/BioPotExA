import pytest
from utils.entity_interactions import gene_compound_interaction_processing as gc_proc

@pytest.mark.usefixtures("get_mock_ToxCSM")
def test_extract_dropdown_options_from_data_compoundname(get_mock_ToxCSM):
    """
    Test extraction of dropdown options for 'compoundname' field.

    Parameters
    ----------
    get_mock_ToxCSM : pd.DataFrame
        Fixture providing mock compound toxicity data.

    Expected
    --------
    Returns a sorted list of dicts with 'label' and 'value' keys for each unique compoundname.
    Verifies correct extraction and sorting of dropdown options.
    """
    data = get_mock_ToxCSM.to_dict(orient="records")
    result = gc_proc.extract_dropdown_options_from_data(data, "compoundname")
    expected = sorted(get_mock_ToxCSM["compoundname"].dropna().unique())
    assert isinstance(result, list)
    assert all("label" in d and "value" in d for d in result)
    assert [d["value"] for d in result] == list(expected)

@pytest.mark.usefixtures("get_mock_KEGG")
def test_extract_dropdown_options_from_data_genesymbol(get_mock_KEGG):
    """
    Test extraction of dropdown options for 'genesymbol' field.

    Parameters
    ----------
    get_mock_KEGG : pd.DataFrame
        Fixture providing mock KEGG gene symbol data.

    Expected
    --------
    Returns a sorted list of dicts for unique gene symbols.
    Verifies correct extraction and sorting.
    """
    data = get_mock_KEGG.to_dict(orient="records")
    result = gc_proc.extract_dropdown_options_from_data(data, "genesymbol")
    expected = sorted(get_mock_KEGG["genesymbol"].dropna().unique())
    assert [d["value"] for d in result] == list(expected)

def test_extract_dropdown_options_from_data_empty():
    """
    Test extraction with empty data.

    Expected
    --------
    Returns an empty list when data is empty.
    """
    result = gc_proc.extract_dropdown_options_from_data([], "compoundname")
    assert result == []

def test_extract_dropdown_options_from_data_missing_field():
    """
    Test extraction when the field is missing in data.

    Expected
    --------
    Returns an empty list if the field is not present in the data dicts.
    """
    data = [{"foo": "bar"}]
    result = gc_proc.extract_dropdown_options_from_data(data, "compoundname")
    assert result == []

@pytest.mark.usefixtures("get_mock_ToxCSM")
def test_filter_gene_compound_df_by_compound(get_mock_ToxCSM):
    """
    Test filtering DataFrame by selected compounds.

    Parameters
    ----------
    get_mock_ToxCSM : pd.DataFrame
        Fixture providing mock compound toxicity data.

    Expected
    --------
    Returns only rows where 'compoundname' matches selected_compounds.
    """
    data = get_mock_ToxCSM.to_dict(orient="records")
    compounds = get_mock_ToxCSM["compoundname"].unique()[:1].tolist()
    filtered = gc_proc.filter_gene_compound_df(data, selected_compounds=compounds)
    assert all(row["compoundname"] in compounds for _, row in filtered.iterrows())
    assert len(filtered) <= len(get_mock_ToxCSM)

@pytest.mark.usefixtures("get_mock_KEGG")
def test_filter_gene_compound_df_by_gene(get_mock_KEGG):
    """
    Test filtering DataFrame by selected genes.

    Parameters
    ----------
    get_mock_KEGG : pd.DataFrame
        Fixture providing mock KEGG gene symbol data.

    Expected
    --------
    Returns only rows where 'genesymbol' matches selected_genes.
    """
    # Add 'compoundname' column to match function expectations
    df = get_mock_KEGG.copy()
    df["compoundname"] = "dummy"
    data = df.to_dict(orient="records")
    genes = df["genesymbol"].unique()[:1].tolist()
    filtered = gc_proc.filter_gene_compound_df(data, selected_genes=genes)
    assert all(row["genesymbol"] in genes for _, row in filtered.iterrows())
    assert len(filtered) <= len(df)

@pytest.mark.usefixtures("get_mock_ToxCSM", "get_mock_KEGG")
def test_filter_gene_compound_df_by_compound_and_gene(get_mock_ToxCSM, get_mock_KEGG):
    """
    Test filtering DataFrame by both compounds and genes.

    Parameters
    ----------
    get_mock_ToxCSM : pd.DataFrame
        Fixture providing mock compound toxicity data.
    get_mock_KEGG : pd.DataFrame
        Fixture providing mock KEGG gene symbol data.

    Expected
    --------
    Returns only rows matching both selected_compounds and selected_genes.
    """
    # Create a merged mock DataFrame with both columns
    df = get_mock_ToxCSM.copy()
    df["genesymbol"] = "GENE1"
    data = df.to_dict(orient="records")
    compounds = df["compoundname"].unique()[:1].tolist()
    genes = ["GENE1"]
    filtered = gc_proc.filter_gene_compound_df(data, selected_compounds=compounds, selected_genes=genes)
    assert all(
        (row["compoundname"] in compounds and row["genesymbol"] in genes)
        for _, row in filtered.iterrows()
    )
    assert len(filtered) <= len(df)

def test_filter_gene_compound_df_no_filters():
    """
    Test filtering with no filters applied.

    Expected
    --------
    Returns the original DataFrame unchanged.
    """
    data = [
        {"compoundname": "A", "genesymbol": "X"},
        {"compoundname": "B", "genesymbol": "Y"},
    ]
    filtered = gc_proc.filter_gene_compound_df(data)
    assert len(filtered) == 2
    assert set(filtered["compoundname"]) == {"A", "B"}
    assert set(filtered["genesymbol"]) == {"X", "Y"}
