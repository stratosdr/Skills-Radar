import joblib
import os

def load_model():
    model_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'skill_classifier.pkl')
    vectorizer_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'vectorizer.pkl')

    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)

    return model, vectorizer
