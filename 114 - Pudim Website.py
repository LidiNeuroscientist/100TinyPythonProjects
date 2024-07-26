'''WEBSITE PUDIM

Create a code in Python that tests whether the PUDIM website is accessible from
 the user's computer '''


import requests

def is_online(url, timeout=5):
    '''Checks internet connection by attempting to access a website.'''
    try:
        requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        return False


if not is_online('https://chatgpt.com/c/c31e065b-3914-45fc-95a1-9a65e9654731'):
    print('\033[1;31mNOT CONNECTED!\033[m')
else:
    print('\033[1;32mConnection OK!\033[m')



''' SECOND'''

import urllib.request
import urllib.error

try:
    site = urllib.request.urlopen('https://chatgpt.com/c/c31e065b-3914-45fc-95a1-9a65e9654731')
except urllib.error.URLError as e:
    print(f'ERROR NOT FOUND: {e.reason}')
except urllib.error.HTTPError as e:
    print(f'HTTP ERROR: {e.code}')
else:
    print('CONNECTION ON')
