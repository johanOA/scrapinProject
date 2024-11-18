from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from scraping_scripts import prices


app = Flask(__name__)

CORS(app)

# Ruta para la interfaz principal que mostrará el archivo index.html
@app.route('/')
def main_menu():
    return render_template('index.html')

# Ruta para manejar las solicitudes de scraping de precios
@app.route('/api/scrape/precios', methods=['POST'])
def scrape_precios():
    # Recibimos el nombre del scraper y la categoría desde el formulario
    scraper_name = request.json.get('scraperName', '')
    category = request.json.get('category', '')
    url = request.json.get('url','')
    
    result = prices.scrape_prices_safari(url, scraper_name)
    
    return jsonify({"mensaje": result})

# Ruta para manejar las solicitudes de scraping de noticias
@app.route('/api/scrape/noticias', methods=['POST'])
def scrape_noticias():
    # Recibimos el nombre del scraper y la categoría desde el formulario
    scraper_name = request.json.get('scraperName', '')
    category = request.json.get('category', '')
    url = request.json.get('url','')

    # Aquí iría la lógica para hacer scraping de noticias con la categoría seleccionada
    # Simulando el scraping de noticias
    result = f"Scraping iniciado para {scraper_name} en la categoría {category}. y URL {url} Noticias obtenidas..."
    
    return jsonify({"mensaje": result})

# Ruta para manejar las solicitudes de scraping de redes sociales
@app.route('/api/scrape/redes_sociales', methods=['POST'])
def scrape_redes_sociales():
    # Recibimos el nombre del scraper y la categoría desde el formulario
    scraper_name = request.json.get('scraperName', '')
    category = request.json.get('category', '')
    url = request.json.get('url','')

    # Aquí iría la lógica para hacer scraping de redes sociales
    # Simulando el scraping de redes sociales
    result = f"Scraping iniciado para {scraper_name} en la categoría {category}. y URL {url} Datos de redes sociales obtenidos..."
    
    return jsonify({"mensaje": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=15000)
