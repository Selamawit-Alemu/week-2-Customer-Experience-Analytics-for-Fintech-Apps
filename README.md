B5W2: Customer Experience Analytics for Fintech Apps
A Real-World Data Engineering Challenge: Scraping, Analyzing, and Visualizing Google Play Store Reviews

This project, part of the B5W2 challenge, focuses on performing comprehensive customer experience analytics for mobile banking applications. By scraping, analyzing, and visualizing user reviews from the Google Play Store, it simulates the role of a Data Analyst at Omega Consultancy, providing actionable insights to enhance customer retention and satisfaction for Ethiopian banks.
🚀 Challenge Overview

This week's challenge centers on analyzing customer satisfaction with mobile banking apps by collecting and processing user reviews from the Google Play Store for three major Ethiopian banks:

    Commercial Bank of Ethiopia (CBE)
    Bank of Abyssinia (BOA)
    Dashen Bank

You'll scrape app reviews, analyze sentiments and themes, and visualize insights to deliver a data-driven report with actionable recommendations. Building on foundational skills from Week 1, this project introduces web scraping, thematic NLP analysis, and basic database engineering.
🎯 Business Objective

Omega Consultancy is supporting banks to improve their mobile apps to enhance customer retention and satisfaction. As a Data Analyst, your role involves:

    Scraping User Reviews: Collect reviews from the Google Play Store for the specified banks.
    Sentiment and Thematic Analysis: Analyze sentiment (positive/negative/neutral) and extract key themes (e.g., "bugs", "UI").
    Insight Generation: Identify satisfaction drivers (e.g., speed) and pain points (e.g., crashes).
    Data Storage: Store cleaned review data in an Oracle database.
    Reporting: Deliver a report with compelling visualizations and actionable recommendations to business stakeholders.

Real-World Scenarios Addressed:

This project addresses key scenarios simulating real consulting tasks faced by product, marketing, and engineering teams in the banking sector:

    Scenario 1: Retaining Users
        Problem: CBE has a 4.4-star rating, BOA 2.8, and Dashen 4.0. Users complain about slow loading during transfers.
        Task: Analyze if slow loading is a broader issue across banks and suggest areas for app investigation.
    Scenario 2: Enhancing Features
        Problem: Banks need to stay competitive.
        Task: Extract desired features (e.g., transfer, fingerprint login, faster loading times) through keyword and theme extraction. Recommend how each bank can stay competitive.
    Scenario 3: Managing Complaints
        Problem: Efficiently handle customer complaints.
        Task: Cluster and track complaints (e.g., “login error”) to guide AI chatbot integration and faster support resolution strategies.

These scenarios highlight user retention, feature innovation, and support efficiency, aligning directly with fintech priorities.
📊 Dataset Overview

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
 Conversation with Gemini

help me to write read me for my project

A great README is essential for any project! It's often the first thing people see and can make a big difference in how your project is perceived and used. To help you write an effective one, I need a little more information about your project.

Please tell me:

    What is the name of your project?
    What does your project do? (A brief, one-sentence description is a good start.)
    What problem does your project solve?
    Who is your target audience? (Developers, end-users, etc.?)
    What are the key features of your project?
    What technologies are used in your project? (e.g., Python, React, Node.js, specific frameworks or libraries)
    How do users install and run your project? (e.g., npm install, pip install, git clone, setup steps)
    How can others contribute to your project? (Are you open to contributions? Do you have guidelines?)
    What license are you using for your project? (e.g., MIT, GPL, Apache 2.0)
    Are there any known issues or limitations?
    Do you have examples of usage or screenshots? (These can be very helpful!)

Once I have this information, I can help you structure your README with appropriate headings and content, suggest common sections, and even help you draft some of the text.

"B5W2: Customer Experience Analytics for Fintech Apps

A Real-World Data Engineering Challenge: Scraping, Analyzing, and Visualizing Google Play Store Reviews

Challenge Overview

Business Objective

Dataset Overview

Team

Key Dates

