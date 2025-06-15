import sys
import os

from utils.intersections_and_groups.clustering_dendrogram_processing import calculate_sample_clustering

# Adiciona o diretório raiz ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import cProfile
import pstats
import pandas as pd
import plotly.express as px

from utils.core.data_processing import (
    merge_input_with_database,
    merge_with_kegg,
    merge_with_toxcsm,
    process_ko_data,
    count_ko_per_pathway,
    count_ko_per_sample_for_pathway,
    process_sample_ranking,
    process_compound_ranking,
    process_compound_gene_ranking,
    process_gene_compound_association,
    process_gene_sample_association,
    process_sample_reference_heatmap,   
    process_gene_sample_data,
    process_pathway_data,
    get_ko_per_sample_for_pathway,
    count_unique_enzyme_activities,
    prepare_upsetplot_data
)


from utils.intersections_and_groups.sample_grouping_by_compound_class_processing import group_by_class, minimize_groups

from utils.core.data_validator import validate_and_process_input

output_img = "output_plot.png"

def teste_local():
    print("[INFO] Iniciando simulação de ciclo completo com profiling...")

    input_path = os.path.join("..", "data", "genomasBD.txt")
    filename = "genomasBD.txt"

    if not os.path.exists(input_path):
        print(f"[ERRO] Arquivo de input não encontrado em: {os.path.abspath(input_path)}")
        return

    with open(input_path, 'r', encoding='utf-8') as file:
        contents = file.read()

    input_data, error = validate_and_process_input(contents, filename)
    if error:
        print(f"[ERRO] Falha na validação do arquivo: {error}")
        return
    print("[INFO] Dados carregados com sucesso!")

    db_path = os.path.join("..", "data", "database.csv")
    kegg_path = os.path.join("..", "data", "kegg_degradation_pathways.xlsx")
    tox_path = os.path.join("..", "data", "database_toxcsm.xlsx")

    print("[INFO] Mesclando com database.csv...")
    merged_1 = merge_input_with_database(input_data, database_filepath=db_path)

    print("[INFO] Mesclando com kegg_degradation_pathways.xlsx...")
    merged_2 = merge_with_kegg(merged_1, kegg_path=kegg_path)

    print("[INFO] Mesclando com database_toxcsm.xlsx...")
    merged_3 = merge_with_toxcsm(merged_2, toxcsm_filepath=tox_path)

    print("[INFO] Processando KOs por sample...")
    processed = process_ko_data(merged_3)

    print(f"[INFO] Gerando gráfico e salvando em '{output_img}'...")
    fig = px.bar(processed, x='sample', y='ko_count')
    fig.write_image(output_img)

    print("[INFO] Executando análises complementares de agrupamento...")

    count_ko_per_pathway(merged_2)
    count_ko_per_sample_for_pathway(merged_2, "Hydrocarbon degradation")d
    process_sample_ranking(merged_3)
    process_compound_ranking(merged_3)

    # GENE ANALYSIS
    if 'genesymbol' in merged_3.columns:
        process_compound_gene_ranking(merged_3)
        process_gene_compound_association(merged_3)
        process_gene_sample_association(merged_3)
    else:
        print("[AVISO] Coluna 'genesymbol' não encontrada. Pulando análises de gene.")

    # HEATMAP
    if 'referenceAG' in merged_3.columns:
        process_sample_reference_heatmap(merged_3)
    else:
        print("[AVISO] Coluna 'referenceAG' não encontrada. Pulando heatmap.")

    # AGRUPAMENTO POR CLASSES
    if 'compoundclass' in merged_3.columns:
        tabela_grupos = group_by_class("Hydrocarbon", merged_3)
        minimize_groups(tabela_grupos)
    else:
        print("[AVISO] Coluna 'compoundclass' não encontrada. Pulando agrupamento por classe.")

    # GENE + PATHWAY COUNT
    if all(col in merged_3.columns for col in ['sample', 'Gene', 'compound_pathway', 'Pathway']):
        process_gene_sample_data(merged_3)
    else:
        print("[AVISO] Colunas para 'process_gene_sample_data' ausentes.")

    # PATHWAY COUNT
    if all(col in merged_3.columns for col in ['Pathway', 'compound_pathway', 'sample']):
        process_pathway_data(merged_3)
    else:
        print("[AVISO] Colunas para 'process_pathway_data' ausentes.")

    # GET KO POR PATHWAY
    if 'pathname' in merged_3.columns:
        get_ko_per_sample_for_pathway(merged_3, "Hydrocarbon degradation")
    else:
        print("[AVISO] Coluna 'pathname' não encontrada. Pulando get_ko_per_sample_for_pathway.")

    # ENZIMAS
    if all(col in merged_3.columns for col in ['sample', 'enzyme_activity']):
        sample = merged_3['sample'].iloc[0]
        count_unique_enzyme_activities(merged_3, sample)
    else:
        print("[AVISO] Colunas para 'count_unique_enzyme_activities' ausentes.")

    # CLUSTERING + UPSETPLOT
    if all(col in merged_3.columns for col in ['sample', 'ko']):
        calculate_sample_clustering(merged_3, distance_metric="euclidean", method="ward")
        prepare_upsetplot_data(merged_3, merged_3['sample'].unique().tolist())
    else:
        print("[AVISO] Colunas para clustering ou upsetplot ausentes.")

# Execução com profiling
if __name__ == '__main__':
    print("[INFO] Executando profiling com cProfile...")

    profile_file = "saida_profile.prof"
    profile_txt = "saida_profile.txt"

    cProfile.run('teste_local()', profile_file)

    with open(profile_txt, "w") as f:
        stats = pstats.Stats(profile_file, stream=f)
        stats.strip_dirs().sort_stats("cumtime").print_stats(30)

    print(f"[INFO] Profiling finalizado com sucesso!")
    print(f"       > Arquivo de perfil: {profile_file}")
    print(f"       > Estatísticas salvas em: {profile_txt}")
    print(f"       > Gráfico exportado para: {os.path.abspath(output_img)}")
