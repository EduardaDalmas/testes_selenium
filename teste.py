from selenium import webdriver

#iniciar o chrome
driver = webdriver.Chrome()

#abrir o site
driver.get('https://www.saucedemo.com/')

#pegar o elemento usuário
campo_usuario = driver.find_element('css selector', '#user-name').send_keys('standard_user')

#pegar o elemento senha
campo_senha = driver.find_element('css selector', '#password').send_keys('secret_sauce')

#pegar o elemento botão
botao_login = driver.find_element('css selector', '#login-button').click()

#fechar o navegador
driver.quit()