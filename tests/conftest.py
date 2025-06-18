import pandas as pd
import pytest

@pytest.fixture
def get_mock_HADEG():
    data = {
        'Gene': ['alkB', 'ahpC'],
        'ko': ['K00496', 'K03386'],
        'Pathway': ['Alkane degradation', 'Alkane degradation'],
        'compound_pathway': ['Alkanes', 'Alkanes']
    }
    return pd.DataFrame(data)

@pytest.fixture
def get_mock_ToxCSM():
    data = {
        'cpd': ['C00001', 'C00002'],
        'compoundname': ['Phenol', 'Toluene'],
        'toxicity': ['High', 'Medium'],
        'LD50': [56.0, 636.0],
        'label_NR_AhR': ['High Safety', 'Medium Safety']
    }
    return pd.DataFrame(data)

@pytest.fixture
def get_mock_BioRemPP():
    data = {
        'ko': ['K00001', 'K00002'],
        'desc': ['dehydrogenase', 'oxidoreductase'],
        'compound': ['Lead', 'Toluene'],
        'enzyme_activity': ['dehydrogenase', 'oxidoreductase']
    }
    return pd.DataFrame(data)

@pytest.fixture
def get_mock_KEGG():
    data = {
        'ko': ['K00001', 'K00002'],
        'pathname': ['Toluene degradation', 'Xylene degradation'],
        'genesymbol': ['E1.1.1.1', 'AKR1A1']
    }
    return pd.DataFrame(data)
