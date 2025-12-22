from pyparsing import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import time

## setup - cria o contexto da automação
def setup(driver, timeout=5):
    return {
        "driver": driver,
        "wait": WebDriverWait(driver, timeout)
    }


## switchBranch - muda a filial que vai ser acessada
def switchBranch(branchCode):

    perfil_btn = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@aria-label, 'perfil')]")
        )
    )
    perfil_btn.click()

    ## clica nas opções

    options_btn = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@data-cy, 'navbar-access-options-link')]")
        )
    )

    options_btn.click()

    ## pesquisa a filial

    branch_input = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//input[contains(@data-cy, 'access-options-modal-search-input')]")
        )
    )

    branch_input.send_keys(branchCode)

    ## seleciona a filial 
    option_td = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//p[@data-cy='item-select-client-code' and text()='206337']/ancestor::td"
            )
        )
    )

    option_td.click()

    ## clica no botão selecionar
    btn = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@data-cy='data-access-select-button']")
        )
    )

    btn.click()

    ## aguarda a mudança ser feita
    sleep(5)

## scrapTable - coleta as informações da tabela
def scrapTable():
    driver.get('https://plataforma.ticketlog.com.br/legacy?link=R29vZE1hbmFnZXJTU0wvY29tdW0vZm9ybW5vdGFmaXNjYWxlbGV0cm9uaWNhLmNmbQ%3D%3D')


    row = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//table//tbody/tr[1]")
        )
    )

    cols = row.find_elements(By.TAG_NAME, "td")

    if cols[3].text.strip() != "":
        vencimento = cols[2].text.strip()
        valor_boleto = cols[5].text.strip()
        nf = cols[8].text.strip()

        return vencimento, valor_boleto, nf


    else:
        driver.get('https://plataforma.ticketlog.com.br/home')
        return False


## downloadPDFs - baixar os pdfs
def downloadPDFs():
    boleto_btn = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@onClick, 'aBoleto')]")
        )
    )

    boleto_btn.click()

    ## caminhos dos diretórios 
    BASE_DIR = Path(__file__).resolve().parents[1]
    DOWNLOAD_DIR = BASE_DIR / "downloads"
    RAW = BASE_DIR / "storage/raw"

    try:
        timeout = 10

        end = time.time() + timeout
        pdfs = list(DOWNLOAD_DIR.glob("*.pdf"))

        boleto_pdf ## retorna o boleto 
        while time.time() < end:
            if pdfs:
                global boleto_pdf 
                boleto_pdf = pdfs[0]
                return True
    
            time.sleep(0.5)

        ## move o pdf para storage/raw


    except Exception as e:
        driver.get('https://plataforma.ticketlog.com.br/home')
        return False
    

    
# TODO: def scrapper()
# toda lógica e execução da automação da parte do site - função com execução unica, 
# a lógica de execução multipla vai acontecer lá no main.py



