import pandas as pd
import pyodbc

# Connect to SQL Server
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=bank_reviews;"
    "Trusted_Connection=yes;"
)

# Query to fetch reviews and bank names
query = """
SELECT r.review_id, b.bank_name, r.review_text, r.rating, r.review_date, r.sentiment_label
FROM reviews r
JOIN banks b ON r.bank_id = b.bank_id
ORDER BY r.review_date DESC;
"""

df = pd.read_sql(query, conn)
conn.close()

print(df.head(10))  # Show first 10 rows
