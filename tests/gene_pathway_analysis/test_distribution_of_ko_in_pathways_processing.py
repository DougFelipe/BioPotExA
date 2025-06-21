import pytest
import pandas as pd
from utils.gene_pathway_analysis import distribution_of_ko_in_pathways_processing as dkp

@pytest.mark.usefixtures("get_mock_KEGG")
class TestDistributionOfKoInPathwaysProcessing:
    """
    Test suite for distribution_of_ko_in_pathways_processing.py using mock KEGG DataFrame fixture.
    """

    def test_validate_columns_success(self, get_mock_KEGG):
        """
        Test that validate_columns passes when all required columns are present.

        Parameters
        ----------
        get_mock_KEGG : pd.DataFrame
            Fixture providing a DataFrame with columns ['sample', 'ko', 'pathname', 'genesymbol'].

        Expected
        -------
        No exception is raised when required columns are present.
        """
        required_columns = ['sample', 'pathname', 'ko']
        # Should not raise
        dkp.validate_columns(get_mock_KEGG, required_columns)

    def test_validate_columns_missing(self, get_mock_KEGG):
        """
        Test that validate_columns raises KeyError when required columns are missing.

        Parameters
        ----------
        get_mock_KEGG : pd.DataFrame
            Fixture providing a DataFrame with columns ['sample', 'ko', 'pathname', 'genesymbol'].

        Expected
        -------
        KeyError is raised if a required column is missing.
        """
        df = get_mock_KEGG.drop(columns=['ko'])
        required_columns = ['sample', 'pathname', 'ko']
        with pytest.raises(KeyError):
            dkp.validate_columns(df, required_columns)

    def test_count_ko_per_pathway_basic(self, get_mock_KEGG):
        """
        Test count_ko_per_pathway returns correct unique KO counts per pathway per sample.

        Parameters
        ----------
        get_mock_KEGG : pd.DataFrame
            Fixture providing a DataFrame with columns ['sample', 'ko', 'pathname', 'genesymbol'].

        Expected
        -------
        DataFrame with columns ['sample', 'pathname', 'unique_ko_count'].
        Each row represents a (sample, pathway) pair and the count of unique KOs.
        """
        result = dkp.count_ko_per_pathway(get_mock_KEGG)
        assert isinstance(result, pd.DataFrame)
        assert set(['sample', 'pathname', 'unique_ko_count']).issubset(result.columns)
        # All unique (sample, pathname) pairs should be present
        expected_pairs = get_mock_KEGG.groupby(['sample', 'pathname']).size().reset_index()[['sample', 'pathname']]
        merged = pd.merge(result, expected_pairs, on=['sample', 'pathname'])
        assert len(merged) == len(expected_pairs)
        # Each count should match nunique of 'ko'
        for _, row in expected_pairs.iterrows():
            mask = (get_mock_KEGG['sample'] == row['sample']) & (get_mock_KEGG['pathname'] == row['pathname'])
            expected_count = get_mock_KEGG[mask]['ko'].nunique()
            actual_count = result[(result['sample'] == row['sample']) & (result['pathname'] == row['pathname'])]['unique_ko_count'].iloc[0]
            assert actual_count == expected_count

    def test_count_ko_per_pathway_missing_column(self, get_mock_KEGG):
        """
        Test count_ko_per_pathway raises KeyError if required columns are missing.

        Parameters
        ----------
        get_mock_KEGG : pd.DataFrame
            Fixture providing a DataFrame with columns ['sample', 'ko', 'pathname', 'genesymbol'].

        Expected
        -------
        KeyError is raised if a required column is missing.
        """
        df = get_mock_KEGG.drop(columns=['pathname'])
        with pytest.raises(KeyError):
            dkp.count_ko_per_pathway(df)

    def test_count_ko_per_sample_for_pathway_success(self, get_mock_KEGG):
        """
        Test count_ko_per_sample_for_pathway returns correct KO counts for a valid pathway.

        Parameters
        ----------
        get_mock_KEGG : pd.DataFrame
            Fixture providing a DataFrame with columns ['sample', 'ko', 'pathname', 'genesymbol'].

        Expected
        -------
        DataFrame with columns ['sample', 'unique_ko_count'], sorted descending by count.
        Only samples for the selected pathway are included.
        """
        # Pick a valid pathway from the fixture
        selected_pathway = get_mock_KEGG['pathname'].iloc[0]
        result = dkp.count_ko_per_sample_for_pathway(get_mock_KEGG, selected_pathway)
        assert isinstance(result, pd.DataFrame)
        assert set(['sample', 'unique_ko_count']).issubset(result.columns)
        # All samples in result should have the selected pathway in the original data
        samples_in_pathway = get_mock_KEGG[get_mock_KEGG['pathname'] == selected_pathway]['sample'].unique()
        assert set(result['sample']).issubset(set(samples_in_pathway))
        # Each count should match nunique of 'ko' for that sample and pathway
        for _, row in result.iterrows():
            mask = (get_mock_KEGG['sample'] == row['sample']) & (get_mock_KEGG['pathname'] == selected_pathway)
            expected_count = get_mock_KEGG[mask]['ko'].nunique()
            assert row['unique_ko_count'] == expected_count
        # Check descending order
        assert result['unique_ko_count'].is_monotonic_decreasing

    def test_count_ko_per_sample_for_pathway_not_found(self, get_mock_KEGG):
        """
        Test count_ko_per_sample_for_pathway raises ValueError if pathway is not present.

        Parameters
        ----------
        get_mock_KEGG : pd.DataFrame
            Fixture providing a DataFrame with columns ['sample', 'ko', 'pathname', 'genesymbol'].

        Expected
        -------
        ValueError is raised if the selected pathway is not present in the DataFrame.
        """
        non_existent_pathway = "nonexistent_pathway_123"
        with pytest.raises(ValueError):
            dkp.count_ko_per_sample_for_pathway(get_mock_KEGG, non_existent_pathway)

    def test_count_ko_per_sample_for_pathway_missing_column(self, get_mock_KEGG):
        """
        Test count_ko_per_sample_for_pathway raises KeyError if required columns are missing.

        Parameters
        ----------
        get_mock_KEGG : pd.DataFrame
            Fixture providing a DataFrame with columns ['sample', 'ko', 'pathname', 'genesymbol'].

        Expected
        -------
        KeyError is raised if a required column is missing.
        """
        df = get_mock_KEGG.drop(columns=['sample'])
        selected_pathway = get_mock_KEGG['pathname'].iloc[0]
        with pytest.raises(KeyError):
            dkp.count_ko_per_sample_for_pathway(df, selected_pathway)
