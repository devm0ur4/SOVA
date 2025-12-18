from pathlib import Path

BASE_DIR = Path(__file__).parent
DB_FILE = BASE_DIR / "database.db"


def start_database():
    if DB_FILE.exists():
        print("Banco já existe. Pulando inicialização.")
        return

    from src.db.initialize import start_db
    start_db()
    print("Banco criado com sucesso.")


def start_app():
    from src.main import main
    main()


if __name__ == "__main__":
    start_database()
    start_app()
