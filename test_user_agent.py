import pytest
import requests
import json

class TestUserAgent:

    user_agent_string = [
        ("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
         'Mobile',  'No', 'Android', 1),
        ('Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1',
         'Mobile', 'Chrome', 'iOS', 2),
        ('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
         'Googlebot', 'Unknown', 'Unknown', 3),
        ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0',
         'Web', 'Chrome', 'No', 4),
        ('Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
         'Mobile', 'No', 'iPhone', 5)
    ]

    @pytest.mark.parametrize('user_agent', user_agent_string)
    def test_user_agent(self, user_agent):

        response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check",
                                headers={"User-Agent":user_agent[0]})

        response_dict = response.json()
        platform = response_dict['platform']
        browser = response_dict['browser']
        device = response_dict['device']
        assert platform == user_agent[1], \
            f"Platform {platform} in response {user_agent[4]} doesn't match {user_agent[1]}"
        assert browser == user_agent[2], \
            f"Browser {browser} in response {user_agent[4]} doesn't match {user_agent[2]}"
        assert device == user_agent[3], \
            f"Device {device} in response {user_agent[4]} doesn't match {user_agent[3]}"