Communication & Support

Learning Objectives

Project Planning - Data Collection & Analysis

Deliverables and Tasks

Due Dates

Other Considerations

Tutorials Schedule

References

Challenge Overview

This

week’s challenge centers on analyzing customer satisfaction with mobile

banking apps by collecting and processing user reviews from the Google

Play Store for three Ethiopian banks:

Commercial Bank of Ethiopia (CBE)

Bank of Abyssinia (BOA)

Dashen Bank

You’ll

scrape app reviews, analyze sentiments and themes, and visualize

insights to simulate the role of a Data Analyst at Omega Consultancy, a

firm advising banks.

Building on Week 1’s foundational skills, this

week introduces web scraping, thematic NLP analysis, and basic database

engineering.

 

Business Objective

Omega

Consultancy is supporting banks to improve their mobile apps to enhance

customer retention and satisfaction. Your role as a Data Analyst is to:


Scrape user reviews from the Google Play Store.

Analyze sentiment (positive/negative/neutral) and extract themes (e.g., "bugs", "UI").

Identify satisfaction drivers (e.g., speed) and pain points (e.g., crashes).

Store cleaned review data in a Oracle database.

Deliver a report with visualizations and actionable recommendations.

Scenarios 

These scenarios simulate real consulting tasks faced by product, marketing, and engineering teams in the banking.


Scenario 1: Retaining Users

CBE

has a 4.4-star rating, BOA 2.8, and Dashen 4.0. Users complain about

slow loading during transfers. Analyze if this is a broader issue and

suggest areas for app investigation.

Scenario 2: Enhancing Features

Extract

desired features (e.g., transfer, fingerprint login, faster loading

times) through keyword and theme extraction. Recommend how each bank can

stay competitive.


Scenario 3: Managing Complaints

Cluster and track complaints (e.g., “login error”) to guide AI chatbot integration and faster support resolution strategies.

These scenarios highlight user retention, feature innovation, and support efficiency, aligning with fintech priorities.

Dataset Overview

You will scrape reviews from the Google Play Store for three banks’ apps, collecting:


Review Text: User feedback (e.g., “Love the UI, but it crashes often”).

Rating: 1–5 stars.

Date: Posting date (time optional).

Bank/App Name: E.g., “Commercial bank of Ethiopia Mobile”.

Source: Google Play.

Minimum: 400 reviews per bank (1200 total). If scraping is limited, 

Team

Facilitators:


Mahlet 

Kerod 

Rediet 

Rehmet 

Key Dates

 

Introduction: 8:00 AM UTC, Wednesday, 04 June 2024

Interim Submission: 8:00 PM UTC, Sunday, 08 June 2024

Final Submission: 8:00 PM UTC, Tuesday, 10 June 2024

Communication & Support

 

Slack channel: #all-week-2

Office hours: Mon–Fri, 08:00–15:00 UTC 

Learning Objectives

By the end of this week, you will be able to:


Scrape and preprocess user reviews from the Google Play Store to prepare text data for analysis.

Apply NLP techniques to analyze review sentiment and identify key customer feedback themes.

Design and implement a relational database schema in Oracle to store and manage review data.

Derive actionable insights from analyzed data and create compelling visualizations for business stakeholders.

Develop and present a data-driven report with recommendations for app improvement in a fintech context.

Employ Git for version control and write unit tests to ensure the reliability of data processing scripts.

Project Planning - Data Collection & Analysis" this was the task and let me provide u my folder structure

Okay, this is fantastic! You've provided a comprehensive overview of your project, "B5W2: Customer Experience Analytics for Fintech Apps." This information is perfect for crafting a detailed and informative README.

Now, to make this README truly helpful, let's consider your folder structure. Knowing how your code and other project assets are organized will allow me to suggest where people can find different parts of your project.

Please provide your folder structure. You can do this by listing the main directories and a few key files within them, like this:

