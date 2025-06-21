import pytest
import pandas as pd
from utils.rankings.ranking_compounds_by_gene_interaction_processing import process_compound_gene_ranking

def build_input_df(get_mock_BioRemPP):
    # Adapta o mock para as colunas esperadas pela função
    df = get_mock_BioRemPP.rename(columns={'compound': 'compoundname', 'enzyme_activity': 'genesymbol'})
    return df[['compoundname', 'genesymbol']]

def test_process_compound_gene_ranking_basic(get_mock_BioRemPP):
    input_df = build_input_df(get_mock_BioRemPP)
    result = process_compound_gene_ranking(input_df)
    assert not result.empty
    assert set(result.columns) == {'compoundname', 'num_genes'}
    assert result['num_genes'].is_monotonic_decreasing

def test_process_compound_gene_ranking_missing_columns(get_mock_BioRemPP):
    input_df = build_input_df(get_mock_BioRemPP)[['compoundname']]  # Remove 'genesymbol'
    with pytest.raises(ValueError) as excinfo:
        process_compound_gene_ranking(input_df)
    assert "Missing required columns" in str(excinfo.value)
    assert "genesymbol" in str(excinfo.value)

def test_process_compound_gene_ranking_empty_dataframe():
    input_df = pd.DataFrame(columns=['compoundname', 'genesymbol'])
    with pytest.raises(ValueError) as excinfo:
        process_compound_gene_ranking(input_df)
    assert "Input DataFrame is empty" in str(excinfo.value)

def test_process_compound_gene_ranking_unique_gene_count(get_mock_BioRemPP):
    df = build_input_df(get_mock_BioRemPP)
    if not df.empty:
        duplicate_row = df.iloc[[0]]
        df = pd.concat([df, duplicate_row], ignore_index=True)
    result = process_compound_gene_ranking(df)
    for _, row in result.iterrows():
        compound = row['compoundname']
        expected_count = df[df['compoundname'] == compound]['genesymbol'].nunique()
        assert row['num_genes'] == expected_count

def test_process_compound_gene_ranking_multiple_compounds(get_mock_BioRemPP):
    df = build_input_df(get_mock_BioRemPP)
    compounds = df['compoundname'].unique()
    result = process_compound_gene_ranking(df)
    assert set(result['compoundname']) == set(compounds)
    assert result['num_genes'].is_monotonic_decreasing
