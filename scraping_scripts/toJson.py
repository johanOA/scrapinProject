import json

def save_to_json(product_list, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        product_dicts = [{'name': name, 'price': price} for name, price in product_list]
        json.dump(product_dicts, f, ensure_ascii=False, indent=4)