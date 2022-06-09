import requests
from random import choice

from fake_useragent import UserAgent
from bs4 import BeautifulSoup as BS

import config


if config.use_proxies:
    with open('proxies.txt', 'r') as file:
        proxies = [line.strip() for line in file.readlines()]
    
def get_random_IPv4():
    proxy = choice(proxies)
    return  {'http': proxy,
             'https':proxy}

def make_soup(url, use_proxies=True):
    headers = {'user-agent': UserAgent().random}
    
    proxies = get_random_IPv4() if use_proxies else {}
    r = requests.get(url, headers=headers, proxies=proxies)
        
    if r.status_code == 200:
        return BS(r.text, 'lxml')
    else:
        raise Exception(f"""
Что-то пошло не так
Открываемая страница - {url}
Статус код - {r.status_code}
Используемые прокси - {proxies}
""")
    
