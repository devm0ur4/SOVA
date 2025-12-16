from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def check_captcha(driver):
    try:
        # Verifica se tem um iframe do CAPTCHA
        driver.find_element(By.XPATH, "//iframe[contains(@src, 'captcha')]")
        print("CAPTCHA detectado: iframe encontrado.")
        return True
    except NoSuchElementException:
        pass

    try:
        # Verifica se tem um elemento com 'captcha' no ID ou classe
        driver.find_element(By.XPATH, "//*[contains(@id, 'captcha') or contains(@class, 'captcha')]")
        print("CAPTCHA detectado: elemento com 'captcha' encontrado.")
        return True
    except NoSuchElementException:
        pass

    print("Nenhum CAPTCHA detectado.")
    return False