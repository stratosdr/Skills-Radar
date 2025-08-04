import joblib
from pathlib import Path

def load_model():
    model_path = Path("data/model.pkl")
    vectorizer_path = Path("data/vectorizer.pkl")

    if not model_path.exists() or not vectorizer_path.exists():
        raise FileNotFoundError("Model or vectorizer file not found in data/")

    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
    return model, vectorizer
