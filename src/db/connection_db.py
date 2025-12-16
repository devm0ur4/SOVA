import sqlite3

DB_PATH = 'units.db'
sql_file = 'initialize_db.sql'

def start_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    with open(sql_file, 'r') as f:
        sql_script = f.read()

    cursor.executescript(sql_script)
    conn.commit()
    conn.close()

