import sqlite3
import os

sql = """CREATE TABLE IF NOT EXISTS rextinta(id INTEGER PRIMARY KEY, nome TEXT NOT NULL, data TEXT NOT NULL, cor TEXT NOT NULL, lata TEXT NOT NULL, linha TEXT NOT NULL, quantidade TEXT NOT NULL, base TEXT NOT NULL)"""

try:
    conn = sqlite3.connect(os.path.join('db_tinta', 'tinta.db'))
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
except Exception as e:
    print(f"Houve um erro em {e}")


