from utils import analyze_sentiments

input_path = "../data/processed/cleaned_reviews.csv"
output_path = "../data/processed/analyzed_reviews.csv"

analyze_sentiments(input_path, output_path)
