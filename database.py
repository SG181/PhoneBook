import sqlite3
conn = sqlite3.connect('database.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Person (
                 person_id INTEGER PRIMARY KEY AUTOINCREMENT,
                 Person_name TEXT,
                 Person_surname TEXT,
                 Person_email TEXT,
                 phone TEXT
             )''')

conn.commit()
conn.close()
