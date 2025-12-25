from pathlib import Path

# raiz do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# diretórios principais
SRC_DIR = BASE_DIR / "src"
CONFIG_DIR = BASE_DIR / "config"

DB_DIR = SRC_DIR / "db"
DOWNLOAD_DIR = BASE_DIR / "downloads"
STORAGE_DIR = BASE_DIR / "storage"
RAW_DIR = STORAGE_DIR / "raw"
