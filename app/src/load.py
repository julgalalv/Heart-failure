from . import config as cfg
import pandas as pd

# Carga del archivo de datos
def load_csv_as_df(filepath = cfg.DATA_FILE_PATH):
 return pd.read_csv(filepath)

# Procesado de datos para la vista de usuario
def load_csv_as_df_refactor(filepath = cfg.DATA_FILE_PATH):
    df = load_csv_as_df(filepath)
    reorder = [
        'age',
        'sex',
        'smoking',
        'anaemia',
        'diabetes',
        'high_blood_pressure',
        'creatinine_phosphokinase',
        'ejection_fraction',
        'platelets',
        'serum_creatinine',
        'serum_sodium',
        'time',
        'DEATH_EVENT'
    ]   
    df = df[reorder]
    # 'age' como int en lugar de float
    df['age'] = df['age'].astype(int)
    # Variables categóricas a literales
    df['sex'] = df['sex'].map({1:'H', 0:'M'})
    for col in ['anaemia','diabetes','high_blood_pressure','smoking','DEATH_EVENT']:
        df[col] =  df[col].map({1:'Sí', 0:'No'})

    return df

# Datos cargados para visualizar en UI
refactored_df = load_csv_as_df_refactor()

