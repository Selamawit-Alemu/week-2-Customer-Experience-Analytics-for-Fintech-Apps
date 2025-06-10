The project involves scraping user reviews from the Google Play Store for the three specified banks' apps. For each review, the following data points are collected:

    Review Text: User feedback (e.g., “Love the UI, but it crashes often”).
    Rating: 1–5 stars.
    Date: Posting date (time optional).
    Bank/App Name: E.g., “Commercial Bank of Ethiopia Mobile”.
    Source: Google Play.

Minimum Requirement: 400 reviews per bank (1200 total).
🛠️ Technologies Used

    Programming Language: Python
    Web Scraping: Libraries for fetching data from Google Play Store (e.g., google-play-scraper).
    Data Manipulation: pandas
    Natural Language Processing (NLP): Libraries for sentiment analysis and topic modeling (e.g., nltk, spacy, scikit-learn).
    Database: Oracle (for storing cleaned review data).
    Data Visualization: Libraries for creating compelling charts and graphs (e.g., matplotlib, seaborn, plotly).
    Version Control: Git
    CI/CD: GitHub Actions

⚙️ Project Structure

The repository is organized to ensure a clear separation of concerns, making it easy to navigate and understand the project workflow.

        week-2-Customer-Experience-Analytics-for-Fint.../
        ├── .github/
        │   └── workflows/
        │       └── python-ci.yml             # GitHub Actions workflow for CI
        ├── data/
        │   ├── processed/
        │   │   ├── analyzed_reviews.csv      # Reviews after sentiment/topic analysis
        │   │   ├── cleaned_reviews.csv       # Cleaned and preprocessed reviews
        │   │   └── sentiment_aggregated.csv  # Aggregated sentiment insights
        │   └── raw/
        │       └── reviews.csv               # Raw scraped reviews
        ├── db_dumps/
        │   └── bank_reviews_data_dump.sql    # SQL dump for database schema and data
        ├── notebooks/
        │   ├── Insight_from_sentiment_analysis.ipynb  # Notebook for sentiment analysis insights
        │   ├── reviews_with_themes.csv       # CSV output from topic modeling notebook
        │   └── sentiment_analysis.ipynb      # Notebook for sentiment analysis exploration
        ├── scripts/
        │   ├── check_db_connection.py        # Script to test database connection
        │   ├── create_db.py                  # Script to create the Oracle database
        │   ├── create_tables.py              # Script to create database tables
        │   ├── export_to_sql.py              # Script to export data to SQL
        │   ├── insert_data.py                # Script to insert data into the database
        │   ├── preprocess.py                 # Script for data cleaning and preprocessing
        │   ├── run_sentiment.py              # Script to run sentiment analysis
        │   ├── run_topic_modeling.py         # Script to run topic modeling
        │   ├── scrape.py                     # Script for web scraping Google Play reviews
        │   ├── test.py                       # Unit tests for scripts
        │   ├── utils.py                      # Utility functions
        │   ├── view_DB_data.py               # Script to view data in the database
        │   └── visualize_topics.py           # Script to visualize topic models
        ├── venv/                             # Python virtual environment
        ├── .gitignore                        # Specifies intentionally untracked files to ignore
        ├── README.md                         # This README file
        └── requirements.txt                  # List of Python dependencies

🚀 Getting Started

Follow these steps to set up and run the project locally.
Prerequisites

    Python 3.8+
    Oracle Database (or access to an Oracle instance)
    git

Installation

    Clone the repository:
    Bash

git clone https://github.com/Selamawit-Alemu/week-2-Customer-Experience-Analytics-for-Fintech-Apps.git
cd week-2-Customer-Experience-Analytics-for-Fintech

(Note: Replace your-username with the actual GitHub username or organization.)

Create and activate a virtual environment:
Bash

    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate

3.  Install dependencies:

```bash
pip install -r requirements.txt
```

Database Setup (SQL Server)

    Ensure SQL Server is running and accessible.

    Configure connection details: You will need to set environment variables or create a configuration file (e.g., .env, config.ini) for your SQL Server database connection details (e.g., server, database name, username, password). These details should not be committed to version control.
        Example (using environment variables for a SQL Server instance):
        Bash

    export DB_SERVER="your_sql_server_host" # e.g., localhost or an IP address
    export DB_DATABASE="your_database_name"
    export DB_USER="your_sql_user"
    export DB_PASSWORD="your_sql_password"

 

Create the database and tables:
Bash

    python scripts/create_db.py
    python scripts/create_tables.py

The db_dumps/bank_reviews_data_dump.sql file contains the SQL schema and potentially sample data, which can be executed directly on your SQL Server instance if needed, or the create_db.py and create_tables.py scripts should handle this programmatically.
Running the Project Workflow

The typical workflow involves scraping, preprocessing, analyzing, inserting into the database, and visualizing.

    Scrape Reviews:
    Bash

    python scripts/scrape.py

This script will save raw reviews to data/raw/reviews.csv.

Preprocess Data:
Bash

python scripts/preprocess.py

This script cleans and preprocesses the scraped data, saving it to data/processed/cleaned_reviews.csv.

Run Sentiment Analysis:
Bash

python scripts/run_sentiment.py

This script performs sentiment analysis, storing results in data/processed/analyzed_reviews.csv and data/processed/sentiment_aggregated.csv. You can also explore sentiment using notebooks/sentiment_analysis.ipynb.

Run Topic Modeling:
Bash

python scripts/run_topic_modeling.py

This script performs topic modeling to identify key themes. Results might be used in notebooks/reviews_with_themes.csv or scripts/visualize_topics.py.

Insert Data into Oracle DB:
Bash

python scripts/insert_data.py

This script takes the processed data and inserts it into your Oracle database.

View Data in DB (Optional):
Bash

    python scripts/view_DB_data.py

    Generate Visualizations and Insights:
    Refer to the notebooks for in-depth analysis and visualization:
        notebooks/Insight_from_sentiment_analysis.ipynb
        notebooks/sentiment_analysis.ipynb
        scripts/visualize_topics.py

