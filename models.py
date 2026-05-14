import pickle
import os
from config import SAVED_MODELS_DIR

def load_model(name):
    path = os.path.join(SAVED_MODELS_DIR, name)
    try:
        return pickle.load(open(path, "rb"))
    except:
        return None

diabetes_model = load_model("diabetes.pkl")
heart_model = load_model("heart.pkl")
kidney_model = load_model("kidney.pkl")