my_project/
├── src/
│   ├── data_collection.py
│   ├── sentiment_analysis.py
│   └── database_management.py
├── notebooks/
│   ├── exploration.ipynb
│   └── data_analysis.ipynb
├── data/
│   ├── raw/
│   └── processed/
├── reports/
│   └── final_report.pdf
├── README.md
├── requirements.txt
└── .gitignore

Once I have your folder structure, I can start drafting your README, incorporating all the great details you've already shared!

this is my folder structure

    Query successful

This is excellent! The folder structure makes perfect sense for a data engineering and analytics project. You've got clear divisions for data, notebooks, scripts, and even CI/CD workflows.

Here's a draft README for your "B5W2: Customer Experience Analytics for Fintech Apps" project, incorporating all the details you've provided and structured according to best practices.
B5W2: Customer Experience Analytics for Fintech Apps
A Real-World Data Engineering Challenge: Scraping, Analyzing, and Visualizing Google Play Store Reviews

This project, part of the B5W2 challenge, focuses on performing comprehensive customer experience analytics for mobile banking applications. By scraping, analyzing, and visualizing user reviews from the Google Play Store, it simulates the role of a Data Analyst at Omega Consultancy, providing actionable insights to enhance customer retention and satisfaction for Ethiopian banks.
🚀 Challenge Overview

This week's challenge centers on analyzing customer satisfaction with mobile banking apps by collecting and processing user reviews from the Google Play Store for three major Ethiopian banks:

    Commercial Bank of Ethiopia (CBE)
    Bank of Abyssinia (BOA)
    Dashen Bank

You'll scrape app reviews, analyze sentiments and themes, and visualize insights to deliver a data-driven report with actionable recommendations. Building on foundational skills from Week 1, this project introduces web scraping, thematic NLP analysis, and basic database engineering.
🎯 Business Objective

Omega Consultancy is supporting banks to improve their mobile apps to enhance customer retention and satisfaction. As a Data Analyst, your role involves:

    Scraping User Reviews: Collect reviews from the Google Play Store for the specified banks.
    Sentiment and Thematic Analysis: Analyze sentiment (positive/negative/neutral) and extract key themes (e.g., "bugs", "UI").
    Insight Generation: Identify satisfaction drivers (e.g., speed) and pain points (e.g., crashes).
    Data Storage: Store cleaned review data in an Oracle database.
    Reporting: Deliver a report with compelling visualizations and actionable recommendations to business stakeholders.

Real-World Scenarios Addressed:

This project addresses key scenarios simulating real consulting tasks faced by product, marketing, and engineering teams in the banking sector:

    Scenario 1: Retaining Users
        Problem: CBE has a 4.4-star rating, BOA 2.8, and Dashen 4.0. Users complain about slow loading during transfers.
        Task: Analyze if slow loading is a broader issue across banks and suggest areas for app investigation.
    Scenario 2: Enhancing Features
        Problem: Banks need to stay competitive.
        Task: Extract desired features (e.g., transfer, fingerprint login, faster loading times) through keyword and theme extraction. Recommend how each bank can stay competitive.
    Scenario 3: Managing Complaints
        Problem: Efficiently handle customer complaints.
        Task: Cluster and track complaints (e.g., “login error”) to guide AI chatbot integration and faster support resolution strategies.

These scenarios highlight user retention, feature innovation, and support efficiency, aligning directly with fintech priorities.
📊 Dataset Overview

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

git clone https://github.com/your-username/week-2-Customer-Experience-Analytics-for-Fintech.git
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

Database Setup (Oracle)

    Ensure Oracle Database is running and accessible.

    Configure connection details: You will likely need to set environment variables or create a configuration file (e.g., config.ini or similar) for your Oracle database connection details (hostname, port, service name, username, password). These details should not be committed to version control.

    Create the database and tables:
    Bash

    python scripts/create_db.py
    python scripts/create_tables.py

    You can use db_dumps/bank_reviews_data_dump.sql for a reference or to directly load a sample schema/data if provided.

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

🧪 Testing

