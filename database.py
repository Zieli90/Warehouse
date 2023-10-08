import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = 'tomek123',
    database = 'stan'
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS stan")
cursor.execute("USE stan")
cursor.execute("CREATE TABLE IF NOT EXISTS stan_magazynu (id INT AUTO_INCREMENT PRIMARY KEY,nazwa VARCHAR(200), opis VARCHAR(250), ilość INT)")

cursor.execute ("SELECT * FROM stan_magazynu")
rows = cursor.fetchall()

for row in rows:
    print(row)
    
table_name = 'stan_magazynu'
query = f'SELECT * from {table_name}'
cursor.execute(query)

rows = cursor.fetchall()

for row in rows:
    print

conn.commit()

cursor.close()
conn.close()