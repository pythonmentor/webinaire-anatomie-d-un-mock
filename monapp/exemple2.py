import random

import requests


def get_random_pizzas(quantity=3):
    """Returns a list of pizza names.

    If request is not successful, returns an empty."""
    if quantity > 50:
        raise ValueError("max quantity is 50")
    products = []
    payload = {
        "action": "process",
        "json": 1,
        "tagtype_0": "categories",
        "tag_contains_0": "contains",
        "tag_0": "pizzas",
        "page_size": 1000,
    }
    response = requests.get(
        'https://fr.openfoodfacts.org/cgi/search.pl', params=payload
    )
    if response.status_code == 200:
        products = response.json()['products']

    return random.sample(
        [
            product['product_name']
            for product in products
            if 'product_name' in product
        ],
        k=quantity,
    )


if __name__ == "__main__":
    print(get_random_pizzas(5))