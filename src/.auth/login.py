from time import sleep
from .captcha import check_captcha
from selenium.webdriver.common.by import By
from time import sleep
from src import GUI

def get_credentials():
    GUI.updateOrder("Insira seu usuario:")
    _user = GUI.waitForUserInput()

    GUI.updateOrder("Insira sua senha:")
    _password = GUI.waitForUserInput()

    GUI.updateStatus("Realizando login...")
    GUI.updateOrder("Aguarde mais instruções...")
    return _user, _password

def perform_login(driver, username, password):
    try:
        # Localiza os campos de login
        user_field = driver.find_element(By.XPATH, "//input[@id='Username']")
        password_field = driver.find_element(By.XPATH, "//input[@id='Password']")
        login_button = driver.find_element(By.XPATH, "//button[@id='login']")

        # Limpa e depois Preenche os campos e clica no botão de login
        user_field.clear()
        password_field.clear()
        user_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

        # Verifica se há um CAPTCHA antes de prosseguir
        sleep(3)
        if check_captcha(driver):
            GUI.updateOrder("CAPTCHA detectado. Por favor, resolva o CAPTCHA na página. Clique em OK quando terminar.")
            GUI.waitForOkButton()
            GUI.updateStatus("CAPTCHA resolvido. Continuando...")


        print("Login realizado com sucesso.")
    except Exception as e:
        print(f"Erro ao realizar login: {e}")

def isLoggedIn(driver):
    sleep(10)
    current_url = driver.current_url
    if "home" in current_url.lower():
        return True
    else:
        return False