import sqlite3
import os

sql = """CREATE TABLE IF NOT EXISTS rextinta(id INTEGER PRIMARY KEY, nmov TEXT, nome TEXT, data TEXT, produto TEXT, cor TEXT)"""

try:
    conn = sqlite3.connect(os.path.join('db_tinta', 'tinta.db'))
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
except Exception as e:
    print(f"Houve um erro em {e}")


