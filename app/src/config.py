import yaml
import os
from pathlib import Path

# Directorio raíz
ROOT = Path(__file__).parent.parent.parent
# carga del archivo de configuración
config = yaml.safe_load(open(os.path.join(ROOT,"config.yaml")))

# =======================================================================================================
# ENTORNO
# =======================================================================================================
_ENV_LOCAL = 'LOCAL'
_ENV_DEV = 'DEV'
_ENV_PROD = 'PROD'

ENV = config.get("ENV", _ENV_LOCAL)

# Define environment constants
ENV_LOCAL = ENV == _ENV_LOCAL 
ENV_DEV = ENV == _ENV_DEV
ENV_PROD = ENV == _ENV_PROD

DEBUG_SERVER = config.get("DEBUG", True)

PORT =  config.get("PORT", 8050)

# =======================================================================================================
# DATASOURCE
# =======================================================================================================
DATA_CONFIG = config.get("DATA")
# Definir la ruta del archivo CSV
DATA_FILE_PATH = os.path.join(ROOT,DATA_CONFIG.get("DATA_PATH"),DATA_CONFIG.get("DATA_FILENAME"))

# =======================================================================================================
# CONFIGURACIÓN MODELO
# =======================================================================================================
MODEL_CONFIG = config.get("MODEL")
PREPROCESS_PATH = os.path.join(ROOT,MODEL_CONFIG.get('MODEL_PATH'),MODEL_CONFIG.get('PREPROC_FILENAME'))
MODEL_PATH= os.path.join(ROOT,MODEL_CONFIG.get('MODEL_PATH'),MODEL_CONFIG.get('MODEL_FILENAME'))
MODEL_THRESHOLD = MODEL_CONFIG.get('THRESHOLD')
