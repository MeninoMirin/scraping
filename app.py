from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from flask import Flask, jsonify
from time import sleep

app = Flask(__name__)

@app.route('/')
def index():
    # Configuração do Selenium
    options = Options()
    options.add_argument('--headless')  # Executa o navegador em modo headless
    options.add_argument('--disable-logging')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Seu código de automação aqui
    driver.get('https://estrelabet.com/ptb/bet/main')
    sleep(10)  # Exemplo de espera para garantir que o site carregue

    # Coleta de dados
    data = driver.title  # Exemplo de coleta de dados, aqui você deve coletar o que precisa

    driver.quit()  # Fechar o driver depois da coleta

    return jsonify({'data': data})

if __name__ == '__main__':
    app.run()
