import pytest
import requests

class TestCooikes:

    def test_cookies(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")

        returned_cookie = response.cookies.get("HomeWork")

        assert returned_cookie == 'hw_value', "Wrong cookie value returned"