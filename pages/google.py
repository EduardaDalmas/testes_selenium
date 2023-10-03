from behave import *
from nose.tools import *
from pages.google import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from browser import Browser

driver = webdriver.Chrome()

class ComponentesGoogle(object):
    barra_pesquisa = '[name="q"]'
    botao_pesquisa = '[name="btnK"]'
    visualizar_pesquisa = '[data-attrid="title"]'

class GoogleResultados():
    def __init__(self, driver):
        self.driver = driver

    def pegar_elemento(self, locator):
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def acessar_pagina(self, link):
        self.driver.get(link)

    def escrever_texto(self):
        self.pegar_elemento(ComponentesGoogle.barra_pesquisa).send_keys('Grêmio')

    def clicar_pesquisar(self):
        element = self.pegar_elemento(ComponentesGoogle.botao_pesquisa)
        WebDriverWait(self.driver, 20).until(EC.visibility_of(element))
        element.click()
    def visualizar_resultados(self):
        self.pegar_elemento(ComponentesGoogle.visualizar_pesquisa).is_displayed()