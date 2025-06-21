import pytest
import pandas as pd
from utils.entity_interactions.sample_gene_associations_processing import extract_dropdown_options, filter_sample_gene_data

@pytest.fixture
def mock_BioRemPP_with_genesymbol():
    """
    Fixture que retorna DataFrame simulado contendo colunas 'sample' e 'genesymbol'.
    """
    data = {
        "sample": ["Sample1", "Sample2", "Sample1", "Sample3"],
        "genesymbol": ["geneA", "geneB", "geneC", "geneD"],
        "ko": ["K00001", "K00002", "K00003", "K00004"]
    }
    return pd.DataFrame(data)

def test_extract_dropdown_options_with_data(mock_BioRemPP_with_genesymbol):
    """
    Testa se as opções extraídas dos dropdowns de amostras e genes estão corretas.
    """
    data = mock_BioRemPP_with_genesymbol.to_dict(orient="records")
    sample_opts, gene_opts = extract_dropdown_options(data)
    expected_samples = sorted(mock_BioRemPP_with_genesymbol["sample"].unique())
    expected_genes = sorted(mock_BioRemPP_with_genesymbol["genesymbol"].unique())
    assert [opt["value"] for opt in sample_opts] == expected_samples
    assert [opt["value"] for opt in gene_opts] == expected_genes
    assert all('label' in opt and 'value' in opt for opt in sample_opts)
    assert all('label' in opt and 'value' in opt for opt in gene_opts)

def test_extract_dropdown_options_empty():
    sample_opts, gene_opts = extract_dropdown_options([])
    assert sample_opts == []
    assert gene_opts == []

def test_filter_sample_gene_data_no_filters(mock_BioRemPP_with_genesymbol):
    data = mock_BioRemPP_with_genesymbol.to_dict(orient="records")
    result = filter_sample_gene_data(data)
    pd.testing.assert_frame_equal(result.reset_index(drop=True), mock_BioRemPP_with_genesymbol.reset_index(drop=True))

def test_filter_sample_gene_data_sample_filter(mock_BioRemPP_with_genesymbol):
    samples = mock_BioRemPP_with_genesymbol['sample'].unique()[:1].tolist()
    data = mock_BioRemPP_with_genesymbol.to_dict(orient="records")
    result = filter_sample_gene_data(data, selected_samples=samples)
    assert set(result['sample'].unique()) == set(samples)
    assert all(s in samples for s in result['sample'])

def test_filter_sample_gene_data_gene_filter(mock_BioRemPP_with_genesymbol):
    genes = mock_BioRemPP_with_genesymbol['genesymbol'].unique()[:1].tolist()
    data = mock_BioRemPP_with_genesymbol.to_dict(orient="records")
    result = filter_sample_gene_data(data, selected_genes=genes)
    assert set(result['genesymbol'].unique()) == set(genes)
    assert all(g in genes for g in result['genesymbol'])

def test_filter_sample_gene_data_both_filters(mock_BioRemPP_with_genesymbol):
    samples = mock_BioRemPP_with_genesymbol['sample'].unique()[:1].tolist()
    genes = mock_BioRemPP_with_genesymbol['genesymbol'].unique()[:1].tolist()
    data = mock_BioRemPP_with_genesymbol.to_dict(orient="records")
    result = filter_sample_gene_data(data, selected_samples=samples, selected_genes=genes)
    assert set(result['sample'].unique()).issubset(set(samples))
    assert set(result['genesymbol'].unique()).issubset(set(genes))

def test_filter_sample_gene_data_empty():
    result = filter_sample_gene_data([])
    assert isinstance(result, pd.DataFrame)
    assert result.empty
