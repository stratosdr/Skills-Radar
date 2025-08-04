from typing import List
import numpy as np
import re

# Sample known skills list (can be expanded or replaced with a file/database)
KNOWN_SKILLS = {
    "python", "java", "c++", "c#", "javascript", "html", "css",
    "sql", "mysql", "postgresql", "mongodb",
    "pandas", "numpy", "scikit-learn", "tensorflow", "keras", "matplotlib",
    "fastapi", "flask", "django",
    "git", "docker", "kubernetes", "linux", "aws", "azure", "gcp",
    "react", "vue", "angular", "node.js",
    "spark", "hadoop", "airflow", "bash", "rest", "graphql",
    "machine learning", "deep learning", "data analysis", "etl"
}

def get_top_skills(text: str, vectorizer=None, top_n: int = 10):
    """
    Extracts up to `top_n` relevant known skills from the input text.
    """
    text = text.lower()
    matches = set()

    for skill in KNOWN_SKILLS:
        # Use regex to catch whole word/phrase matches
        if re.search(rf'\b{re.escape(skill)}\b', text):
            matches.add(skill)

    return sorted(matches)[:top_n]