import pytest
from ..lib.base_case import BaseCase
from ..lib.assertions import Assertions
from ..lib.my_requests import MyRequests
import allure


class TestUserCreate(BaseCase):
    exclude_params = {
        'username',
        'firstName',
        'lastName',
        'email',
        'password'
    }
    data = {
        'username': 'fakeuser',
        'firstName': 'fake',
        'lastName': 'user',
        'email': '1@1.ru',
        'password': 'string'
    }

    def test_create_user_incorrect_email(self):
        data = self.data.copy()
        data['email'] = 'wrong_email'
        response = MyRequests.post(
            '/user/',
            data=data
        )

        Assertions.assert_text_response_is(
            response,
            "Invalid email format"
        )

    @pytest.mark.parametrize('condition', exclude_params)
    def test_create_user_when_parameter_is_missing(self, condition):
        data = self.data.copy()
        data.pop(condition)
        response = MyRequests.post(
            '/user/',
            data=data
        )
        Assertions.assert_text_response_is(
            response,
            f"The following required params are missed: {condition}"
        )

    def test_create_user_with_short_name(self):
        data = self.data.copy()
        data['username'] = 'f'
        response = MyRequests.post(
            '/user/',
            data=data
        )
        Assertions.assert_text_response_is(
            response,
            f"The value of 'username' field is too short"
        )

    def test_create_user_with_long_name(self):
        data = self.data
        data['username'] = 'В соответствующем классе TestUserRegister, который мы создали на уроке, необходимо написать больше тестов на создающий пользователя POST-метод: https://playground.learnqa.ru/api/user/В соответствующем классе TestUserRegister, который мы создали на уроке, необходимо написать больше тестов на создающий пользователя POST-метод: https://playground.learnqa.ru/api/user/В соответствующем классе TestUserRegister, который мы создали на уроке, необходимо написать больше тестов на создающий пользователя POST-метод: https://playground.learnqa.ru/api/user/',

        response = MyRequests.post(
            '/user/',
            data=data
        )
        Assertions.assert_text_response_is(
            response,
            f"The value of 'username' field is too long"
        )
