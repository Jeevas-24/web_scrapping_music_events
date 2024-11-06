import requests
import selectorlib
import smtplib, ssl
import os

url = 'http://programmer100.pythonanywhere.com/tours/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


# Headers are used for specific web server that don't like script programs, so these helps here showing the program as browser


def scrape(url):
    """Scrape the page source from the url"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')
    value = extractor.extract(source)['tours']
    return value


def send_mail(raw_message):
    host = 'smtp.gmail.com'
    port = 465
    username = 'jeevasathappan2000@gmail.com'
    password = 'ypxn naqt nwau ghhx'
    receiver = 'jeevasathappan2000@gmail.com'
    context = ssl.create_default_context()
    message = f"""\
Subject: New Event on board

{raw_message}
"""
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
    print('Mail sent')


def read():
    with open('data.txt', 'r') as file:
        return file.read()


def store(extracted):
    with open('data.txt', 'a') as file:
        file.write(extracted + '\n')


if __name__ == '__main__':
    scraped = scrape(url)
    extracted = extract(scraped)
    print(extracted)
    content = read()
    if extracted != 'No upcoming tours':
        if extracted not in content:
            store(extracted)
            send_mail(extracted)
