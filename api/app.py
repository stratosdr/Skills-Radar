from fastapi import FastAPI
from pydantic import BaseModel
from .model_loader import load_model
from .utils import get_top_skills
from .category_map import CATEGORY_MAP

app = FastAPI()

class JobDescription(BaseModel):
    text: str

model, vectorizer = load_model()

@app.post("/predict")
def predict_category(input: JobDescription):
    raw_pred = model.predict([input.text])[0]  # just pass raw text to pipeline
    clean_pred = CATEGORY_MAP.get(raw_pred, raw_pred)
    return {"category": clean_pred}


@app.post("/skills")
def extract_skills(input: JobDescription, top_n: int = 5):
    skills = get_top_skills(input.text, vectorizer, top_n)
    return {"top_skills": skills}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Job Category Prediction API"}
