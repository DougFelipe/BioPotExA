import os
import re
import time
import pandas as pd

# Diretórios e arquivos
BASE_DIR = os.path.abspath(os.path.join(os.getcwd(), "../../"))
DATA_FILE = os.path.join(BASE_DIR, "data", "genomasBD.txt")
DATABASE_PATHS = {
    "BioRemPP": os.path.join(BASE_DIR, "data", "database.csv"),
    "KEGG": os.path.join(BASE_DIR, "data", "kegg_degradation_pathways.csv"),
    "HADEG": os.path.join(BASE_DIR, "data", "database_hadegDB.csv"),
    "ToxCSM": os.path.join(BASE_DIR, "data", "database_toxcsm.csv"),
}

# Otimização de tipos com Categorical
def optimize_dtypes(df):
    for col in ['ko', 'genesymbol', 'genename', 'cpd', 'compoundclass', 'referenceAG', 'compoundname', 'enzyme_activity']:
        if col in df.columns:
            df[col] = df[col].astype("category")
    return df

# Função para leitura e merge com medição de tempo
def timed_merge(input_df, db_path, db_name, on_col="ko", use_category=False):
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {db_path}")
    df = pd.read_csv(db_path, sep=";", encoding="utf-8")
    if use_category:
        df = optimize_dtypes(df)
    if on_col not in df.columns:
        raise KeyError(f"Coluna '{on_col}' ausente no banco de dados {os.path.basename(db_path)}.")
    t0 = time.time()
    merged_df = pd.merge(input_df, df, on=on_col, how="inner")
    t1 = time.time()
    elapsed = t1 - t0
    print(f"⏱️ Tempo {db_name}: {elapsed:.4f} segundos")
    print(f"📏 Linhas após {db_name}: {len(merged_df)}")
    return merged_df

# Leitura do input a partir do .txt
def process_content_lines(content: str):
    lines = content.split('\n')
    identifier_pattern = re.compile(r'^>([^\n]+)')
    data_pattern = re.compile(r'^(K\d+)')
    data = []
    current_identifier = None
    for line in lines:
        if identifier_match := identifier_pattern.match(line):
            current_identifier = identifier_match.group(1).strip()
        elif data_match := data_pattern.match(line):
            if current_identifier:
                data.append({'sample': current_identifier, 'ko': data_match.group(1).strip()})
        elif line.strip() != '':
            return None, f"Linha inválida detectada: {line}"
    if not data:
        return None, "Nenhum dado válido encontrado."
    return pd.DataFrame(data), None

# Função principal de benchmark completo
def benchmark_full_merge(use_category=False):
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    df_input, error = process_content_lines(content)
    if error:
        print(f"Erro: {error}")
        return

    print(f"\n🔧 Benchmark {'com' if use_category else 'sem'} uso de category")

    # Merge com BioRemPP
    merged = timed_merge(df_input, DATABASE_PATHS["BioRemPP"], "BioRemPP", use_category=use_category)

    # Merge com KEGG
    merged = timed_merge(merged, DATABASE_PATHS["KEGG"], "KEGG", on_col="ko", use_category=use_category)

    # Merge com HADEG
    merged = timed_merge(merged, DATABASE_PATHS["HADEG"], "HADEG", on_col="ko", use_category=use_category)

    # Merge com ToxCSM
    if all(col in merged.columns for col in ["sample", "compoundclass", "cpd", "ko"]):
        tox_df = pd.read_csv(DATABASE_PATHS["ToxCSM"], sep=";", encoding="utf-8")
        if use_category:
            tox_df = optimize_dtypes(tox_df)
        subset = merged[['sample', 'compoundclass', 'cpd', 'ko']].drop_duplicates()
        t0 = time.time()
        merged = pd.merge(subset, tox_df, on="cpd", how="inner")
        t1 = time.time()
        print(f"⏱️ Tempo ToxCSM: {t1 - t0:.4f} segundos")
        print(f"📏 Linhas após ToxCSM: {len(merged)}")
    else:
        print("⚠️ Colunas necessárias para merge com ToxCSM não encontradas.")

    print(f"\n✅ Resultado final: {len(merged)} linhas.")

# Executar benchmarks
benchmark_full_merge(use_category=False)
benchmark_full_merge(use_category=True)
