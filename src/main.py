from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading
from time import sleep
import GUI
import auth.login as auth_login

driver = webdriver.Chrome()
url = "https://sso.sa.edenred.io/web/session/step/password?returnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fresponse_type%3Dcode%26client_id%3Dfcfc49a2ff3b45ef9c5f245b37b4d567%26state%3Dc0Jib0xEWmY3akRxcnVOUEhySEtlOU84YmtaYngyMEFWODBKMnYudnl0QVow%26redirect_uri%3Dhttps%253A%252F%252Fplataforma.ticketlog.com.br%252Flogin-callback%26scope%3Dopenid%2520profile%2520email%2520portal-fleet-and-mobility-ms_application-mfa%2520offline_access%26code_challenge%3DPJXv1O2fBIfQdgCHAGOIGdcRGzJ3mVyJOpQFwYw9djY%26code_challenge_method%3DS256%26nonce%3Dc0Jib0xEWmY3akRxcnVOUEhySEtlOU84YmtaYngyMEFWODBKMnYudnl0QVow%26acr_values%3Dtenant%253Abr-fleet-mobility"


try:
    # inicia o GUI em uma thread separada
    threading.Thread(target=GUI.startGUI).start()
    sleep(2)

    GUI.updateStatus("SOVA iniciado com sucesso.")
    GUI.updateStatus("Bem vindo ao SOVA!")

    # Iniciando site
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    except Exception as e:
        GUI.updateStatus("NÃO FOI POSSÍVEL INICIAR A APLICAÇÃO, ENCERRANDO O SISTEMA...")
        sleep(4)
        GUI.kill()

    GUI.updateStatus("Site carregado com sucesso.")
    ## Realiza o login
    _user, _password = auth_login.get_credentials()

    auth_login.perform_login(driver, _user, _password)
    while(auth_login.isLoggedIn(driver) == False):
        _user, _password = auth_login.get_credentials()
        auth_login.perform_login(driver, _user, _password)

  
    ## Login realizado com sucesso
    GUI.updateOrder("Aguarde mais instruções...")
    GUI.updateStatus("Login realizado com sucesso.")
    GUI.updateStatus("Agora vamos começar com a automatização...")

    
except Exception as e:
    GUI.updateStatus(f"ERRO : {e}")
    GUI.updateStatus("ENCERRANDO O SISTEMA...")
    sleep(3)
    GUI.kill()