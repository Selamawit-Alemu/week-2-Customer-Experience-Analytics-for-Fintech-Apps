import pyLDAvis.gensim_models
import gensim.corpora
from gensim.models import LdaModel
import pandas as pd
import pickle

from utils import preprocess_text

# Load cleaned reviews
df = pd.read_csv('../data/processed/cleaned_reviews.csv')

# Preprocess
texts = df['cleaned'].apply(eval)  # Assuming it's stored as stringified lists

# Prepare data
dictionary = gensim.corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

# Load or retrain model
lda_model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=5, random_state=42, passes=10)

# Visualize
vis = pyLDAvis.gensim_models.prepare(lda_model, corpus, dictionary)
pyLDAvis.save_html(vis, '../outputs/topic_modeling_visualization.html')
print("✅ Topic visualization saved to outputs/topic_modeling_visualization.html")
