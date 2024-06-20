# Projeto de BioPExA

## Visão Geral
Este projeto representa uma aplicação Dash Plotly, projetada para a exploração interativa e a análise de conjuntos de dados de identificadores do Kegg Orthology (KO) para investigação do potencial de biorremediação. Através de uma interface responsiva e interativa, os usuários podem carregar dados para analisar e explorar vias metabólicas, identificar genes-chave, elaborar consórcios de espécies para biorremediação, realizar análises de clusterização e executar análises detalhadas dos dados.

BioPExA se destaca pela sua capacidade de permitir que os pesquisadores visualizem diversos parâmetros importantes em uma série de formatos interativos, incluindo gráficos dinâmicos, tabelas ajustáveis e diversas representações gráficas. 

A aplicação foi desenhada para suportar a expansão e integração de novos módulos e recursos, o que permite a inclusão contínua de novas técnicas de análise de dados e visualizações personalizadas. Com uma arquitetura modular e extensível, a aplicação está preparada para adaptar junto com os avanços na pesquisa sobre biorremediação.

## Estrutura e Arquitetura do Projeto
## Diretórios e Arquivos Principais

```plaintext
├───assets
│   ├───custom.js
│   ├───style.css
│   └───images
│       ├───SDG06.png
│       ├───SDG13.png
│       ├───SDG14.png
│       └───SDG15.png
│
├───callbacks
│   ├───callbacks.py
│   ├───P1_COUNT_KO_callbacks.py
│   ├───P2_KO_20PATHWAY_callbacks.py
│   ├───P3_compounds_callbacks.py
│   └───P4_rank_compounds_callbacks.py
│
├───components
│   ├───about_features_list.py
│   ├───features_list.py
│   ├───footer.py
│   ├───header.py
│   └───step_guide.py
│
├───data
│   ├───database.xlsx
│   ├───fasta_like_format.csv
│   ├───genomasBD.txt
│   ├───genomasBD_teste.txt
│   ├───kegg_20degradation_pathways.xlsx
│   ├───sample1.txt
│   ├───sample2.txt
│   ├───sample_teste.txt
│   └───teste.txt
│
├───Documentation
│   ├───callbacks.md
│   ├───data_analysis.md
│   ├───data_processing.md
│   ├───data_validator.md
│   ├───index.md
│   └───style.md
│
├───layouts
│   ├───about.py
│   ├───data_analysis.py
│   ├───LAYOUT_TEMPLATE.py
│   ├───P1_KO_COUNT.py
│   ├───P2_KO_20PATHWAY.py
│   ├───P3_compounds_layout.py
│   ├───P4_rank_compounds_layout.py
│   ├───results.py
│   ├───tempCodeRunnerFile.py
│   └───__init__.py
│
├───models
│   └───.gitkeep
│
├───services
│   └───database_service.py
│
├───tests
│   ├───test_callbacks.py
│   └───test_data_loader.py
│
├───utils
│   ├───backup_modificacoes.md
│   ├───components.py
│   ├───data_loader.py
│   ├───data_processing.py
│   ├───data_validator.py
│   ├───filters.py
│   ├───plot_processing.py
│   └───table_utils.py
│
├───.env
├───.gitignore
├───app.py
├───index.py
├───README.md
├───requirements.txt
└───server.py
```


## Descrição dos Diretórios

### assets
Contém arquivos de recursos como JavaScript, CSS e imagens.
- **custom.js**: Arquivo JavaScript personalizado.
- **style.css**: Arquivo de estilo CSS.
- **images**: Contém imagens utilizadas no projeto.

### callbacks
Inclui todos os callbacks do Dash, separados por funcionalidade.
- **callbacks.py**: Callback principal do Dash.
- **P1_COUNT_KO_callbacks.py**: Callbacks para contagem de KOs.
- **P2_KO_20PATHWAY_callbacks.py**: Callbacks para análise de vias de KO.
- **P3_compounds_callbacks.py**: Callbacks para visualização de compostos.
- **P4_rank_compounds_callbacks.py**: Callbacks para ranking de compostos.

### components
Contém componentes reutilizáveis do Dash.
- **about_features_list.py**: Lista de recursos da seção "About".
- **features_list.py**: Lista de recursos.
- **footer.py**: Rodapé do aplicativo.
- **header.py**: Cabeçalho do aplicativo.
- **step_guide.py**: Guia de passos para o usuário.

### data
Armazena arquivos de dados para processamento e análise.
- **database.xlsx**: Banco de dados principal.
- **fasta_like_format.csv**: Arquivo de dados em formato FASTA-like.
- **genomasBD.txt**: Dados de genomas.
- **genomasBD_teste.txt**: Dados de genomas para teste.
- **kegg_20degradation_pathways.xlsx**: Dados de vias de degradação do KEGG.
- **sample1.txt**: Dados da amostra 1.
- **sample2.txt**: Dados da amostra 2.
- **sample_teste.txt**: Dados de amostra para teste.
- **teste.txt**: Arquivo de teste.

