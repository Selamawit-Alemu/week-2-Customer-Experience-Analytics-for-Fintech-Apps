import pyodbc

# Connect with autocommit enabled
conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;Trusted_Connection=yes;',
    autocommit=True
)
cursor = conn.cursor()

# Create the database
cursor.execute("IF DB_ID('bank_reviews') IS NULL CREATE DATABASE bank_reviews;")

print("✅ Database 'bank_reviews' created or already exists.")
cursor.close()
conn.close()
