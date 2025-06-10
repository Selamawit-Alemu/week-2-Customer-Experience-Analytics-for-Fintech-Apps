import pyodbc

# Connect to your SQL Server
conn = pyodbc.connect(
    r"DRIVER={ODBC Driver 17 for SQL Server};"
    r"SERVER=localhost;"
    r"DATABASE=bank_reviews;"
    r"Trusted_Connection=yes;"
)
cursor = conn.cursor()

# Dump file path
dump_file = "../db_dumps/bank_reviews_data_dump.sql"

with open(dump_file, "w", encoding="utf-8") as f:
    # Write schema creation (you've already created this in your create_tables.py)
    f.write("-- Schema Dump for bank_reviews\n")
    f.write("CREATE DATABASE bank_reviews;\nGO\nUSE bank_reviews;\nGO\n")

    f.write("""
IF OBJECT_ID('banks', 'U') IS NULL
CREATE TABLE banks (
    bank_id INT IDENTITY(1,1) PRIMARY KEY,
    bank_name NVARCHAR(255) UNIQUE
);
GO

IF OBJECT_ID('reviews', 'U') IS NULL
CREATE TABLE reviews (
    review_id INT IDENTITY(1,1) PRIMARY KEY,
    bank_id INT FOREIGN KEY REFERENCES banks(bank_id),
    review_text NVARCHAR(MAX),
    sentiment_label NVARCHAR(10),
    sentiment_score FLOAT,
    identified_theme NVARCHAR(100)
);
GO
""")

    # Export banks
    f.write("\n-- Insert data into banks\n")
    cursor.execute("SELECT bank_id, bank_name FROM banks")
    for row in cursor.fetchall():
        f.write("INSERT INTO banks (bank_id, bank_name) VALUES ({row.bank_id}, N'{row.bank_name.replace(\"'\", \"''\")}');\n")

    f.write("GO\n")

    # Export reviews
    f.write("\n-- Insert data into reviews\n")
    cursor.execute("""
        SELECT bank_id, review_text, sentiment_label, sentiment_score, identified_theme
        FROM reviews
    """)
    for row in cursor.fetchall():
        review_text = row.review_text.replace("'", "''") if row.review_text else ""
        sentiment_label = row.sentiment_label or ''
        identified_theme = row.identified_theme.replace("'", "''") if row.identified_theme else ''
        f.write(f"INSERT INTO reviews (bank_id, review_text, sentiment_label, sentiment_score, identified_theme) "
                f"VALUES ({row.bank_id}, N'{review_text}', '{sentiment_label}', {row.sentiment_score}, N'{identified_theme}');\n")

    f.write("GO\n")

print(" SQL dump file created")
