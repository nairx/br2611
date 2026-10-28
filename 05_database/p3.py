import sqlite3
conn = sqlite3.connect("mydb.db")

cursor = conn.cursor()

cursor.execute("""
select * from students
""")

rows = cursor.fetchall()

for row in rows:
    print(row)