import pyodbc

# Connect to the 'bank_reviews' database
conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=bank_reviews;Trusted_Connection=yes;'
)
cursor = conn.cursor()

# Create Banks table
cursor.execute("""
IF OBJECT_ID('banks', 'U') IS NULL
CREATE TABLE banks (
    bank_id INT IDENTITY(1,1) PRIMARY KEY,
    bank_name NVARCHAR(100) NOT NULL
);
""")

# Create Reviews table
cursor.execute("""
IF OBJECT_ID('reviews', 'U') IS NULL
CREATE TABLE reviews (
    review_id INT IDENTITY(1,1) PRIMARY KEY,
    bank_id INT FOREIGN KEY REFERENCES banks(bank_id),
    review_text NVARCHAR(MAX),
    sentiment_label NVARCHAR(10),
    sentiment_score FLOAT,
    identified_theme NVARCHAR(100)
);
""")

conn.commit()
print("✅ Tables 'banks' and 'reviews' created (or already exist).")

cursor.close()
conn.close()
