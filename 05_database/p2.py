import sqlite3
conn = sqlite3.connect("mydb.db")

cursor = conn.cursor()

sql = """
insert into students(name,age)
values(?,?)
"""

cursor.execute(sql,("Mike",20))

conn.commit()