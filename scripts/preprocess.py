import pandas as pd
import emoji
import re

def remove_emoji(text):
    return emoji.replace_emoji(text, replace='')

def clean_reviews(df, text_col='review'):
    # Drop duplicates by the review text column
    df = df.drop_duplicates(subset=[text_col])
    
    # Remove emojis
    df[text_col] = df[text_col].astype(str).apply(remove_emoji)
    
    # Remove non-ASCII characters (optional, keeps only basic English chars)
    df[text_col] = df[text_col].apply(lambda x: re.sub(r'[^\x00-\x7F]+', '', x))
    
    # Strip leading/trailing whitespace
    df[text_col] = df[text_col].str.strip()
    
    # Drop rows with empty reviews after cleaning
    df = df[df[text_col] != '']
    
    return df

if __name__ == "__main__":
    # Adjust the path to your raw CSV file
    raw_file_path = '../data/raw/reviews.csv'
    cleaned_file_path = '../data/cleaned_reviews.csv'
    
    # Load the raw reviews CSV
    df = pd.read_csv(raw_file_path)
    print("Columns in dataset:", df.columns)
    
    # Replace 'review' with your actual text column name if different
    cleaned_df = clean_reviews(df, text_col='review')
    
    # Save cleaned reviews
    cleaned_df.to_csv(cleaned_file_path, index=False)
    print(f"Cleaned reviews saved to {cleaned_file_path}")
