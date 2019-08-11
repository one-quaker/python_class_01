from bs4 import BeautifulSoup
import requests
from pprint import pprint


BASE_URL = 'https://bash.im'
URL = f'{BASE_URL}/best'
# URL = '{}/best'.format(BASE_URL)


doc = requests.get(URL)
soup = BeautifulSoup(doc.text, 'html.parser')


result = []
for i in soup.find_all('article', class_='quote'):
    item = {}

    # print(16 * '-')
    # print(i.text)

    post = i.find('a', href=True)
    raw_date = i.select_one('div.quote__header_date').text

    try:
        rating = int(i.select_one('div.quote__total').text)
    except ValueError:
        rating = 0
    finally:
        item['rating'] = rating

    item['text'] = i.select_one('div.quote__body').text.strip()
    item['date'] = raw_date.strip().replace(' в  ', ' ')
    # item['text'] = i.find('div', class_='quote__body').text
    item['url'] = '{}{}'.format(BASE_URL, post['href'])
    item['name'] = post.text
    result.append(item)


pprint(result)
# use json module
# just code or function
# save result in  json format into result.json

