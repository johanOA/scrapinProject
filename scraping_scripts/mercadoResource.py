# Usar BeautifulSoup para analizar el HTML y extraer los precios y nombres de los productos
from bs4 import BeautifulSoup
from scraping_scripts.toJson import save_to_json

def mercadoGetRources(page_source):
    soup = BeautifulSoup(page_source, 'html.parser')

    products = soup.find_all('div', {'ui-search-result__wrapper'})

    # Lista para almacenar los productos como tuplas
    product_list = []

    for product in products:
        # Extraer el nombre y el precio del producto
        title = product.find('h2', {'class': 'poly-box poly-component__title'})
        price = product.find('span', {'class': 'andes-money-amount__fraction'})

        if title and price:
            product_name = title.get_text(strip=True)  # Limpiar espacios en blanco
            product_price = price.get_text(strip=True)  # Limpiar espacios en blanco
                    
            # Guardar como tupla
            product_list.append((product_name, product_price))

        # Imprimir la lista de productos
        for name, price in product_list:
                print(f"Producto: {name}, Precio: {price}")

    save_to_json(product_list, "mercado.json")

