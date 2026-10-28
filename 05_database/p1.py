import sqlite3
conn = sqlite3.connect("mydb.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS STUDENTS(
id integer PRIMARY KEY autoincrement,
name text not null,
age integer)
""")

conn.commit()