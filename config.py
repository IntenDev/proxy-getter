"""
TYPE = {'http': 'h',
        'socks5': '5',
        'socks4': '4',
        'https': 's'}
If you need to parse http or socks5 type proxy,
you must assign 'h5' to the proxy_type variable:
proxy_type = 'h5'
where the order of the characters doesn't matter.


ANONYMITY = {'high': '4',
             'average': '3',
             'low': '2',
             'no': '1'
If you need to parse a proxy with a level anonymity high or average,
you must assign '34' to the variable anonymity_level:
anonymity_level = '34'
where the order of the characters doesn't matter

target - site that needs a proxy to be parsed (it can be an empty string)
maxtime - max proxy response time in milliseconds
result_file - the file where you want to save the proxy
display_progress - displaying prints in progress
use_proxies - using a proxy for requests
amount - the number of proxies to be mined
"""


proxy_type = '5'
anonymity_level = '4321'
target = 'https://turk.estate/'
maxtime = 1500
result_file = 'res.txt'
display_progress = True
use_proxies = False
amount = 10
