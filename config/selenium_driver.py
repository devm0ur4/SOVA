from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from config.paths import DOWNLOAD_DIR


class DriverConfig:
    _driver: WebDriver | None = None
    _timeout: int = 5

    @classmethod
    def create_driver(cls) -> WebDriver:
        if cls._driver is not None:
            return cls._driver 

        download_dir = DOWNLOAD_DIR
        download_dir.mkdir(exist_ok=True)

        chrome_options = Options()

        prefs = {
            "download.default_directory": str(download_dir),
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True,
        }

        chrome_options.add_experimental_option("prefs", prefs)

        cls._driver = webdriver.Chrome(options=chrome_options)
        return cls._driver

    @classmethod
    def get_driver(cls) -> WebDriver:
        if cls._driver is None:
            raise RuntimeError(
                "Driver ainda não foi criado. "
                "Chame DriverConfig.create_driver() primeiro."
            )
        return cls._driver

    @classmethod
    def click(cls, xpath: str) -> None:
        driver = cls.get_driver()
        wait = WebDriverWait(driver, cls._timeout)

        element = wait.until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        element.click()
    
    @classmethod
    def send_keys(cls, xpath: str, key: str) -> None:
        driver = cls.get_driver()
        wait = WebDriverWait(driver, cls._timeout)

        element = wait.until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        element.send_keys(key)

    @classmethod
    def get_element(cls, xpath: str) -> WebElement:
        driver = cls.get_driver()
        wait = WebDriverWait(driver, cls._timeout)

        element = wait.until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        
        return element 