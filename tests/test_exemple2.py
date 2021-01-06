import random
from unittest import mock

import requests

from monapp.exemple2 import get_random_pizzas


def test_get_random_izzas_returns_correct_names(monkeypatch):
    product1, product2 = products = ['My product 1', 'My product 2']

    # mock pour requests.get()
    class MockRequestResponse:
        status_code = 200

        def json(self):
            return {
                "products": [{"product_name": product} for product in products]
            }

    def mock_get(*args, **kwargs):
        mock_get.params = {"args": args, "kwargs": kwargs}
        return MockRequestResponse()

    # mock pour random.sample()
    def mock_sample(liste, k):
        mock_sample.called = True
        return liste[:k]

    mock_sample.called = False

    # monkey patching de requests.get
    monkeypatch.setattr('requests.get', mock_get)

    # monkey patching de random.sample
    monkeypatch.setattr('random.sample', mock_sample)

    assert get_random_pizzas(2) == products
    assert mock_sample.called
    assert mock_get.params['args'] == (
        'https://fr.openfoodfacts.org/cgi/search.pl',
    )
    assert mock_get.params['kwargs'] == {
        'params': {
            "action": "process",
            "json": 1,
            "tagtype_0": "categories",
            "tag_contains_0": "contains",
            "tag_0": "pizzas",
            "page_size": 1000,
        }
    }


def test_get_random_izzas_returns_correct_names_with_mock(mocker):
    product1, product2 = products = ['My product 1', 'My product 2']

    # mock pour requests.get()
    mock_get = mocker.patch('requests.get')
    mock_get.return_value.status_code = 200  # requests.get().status_code
    mock_get.return_value.json.return_value = {
        "products": [{"product_name": product} for product in products]
    }

    mock_sample = mocker.patch('random.sample')
    mock_sample.return_value = products[:2]

    assert get_random_pizzas(2) == products
    mock_get.assert_called_once_with(
        'https://fr.openfoodfacts.org/cgi/search.pl',
        params={"error": True},
    )
    mock_get.assert_called()


def test_get_random_izzas_returns_behaves_correctly_if_status_not_ok(mocker):
    product1, product2 = products = ['My product 1', 'My product 2']

    # mock pour requests.get()
    mock_get = mocker.patch('requests.get')
    mock_get.return_value.status_code = 404

    mock_sample = mocker.patch('random.sample')
    mock_sample.return_value = products[:2]

    assert get_random_pizzas(2) == []
