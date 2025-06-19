components package
==================

Pacote de componentes visuais reutilizáveis do BioPotExA.
Este pacote expõe todos os componentes de interface gráfica (UI) necessários para a construção das páginas e funcionalidades do sistema.

Componentes disponíveis incluem alertas, botões, barras de navegação, divisores visuais, filtros e outros widgets, todos implementados no subpacote ``components.ui`` e expostos diretamente pelo pacote ``components``.

Documentação dos componentes
----------------------------

.. automodule:: components
   :members:
   :show-inheritance:
   :undoc-members:

Subpacotes
----------

.. toctree::
   :maxdepth: 2

   components.pages

Notas
-----

Os componentes individuais não são módulos diretos de ``components``, mas sim do subpacote ``components.ui``.
Eles são expostos explicitamente pelo ``__init__.py`` de ``components`` para uso facilitado em toda a aplicação.

Para informações detalhadas sobre cada componente, consulte o código-fonte em ``components/ui``.
