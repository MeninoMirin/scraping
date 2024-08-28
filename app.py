import os
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from flask import Flask, jsonify

app = Flask(__name__)

# Obter credenciais do Firebase a partir das variáveis de ambiente
firebase_creds = json.loads(os.environ.get('FIREBASE_CREDS', '{}'))

cred = credentials.Certificate(firebase_creds)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://banco-8c10d-default-rtdb.firebaseio.com/'
})

@app.route('/')
def index():
    try:
        # Aqui você pode adicionar qualquer lógica que desejar para a API
        return jsonify({'message': 'API funcionando corretamente!'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
