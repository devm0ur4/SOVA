from .connection import get_connection
from pathlib import Path
from config.paths import DB_DIR

SQL_SCHEMA = DB_DIR / "sql/schema.sql"
SQL_SEED = DB_DIR / "sql/seed.sql"

def start_db():
    with get_connection() as conn:
        cursor = conn.cursor()

        with open(SQL_SCHEMA, "r", encoding="utf-8") as f:
            cursor.executescript(f.read())

        with open(SQL_SEED, "r", encoding="utf-8") as f:
            cursor.executescript(f.read())
