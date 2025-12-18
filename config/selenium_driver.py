from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pathlib import Path

def create_driver():
    base_dir = Path(__file__).resolve().parents[1]  # raiz do projeto
    download_dir = base_dir / "downloads"
    download_dir.mkdir(exist_ok=True)

    chrome_options = Options()

    prefs = {
        "download.default_directory": str(download_dir),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True
    }

    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=chrome_options)
    return driver
