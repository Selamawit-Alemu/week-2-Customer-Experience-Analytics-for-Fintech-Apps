import pyodbc

conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;Trusted_Connection=yes;'
)
cursor = conn.cursor()

cursor.execute("SELECT @@VERSION")
row = cursor.fetchone()
print(row)
