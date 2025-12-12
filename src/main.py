from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
url = "https://sso.sa.edenred.io/web/session/step/password?returnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fresponse_type%3Dcode%26client_id%3Dfcfc49a2ff3b45ef9c5f245b37b4d567%26state%3Dc0Jib0xEWmY3akRxcnVOUEhySEtlOU84YmtaYngyMEFWODBKMnYudnl0QVow%26redirect_uri%3Dhttps%253A%252F%252Fplataforma.ticketlog.com.br%252Flogin-callback%26scope%3Dopenid%2520profile%2520email%2520portal-fleet-and-mobility-ms_application-mfa%2520offline_access%26code_challenge%3DPJXv1O2fBIfQdgCHAGOIGdcRGzJ3mVyJOpQFwYw9djY%26code_challenge_method%3DS256%26nonce%3Dc0Jib0xEWmY3akRxcnVOUEhySEtlOU84YmtaYngyMEFWODBKMnYudnl0QVow%26acr_values%3Dtenant%253Abr-fleet-mobility"


try:
    ## tenta carregar o site
    driver.get(url)
    sleep(10)

    ## identifica os elementos
    user = driver.find_element(By.XPATH, "//input[@id='Username']")
    if not user:
        raise Exception("Elemento 'user' nao encontrado")

    password = driver.find_element(By.XPATH, "//input[@id='Password']")
    if not password:
        raise Exception("Elemento 'password' nao encontrado") 
    
    button = driver.find_element(By.XPATH, "//button[@id='login']")
    if not button:
        raise Exception("Elemento 'button' nao encontrado")



except Exception as e:
    print(f"ERRO : {e}")