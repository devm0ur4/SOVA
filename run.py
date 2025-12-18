import os
import sys
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).parent
VENV_DIR = BASE_DIR / ".venv"
REQUIREMENTS_FILE = BASE_DIR / "requirements.txt"
DB_FILE = BASE_DIR / "database.db"
DEPS_FLAG = VENV_DIR / ".deps_installed"


def is_venv():
    return sys.prefix != sys.base_prefix


def venv_python():
    if os.name == "nt":
        return VENV_DIR / "Scripts" / "python.exe"
    return VENV_DIR / "bin" / "python"


def ensure_venv():
    if not VENV_DIR.exists():
        print("Criando venv...")
        subprocess.check_call([sys.executable, "-m", "venv", VENV_DIR])

    if not is_venv():
        python = venv_python()
        os.execv(str(python), [str(python), __file__])


def ensure_dependencies():
    if DEPS_FLAG.exists():
        return

    if not REQUIREMENTS_FILE.exists():
        print("requirements.txt não encontrado.")
        return

    print("Instalando dependências...")
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "-r", REQUIREMENTS_FILE]
    )

    DEPS_FLAG.touch()


def start_database():
    if DB_FILE.exists():
        print("Banco já existe. Pulando inicialização.")
        return

    from src.db.initialize import start_db
    start_db()
    print("Banco criado.")


def start_app():
    from src.main import main
    main()


if __name__ == "__main__":
    ensure_venv()
    ensure_dependencies()
    start_database()
    start_app()
