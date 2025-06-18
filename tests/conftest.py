"""
conftest.py: Fixtures for automated unit tests in the BioPotExA test suite.

This script provides reusable pytest fixtures that generate mock pandas DataFrames
representing various database schemas (HADEG, ToxCSM, BioRemPP, KEGG). These fixtures
are used across multiple test modules to ensure consistent, isolated, and reproducible
test data for validating data processing, loading, and merging functionalities.

Author
------
Douglas Felipe (github.com/DougFelipe)

Date
----
2024-06-09

Version
-------
1.0.0

Dependencies
------------
- pytest >= 7.0
- pandas >= 1.0

Notes
-----
- All fixtures return pandas DataFrames with representative columns and values.
- Designed for use with pytest's fixture injection mechanism.
- Used by multiple test modules in the BioPotExA test suite.

Examples
--------
$ pytest
"""

import pandas as pd
import pytest


@pytest.fixture
def get_mock_HADEG():
    """
    Provides a mock HADEG database DataFrame for testing.

    Returns
    -------
    pd.DataFrame
        DataFrame containing sample, gene, KO, pathway, and compound pathway columns,
        simulating the structure of the HADEG database.
    """
    data = {
        'sample': ['Sample1', 'Sample1', 'Sample2', 'Sample2', 'Sample3'],
        'Gene': ['alkB', 'ahpC', 'catA', 'pcaH', 'todC1'],
        'ko': ['K00496', 'K03386', 'K03782', 'K00448', 'K18067'],
        'Pathway': [
            'Alkane degradation',
            'Alkane degradation',
            'Catechol degradation',
            'Protocatechuate degradation',
            'Toluene degradation'
        ],
        'compound_pathway': [
            'Alkanes',
            'Alkanes',
            'Aromatic compounds',
            'Aromatic compounds',
            'Aromatic compounds'
        ]
    }
    return pd.DataFrame(data)


@pytest.fixture
def get_mock_ToxCSM():
    """
    Provides a mock ToxCSM database DataFrame for testing.

    Returns
    -------
    pd.DataFrame
        DataFrame containing sample, compound, toxicity, LD50, and safety label columns,
        simulating the structure of the ToxCSM database.
    """
    data = {
        'sample': ['Sample1', 'Sample1', 'Sample2', 'Sample3', 'Sample3'],
        'cpd': ['C00001', 'C00002', 'C00003', 'C00004', 'C00005'],
        'compoundname': ['Phenol', 'Toluene', 'Benzene', 'Xylene', 'Naphthalene'],
        'toxicity': ['High', 'Medium', 'Low', 'Medium', 'High'],
        'LD50': [56.0, 636.0, 2100.0, 500.0, 200.0],
        'label_NR_AhR': [
            'High Safety',
            'Medium Safety',
            'Low Safety',
            'Medium Safety',
            'High Safety'
        ]
    }
    return pd.DataFrame(data)


@pytest.fixture
def get_mock_BioRemPP():
    """
    Provides a mock BioRemPP database DataFrame for testing.

    Returns
    -------
    pd.DataFrame
        DataFrame containing sample, KO, enzyme description, compound, and enzyme activity columns,
        simulating the structure of the BioRemPP database.
    """
    data = {
        'sample': ['Sample1', 'Sample1', 'Sample2', 'Sample2', 'Sample3'],
        'ko': ['K00001', 'K00002', 'K00003', 'K00004', 'K00005'],
        'desc': [
            'dehydrogenase',
            'oxidoreductase',
            'hydrolase',
            'lyase',
            'transferase'
        ],
        'compound': ['Lead', 'Toluene', 'Benzene', 'Phenol', 'Xylene'],
        'enzyme_activity': [
            'dehydrogenase',
            'oxidoreductase',
            'hydrolase',
            'lyase',
            'transferase'
        ]
    }
    return pd.DataFrame(data)


@pytest.fixture
def get_mock_KEGG():
    """
    Provides a mock KEGG database DataFrame for testing.

    Returns
    -------
    pd.DataFrame
        DataFrame containing sample, KO, pathway name, and gene symbol columns,
        simulating the structure of the KEGG database.
    """
    data = {
        'sample': ['Sample1', 'Sample1', 'Sample2', 'Sample2', 'Sample3'],
        'ko': ['K00001', 'K00002', 'K00003', 'K00004', 'K00005'],
        'pathname': [
            'Toluene degradation',
            'Xylene degradation',
            'Benzene degradation',
            'Phenol degradation',
            'Naphthalene degradation'
        ],
        'genesymbol': [
            'E1.1.1.1',
            'AKR1A1',
            'CYP2E1',
            'PHN1',
            'NDO'
        ]
    }
    return pd.DataFrame(data)
