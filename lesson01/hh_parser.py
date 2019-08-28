import time
import random
import argparse

import requests
from bs4 import BeautifulSoup as bs


def check_positive(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError('{} must be positive'.format(value))
    return ivalue


text_choices = (
    'python', 'django', 'java', 'javascript',
    'php', 'go', 'ruby',
    'linux', 'devops',
)


parser = argparse.ArgumentParser()
parser.add_argument('-t', '--text', type=str, required=True, help='search text')  # choices=text_choices)
parser.add_argument('-p', '--pages', type=check_positive, default=3, choices=range(1, 11), help='page count')
parser.add_argument('-f', '--out-file', type=str, default='jobs_hh.json')
parser.add_argument('-s', '--save', action='store_true')


ARG = parser.parse_args()
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0'


filename = ARG.out_file
headers = {
    'accept': '*/*',
    'user-agent': USER_AGENT,
}
base_url = 'https://hh.ru/search/vacancy?area=1&search_period=3&text={}&page={}'
jobs_result = []


def write_json(data, fp):
    import json
    with open(fp, 'w') as f:
        json.dump(data, f, indent=4, separators=(',', ': '), sort_keys=True)


def hh_parse(content):
    jobs = []

    soup = bs(content, 'html.parser')
    items = soup.find_all('div', class_='vacancy-serp-item')
    for i in items:
        title = i.find('a', class_='bloko-link').text
        href = i.find('a', class_='bloko-link')['href']
        job = {
            'title': title,
            'href': href.split('?')[0],
        }
        jobs.append(job)
    return jobs


for page in range(0, ARG.pages):
    delay = random.randint(10, 30) / 10
    url = base_url.format(ARG.text, page)
    print('Get request: {1}\nDelay: {0} seconds'.format(delay, url))
    time.sleep(delay)
    session = requests.Session()
    response = session.get(url, headers=headers)

    if response.status_code == 200:
        jobs_result += hh_parse(response.content)
    elif response.status_code == 500:
        print('500 Internal Server Error.')
    elif response.status_code == 404:
        print('404 Not Found')


if ARG.save:
    write_json(jobs_result, filename)
    print('file saved to {}'.format(filename))
else:
    print(jobs_result)
    print(len(jobs_result))
