
from flask import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from scraping_scripts.amazonResource import amazonGetResources
from scraping_scripts.exitoResource import exitoGetRources
from scraping_scripts.mercadoResource import mercadoGetRources
from scraping_scripts.alkostoResource import alkostoGetRources

import time

def scrape_prices_safari(url, search_query):
    
    driver = webdriver.Safari()

    if "amazon" in url:
        cookies_path = "./scraping_scripts/cookies/cookiesAmazon.json"
    elif "exito" in url:
        cookies_path = "./scraping_scripts/cookies/cookiesExito.json"
    elif "mercadolibre" in url:
        cookies_path = "./scraping_scripts/cookies/cookiesMercado.json"
    elif "alkosto" in url:
        cookies_path = "./scraping_scripts/cookies/cookiesAlkosto.json"

    driver.maximize_window()

    try:
        driver.get(url)

        time.sleep(2)

        with open(cookies_path, 'r') as file:
            cookies = json.load(file)

        for cookie in cookies:
            # Renombrar expirationDate a expiry y verificar campos requeridos
            if 'expirationDate' in cookie:
                cookie['expiry'] = int(cookie.pop('expirationDate'))

            # Eliminar campos no soportados o problemáticos
            cookie = {k: v for k, v in cookie.items() if k in ['name', 'value', 'domain', 'path', 'secure', 'httpOnly', 'expiry']}

            try:
                driver.add_cookie(cookie)
            except Exception as e:
                print(f"Error al agregar cookie {cookie.get('name', '(sin nombre)')}: {e}")


        driver.refresh()
        
        time.sleep(5)

        # Intentar encontrar el campo de búsqueda usando los selectores
        search_box = None
        
        css_search = ['[data-testid="store-input"]',
                    '[aria-label="search"]', 
                    '[placeholder="Buscar en exito.com"]']
        
        id_search = ['twotabsearchtextbox', 
                    'cb1-edit', 
                    'autocomplete-0-input']

        for selector in css_search + id_search:
            try:
                search_box = driver.find_element(By.CSS_SELECTOR, selector) if "data" in selector else driver.find_element(By.ID, selector)
                if search_box:
                    break
            except:
                continue

        if search_box:
            search_box.send_keys(search_query)
            search_box.send_keys(Keys.RETURN)
        else:
            print("No se encontró un campo de búsqueda.")

        time.sleep(5)

        if "exito" in url:
            time.sleep(5)

        print(f"Título de la página: {driver.title}")

        # Obtener el HTML de la página
        page_source = driver.page_source

        if "amazon" in url:
            amazonGetResources(page_source)
        elif "exito" in url:
            exitoGetRources(page_source)
        elif "mercado" in url:
            mercadoGetRources(page_source)
        elif "alkosto" in url:
            alkostoGetRources(page_source)

    except Exception as e:
        print(f"Ocurrió un error: {e}")
    finally:
        print("Es toda mano")



# https://www.mercadolibre.com.co
# Ejemplo de uso
#url = "https://www.mercadolibre.com.co"
#url = "https://www.amazon.com"
#url = "https://www.exito.com"
#url = "https://www.alkosto.com"
#search_query = "televisor"
#scrape_prices_safari(url, search_query)