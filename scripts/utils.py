import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


analyzer = SentimentIntensityAnalyzer()

def classify_sentiment(text):
    score = analyzer.polarity_scores(str(text))['compound']
    if score >= 0.05:
        return 'positive'
    elif score <= -0.05:
        return 'negative'
    else:
        return 'neutral'

def analyze_sentiments(input_path, output_path):
    df = pd.read_csv(input_path)
    df['sentiment'] = df['review'].apply(classify_sentiment)
    df.to_csv(output_path, index=False)
    print(f"✅ Sentiment analysis saved to: {output_path}")

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from gensim.utils import simple_preprocess

# Download required resources
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize once
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    """
    Tokenizes, removes stopwords, and lemmatizes input text.
    """
    tokens = simple_preprocess(str(text), deacc=True)
    return [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]
