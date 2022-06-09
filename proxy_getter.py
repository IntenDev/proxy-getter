from time import sleep
import requests
import math

from pathvalidate import sanitize_filepath
from bs4 import BeautifulSoup as BS
import lxml

import my_soup
import config


class HideMyNameParser:

    def __init__(self):
        self.shema = f'https://hidemy.name/ru/proxy-list/?' \
                        f'maxtime={config.maxtime}&' \
                        f'type={config.proxy_type}&' \
                        f'anon={config.anonymity_level}'
        self.proxies = []

    @staticmethod
    def check_proxy(proxy, website):
        try:
            proxies = my_soup.get_random_IPv4() if config.use_proxies else {}
            r = requests.get(website, proxies=proxies)
            return r.status_code == 200
        except ProxyError:
            return False
        
    @staticmethod
    def __parse_line(line):
        cells = [cell.text.strip() for cell in line.find_all('td')]
        ip = cells[0]
        port = cells[1]
        if cells[4] == 'SOCKS4, SOCKS5':
            cells[4] = 'socks5'
        type_ = cells[4].lower()
        return f'{type_}://{ip}:{port}'
        
    def parse_proxies(self, amount=config.amount):
        count = 0
        for i in range(200):
            url = self.shema + f'&start={64*i}#list'

            page = my_soup.make_soup(url, use_proxies=config.use_proxies)
            if not page.select('tbody > tr') or count == amount:
                break
            for line in page.select('tbody > tr'):
                if count == amount:
                    return
                proxy = self.__parse_line(line)
                if not config.target or self.check_proxy(proxy, config.target):
                    self.proxies.append(proxy)
                    count += 1
                    if config.display_progress:
                        print(proxy)

    def get_proxies(self):
        return self.proxies
                        
    def save_proxies(self):
        path = sanitize_filepath(config.result_file)
        with open(path, 'w') as file:
            file.write('\n'.join(self.proxies))
