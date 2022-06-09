from proxy_getter import HideMyNameParser

if __name__ == '__main__':
    parser = HideMyNameParser()
    parser.parse_proxies()
    proxies = parser.get_proxies()
    parser.save_proxies()
