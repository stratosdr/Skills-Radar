# Skills Radar

Skills Radar is a full-stack data project that scrapes Dutch tech job listings, cleans and analyzes job descriptions, and exposes predictions and skill insights via a FastAPI backend and (soon) a Streamlit dashboard.

## Features

- Scrapes job listings using the Adzuna API
- Cleans and processes job descriptions
- Predicts job categories using a trained model
- Extracts relevant technical skills using keyword matching
- Provides API endpoints via FastAPI
- Streamlit dashboard planned for interactive data exploration

## Project Structure

```
skills-radar/
├── api/              # FastAPI app (prediction & skill extraction)
├── dashboard/        # Streamlit frontend (in progress)
├── etl/              # Data scraping and cleaning scripts
├── models/           # Trained model and vectorizer files (.pkl)
├── data/             # Raw and cleaned data files
├── utils/            # Shared utility functions
├── requirements.txt  # Dependencies
└── README.md
```

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/skills-radar.git
   cd skills-radar
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the FastAPI server:

   ```bash
   uvicorn api.app:app --reload
   ```

5. Visit the docs in your browser:
   ```
   http://localhost:8000/docs
   ```

## Running the Servers

To conveniently start both the FastAPI backend and Streamlit dashboard servers on Windows, run the provided Python script:

python start_servers.py

## API Endpoints

### POST /predict

Predicts the job category from a job description.

**Request body:**

```json
{
  "text": "Looking for a backend developer with Python and Django experience."
}
```

**Response:**

```json
{
  "category": "Software Engineering"
}
```

### POST /skills?top_n=5

Extracts the top N skills from a job description.

**Request body:**

```json
{
  "text": "We are hiring a Python developer with experience in Docker, SQL, and REST APIs."
}
```

**Response:**

```json
{
  "skills": ["python", "docker", "sql", "rest", "apis"]
}
```

## Requirements

- Python 3.9 or newer
- See `requirements.txt` for package dependencies

## Next Steps

- Build and deploy the Streamlit dashboard
- Visualize skill frequency trends across roles
- Expand skill detection using NLP or vector similarity
- Add Docker support for easier deployment

## License

MIT License. Contributions welcome.
