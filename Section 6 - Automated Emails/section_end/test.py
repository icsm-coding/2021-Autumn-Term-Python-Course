import smtplib
import ssl

my_email = YOUR_EMAIL_HERE
password = YOUR_PASSWORD_HERE


context = ssl.create_default_context()

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls(context=context) # secure the connection
server.login(my_email, password)
server.sendmail(
    from_addr=my_email,
    to_addrs="codingicsm@gmail.com",
    msg="Subject:Test\n\nThis is a test email."
)

server.quit()