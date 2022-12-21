from joblib import dump, load
from .config import PREPROCESS_PATH,MODEL_PATH, MODEL_THRESHOLD
import numpy as np

# Carga del pipeline de preprocesado de datos
pipe = load(PREPROCESS_PATH)
# Carga del modelo
model = load(MODEL_PATH)

# Preprocesado de datos
def preprocess(x):
    return pipe.transform(x)

# Predicción del modelo
def predict(x):
    x = preprocess(x)
    clf_probs = model.predict_proba(x)[:,1]
    y_pred = clf_probs >= MODEL_THRESHOLD
    return y_pred



