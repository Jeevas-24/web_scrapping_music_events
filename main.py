import requests
import selectorlib

url = 'http://programmer100.pythonanywhere.com/tours/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
# Headers are used for specific web server that don't like script programs, so these help us showing the program as browser
def scrape(url):
    '''Scrape the page source from the url'''
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')
    value = extractor.extract(source)['tours']
    return value

def send_mail(extract):
    print('Mail sent')

def read():
    with open('data.txt','r') as file:
        return file.read()

def store(extracted):
    with open('data.txt', 'a') as file:
        file.write(extracted +'\n')


if __name__ == '__main__':
    scraped = scrape(url)
    extracted = extract(scraped)
    print(extracted)
    content = read()
    if extracted != 'No upcoming tours':
        if extracted not in content:
            store(extracted)
            send_mail(extracted)


