from ..lib.my_requests import MyRequests
from ..lib.base_case import BaseCase
from ..lib.assertions import Assertions
import allure

@allure.epic("Test on user deletion")
class TestUserDelete(BaseCase):

    @allure.feature("Deletion of forbidden user")
    def test_delete_secure_user(self):
        data = {
            'email': 'vinkotov@example.com',
            "password": '1234'
        }

        with allure.step("Step 1. Login as forbidden user"):
            response1 = MyRequests.post("/user/login", data=data)
            auth_sid = self.get_cookie(response1, "auth_sid")
            token = self.get_header(response1, "x-csrf-token")

        with allure.step("Step 2. Delete forbidden user"):
            response2 = MyRequests.delete("/user/2",
                                      headers={"x-csrf-token": token},
                                      cookies={"auth_sid": auth_sid},
                                      )

        with allure.step("Step 3. Assert that deletion failed"):
            Assertions.assert_code_status(response2, 400)
            Assertions.assert_text_response_is(
                response2,
                "Please, do not delete test users with ID 1, 2, 3, 4 or 5."
            )

    @allure.feature("Delete just created user")
    def test_delete_just_created_user(self):
        with allure.step("Step 1. Register new user"):
            register_data = self.prepare_registration_data()
            response1 = MyRequests.post("/user/", data=register_data)
            Assertions.assert_code_status(response1, 200)
            Assertions.assert_json_has_key(response1, "id")

            email = register_data['email']
            password = register_data['password']
            user_id = self.get_json_value(response1, "id")

        with allure.step("Step 2. Login as created user"):
            login_data = {
                'email': email,
                'password': password
            }
            response2 = MyRequests.post("/user/login", data=login_data)
            auth_sid = self.get_cookie(response2, "auth_sid")
            token = self.get_header(response2, "x-csrf-token")

        with allure.step("Step 3. Delete just created user"):
            response3 = MyRequests.delete(
                f"/user/{user_id}",
                headers={"x-csrf-token":token},
                cookies={"auth_sid": auth_sid}
            )
            Assertions.assert_code_status(response3, 200)

        with allure.step("Step 4. Get information about deleted user"):
            response4 = MyRequests.get(f"/user/{user_id}",
                                       headers={"x-csrf-token": token},
                                       cookies={"auth_sid": auth_sid})
            Assertions.assert_code_status(response4, 404)
            Assertions.assert_text_response_is(
                response4,
                'User not found'
            )

    @allure.feature("Delete when login as another user")
    def test_delete_another_user(self):
        with allure.step("Step 1. Register new user"):
            register_data = self.prepare_registration_data()
            response1 = MyRequests.post("/user/", data=register_data)
            Assertions.assert_code_status(response1, 200)
            Assertions.assert_json_has_key(response1, "id")
            email = register_data['email']
            password = register_data['password']
            user_id = self.get_json_value(response1, "id")

        with allure.step("Step 2. Register another new user"):
            register_data2 = self.prepare_registration_data()
            response2 = MyRequests.post("/user/", data=register_data2)
            Assertions.assert_code_status(response2, 200)
            Assertions.assert_json_has_key(response2, "id")

            user_id2 = self.get_json_value(response2, "id")

        with allure.step("Step 3. Login as first created user"):
            login_data = {
                'email': email,
                'password': password
            }
            response3 = MyRequests.post("/user/login", data=login_data)
            Assertions.assert_code_status(response3, 200)
            auth_sid = self.get_cookie(response3, "auth_sid")
            token = self.get_header(response3, "x-csrf-token")

        with allure.step("Step 4. Delete second created user user"):
            response4 = MyRequests.delete(
                f"/user/{user_id2}",
                headers={"x-csrf-token": token},
                cookies={"auth_sid": auth_sid}
            )
            Assertions.assert_code_status(response4, 400)



