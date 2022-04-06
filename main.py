import pandas as pd
import datetime as dt
import random
import smtplib

my_email = "my_email@yahsoo.com"
password = "12345678"

smtp_address_book = {"yahoo.com":"smtp.mail.yahoo.com", "gmail.com":"smtp.gmail.com", "hotmail.com":"smtp.live.com", "outlook.com":"smtp-mail.outlook.com"}

try:
    smtp_address = smtp_address_book[my_email.split('@')[-1].lower()]
except KeyError as message:
    smtp_address = input(f"{message} is not a compatible server. Please input your server smtp: \n")
    if smtp_address == '':
        quit()

birthdays = pd.read_csv("birthdays.csv")
birthdays = birthdays.to_dict(orient="records")

now = dt.datetime.now()
month = now.month
day = now.day

for person in birthdays:
    if person["month"] == month and person["day"] == day:
        with open(f"letter_templates\letter_{random.randint(1, 3)}.txt") as letter:
            random_letter = letter.read()
            random_letter = random_letter.replace("[NAME]", person["name"])

        with smtplib.SMTP(smtp_address) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=person["email"], msg=f"Subject: Happy Birthday! \n\n{random_letter}")


