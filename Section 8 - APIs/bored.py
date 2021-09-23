import requests

API_ENDPOINT = 'http://www.boredapi.com/api/activity/'

filter_variable = input('Would you like to filter your activity? yes/no ')

if filter_variable == 'yes':

    type_activity = input('Type? recreational, busywork, cooking, social, education, charity, diy or music, relaxation: ')
    participants_number = int(input('How many people will partake in this activity? '))

    min_price = float(input('What is the minimum price you will pay where 0 is low and 1 is high? '))
    max_price = float(input('What is the maximum price you will pay where 0 is low and 1 is high? '))

    min_accessibility = float(input('What is the minimum accessibility you want where 0 is low and 1 is high? '))
    max_accessibility = float(input('What is the maximum accessibility you want where 0 is low and 1 is high? '))

    parameters = {'type': type_activity, 'participants': participants_number, 'minprice': min_price, 'maxprice': max_price,
              'minaccessibility': min_accessibility, 'maxaccessibility': max_accessibility}

    response = requests.get(url=API_ENDPOINT, params=parameters)

else:
    response = requests.get(url=API_ENDPOINT)

print(response.json())