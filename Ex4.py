import requests
import time
import json

#Создаем задачу
response1 = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job')

#берем параметры из ответа
json_result1 = json.loads(response1.text)
secs = json_result1['seconds']
payload = {"token": json_result1['token']}

#Делаем запрос до того, как задача готова
response2 = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params=payload)
json_result2 = json.loads(response2.text)

#Проверяем, что поле status корректное
if json_result2['status'] == 'Job is NOT ready':
    print("Задача еще не готова!")
else:
    print("Что-то пошло не так")

#Ждем заданное количество секунд
time.sleep(secs)

#Делаем запрос после заданного количства секунд - задача должна быть готова
response3 = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params=payload)
json_result3 = json.loads(response3.text)

#Проверяем, что в ответе на этот раз есть переменная result
if 'result' in json_result3.keys():
    print("Поле result присутствует в ответе")
else:
    print("Ошибка! Поле result нет в ответе!")

#Проверяем, что поле status содержит информацию о том, что задача готова
if json_result3['status'] == 'Job is ready':
    print("Задача готова!")
else:
    print("Что-то пошло не так")

