from browser import Browser
from multiprocessing import Process

#Executar antes de todos os testes
def before_all(context):
    context.browser = Browser()

#Executar depois de todos os testes
def after_all(context):
    context.browser.fechar_browser()

#Executar depois de cada cenário
def alter_scenario(context, scenario):
    context.browser.limpar_browser()