Unit tests for data processing and utility scripts are located in scripts/test.py.
To run tests:
Bash

python scripts/test.py

🤝 Contribution Guidelines

This project is part of a challenge, and direct external contributions might not be accepted in the same way as open-source projects. However, if you are a participant in the challenge and have suggestions or find issues, please communicate through the designated channels.
📞 Communication & Support

    Slack Channel: #all-week-2
    Office Hours: Mon–Fri, 08:00–15:00 UTC

🗓️ Key Dates

    Introduction: 8:00 AM UTC, Wednesday, June 04, 2024
    Interim Submission: 8:00 PM UTC, Sunday, June 08, 2024
    Final Submission: 8:00 PM UTC, Tuesday, June 10, 2024

📚 Learning Objectives

By the end of this challenge, you will be able to:

    Scrape and preprocess user reviews from the Google Play Store to prepare text data for analysis.
    Apply NLP techniques to analyze review sentiment and identify key customer feedback themes.
    Design and implement a relational database schema in Oracle to store and manage review data.
    Derive actionable insights from analyzed data and create compelling visualizations for business stakeholders.
    Develop and present a data-driven report with recommendations for app improvement in a fintech context.
    Employ Git for version control and write unit tests to ensure the reliability of data processing scripts.

👨‍ facilitators

    Mahlet
    Kerod
    Rediet
    Rehmet

📄 License

(Assuming this project is for an educational challenge, a formal open-source license might not be explicitly required for the challenge itself. However, for real-world projects, always specify a license like MIT, Apache 2.0, or GPL.)

Consider adding a LICENSE file if you intend for this project to be openly reusable outside the challenge context. A common choice for educational projects is the MIT License.
🔗 References

    Google Play Scraper Library (Example, link to the actual library used if different)
    Oracle Database Documentation
    NLTK Documentation
    SpaCy Documentation

Additional Considerations for Your Final README:

    Screenshots/Example Visualizations: Once you have your visualizations ready, embed a few key screenshots of your charts and graphs directly into the README. This significantly enhances its appeal and clarity.
    Report Link: If your final deliverable includes a separate report (PDF, presentation), include a link to it in the README.
    Known Issues/Limitations: If there are any, add a small section.
    Future Enhancements: Briefly mention any ideas for expanding the project if time allowed.

This README should provide a fantastic overview for anyone looking at your project! Let me know if you'd like any adjustments or further sections.

so generate read me for this project

Got it! Based on all the excellent information you've provided, here's the complete README for your "B5W2: Customer Experience Analytics for Fintech Apps" project.

I've made sure to incorporate the current date for the deadlines and used the project details and folder structure you supplied.
B5W2: Customer Experience Analytics for Fintech Apps
A Real-World Data Engineering Challenge: Scraping, Analyzing, and Visualizing Google Play Store Reviews

This project, part of the B5W2 challenge, focuses on performing comprehensive customer experience analytics for mobile banking applications. By scraping, analyzing, and visualizing user reviews from the Google Play Store, it simulates the role of a Data Analyst at Omega Consultancy, providing actionable insights to enhance customer retention and satisfaction for Ethiopian banks.
🚀 Challenge Overview

This week's challenge centers on analyzing customer satisfaction with mobile banking apps by collecting and processing user reviews from the Google Play Store for three major Ethiopian banks:

    Commercial Bank of Ethiopia (CBE)
    Bank of Abyssinia (BOA)
    Dashen Bank

You'll scrape app reviews, analyze sentiments and themes, and visualize insights to deliver a data-driven report with actionable recommendations. Building on foundational skills from Week 1, this project introduces web scraping, thematic NLP analysis, and basic database engineering.
🎯 Business Objective

Omega Consultancy is supporting banks to improve their mobile apps to enhance customer retention and satisfaction. As a Data Analyst, your role involves:

    Scraping User Reviews: Collect reviews from the Google Play Store for the specified banks.
    Sentiment and Thematic Analysis: Analyze sentiment (positive/negative/neutral) and extract key themes (e.g., "bugs", "UI").
    Insight Generation: Identify satisfaction drivers (e.g., speed) and pain points (e.g., crashes).
    Data Storage: Store cleaned review data in an Oracle database.
    Reporting: Deliver a report with compelling visualizations and actionable recommendations to business stakeholders.

