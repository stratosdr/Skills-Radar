import requests
import pandas as pd
import os
import time

APP_ID = '766a9759'
APP_KEY = 'faecdb76cec2a34b4caa649f5760c350'

job_sets = [
    ('data engineer', 'Data Engineer'),
    ('machine learning', 'Machine Learning'),
    ('backend developer', 'Backend Developer'),
    ('devops', 'DevOps'),
    ('data analyst', 'Data Analyst'),
    ('software engineer', 'Software Engineer'),
    ('cloud engineer', 'Cloud Engineer'),
    ('junior developer', 'Junior Developer'),
]

def fetch_jobs(keyword, label, location='netherlands', results=30):
    url = 'https://api.adzuna.com/v1/api/jobs/nl/search/1'
    params = {
        'app_id': APP_ID,
        'app_key': APP_KEY,
        'what': keyword,
        'where': location,
        'results_per_page': results,
        'content-type': 'application/json'
    }

    print(f"🔍 Fetching '{label}' jobs for keyword: {keyword}")
    response = requests.get(url, params=params)
    print("📡 STATUS CODE:", response.status_code)

    if response.status_code != 200:
        print("❌ Failed to fetch data for:", keyword)
        return []

    data = response.json()
    results = data.get('results', [])
    print("📦 RESULTS:", len(results))

    jobs = []
    for job in results:
        jobs.append({
            'title': job.get('title'),
            'company': job.get('company', {}).get('display_name'),
            'location': job.get('location', {}).get('display_name'),
            'description': job.get('description'),
            'created': job.get('created'),
            'category': label
        })

    return jobs

def main():
    all_jobs = []
    for keyword, label in job_sets:
        jobs = fetch_jobs(keyword, label)
        all_jobs.extend(jobs)
        time.sleep(1)  # small delay between calls (avoid rate-limiting)

    if all_jobs:
        os.makedirs('data', exist_ok=True)
        df = pd.DataFrame(all_jobs)
        df.to_csv('data/jobs_raw.csv', index=False)
        print(f"✅ Saved {len(df)} jobs to data/jobs_raw.csv.")
    else:
        print("⚠️ No jobs were saved.")

if __name__ == '__main__':
    main()