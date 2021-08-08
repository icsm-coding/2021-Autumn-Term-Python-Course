import requests

sentence = 'Today I ran 8,849m up Mt Everest and swam 20km across the channel'
gender = 'male'
weight = 70
height = 183
age = 21

# API endpoint
nutritionix_api_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

# Below are the 5 parameters
parameters = {
    'query': sentence,
    'gender': gender,
    'weight_kg': weight,
    'height_cm': height,
    'age': age
}

# Below are the variables we need to specify in the headers kwarg
app_id = 'b4c63e15'
app_key = '96fdc8ad0e5896266d705244bd63b0f8'

# headers dictionary to authorize the request
headers = {
    'x-app-id': app_id,
    'x-app-key': app_key
}

response = requests.post(url=nutritionix_api_endpoint, json=parameters, headers=headers)

data = response.json()['exercises'][0]
calories = data['nf_calories']
duration = data['duration_min']
type = data['name']

print(f"Type of exercise: {type}\nDuration: {duration} mins\nCalories burnt: {calories}")