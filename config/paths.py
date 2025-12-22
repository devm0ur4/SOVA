from pathlib import Path


## raiz do projeto
BASE_DIR = Path(__file__).resolve().parents[2]  


## diretorios do projeto
DB_DIR = BASE_DIR / "src/db"
DOWNLOAD_DIR = BASE_DIR / "downloads"
RAW_DIR = BASE_DIR / "storage/raw"