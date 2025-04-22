#!/bin/bash

# Criação da estrutura de diretórios
mkdir -p benchmarking/{config,data,reports,utils}

# Criação de arquivos __init__.py
touch benchmarking/__init__.py
touch benchmarking/config/__init__.py
touch benchmarking/utils/__init__.py

# Arquivos de configuração e scripts principais
touch benchmarking/config/test_settings.py
touch benchmarking/summarize_banks.py
touch benchmarking/benchmark_processor.py
touch benchmarking/plot_results.py

# Arquivos de dados (placeholders)
touch benchmarking/data/database.csv
touch benchmarking/data/kegg_20degradation_pathways.csv
touch benchmarking/data/database_toxcsm.csv
touch benchmarking/data/example_input_50samples.txt

# Arquivos de relatórios (vazios, serão preenchidos depois)
touch benchmarking/reports/dtype_summary.csv
touch benchmarking/reports/time_logs.csv

# Utilitários
touch benchmarking/utils/log_utils.py
touch benchmarking/utils/dtype_utils.py

echo "✅ Estrutura de benchmark criada com sucesso em 'tests/benchmarking/'"
