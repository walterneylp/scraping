from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
# roda o chromedriver em modo headless(em segundo plano)
chrome_options.add_argument("--headless")
# Opção obrigatória de compatibilidade para fazer funcionar no Mac OS
chrome_options.add_argument('--no-sandbox')
# Opção obrigatória de compatibilidade para fazer funcionar no Windows
chrome_options.add_argument('--disable-gpu')
# Escolha a resolução a ser usada por seu navegador.(importante sendo que resoluções muito baixas, transformam o navegador em modo mobile)
chrome_options.add_argument('window-size=1920x1080')
driver = webdriver.Chrome(
    executable_path=r'./chromedriver', options=chrome_options)
driver.get('https://www.google.com.br')
print(driver.current_url)
