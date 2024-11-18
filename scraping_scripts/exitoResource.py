# Usar BeautifulSoup para analizar el HTML y extraer los precios y nombres de los productos
from bs4 import BeautifulSoup
from scraping_scripts.toJson import save_to_json

def exitoGetRources(page_source):
    soup = BeautifulSoup(page_source, 'html.parser')

    products = soup.find_all('div', {'class': 'productCard_contentInfo__CBBA7 productCard_column__Lp3OF'})

    # Lista para almacenar los productos como tuplas
    product_list = []

    for product in products:
        # Extraer el nombre y el precio del producto
        title = product.find('p', {'class': 'styles_name__qQJiK'})
        price = product.find('p', {'class': 'ProductPrice_container__price__XmMWA'})

        if title and price:
            product_name = title.get_text(strip=True)  # Limpiar espacios en blanco
            product_price = price.get_text(strip=True)  # Limpiar espacios en blanco
                    
            # Guardar como tupla
            product_list.append((product_name, product_price))

        # Imprimir la lista de productos
        for name, price in product_list:
                print(f"Producto: {name}, Precio: {price}")
    
    save_to_json(product_list, "exito.json")