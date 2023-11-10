import requests

response_without_method = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type')
print(response_without_method.text)
#Результат: Wrong method provided

payload = {"method": "HEAD"}
response_head = requests.head('https://playground.learnqa.ru/ajax/api/compare_query_type',
                                       params=payload)
print(response_head.text)
#Результат: пустой ответ

payload = {"method": "GET"}
response_get = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type',
                                       params=payload)
print(response_get.text)
#Результат: {"success":"!"}

combination = [{"method": "GET"}, {"method": "POST"}, {"method": "PUT"}, {"method": "DELETE"}]

for i in range(len(combination)):
    response_get = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type',
                                       params=combination[i])
    response_post = requests.post('https://playground.learnqa.ru/ajax/api/compare_query_type',
                                       data=combination[i])
    response_put = requests.put('https://playground.learnqa.ru/ajax/api/compare_query_type',
                                  data=combination[i])
    response_delete = requests.delete('https://playground.learnqa.ru/ajax/api/compare_query_type',
                                  data=combination[i])
    print(f"get with {combination[i]['method']} = {response_get.text}")
    print(f"post with {combination[i]['method']} = {response_post.text}")
    print(f"put with {combination[i]['method']} = {response_put.text}")
    print(f"delete with {combination[i]['method']} = {response_delete.text}")
#Неверный ответ только один: delete with GET = {"success":"!"}


