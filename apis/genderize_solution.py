import requests

API_ENDPOINT = 'https://api.genderize.io'

name = input('what is your name? ')

parameters = {'name': name}

response = requests.get(url=API_ENDPOINT, params=parameters)
data = response.json()
print('hello')

print(f"The probability that {name} is the name of a {data['gender']} is {data['probability']}.")
