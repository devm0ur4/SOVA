# selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

## python
import threading
import shutil
from time import sleep

## projeto
from config.selenium_driver import DriverConfig
from config.paths import DOWNLOAD_DIR
from src import GUI
from src.automation import pdf_utils
from src.automation import web_scraper
from src.repo.fatura import Fatura
from src.repo import fatura, unidade

DriverConfig.create_driver()
driver = DriverConfig.get_driver()
url = "https://sso.sa.edenred.io/web/session/step/password?returnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fresponse_type%3Dcode%26client_id%3Dfcfc49a2ff3b45ef9c5f245b37b4d567%26state%3Dc0Jib0xEWmY3akRxcnVOUEhySEtlOU84YmtaYngyMEFWODBKMnYudnl0QVow%26redirect_uri%3Dhttps%253A%252F%252Fplataforma.ticketlog.com.br%252Flogin-callback%26scope%3Dopenid%2520profile%2520email%2520portal-fleet-and-mobility-ms_application-mfa%2520offline_access%26code_challenge%3DPJXv1O2fBIfQdgCHAGOIGdcRGzJ3mVyJOpQFwYw9djY%26code_challenge_method%3DS256%26nonce%3Dc0Jib0xEWmY3akRxcnVOUEhySEtlOU84YmtaYngyMEFWODBKMnYudnl0QVow%26acr_values%3Dtenant%253Abr-fleet-mobility"

def run():
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
                    GUI.kill("NÃO FOI POSSÍVEL INICIAR A APLICAÇÃO, ENCERRANDO O SISTEMA...")

                GUI.updateStatus("Site carregado com sucesso.")

                ## Fazendo login manualmente
                GUI.waitForOkButton('Faça o login até a página principal da TICKETLOG, quando concluído, aperte OK')

                ## Login realizado com sucesso
                GUI.updateStatus("Login realizado com sucesso.")
                GUI.updateStatus("Agora vamos começar com a automatização...")

                ## Iniciando coleta de informações
                units = unidade.readAll()

                ## Configurando antes de iniciar o looping
                web_scraper.startScrapper()
                web_scraper.resetting()

                ## esperando a página carregar completamente
                WebDriverWait(driver, 10).until(
                        lambda d: d.execute_script("return document.readyState") == "complete"
                    )
                
                web_scraper.switchBranch('236886')
                GUI.updateStatus("Configuração inicial concluída.") 

                ## coletando informações das faturas
                for unit in units: 
                    ## resetando para a página inicial
                    web_scraper.resetting()

                    GUI.updateStatus('Retornando à página principal')

                    fat = Fatura()

                    ## selecionando a unidade
                    GUI.updateStatus(f'Selecionando a unidade {unit[0]}')
                    web_scraper.switchBranch(unit[0])

                    ## coletando as informações da fatura na tabela
                    GUI.updateStatus(f'Coletando informações da fatura da unidade {unit[0]}')
                    infos = web_scraper.scrapTable()

                    if infos != False:
                        fat.vencimento = infos[0]
                        fat.valor_boleto = float(infos[1])
                        fat.nf = infos[2]

                        ## baixando os PDFs
                        GUI.updateStatus('Baixando os PDFs...')
                        web_scraper.downloadPDFs()

                        GUI.updateStatus('PDFs baixados com sucesso.')

                        ## mesclando os PDFs
                        pdfs_merge = pdf_utils.merge()
                        GUI.updateStatus('PDFs mesclados com sucesso.')

                        ## apagando os PDFs antigos
                        for item in DOWNLOAD_DIR.iterdir():
                            if item.is_file() or item.is_symlink():
                                item.unlink()
                            elif item.is_dir():
                                shutil.rmtree(item)

                        ## extraindo as informações do PDF
                        GUI.updateStatus('Extraindo as informações do PDF...')
                        pdf_infos = pdf_utils.read_pdf(pdfs_merge)  

                        ## guardando ultimas informações
                        GUI.updateStatus('Informações extraídas com sucesso.')
                        fat.data_emissao = pdf_infos['data_emissao']
                        fat.valor_total = pdf_infos['valor_total']

                        ## renomeando fatura
                        pdfs_merge.rename(f'{unit[0]} - {unit[3]} - NF {fat.nf} - {fat.vencimento} - RATEIO')

                        ## inserindo no banco de dados
                        fatura.insert(fat)


                    elif infos == 'paid':
                        GUI.updateStatus(f'A fatura da unidade {unit[0]} já foi paga. Pulando para a próxima unidade.')
                        continue
                    else:
                        raise Exception("Não foi possível coletar as informações da fatura.")


                
            except Exception as e:
                GUI.updateStatus(f"ERRO : {e}")
                GUI.updateStatus("ENCERRANDO O SISTEMA...")
                sleep(3)
                GUI.kill()
                
if __name__ == "__main__":
    run()