'''
the python challenge 3
'''
import requests
import webbrowser
import collections
import re


def webpage_ok(url):
    # OK status code is 200
    # Not found is 404 (and there are many other codes...)
    return requests.get(url).status_code == 200


if __name__ == '__main__':
    url = 'http://www.pythonchallenge.com/pc/def/equality.html'
    webbrowser.open(url)
    print(f'Source for {url}:')
    print()
    print(requests.get(url).text)

    mess_below = requests.get(url).text.strip().split('<!--')[1]
    pattern = '[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}'
    matches = re.findall(pattern, mess_below)
    print()

    url1 = 'http://www.pythonchallenge.com/pc/def/'
    url2 = ''.join(s[4] for s in matches)
    url3 = '.html'
    url = url1 + url2 + url3
    print(f'Trying {url}...')
    print(f'Status is {webpage_ok(url)}.')

    webbrowser.open(url)

    url1 = 'http://www.pythonchallenge.com/pc/def/'
    url2 = ''.join(s[4] for s in matches)
    url3 = '.php'
    url = url1 + url2 + url3
    print(f'Next challenge page: {url}')
    print(f'Status is {webpage_ok(url)}.')

    webbrowser.open(url)
