import random

names_list = ['Ian', 'Icarus', 'Isabel', 'Indigo']

with open('activities.txt', 'r') as activities_file:
    activities_list = [e[0:-1:1] for e in activities_file.readlines()]


def generate_activity():
    random_index = random.randint(0, len(activities_list) - 1)
    return activities_list[random_index]


def generate_email(person_name):
    with open('./email_template.txt', 'r') as template_file:
        email_template = template_file.read()
        activity = generate_activity()
        message = email_template.replace('[name]', person_name).replace('[activity]', activity)

    file_name = person_name + '_email.txt'
    with open(f'./emails_to_send/{file_name}', 'w') as email_file:
        email_file.write(message)


for person_name in names_list:
    generate_email(person_name)