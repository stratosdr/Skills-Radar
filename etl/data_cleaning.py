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


def clean_job_data(input_path='skills-radar/data/jobs_raw.csv', output_path='skills-radar/data/jobs_clean.csv'):
    if not os.path.exists(input_path):
        print(f"❌ Input file not found: {input_path}")
        return

    df = pd.read_csv(input_path)
    print(f"📄 Loaded {len(df)} rows")

    df['clean_description'] = df['description'].apply(clean_text)
    df.to_csv(output_path, index=False)
    print(f"✅ Cleaned data saved to: {output_path}")

if __name__ == '__main__':
    clean_job_data()
