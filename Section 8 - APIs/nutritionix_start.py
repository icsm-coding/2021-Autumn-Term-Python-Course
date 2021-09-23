import requests

API_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'

APP_ID = 'b4c63e15'
APP_KEY = '96fdc8ad0e5896266d705244bd63b0f8'

headers = {'x-app-id':APP_ID, 'x-app-key':APP_KEY}

parameters = {'query': 'Today, I cycled 20k to the beach for a 5k run', 'gender': 'male', 'weight_kg': 70, 'height_cm': 183, 'age': 21}

response = requests.post(url=API_ENDPOINT, json=parameters, headers=headers)

