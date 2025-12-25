## selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

##python
from pyparsing import Path
from time import sleep
import time

##project
import config.selenium_driver as selenium_driver
from config.paths import DOWNLOAD_DIR, RAW_DIR


## define o driver
driver_config = selenium_driver.DriverConfig
driver = driver_config.get_driver()

FINANCEIRO_URL = 'https://plataforma.ticketlog.com.br/legacy?link=R29vZE1hbmFnZXJTU0wvY29tdW0vZm9ybW5vdGFmaXNjYWxlbGV0cm9uaWNhLmNmbQ%3D%3D'
    
## switchBranch - muda a filial que vai ser acessada
def switchBranch(branchCode):
    ## clica no perfil
    driver.click("//a[contains(@aria-label, 'perfil')]")

    ## clica nas opções
    driver.click("//a[contains(@data-cy, 'navbar-access-options-link')]")

    ## pesquisa a filial
    driver.send_keys("//input[contains(@data-cy, 'access-options-modal-search-input')]", branchCode)

    ## seleciona a filial 
    driver.click(f"//p[@data-cy='item-select-client-code' and text()='{branchCode}']/ancestor::td")

    ## clica no botão selecionar
    driver.click("//button[@data-cy='data-access-select-button']")

    ## aguarda a mudança ser feita
    sleep(5)

## scrapTable - coleta as informações da tabela
def scrapTable():
    driver.get(FINANCEIRO_URL)

    row = driver_config.get_element("//table//tbody/tr[1]")

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
    ## clica no botão de gerar boletos
    driver_config.click("//a[contains(@onClick, 'aBoleto')]")

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

        
        ## acha o pdf e renomeia ele para 2.pdf
        """
        pdf2 = max(
            DOWNLOAD_DIR.glob("*.pdf"),
            key=lambda f: f.stat().st_mtime
        )

        pdf2.rename(DOWNLOAD_DIR / "2.pdf")
        """

        boleto_pdf.rename(DOWNLOAD_DIR / "2.pdf")

        ## volta para a pagina do financeiro
        driver.get(FINANCEIRO_URL)


        ## encontra o link de acesso ao NFe
        row = driver_config.get_element("//table//tbody/tr[1]")
        cols = row.find_elements(By.TAG_NAME, "td")
        col = cols[8]
        
        link = col.find_element(By.TAG_NAME, "a").get_attribute("href")

        ## entra no link de acesso à NFe
        driver.get(link)



    except Exception as e:
        driver.get('https://plataforma.ticketlog.com.br/home')
        print(f"Erro ao baixar PDF: {e}")
        return False
    

    
# TODO: def scrapper()
# toda lógica e execução da automação da parte do site - função com execução unica.

# TODO: def scrapAll()
# lista todas as unidades e faz a execução do scrapper em cada uma delas.


