import pandas as pd
import re
import string
import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# # Only needed once (downloads the stopwords + tokenizer)
# nltk.download('punkt')
# nltk.download('stopwords')

def clean_text(text):
    if pd.isnull(text):
        return ""
    text = re.sub('<.*?>', '', text)  # remove HTML
    text = re.sub(r"http\S+", "", text)  # remove URLs
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()  # 🔁 changed: no tokenizers
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if w.isalpha() and w not in stop_words]
    return " ".join(words)


def clean_job_data(input_path='data/jobs_raw.csv', output_path='data/jobs_clean.csv'):
    if not os.path.exists(input_path):
        print(f"❌ Input file not found: {input_path}")
        return

    df = pd.read_csv(input_path)
    print(f"📄 Loaded {len(df)} rows")

    # Define allowed categories (updated to match actual data)
    allowed_categories = [
        'Data Engineer',
        'Machine Learning', 
        'Backend Developer',
        'DevOps',
        'Data Analyst',
        'Software Engineer',
        'Cloud Engineer',
        'Junior Developer'
    ]

    # Filter rows based on category (keep all tech-related jobs)
    df = df[df['category'].isin(allowed_categories)]

    df['clean_description'] = df['description'].apply(clean_text)
    df.to_csv(output_path, index=False)
    print(f"✅ Cleaned & filtered data saved to: {output_path}")


if __name__ == '__main__':
    clean_job_data()
