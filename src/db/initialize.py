from .connection import get_connection
from pathlib import Path

BASE_DIR = Path(__file__).parent

SQL_SCHEMA = BASE_DIR / "sql/schema.sql"
SQL_SEED = BASE_DIR / "sql/seed.sql"

def start_db():
    with get_connection() as conn:
        cursor = conn.cursor()

        with open(SQL_SCHEMA, "r", encoding="utf-8") as f:
            cursor.executescript(f.read())

        with open(SQL_SEED, "r", encoding="utf-8") as f:
            cursor.executescript(f.read())
