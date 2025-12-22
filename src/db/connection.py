import sqlite3
from config.paths import BASE_DIR

DB_PATH = BASE_DIR / "database.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

