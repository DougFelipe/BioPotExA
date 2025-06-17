"""
components.pages 
========================
Factory functions that build every page layout presented in the **BioRemPP** Dash web
application.  Importing the package will expose a convenient set of helpers so that a
layout can be obtained with a single call, without the need to remember the underlying
file where it lives.

Each sub‑module owns the visual composition of one page and exposes exactly **one or
more** public callables; these are highlighted below together with the file in which
they live.

Sub‑modules & public callables
------------------------------
* **about.py**
  * ``get_about_layout`` – returns the *About* page layout.
* **bioremediation.py**
  * ``get_bioremediation_layout`` – returns the *Bioremediation* information page.
* **contact.py**
  * ``get_contact_page`` – returns the *Contact* page.
* **data_analysis.py**
  * ``get_dataAnalysis_page`` – full *Data Analysis* page with internal state.
  * ``get_dataAnalysis_layout`` – thin wrapper around :pyfunc:`get_dataAnalysis_page` for
    reuse inside other pages (e.g. *About*).
* **documentation.py**
  * ``get_features_layout`` – returns the *Documentation / Features* page.
* **help.py**
  * ``get_help_layout`` – returns the *Help & Support* page.
* **publications.py**
  * ``get_publications_layout`` – returns the *Previous Publications* page.
* **regulatory_agencies.py**
  * ``get_regulatory_agencies_layout`` – returns the *Regulatory Agencies* page.
* **results.py**
  * ``get_results_layout`` – returns the main *Results* dashboard.

Re‑exports
~~~~~~~~~~
All the callables listed above are re‑exported at the package level so they can be
imported directly::

    from components.pages import get_results_layout, get_help_layout

"""

from __future__ import annotations

# Public factory functions – import order is irrelevant but grouped for readability.
from .about import get_about_layout
from .bioremediation import get_bioremediation_layout
from .contact import get_contact_page
from .data_analysis import get_dataAnalysis_page, get_dataAnalysis_layout
from .documentation import get_features_layout
from .help import get_help_layout
from .publications import get_publications_layout
from .regulatory_agencies import get_regulatory_agencies_layout
from .results import get_results_layout

__all__ = [
    # about.py
    "get_about_layout",
    # bioremediation.py
    "get_bioremediation_layout",
    # contact.py
    "get_contact_page",
    # data_analysis.py
    "get_dataAnalysis_page",
    "get_dataAnalysis_layout",
    # documentation.py
    "get_features_layout",
    # help.py
    "get_help_layout",
    # publications.py
    "get_publications_layout",
    # regulatory_agencies.py
    "get_regulatory_agencies_layout",
    # results.py
    "get_results_layout",
]
