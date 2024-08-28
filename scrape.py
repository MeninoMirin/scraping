import os
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from flask import Flask, jsonify
from time import sleep

app = Flask(__name__)

# Obter credenciais do Firebase a partir das variáveis de ambiente
firebase_creds = json.loads(os.environ.get('FIREBASE_CREDS', '{}'))

cred = credentials.Certificate(firebase_creds)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://banco-8c10d-default-rtdb.firebaseio.com/'
})

@app.route('/')
def index():
    options = Options()
    options.add_argument('--headless')  # Executa o navegador em modo headless
    options.add_argument('--disable-logging')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get('https://estrelabet.com/ptb/bet/main')
        sleep(10)
        data = driver.title
        driver.quit()
        
        # Referência para o banco de dados
        ref = db.reference('resultados')
        ref.push({'resultado': data})

        return jsonify({'data': data})
    
    except Exception as e:
        print(f"Erro durante a execução do Selenium: {e}")
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
