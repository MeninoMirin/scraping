from flask import Flask, render_template
import scrape

app = Flask(__name__)

@app.route('/')
def index():
    resultados = scrape.execute_scraping()
    return render_template('index.html', resultados=resultados)

if __name__ == '__main__':
    app.run(debug=True)
