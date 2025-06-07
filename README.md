# mobile-banking-app-reviews-analysis
# Bank Mobile Reviews Analysis

## Objective
Scrape and analyze user reviews from Google Play Store for three Ethiopian bank mobile apps to identify satisfaction drivers and pain points.

## Project Structure
- `data/raw`: Raw scraped data CSVs.
- `data/processed`: Cleaned data CSVs ready for analysis.
- `scripts`: Python scripts for scraping and preprocessing.
- `docs`: Documentation and reports.

## How to Run

1. Install dependencies:

pip install -r requirements.txt


2. Scrape reviews:

python scripts/scrape.py


3. Preprocess data:

python scripts/preprocess.py


## Methodology
- Used `google-play-scraper` to collect 400+ reviews per bank.
- Cleaned data by removing duplicates and standardizing dates.
- Stored cleaned data in CSV for further analysis.