import smtplib
import ssl
from datetime import datetime

from patients import patients_list

my_email = YOUR_EMAIL_HERE
password = YOUR_PASSWORD_HERE

context = ssl.create_default_context()


def compare_date(date):

    patient_day = date.split('/')[0]
    patient_month = date.split('/')[1]
    patient_year = date.split('/')[2]

    now = datetime.now()
    day = now.strftime("%d")
    month = now.strftime("%m")
    year = now.strftime("%Y")

    if day == patient_day and month == patient_month and year == patient_year:
        return True
    else:
        return False


def get_email_message(patient_dict):
    with open('template.txt', 'r') as file:
        template_text = file.read()
        message_output = template_text.replace('[patient_name]', patient_dict['name']).replace('[appointment_type]',
                                                                                             patient_dict[
                                                                                                 'appointment_type'])

    return message_output


def send_email(patient_dict, message_input):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls(context=context)  # secure the connection
    server.login(my_email, password)
    server.sendmail(
        from_addr=my_email,
        to_addrs=patient_dict['email'],
        msg=f"Subject:{patient_dict['appointment_type']} Tomorrow\n\n{message_input}"
    )

    server.quit()


for patient in patients_list:
    if compare_date(patient['date']):
        message = get_email_message(patient)
        send_email(patient, message)
