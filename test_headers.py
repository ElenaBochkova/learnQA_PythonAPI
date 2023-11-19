import requests
import pytest


class TestHomework:

    def test_headers(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")

        assert 'x-secret-homework-header' in response.headers, f"There is no x-secret-homework-header header in headers"

        homework_header = response.headers['x-secret-homework-header']

        assert homework_header == 'Some secret value', f"The header 'x-secret-homework-header' contains wrong value"
