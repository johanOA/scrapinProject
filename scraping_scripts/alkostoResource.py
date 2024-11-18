# Usar BeautifulSoup para analizar el HTML y extraer los precios y nombres de los productos
from bs4 import BeautifulSoup
from scraping_scripts.toJson import save_to_json

def alkostoGetRources(page_source):
    soup = BeautifulSoup(page_source, 'html.parser')

    products = soup.find_all('li', {'ais-InfiniteHits-item product__item js-product-item js-algolia-product-click'})

    # Lista para almacenar los productos como tuplas
    product_list = []

    for product in products:
        # Extraer el nombre y el precio del producto
        title = product.find('h3', {'class': 'product__item__top__title js-algolia-product-click js-algolia-product-title'})
        price = product.find('span', {'class': 'price'})

        if title and price:
            product_name = title.get_text(strip=True)  # Limpiar espacios en blanco
            product_price = price.get_text(strip=True)  # Limpiar espacios en blanco
                    
            # Guardar como tupla
            product_list.append((product_name, product_price))

        # Imprimir la lista de productos
        for name, price in product_list:
                print(f"Producto: {name}, Precio: {price}")