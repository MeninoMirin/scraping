from flask import Flask, render_template
import scrape

app = Flask(__name__)

@app.route('/')
def index():
    try:
        resultados = scrape.execute_scraping()
        return render_template('index.html', resultados=resultados)
    except Exception as e:
        return str(e)  # Exibir o erro no navegador (para depuração)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
