index.py

Este arquivo é o ponto de entrada para a aplicação Dash. Ele configura o layout principal do aplicativo
e liga os componentes visuais aos callbacks que definem sua lógica interativa.

Componentes:
- Header: Componente personalizado que exibe o cabeçalho da aplicação.
- dcc.Tabs: Conjunto de abas que permite a navegação entre as diferentes seções da aplicação.
- dcc.Store: Armazenamento de dados no lado do cliente, usado para armazenar dados entre callbacks.
- html.Div: Container para o conteúdo dinâmico que é atualizado com base na aba selecionada.

O servidor é iniciado neste arquivo, tornando-o o script que deve ser executado para iniciar a aplicação Dash.

