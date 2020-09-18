# --------------------------------
# --------------------------------

# MEU DISCORD É [  facury#0262   ]

# --------------------------------
# --------------------------------


import selenium # CASO VOCÊ NUNCA TENHA INSTALADO O SELENIUM, ESCREVA NO CMD DO WINDOWS --->  pip install selenium
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


url = "https://www.nike.com.br/Snkrs#estoque" # URL DO SITE QUE VOCÊ QUER CONSULTAR
driver = selenium.webdriver.Chrome() # VAI EXECUTAR O WEBDRIVER
driver.get(url) # NÃO MEXER
sleep(7) # O COMANDO SLEEP SERVE PARA 'ESPERAR' DETERMINADO TEMPO, EU RECOMENDO QUE DEIXEI IGUAL AO QUE EU DEIXEI

print('STARTING') # VAI PRINTAR NO CONSOLE DO PYTHON QUE COMEÇOU
while True: # BASICAMENTE UM LOOP PARA FICAR CHECKANDO O STOCK E ENVIANDO NO WHATS APP
    driver.get(url) 
    sleep(7)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # VAI DESCER ATÉ O FINAL DO SITE,PARA CARREGAR MAIS PRODUTOS
    sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # VAI DESCER ATÉ O FINAL DO SITE,PARA CARREGAR MAIS PRODUTOS
    sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # VAI DESCER ATÉ O FINAL DO SITE,PARA CARREGAR MAIS PRODUTOS
    sleep(2)
    lista = []  # AQUI VÃO SER ARMAZENADOS OS LINKS

    # IMPORTANTE IMPORTANTE 

    hrefs = driver.find_elements_by_class_name("aspect-radio-box")  # MUDE PARA O ELEMENTO DO PRODUTO DO SITE,QUALQUER DUVIDA MANDE UMA MENSAGEM PARA MIM

    # IMPORTANTE IMPORTANTE 

    for fire in range (1, len(hrefs), 1):
        lista.append(hrefs[fire].get_attribute("href")) # VAI ARMAZENAR OS LINKS NA LISTA ,CASO QUEIRA TROCAR, MUDE O ATRIBUTO
        fire += 1

    # PASSOS IMPORTANTES 

    # 1 - NA MESMA SEÇÃO DO GOOGLE VOCÊ TEM QUE ABRIR O WHATS APP WEB 

    # 2 - DEPOIS QUE VOCÊ ESCANEAR O CODIGO E LOGAR, NAO CLIQUE EM NADA

    # 3 - VOLTE PARA A ABA DO PRIMEIRO SITE

    # 4 - A PARTIR DAQUI O COMPUTADOR VAI FAZER TUDO SOZINHO ATÉ QUE VOCÊ FECHAR O PROGRAMA

    print('Faltam 30 Segundos,Lembre de seguir os passos comentados no código')
    sleep(30)
    driver.switch_to_window(driver.window_handles[1]) # VAI MUDAR A GUIA PARA A DO WHATS APP, POR ISSO DEPOIS DE LOGAAR NO WHATS APPP, VOCÊ TERA QUE VOLTAR PARA ABA ANTERIOR
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]') # ELEMENTO DE PESQUISA WHATS APP
    sleep(6)
    campo_pesquisa.click()
    campo_pesquisa.send_keys('O contato da pessoa aqui') # O NOME DO CONTATO EXATO
    campo_pesquisa.send_keys(Keys.ENTER)
    sleep(3)
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]') # CAMPO DA MENSAGEM
    for start_msg in range(0, len(lista), 1): # AQUI É O LOOP PARA ENVIAR TODOS OS LINKS DA LISTA 
        campo_mensagem[1].click()
        sleep(2)
        campo_mensagem[1].send_keys(lista[start_msg])
        campo_mensagem[1].send_keys(Keys.ENTER)
        start_msg += 1
    campo_mensagem[1].send_keys(f'Foram encontrados {len(hrefs)} Produtos') # QUANTIDADE DE PRODUTOS
    campo_mensagem[1].send_keys(Keys.ENTER)
    campo_mensagem[1].send_keys('PROGRAMA FINALIZADO | EM 30 MINUTOS ESTAREI ENVIANDO NOVAMENTE')
    campo_mensagem[1].send_keys(Keys.ENTER)
    driver.switch_to_window(driver.window_handles[0]) # VAI VOLTAR PARA A ABA DOS PRODUTOS
    sleep(1800) # TEMPO DE ESPERA PARA RECOMEÇAR O PROCESSO EM SEGUNDOS


# CASO VOCÊ NÃO ESTEJA CONSEGUINDO, MANDE UMA MENSAGEM NO MEU DISCORD  facury#0262













