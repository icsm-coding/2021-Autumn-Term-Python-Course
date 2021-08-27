import requests

API_ENDPOINT = 'https://api.nationalize.io'

name = input('What is your name? ')

parameters = {'name': name}

response = requests.get(params=parameters, url=API_ENDPOINT)

print(f"Most likely nationality of a person called {name} is {response.json()['country'][0]['country_id']}")