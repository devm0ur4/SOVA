from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pathlib import Path
from config.paths import BASE_DIR

def create_driver():
    download_dir = BASE_DIR / "downloads"
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
