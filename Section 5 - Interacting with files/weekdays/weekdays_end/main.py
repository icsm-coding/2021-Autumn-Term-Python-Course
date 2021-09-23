def read_weekdays():
    with open('./weekdays.txt', 'r') as file:
        print(file.read())


def append_sunday():
    with open('./weekdays.txt', 'a') as file:
        print(file.write('Sunday'))


def overwrite_weekdays():
    with open('./weekdays.txt', 'w') as file:
        print(file.write('Sunday'))