import os
import sys

# Adiciona a raiz do projeto ao path
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
project = 'BioPotExA'
copyright = '2024, Douglas Felipe'
author = 'Douglas Felipe'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',        # Suporte Google/Numpy docstrings
    'sphinx_autodoc_typehints',   # Tipagem nos docs automáticos
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
