import requests

response = requests.get('https://playground.learnqa.ru/api/long_redirect', allow_redirects=True)
print(len(response.history))
#2 - число редиректов

for i in range(len(response.history)):
    print(response.history[i].url)

print(response.url)
#https://learnqa.ru/ - конечный URL
