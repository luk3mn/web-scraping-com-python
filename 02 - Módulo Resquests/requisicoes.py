import requests

response = requests.get('https://www.walissonsilva.com/')

print('Status Code:', response.status_code)
print('|| Header ||')
print(response.headers)
print('\n || Content ||')
print(response.content)