import requests
import pandas as pd
import os

APP_ID = '766a9759'
APP_KEY = 'faecdb76cec2a34b4caa649f5760c350'

def fetch_jobs(keyword='data engineer', location='netherlands', results=50):
    url = 'https://api.adzuna.com/v1/api/jobs/nl/search/1'
    params = {
        'app_id': APP_ID,
        'app_key': APP_KEY,
        'what': keyword,
        'where': location,
        'results_per_page': results,
        'content-type': 'application/json'
    }

    print(f"🔍 Sending request to Adzuna...")
    response = requests.get(url, params=params)
    print("📡 STATUS CODE:", response.status_code)

    if response.status_code != 200:
        print("❌ Failed to fetch data. Check your API key or parameters.")
        return

    data = response.json()
    results = data.get('results', [])
    print("📦 TOTAL RESULTS:", len(results))

    if not results:
        print("⚠️ No jobs returned. Try different keyword/location.")
        return

    jobs = []
    for job in results:
        jobs.append({
            'title': job.get('title'),
            'company': job.get('company', {}).get('display_name'),
            'location': job.get('location', {}).get('display_name'),
            'description': job.get('description'),
            'category': job.get('category', {}).get('label'),
            'created': job.get('created')
        })

    os.makedirs('data', exist_ok=True)
    df = pd.DataFrame(jobs)
    df.to_csv('data/jobs_raw.csv', index=False)
    print(f"✅ Fetched and saved {len(df)} job listings to data/jobs_raw.csv.")

if __name__ == '__main__':
    fetch_jobs(keyword='data engineer')