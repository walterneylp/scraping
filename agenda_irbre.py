from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as CondicaoEsperada
from selenium.webdriver.common.keys import Keys
import time


class CursoAutomacao:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        chrome_options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', options=chrome_options)
        self.wait = WebDriverWait(
            driver=self.driver,
            timeout=10,
            poll_frequency=1,
            ignored_exceptions=[
                NoSuchElementException,
                ElementNotVisibleException,
                ElementNotSelectableException
            ]
        )

    def Iniciar(self):
        self.driver.get('https://ri.irbre.com/')

        ''' fechar popup '''
        btn_fechar = self.driver.find_element_by_xpath(
            '//*[@id="popup-fancybox"]/div/a')
        btn_fechar.click()

        ''' selecionar calendário '''
        agenda = self.driver.find_element_by_xpath(
            '//*[@id="toolbox"]/ul/li[1]/a')
        agenda.click()

        ''' procura eventos '''
        for x in range(1, 50):
            try:
                eventos_titulo = self.driver.find_element_by_xpath(
                    '//*[@id="eventos-futuros"]/div/div['+str(x)+']/div/div[1]/div[1]')
                eventos_data = self.driver.find_element_by_xpath(
                    '//*[@id="eventos-futuros"]/div/div['+str(x)+']/div/div[2]/div[1]')
                print(eventos_titulo.text)
                print(eventos_data.text)
            except:
                pass


curso = CursoAutomacao()
curso.Iniciar()
