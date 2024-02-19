# my_dash_app/utils/data_loader.py
import pandas as pd
def load_database(filepath):
    df = pd.read_excel(filepath)
    return df