Real-World Scenarios Addressed:

This project addresses key scenarios simulating real consulting tasks faced by product, marketing, and engineering teams in the banking sector:

    Scenario 1: Retaining Users
        Problem: CBE has a 4.4-star rating, BOA 2.8, and Dashen 4.0. Users complain about slow loading during transfers.
        Task: Analyze if slow loading is a broader issue across banks and suggest areas for app investigation.
    Scenario 2: Enhancing Features
        Problem: Banks need to stay competitive.
        Task: Extract desired features (e.g., transfer, fingerprint login, faster loading times) through keyword and theme extraction. Recommend how each bank can stay competitive.
    Scenario 3: Managing Complaints
        Problem: Efficiently handle customer complaints.
        Task: Cluster and track complaints (e.g., “login error”) to guide AI chatbot integration and faster support resolution strategies.

These scenarios highlight user retention, feature innovation, and support efficiency, aligning directly with fintech priorities.
📊 Dataset Overview

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

git clone https://github.com/your-username/week-2-Customer-Experience-Analytics-for-Fintech.git
cd week-2-Customer-Experience-Analytics-for-Fintech

(Note: Replace your-username with the actual GitHub username or organization where the project is hosted.)

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

Database Setup (Oracle)

    Ensure Oracle Database is running and accessible.

    Configure connection details: You will need to set environment variables or create a configuration file (e.g., .env, config.ini) for your Oracle database connection details (e.g., hostname, port, service name/SID, username, password). These details should not be committed to version control.
        Example (using environment variables):
        Bash

    export DB_USER="your_oracle_user"
    export DB_PASSWORD="your_oracle_password"
    export DB_HOST="your_oracle_host"
    export DB_PORT="1521"
    export DB_SERVICE_NAME="your_service_name" # or DB_SID="your_sid"

    (You might need to adjust scripts/utils.py or other connection scripts to read these.)

Create the database and tables:
Bash

    python scripts/create_db.py
    python scripts/create_tables.py

    You can also use db_dumps/bank_reviews_data_dump.sql to directly load a sample schema and data if provided for development or testing purposes.

Running the Project Workflow

The typical workflow involves scraping, preprocessing, analyzing, inserting into the database, and visualizing.

    Scrape Reviews:
    Bash

python scripts/scrape.py

This script will fetch reviews from Google Play Store and save raw data to data/raw/reviews.csv.

Preprocess Data:
Bash

python scripts/preprocess.py

This script cleans and preprocesses the scraped data, saving the cleaned version to data/processed/cleaned_reviews.csv.

Run Sentiment Analysis:
Bash

python scripts/run_sentiment.py

This script performs sentiment analysis on the preprocessed data, storing results in data/processed/analyzed_reviews.csv and aggregated sentiments in data/processed/sentiment_aggregated.csv. For interactive exploration, refer to notebooks/sentiment_analysis.ipynb.

Run Topic Modeling:
Bash

python scripts/run_topic_modeling.py

This script identifies key themes within the review data. Outputs might be used in notebooks/reviews_with_themes.csv or by scripts/visualize_topics.py.

Insert Data into Oracle DB:
Bash

python scripts/insert_data.py

This script takes the processed and analyzed data and inserts it into your configured Oracle database tables.

View Data in DB (Optional):
Bash

    python scripts/view_DB_data.py

    Use this script to verify the data has been correctly stored in your database.

    Generate Visualizations and Insights:
    Refer to the Jupyter notebooks for in-depth analysis and visualization:
        notebooks/Insight_from_sentiment_analysis.ipynb
        notebooks/sentiment_analysis.ipynb
        You can also run the visualization script: python scripts/visualize_topics.py


