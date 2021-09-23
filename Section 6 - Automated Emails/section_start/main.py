import smtplib
import ssl
import datetime

from patients import patients_list

my_email = "icsmpython@gmail.com"
password = 'python1999'

context = ssl.create_default_context()

def compare_date(patient_date):
    # '22/09/2021'
    patient_day = patient_date.split('/')[0]
    patient_month = patient_date.split('/')[1]
    patient_year = patient_date.split('/')[2]

    now = datetime.datetime.now()

    current_day = now.strftime('%d')
    current_month = now.strftime('%m')
    current_year = now.strftime('%Y')

    if patient_day == current_day and patient_month == current_month and patient_year == current_year:
        return True

    else:
        return False

def get_email_message(patient_dict):
    with open('./template.txt', 'r') as template_file:
        template_text = template_file.read()

        patient_name = patient_dict['name']
        appointment = patient_dict['appointment_type']

        message = template_text.replace('[patient_name]', patient_name).replace('[appointment_type]', appointment)

        return message

def send_email(patient_dict):
    message = get_email_message(patient_dict)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls(context=context)  # secure the connection
    server.login(my_email, password)
    server.sendmail(
        from_addr=my_email,
        to_addrs=patient_dict['email'],
        msg=f"Subject:{patient_dict['appointment_type']}\n\n{message}"
    )

    server.quit()

for patient_dict in patients_list:
    if compare_date(patient_dict['date']) == True:
        send_email(patient_dict)


