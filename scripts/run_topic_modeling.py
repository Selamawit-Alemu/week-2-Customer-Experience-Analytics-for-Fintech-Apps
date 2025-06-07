import pandas as pd
from gensim import corpora, models
from utils import preprocess_text

# Load data
df = pd.read_csv("../data/processed/analyzed_reviews.csv")

# Preprocess
df['tokens'] = df['review'].apply(preprocess_text)

# Create Dictionary and Corpus
dictionary = corpora.Dictionary(df['tokens'])
corpus = [dictionary.doc2bow(text) for text in df['tokens']]

# LDA Model
lda_model = models.LdaModel(corpus=corpus, id2word=dictionary, num_topics=5, random_state=42, passes=10)

# Print Topics
topics = lda_model.print_topics(num_words=5)
for topic in topics:
    print(f"Topic {topic[0]}: {topic[1]}")
