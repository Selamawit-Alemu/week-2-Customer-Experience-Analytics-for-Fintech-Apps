import pandas as pd
import pyodbc

# Connect to SQL Server


conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=bank_reviews;Trusted_Connection=yes;")
cursor = conn.cursor()
# Load processed CSV file
df = pd.read_csv("../data/processed/analyzed_reviews.csv")

for _, row in df.iterrows():
    bank_name = row['bank']

    # Check if bank exists, get bank_id
    cursor.execute("SELECT bank_id FROM banks WHERE bank_name = ?", bank_name)
    result = cursor.fetchone()

    if result:
        bank_id = result[0]
    else:
        # Insert bank if not exists
        cursor.execute("INSERT INTO banks (bank_name) VALUES (?)", bank_name)
        conn.commit()
        cursor.execute("SELECT bank_id FROM banks WHERE bank_name = ?", bank_name)
        bank_id = cursor.fetchone()[0]

    # Insert review
    cursor.execute("""
        INSERT INTO reviews (bank_id, review_text, sentiment_label, sentiment_score, identified_theme)
        VALUES (?, ?, ?, ?, ?)
    """, bank_id, row['review'], row['sentiment'], row.get('sentiment_score', None), row.get('identified_theme', None))


conn.commit()
cursor.close()
conn.close()
print("✅ Data inserted successfully.")