### Documentation
Documentação detalhada do projeto.
- **callbacks.md**: Documentação dos callbacks.
- **data_analysis.md**: Documentação da análise de dados.
- **data_processing.md**: Documentação do processamento de dados.
- **data_validator.md**: Documentação do validador de dados.
- **index.md**: Documentação do arquivo index.
- **style.md**: Documentação de estilos.

### layouts
Define a estrutura e o layout das diferentes seções do aplicativo.
- **about.py**: Layout da seção "About".
- **data_analysis.py**: Layout da análise de dados.
- **LAYOUT_TEMPLATE.py**: Template de layout.
- **P1_KO_COUNT.py**: Layout para contagem de KOs.
- **P2_KO_20PATHWAY.py**: Layout para análise de vias de KO.
- **P3_compounds_layout.py**: Layout para visualização de compostos.
- **P4_rank_compounds_layout.py**: Layout para ranking de compostos.
- **results.py**: Layout de resultados.
- **tempCodeRunnerFile.py**: Arquivo temporário.
- **__init__.py**: Inicializador do pacote.

### models
Contém modelos utilizados no projeto.
- **.gitkeep**: Arquivo para manter o diretório no controle de versão.

### services
Inclui serviços para operações como banco de dados.
- **database_service.py**: Serviço para operações de banco de dados.

### tests
Armazena scripts de testes para validar o funcionamento do projeto.
- **test_callbacks.py**: Testes para os callbacks.
- **test_data_loader.py**: Testes para o carregador de dados.

### utils
Utilitários e funções auxiliares para o projeto.
- **backup_modificacoes.md**: Backup das modificações.
- **components.py**: Componentes utilitários.
- **data_loader.py**: Carregador de dados.
- **data_processing.py**: Processamento de dados.
- **data_validator.py**: Validador de dados.
- **filters.py**: Filtros de dados.
- **plot_processing.py**: Processamento de plots.
- **table_utils.py**: Utilitários para tabelas.

### Raiz do Projeto
Arquivos principais e de configuração do projeto.
- **.env**: Arquivo de configuração do ambiente.
- **.gitignore**: Arquivo para ignorar arquivos no controle de versão.
- **app.py**: Arquivo principal do aplicativo Dash.
- **index.py**: Arquivo de indexação do projeto.
- **README.md**: Documentação principal do projeto.
- **requirements.txt**: Dependências do projeto.
- **server.py**: Arquivo de inicialização do servidor.

## Diagrama de Estrutura de Dados

```plaintext
[Input Data]
    |
    v
[Data Processing] 
    |
    v
[Database]
    |
    v
[Dash Callbacks] 
    |
    v
[Dash Layouts] 
    |
    v
[Dash Application]
```

## Descrição dos Principais Arquivos

### .env
Arquivo de configuração do ambiente contendo variáveis de configuração sensíveis.

### .gitignore
Arquivo para ignorar arquivos no controle de versão, como arquivos de configuração sensíveis e diretórios de build.

### app.py
Arquivo principal do aplicativo Dash, onde o servidor é inicializado e configurado.

### index.py
Arquivo de indexação do projeto, configurando o layout principal e incluindo os callbacks.

### README.md
Documentação principal do projeto, fornecendo uma visão geral, instruções de instalação e uso.

### requirements.txt
Lista de dependências do projeto, necessárias para instalar todas as bibliotecas e pacotes Python utilizados.

### server.py
Arquivo de inicialização do servidor, configurando e executando o servidor Flask para o aplicativo Dash.


## Uso da Ferramenta

A aplicação oferece um ambiente para análise de dados com as seguintes funcionalidades:

- **Carregamento de Dados**: Os usuários podem facilmente carregar seus conjuntos de dados para análise imediata.
- **Visualização Interativa**: Dados podem ser explorados através de gráficos interativos e tabelas dinâmicas.
- **Análise de Consórcios**: Avalie e projete consórcios microbianos para aplicações específicas de biorremediação.
- **Contagem de Genes e Clusterização**: Realize análises para compreender a distribuição e a correlação entre diferentes genes e amostras.
- **Expansão Contínua**: A plataforma está pronta para incorporar novas funcionalidades e módulos de análise conforme eles são desenvolvidos.

A interatividade da aplicação permite aos usuários não apenas visualizar dados complexos de forma intuitiva, mas também manipulá-los e analisá-los em tempo real, proporcionando um ambiente para a exploração de dados.


## Contribuições

Contribuições são bem-vindas! Por favor, leia o `CONTRIBUTING.md` para saber como você pode contribuir para o desenvolvimento deste projeto.

## Licença

Este projeto está sob a licença All Rights Reserved . Veja o arquivo `LICENSE` para mais detalhes.

## Contato

Para suporte ou para entrar em contato com os desenvolvedores, envie um e-mail para [email](dougbiomed@gmail.com).
