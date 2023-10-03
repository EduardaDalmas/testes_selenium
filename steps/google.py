from behave import *
from pages.google import *

componentesGoogle = ComponentesGoogle()
googleResultados = GoogleResultados(driver)

@given(u'que acesso a página do Google')
def step_impl(context):
    googleResultados.acessar_pagina('https://www.google.com.br')


@given(u'que eu preencho a barra de pesquisar com Grêmio')
def step_impl(context):
    googleResultados.escrever_texto()


@when(u'eu clicar no botão de pesquisar')
def step_impl(context):
    googleResultados.clicar_pesquisar()


@then(u'devo visualizar os resultados da pesquisa')
def step_impl(context):
    googleResultados.visualizar_resultados(), 'Grêmio - Pesquisa Google'