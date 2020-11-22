import requests
from bs4 import BeautifulSoup
import time
import os
import ssl
import smtplib
import datetime

UP_SLEEP = 300
DOWN_SLEEP = 600
SUBJECT = 'ToDo is down!!!'
URL = 'http://35.197.22.173/home/'
QUICK_LINK = 'https://console.cloud.google.com/'
EMAIL = os.environ['GMAIL_ADDRESS']
PASSWORD = os.environ['GMAIL_PASSWORD']
# EMAIL_LIST = ['ronniesong0809@gmail.com']
EMAIL_LIST = ['boxuan@pdx.edu', 'cecishi@pdx.edu', 'ronsong@pdx.edu', 'yl6@pdx.edu']

def email_alert():
    timestamp = datetime.datetime.now().strftime("%H:%M:%S %Y/%m/%d")
    body = 'Hey,\n\n' + URL + ' is currently DOWN!\n\nQuick links:\n' + QUICK_LINK + '\n' + URL + '\n\nTimestamp: ' + str(timestamp) + '\n\nRegards,\nRonnie Song\nThis email was sent from a Python script. Please do not reply to this message.'
    msg = 'Form: ' + EMAIL + '\nTO: ' + ';'.join(EMAIL_LIST) + '\nX-Priority: 2\nSubject: ' + SUBJECT + '\n\n' + body

    context = ssl.create_default_context()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(EMAIL, password)

    server.sendmail(EMAIL, EMAIL_LIST, msg)
    print('DOWN: ' + datetime.datetime.now().strftime("%H:%M:%S %Y/%m/%d") + ', alert email Sent to ' + str(EMAIL_LIST))
    server.quit()
    

def run():
    while True:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
        response = requests.get(URL, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')

        if str(soup).find('NewBee.Todo') != -1:
            print('UP: ' + datetime.datetime.now().strftime("%H:%M:%S %Y/%m/%d"))
            time.sleep(UP_SLEEP)
            continue
        else:
            email_alert()
            time.sleep(DOWN_SLEEP)
            continue

if __name__ =='__main__':
    run()