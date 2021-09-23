import requests

APP_ID = 'b4c63e15'
APP_KEY = '96fdc8ad0e5896266d705244bd63b0f8'

headers = {'x-app-id': APP_ID, 'x-app-key': APP_KEY}

API_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'

parameters = {'query': 'I cycled 20k to the beach for a 5k run',
              'gender': 'male',
              'age': 21,
              'weight_kg': 70,
              'height_cm': 183}

response = requests.post(url=API_ENDPOINT, data=parameters, headers=headers)

exercise_list = response.json()['exercises']

total_number_calories = 0
for exercise in exercise_list:
    total_number_calories += exercise['nf_calories']
    print(f"You burnt {exercise['nf_calories']} while doing {exercise['name']}")

print(f"Your total number of calories burnt is therefore {total_number_calories}")
