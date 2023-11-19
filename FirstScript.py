import requests
from json.decoder import JSONDecodeError

payload = {"name": "User"}
response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
parsed_response_text = response.json()
print(parsed_response_text["answer"])

response2 = requests.get("https://playground.learnqa.ru/api/get_text")
try:
    parsed_response_text = response2.json()
    print(parsed_response_text["answer"])
except JSONDecodeError:
    print("Response is not a JSON format")

response3 = requests.post("https://playground.learnqa.ru/api/check_type", data = {"params":"value1"})
print(response3.status_code)

response4 = requests.post("https://playground.learnqa.ru/api/something")
print(response4.status_code)

response5 = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
first_response = response5.history[0]
second_response = response5
print(first_response.url)
print(second_response.url)
print(response5.status_code)

headers = {"some_headers":"123"}
response6 = requests.post("https://playground.learnqa.ru/api/show_all_headers", headers=headers)
print(response6.text)
print(response6.headers)

payload={"login":"secret_login", "password":"secret_pass2"}

response7 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)

print(response7.text)
print(response7.status_code)
print(dict(response7.cookies))
print(response7.headers)

cookie_value = response7.cookies.get('auth_cookie')
cookies = {}
if cookie_value is not None:
    cookies.update({'auth_cookie': cookie_value})

response8 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)

print(response8.text)

