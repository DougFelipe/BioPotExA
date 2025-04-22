# tests/benchmarking/summarize_banks.py

import os
import pandas as pd
from ydata_profiling import ProfileReport  # substituto do pandas_profiling
from datetime import datetime

# Caminhos corrigidos para os bancos de dados
BANK_PATHS = {
    "BioRemPP": os.path.abspath("data/database.csv"),
    "HADEG": os.path.abspath("data/database_hadegDB.csv"),
    "ToxCSM": os.path.abspath("data/database_toxcsm.csv"),
    "KEGG": os.path.abspath("data/kegg_20degradation_pathways.csv"),
}

# Pasta de saída com o mesmo nome do script
OUTPUT_DIR = os.path.join("tests", "benchmarking", "summarize_banks")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def analyze_and_save_summary(df: pd.DataFrame, name: str):
    print(f"\n📊 Analisando banco: {name}")
    output_path = os.path.join(OUTPUT_DIR, name)
    os.makedirs(output_path, exist_ok=True)

    summary = {
        "n_rows": len(df),
        "n_columns": len(df.columns),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isna().sum().to_dict(),
        "unique_counts": df.nunique().to_dict(),
    }

    # Sugestões para uso de category
    summary["category_suggestions"] = {
        col: df[col].nunique()
        for col in df.select_dtypes(include="object").columns
        if df[col].nunique() / len(df) < 0.2
    }

    # Estatísticas numéricas
    df.describe(include="all").to_csv(os.path.join(output_path, "describe_all.csv"))

    # Frequências de categorias (top 10)
    freq_data = {}
    for col in df.select_dtypes(include=["object", "category"]):
        freq_data[col] = df[col].value_counts().head(10).to_dict()
    pd.DataFrame(freq_data).to_csv(os.path.join(output_path, "categorical_frequencies.csv"))

    # Preview
    df.head(3).to_csv(os.path.join(output_path, "head.csv"), index=False)

    # Pandas Profiling Report
    try:
        profile = ProfileReport(df, title=f"Relatório - {name}", minimal=True)
        profile.to_file(os.path.join(output_path, f"{name}_profile.html"))
    except Exception as e:
        with open(os.path.join(output_path, "profile_error.log"), "w") as f:
            f.write(f"Erro ao gerar relatório com ydata-profiling: {str(e)}")

    # Salva sumário geral
    pd.Series(summary).to_json(os.path.join(output_path, "summary.json"))

def summarize_banks():
    print("🚀 Iniciando leitura e análise dos bancos de dados...\n")
    for bank_name, path in BANK_PATHS.items():
        try:
            df = pd.read_csv(path, sep=";", encoding="utf-8")
            if df.empty:
                raise ValueError("DataFrame vazio.")
            analyze_and_save_summary(df, bank_name)
        except Exception as e:
            print(f"[ERRO] Falha ao processar o banco {bank_name}: {e}")

if __name__ == "__main__":
    summarize_banks()
