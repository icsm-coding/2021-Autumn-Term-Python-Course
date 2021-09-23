import requests

API_ENDPOINT = 'https://api.nationalize.io'

name_input = input('What is you name? ')

parameters = {'name':name_input}

response = requests.get(url=API_ENDPOINT, params=parameters)

print(response.json()['country'][0]['country_id'])