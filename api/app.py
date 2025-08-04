from fastapi import FastAPI
from pydantic import BaseModel
from .model_loader import load_model
from .utils import get_top_skills


# Create FastAPI instance
app = FastAPI()

# Define request schema
class JobDescription(BaseModel):
    text: str

# Load model and vectorizer
model, vectorizer = load_model()

# Define prediction endpoint
@app.post("/predict")
def predict_category(input: JobDescription):
    features = vectorizer.transform([input.text])
    prediction = model.predict(features)[0]
    return {"category": prediction}

@app.post("/skills")
def extract_skills(input: JobDescription, top_n: int = 5):
    skills = get_top_skills(input.text, vectorizer, top_n)
    return {"top_skills": skills}


@app.get("/")
def read_root():
    return {"message": "Welcome to the Job Category Prediction API"}