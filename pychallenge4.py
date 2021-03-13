'''
the python challenge #4
'''

import requests
import webbrowser
import collections
import re

SPACE = ' '

def webpage_ok(url):
    # OK status code is 200
    # Not found is 404 (and there are many other codes...)
    return requests.get(url).status_code == 200


if __name__ == '__main__':
    url1 = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    url2 = '12345'
    url = url1 + url2

    while True:
        try:
            url2 = re.findall('\d+', requests.get(url).text)[0]
            url = url1 + url2
        except:
            no_nothing = requests.get(url).text
            print(f'First end of the chain message: {url2} {no_nothing}')
            break

    url2 = '8022'
    url = url1 + url2

    while True:
        try:
            url2 = requests.get(url).text.strip().split('next nothing is ')[1]
            url = url1 + url2
        except:
            no_nothing = requests.get(url).text
            print(f'End of the chain message: {url2} {no_nothing}')
            break

    url1 = 'http://www.pythonchallenge.com/pc/def/'
    url2 = no_nothing
    url = url1 + url2
    print(f'Next challenge page: {url}...')
    print(f'Status is {webpage_ok(url)}.')

    webbrowser.open(url)
