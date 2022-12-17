from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.command import Command
from drivers import *
from time import sleep

class ExportReport:
    def __init__(self):
        self.__driver = iniciar_driver_solar()
        

    # Função que realiza o processamento do sistema
    def processar(self, banda):
        self.__driver.get('https://www.palcomp3.com.br')
        self.pesquisa(banda)
        
         
    def pesquisa(self, banda):
        campo_pesquisa = WebDriverWait(self.__driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#js-startInputSearch')))
        campo_pesquisa.click()
        
        clica_inpt = WebDriverWait(self.__driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#search-container > div._2GCGi > div > input')))
        clica_inpt.click()
        
        self.preencher_pesquisa(clica_inpt, banda)
        self.clica_nome()
        
    def clica_nome(self):
        click_nome = self.__driver.find_element(By.XPATH, '//*[@id="search-container"]/div[2]/div[2]/div[1]/div[1]/div/a')
        sleep(1)
        click_nome.click()
        
        
        
    # Preenche o elemento indicado com o texto informado
    def preencher_pesquisa(self, input, text):
            sleep(1)
            input.click()
            sleep(0.5)
            for l in text:
                input.send_keys(l)
                sleep(0.075)


            
    # # Limpa o campo de texto
    # def __limpar_campo(self, input):
    #     sleep(1.5)
    #     input.click()
    #     sleep(0.5)
    #     input.send_keys(Keys.CONTROL, 'a')
    #     sleep(0.25)
    #     input.send_keys(Keys.DELETE)