callbacks.py

Este arquivo define os callbacks do Dash que permitem a interatividade da aplicação. Os callbacks são
funções que são acionadas por mudanças nos inputs dos componentes e podem alterar o conteúdo de outros
componentes ou armazenar dados de forma reativa.

Callbacks:
- render_tab_content: Atualiza o conteúdo mostrado com base na aba selecionada pelo usuário.
- update_upload_status: Atualiza o status do botão de processamento e mostra um alerta quando um arquivo é carregado.
- process_file: Processa os dados carregados e retorna visualizações como gráficos e tabelas.
- process_and_store_data: Processa e armazena os dados carregados em dcc.Store.
- update_graphs: Atualiza os gráficos com base nos dados armazenados no dcc.Store.
- toggle_graph_visibility: Alterna a visibilidade dos gráficos com base na aba selecionada.

Cada callback é documentado com informações sobre seus inputs, outputs e a lógica interna.

